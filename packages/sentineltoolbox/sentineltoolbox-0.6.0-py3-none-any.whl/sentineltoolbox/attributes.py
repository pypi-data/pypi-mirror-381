import copy
import logging
import warnings
from pathlib import Path, PurePosixPath
from typing import Any, Dict, Generator, Hashable, MutableMapping

from sentineltoolbox._utils import _get_attr_dict, string_to_slice
from sentineltoolbox.hotfix import (
    Hotfix,
    HotfixManager,
    HotfixPath,
    load_hotfix,
)
from sentineltoolbox.metadata_utils import guess_product_type
from sentineltoolbox.typedefs import (
    AttrsVisitor,
    MetadataType_L,
    T_Attributes,
    T_ContainerWithAttributes,
    category_paths,
)
from sentineltoolbox.writers.json import serialize_to_zarr_json

logger = logging.getLogger("sentineltoolbox")

__all__ = ["AttributeHandler"]

PATH_STAC_ROOT = "stac_discovery/"
PATH_STAC_PROPERTIES = "stac_discovery/properties/"
PATH_OTHER_METADATA = "other_metadata/"


def visit_attrs_node(visitor: AttrsVisitor, root: T_Attributes, path: str, obj: Any) -> None:
    try:
        visitor.visit_node(root, path, obj)
        if isinstance(obj, dict):
            for k, v in obj.items():
                if path.endswith("/"):
                    path = path + k
                else:
                    path = path + "/" + k
                if isinstance(v, dict):
                    visit_attrs_node(visitor, root, path, v)
                if isinstance(v, list):
                    visit_attrs_node(visitor, root, path, v)
    except TypeError:
        pass


def visit_attrs(attrs: T_Attributes, visitor: AttrsVisitor) -> None:
    visit_attrs_node(visitor, attrs, "/", attrs)


def recursive_update(
    d1: Dict[Hashable, Any],
    d2: Dict[Hashable, Any],
    mode_for_dict: str = "merge",
    mode_for_list: str = "replace",
    mode_for_set: str = "replace",
) -> None:
    """
    Recursively updates dictionary `d1` with values from `d2`,
    allowing separate modes for handling dictionaries, lists, and sets.

    Arguments:
    - d1: The destination dictionary to update.
    - d2: The source dictionary to update from.
    - mode_for_dict: The update mode for dictionaries (default: "replace"):
        - "replace": Overwrite existing keys.
        - "add": Add only new keys.
        - "merge": Recursively merge keys.
    - mode_for_list: The update mode for lists (default: "replace"):
        - "replace": Overwrite existing lists.
        - "merge": Concatenate lists.
    - mode_for_set: The update mode for sets (default: "replace"):
        - "replace": Overwrite existing sets.
        - "merge": Union of sets.

    Returns:
    - The updated dictionary `d1`.
    """
    for key, value in d2.items():
        if key in d1:
            if isinstance(value, dict) and isinstance(d1[key], dict):
                if mode_for_dict == "merge":
                    recursive_update(
                        d1[key],
                        copy.copy(value),
                        mode_for_dict=mode_for_dict,
                        mode_for_list=mode_for_list,
                        mode_for_set=mode_for_set,
                    )
                elif mode_for_dict == "replace":
                    d1[key] = value
                elif mode_for_dict == "add":
                    pass  # Keep existing keys, do nothing
            elif isinstance(value, list) and isinstance(d1[key], list):
                if mode_for_list == "merge":
                    d1[key].extend(value)
                elif mode_for_list == "replace":
                    d1[key] = copy.copy(value)
            elif isinstance(value, set) and isinstance(d1[key], set):
                if mode_for_set == "merge":
                    d1[key].update(value)
                elif mode_for_set == "replace":
                    d1[key] = copy.copy(value)
            else:
                if isinstance(d1[key], (list, dict, set)):
                    # We try to update a dict, set or list with something not compatible, keep initial value
                    logger.warning(f"Cannot update data of type {type(d1[key])} with data of type {type(value)}")
                else:
                    d1[key] = value  # For non-iterable types, always replace
        else:
            d1[key] = copy.deepcopy(value)  # Add new keys from d2


def path_relative_to_category(path: str, category: MetadataType_L | None, **kwarg: Any) -> str:
    if category in ("stac_properties", "stac_discovery", "metadata"):
        return path.replace(category_paths[category], "")
    else:
        return path


def fix_attribute_value(
    data: T_Attributes,
    path: str,
    value: Any,
    category: MetadataType_L | None,
    **kwargs: Any,
) -> Any:
    hotfix_manager, _ = get_hotfix_manager(**kwargs)
    if category is None:
        category = "root"
    for hotfix in hotfix_manager.value(data, product_type=kwargs.get("product_type", "")):
        relpath = path_relative_to_category(path, category, **kwargs)
        conversions = hotfix.data.get(category, {})
        if relpath in conversions:
            fix_function = conversions[relpath]
            try:
                value = fix_function(value, path=path, **kwargs)
            except Exception as e:
                logger.warning(f"Failed to fix value for {path!r}", exc_info=e)

    return value


def to_json(data: T_Attributes, path: str, value: Any, category: MetadataType_L | None, **kwargs: Any) -> Any:
    relpath = path_relative_to_category(path, category, **kwargs)
    hotfix_manager, _ = get_hotfix_manager(**kwargs)
    for hotfix in hotfix_manager.wrapper(data, product_type=kwargs.get("product_type", "")):
        conversions = hotfix.data.get(category, {})
        if relpath in conversions:
            converter = conversions[relpath]
            return converter.to_json(value, path=path)

    return value


def from_json(data: T_Attributes, path: str, value: Any, category: MetadataType_L | None, **kwargs: Any) -> Any:
    relpath = path_relative_to_category(path, category, **kwargs)

    hotfix_manager, _ = get_hotfix_manager(**kwargs)
    for hotfix in hotfix_manager.wrapper(data, product_type=kwargs.get("product_type", "")):
        conversions = hotfix.data.get(category, {})
        if relpath in conversions:
            converter = conversions[relpath]
            return converter.from_json(value, path=path)

    return value


def guess_category(path: str, **kwargs: Any) -> MetadataType_L | None:
    category = kwargs.get("category")
    if category is not None:
        return category
    if path.startswith("properties") or path.startswith("stac_discovery/properties"):
        return "stac_properties"
    elif path.startswith("stac_discovery"):
        return "stac_discovery"
    elif path.startswith("other_metadata") or path.startswith("metadata"):
        return "metadata"
    else:
        hotfix_manager, _ = get_hotfix_manager(**kwargs)
        return hotfix_manager.get_alias(path, **kwargs)[0]


def fix_attribute_path(
    path: str,
    category: MetadataType_L | None = None,
    **kwargs: Any,
) -> tuple[str, MetadataType_L | None]:
    """
    Adjusts the given attribute path to match a canonical format based on its category.
    Applies hotfixes if specified. Look at short names (alias_dict)

    >>> fix_attribute_path("properties/test", category="stac_properties")
    ('stac_discovery/properties/test', 'stac_properties')
    >>> fix_attribute_path("test", category="stac_properties")
    ('stac_discovery/properties/test', 'stac_properties')
    >>> fix_attribute_path("properties/test") # category is recognized here
    ('stac_discovery/properties/test', 'stac_properties')
    >>> fix_attribute_path("properties/test", category="metadata") # category is recognized but fix trust user inputs
    ('other_metadata/test', 'metadata')
    >>> fix_attribute_path("test") # category not recognized, no user inputs => path unchanged
    ('test', None)

    Use short names if provided
    >>> fix_attribute_path("eo:bands", alias_dict={"eo:bands":("stac_properties", "bands")})
    ('stac_discovery/properties/bands', 'stac_properties')

    Args:
        path: The initial attribute path.
        category: The category of the attribute (e.g., "stac_properties", "metadata").
        **kwargs: Additional options, including a "hotfix_list" for path adjustments.

    Returns:
        The corrected and fixed attribute path.
    """
    # Clean up the provided path
    path = path.strip().rstrip("/")

    # Resolve the category and path using aliases, if applicable
    if category is None:
        hotfix_manager, _ = get_hotfix_manager(**kwargs)
        category, path = hotfix_manager.get_alias(
            path,
            attrs=kwargs.get("attrs", {}),
            product_type=kwargs.get("product_type", ""),
        )

    # Attempt to determine the category if not already provided
    if category is None:
        category = guess_category(path, **kwargs)

    if category is None:
        # If the category cannot be determined, return the path unchanged
        return path, None

    # Determine the appropriate prefix based on the category
    if category == "stac_properties":
        prefix = PATH_STAC_PROPERTIES
    elif category == "stac_discovery":
        prefix = PATH_STAC_ROOT
    elif category == "metadata":
        prefix = PATH_OTHER_METADATA
    else:
        prefix = ""

    # Strip any existing recognized prefixes from the path

    # Define recognized prefixes for different categories
    recognized_properties = [PATH_STAC_PROPERTIES, "properties/"]
    recognized_stac = [PATH_STAC_ROOT]
    recognized_metadata = [PATH_OTHER_METADATA, "metadata/"]
    recognized_prefixes = recognized_properties + recognized_stac + recognized_metadata

    for possible_prefix in recognized_prefixes:
        prefix_parts = possible_prefix.split("/")

        for prefix_part in prefix_parts:
            if prefix_part and path.startswith(prefix_part):
                # Remove the matched prefix from the path
                path = path[len(prefix_part) + 1 :]  # noqa: E203 (whitespace issue in slicing)

    final_path = prefix + path
    if kwargs.get("fix", True):
        hotfix_manager, _ = get_hotfix_manager(**kwargs)
        for hotfix in hotfix_manager.path(attrs=kwargs.get("attrs", {}), product_type=kwargs.get("product_type", "")):
            try:
                category, final_path = hotfix.data[final_path]
            except KeyError:
                pass
            else:
                # volountary force hotfix list to empty to avoid recursion error, for example
                # if user write fix like "stac_discovery/properties/eo:bands" -> ("stac_properties", "eo:bands")
                kwargs = copy.copy(kwargs)
                if "hotfix" in kwargs:
                    kwargs.pop("hotfix")
                return fix_attribute_path(final_path, category, hotfix=HotfixManager([]), **kwargs)

    # Prepend the determined prefix to the stripped path
    return final_path, category


def _get_value_from_path(group: T_Attributes, path: str, **kwargs: Any) -> Any:
    """
    Extract value at path. No path fix. If path is wrong => KeyError
    """
    path = path.strip().rstrip("/")
    # Determine if value conversion should be performed
    real_path_parts = []

    parts: list[str] = path.split("/")  # Split the path into components
    value_found = False
    msg = path

    # Traverse the path parts within the current location
    for part in parts:
        try:
            # Attempt to convert the part to an integer for list indexing
            valid_part: int | slice | str = int(part)
        except ValueError:
            try:
                # Attempt to interpret the part as a slice
                valid_part = string_to_slice(part)
            except ValueError:
                valid_part = part  # Default to a string if conversion fails

        if isinstance(valid_part, (int, slice)):
            # Handle list indexing
            real_path_parts.append(part)
            if isinstance(group, list):
                group = group[valid_part]
                value_found = True
            else:
                raise KeyError(
                    f"Invalid path {path!r}. Part {valid_part!r} is not correct because {group} is not a list",
                )
        else:
            # Handle dictionary key access
            _kwargs = copy.copy(kwargs)
            _kwargs["warn_deprecated"] = False
            if part in group:
                value_found = True
                group = group[part]
                real_path_parts.append(part)
            else:
                # Stop further processing if the key is not found
                value_found = False
                if part != parts[0]:
                    valid_part = "/".join(real_path_parts)
                    msg = f"{path}. {valid_part} exists but not {part}"
                break

    if value_found:
        return group
    else:
        raise KeyError(msg)


def find_and_fix_attribute(
    attrs: T_Attributes,  # The attributes dictionary or object to search in
    path: str,  # The path to the attribute to locate
    *,
    category: MetadataType_L | None = None,  # The category of the attribute (optional)
    **kwargs: Any,  # Additional options, such as conversion settings or defaults
) -> tuple[Any, str, str]:  # Returns the found value, fixed path, and real path
    """
    Finds an attribute in a hierarchical structure and optionally fixes its path or value.
    Creates a new attribute if requested and not found.

    Args:
        attrs: The attributes dictionary or object to search within.
        fixed_path: The path of the attribute to find.
        category: The category of the attribute, if known.
        **kwargs: Additional options like 'convert_value_type', 'default', or 'create'.

    Returns:
        A tuple of the found value, the fixed path, and the real path.

    Raises:
        KeyError: If the attribute is not found and no default is specified.
    """

    # convert input path to canonical path
    user_path = path
    product_type = guess_product_type(attrs, metadata_extractors=["user", "metadata", "filename"], **kwargs)
    kwargs["product_type"] = product_type
    kwargs["attrs"] = attrs
    fixed_path, category = fix_attribute_path(path, category, **kwargs)
    # Now that path is correct, tries to return it
    err_msg = ""
    try:
        return _get_value_from_path(attrs, fixed_path, **kwargs), fixed_path, fixed_path
    except KeyError as err:
        err_msg = err.args[0]

    # If not found tries to search with user path not fixed
    try:
        return _get_value_from_path(attrs, user_path, **kwargs), fixed_path, user_path
    except KeyError as err:
        err_msg = err.args[0]

    # if not found, tries to search in old places by reversing hotfix path
    hotfix_manager = kwargs.get("hotfix_manager")
    if hotfix_manager:
        for hotfix in hotfix_manager.path(attrs=attrs, product_type=product_type):
            for wrong_path, correct_data in hotfix.data.items():
                correct_cat, correct_rel_path = correct_data
                correct_path, correct_cat = fix_attribute_path(correct_rel_path, correct_cat, **kwargs)
                if correct_path == fixed_path:
                    try:
                        return _get_value_from_path(attrs, wrong_path, **kwargs), fixed_path, user_path
                    except KeyError:
                        pass

    # If not found, search in probable places
    # Define potential search locations based on the category
    places_properties = [
        (PATH_STAC_PROPERTIES, attrs.get("stac_discovery", {}).get("properties")),
        ("properties/", attrs.get("properties")),
    ]
    places_metadata = [
        (PATH_OTHER_METADATA, attrs.get("other_metadata")),
        ("metadata/", attrs.get("metadata")),
    ]
    places_stac = [
        (PATH_STAC_ROOT, attrs.get("stac_discovery")),
    ]
    places_root: list[tuple[str, Any]] = [("", attrs)]

    # Select search places based on category
    if category == "stac_properties":
        # Search order: stac_discovery/properties -> properties -> root
        places = places_properties + places_root
    elif category == "metadata":
        # Search order: other_metadata -> metadata -> root
        places = places_metadata + places_root
    elif category == "stac_discovery":
        # Search order: stac_discovery -> root
        places = places_stac + places_root
    elif category == "root":
        # Only root-level attributes
        places = places_root
    else:
        # Default to searching all places if the category is unknown
        category = None
        places = places_root + places_properties + places_stac + places_metadata

    # Iterate over the possible locations to find the attribute
    for place_path, place in places:
        if place is None:
            continue  # Skip if the current location is invalid

        paths: list[str] = []
        fixed_path, category = fix_attribute_path(fixed_path, category, **kwargs)
        paths.append(fixed_path)
        path = path_relative_to_category(fixed_path, category, **kwargs)
        paths.append(path)

        paths.append(user_path)
        path = path_relative_to_category(user_path, category, **kwargs)
        paths.append(path)

        for path in paths:
            try:
                value = _get_value_from_path(place, path, **kwargs)
            except KeyError:
                pass
            else:
                return value, fixed_path, place_path + path

    # Handle the case where the attribute is not found
    if "default" in kwargs or "create" in kwargs:
        default = kwargs.get("default")
        if "create" in kwargs:
            set_attr(attrs, fixed_path, default, category=category, **kwargs)
            return default, fixed_path, fixed_path
        else:
            return default, fixed_path, ""
    else:
        raise KeyError(err_msg)


def recurse_json_dict(
    d: MutableMapping[Any, Any] | list[Any],
    root: str = "",
) -> Generator[tuple[str, Any], None, None]:
    if isinstance(d, dict):
        items = list(d.items())
    elif isinstance(d, list):
        items = [(str(i), v) for i, v in enumerate(d)]
    else:
        items = []

    for k, v in items:
        path = root + k + "/"
        yield path, v
        if isinstance(v, (dict, list)):
            yield from recurse_json_dict(v, path)


def search_attributes(
    attrs: T_ContainerWithAttributes | T_Attributes,
    path: str,
    *,
    category: MetadataType_L | None = None,
    **kwargs: Any,
) -> list[str]:
    kwargs["warn_deprecated"] = kwargs.get("warn_deprecated", False)
    kwargs["convert_value_type"] = kwargs.get("convert_value_type", False)
    kwargs["builtins"] = kwargs.get("builtins", kwargs.get("fix", True))
    recursive = kwargs.get("recursive", True)
    limit = kwargs.get("limit")

    dict_attrs: T_Attributes = _get_attr_dict(attrs)
    results = set()

    try:
        value, fixed, real = find_and_fix_attribute(dict_attrs, path, category=category, **kwargs)
        results.add(real)
    except KeyError:
        pass

    if recursive:
        for p, v in recurse_json_dict(dict_attrs):
            if isinstance(limit, int) and len(results) > limit:
                break
            if not isinstance(v, dict):
                continue
            current_category = guess_category(p, **kwargs)
            if category is not None and current_category != category:
                continue
            try:
                value, fixed, real = find_and_fix_attribute(v, path, category=category, **kwargs)
            except KeyError:
                pass
            else:
                results.add(p + real)
    return list(sorted(results))


def extract_attr(
    data: T_ContainerWithAttributes | T_Attributes,
    path: str | None = None,
    *,
    category: MetadataType_L | None = None,
    **kwargs: Any,
) -> Any:
    attrs = _get_attr_dict(data)
    if path is None:
        if category is None:
            return attrs
        else:
            category_path = category_paths[category]
            return extract_attr(attrs, category_path, **kwargs)
    else:
        value, fixed_path, real_path = find_and_fix_attribute(attrs, path, category=category, **kwargs)
        if kwargs.get("trace", False):
            if fixed_path != real_path:
                logger.info(f"try to access to path {real_path!r} instead of {fixed_path!r}")
        kwargs["product_type"] = guess_product_type(attrs)
        kwargs["attrs"] = data
        if real_path:
            # value exists in dict, we want to apply hotfix
            # if real_path is not defined, that means user pass a default value and we get this default value
            # in this case, we do not want to fix user input
            category = guess_category(fixed_path, category=category, **kwargs)
            if category is None:
                category = "root"
            if kwargs.get("fix", True):
                value = fix_attribute_value(attrs, path, value, category=category, **kwargs)
            if kwargs.get("format", True):
                value = from_json(attrs, fixed_path, value, category=category, **kwargs)
            return value
        else:
            return value


def set_attr(
    data: T_ContainerWithAttributes | T_Attributes,
    path: str,
    value: Any,
    category: MetadataType_L | None = None,
    **kwargs: Any,
) -> MutableMapping[Any, Any]:
    root_attrs = _get_attr_dict(data)
    path, category = fix_attribute_path(path, category=category, **kwargs)
    category = guess_category(path, category=category, **kwargs)
    if category is None:
        category = "root"
    attrs = root_attrs
    parts = path.split("/")
    for part in parts[:-1]:
        attrs = attrs.setdefault(part, {})
    if kwargs.get("fix", True):
        old_value = value
        kwargs["product_type"] = guess_product_type(data)
        value = fix_attribute_value(root_attrs, path, value, category=category, **kwargs)
        try:
            if value != old_value:
                logger.info(f"{path}: value {old_value!r} has been fixed to {value!r}")
        except ValueError:
            pass  # TODO: support array comparisons
    if kwargs.get("format", True):
        value = from_json(attrs, path, value, category=category, **kwargs)
    attrs[parts[-1]] = to_json(attrs, path, value, category=category, **kwargs)
    return root_attrs


def append_log(container: T_ContainerWithAttributes, log_data: Any, **kwargs: Any) -> None:
    """
    See :obj:`AttributeHandler.append_log`

    :param container: container to update
    """
    AttributeHandler(container, **kwargs).append_log(log_data, **kwargs)


def get_logs(container: T_ContainerWithAttributes, **kwargs: Any) -> list[Any]:
    """
    See :obj:`AttributeHandler.get_logs`

    :param container: container containing log metadata
    """
    return AttributeHandler(container, **kwargs).get_logs(**kwargs)


def _extract_namespace_name(attribute_handler_name: str | None, **kwargs: Any) -> tuple[str, str]:
    namespace = kwargs.get("namespace", "processing_unit_history")
    name = kwargs.get("name", attribute_handler_name if attribute_handler_name is not None else "root")
    return namespace, name


def get_hotfix_manager(**kwargs: Any) -> tuple[HotfixManager, dict[str, Any]]:
    if kwargs.get("alias_dict"):
        lst: list[Hotfix] = [
            HotfixPath(
                kwargs.pop("alias_dict"),
                name="AutomaticAliasFix",
                description="Fix alias using alias_dict provided by user",
                priority=2,
            ),
        ]
    else:
        lst = []

    if kwargs.get("alias_only", False):
        builtins_category = ["convenience"]
    else:
        builtins_category = None

    # official new name is hotfix_manager but we keep "hotfix" for backward compatibility
    hotfix_manager = kwargs.get("hotfix_manager", kwargs.get("hotfix"))
    builtins = kwargs.get("builtins", False)
    builtins_categories = kwargs.get("builtins_category", builtins_category)
    if isinstance(builtins_categories, str):
        builtins_categories = [builtins_categories]
    elif isinstance(builtins_categories, list):
        pass
    else:
        builtins_categories = None

    if builtins_categories:
        builtins = True

    if hotfix_manager is None:
        if kwargs.get("hotfix_list") is None:
            if builtins:
                hotfix_list = load_hotfix()
                if builtins_categories is not None:
                    hotfix_list = list(filter(lambda hotfix: hotfix.category in builtins_categories, hotfix_list))
            else:
                hotfix_list = []
        else:
            hotfix_list = kwargs["hotfix_list"]
        hotfix_manager = HotfixManager(hotfix_list + lst)
    elif isinstance(hotfix_manager, HotfixManager):
        hotfix_manager.add_hotfixes(lst)
    else:
        logger.warning("hotfix is not a HotfixManager instance, ignoring it")

    # alias_dict already removed before
    if "hotfix_list" in kwargs:
        del kwargs["hotfix_list"]

    if "hotfix" in kwargs:
        del kwargs["hotfix"]

    kwargs["hotfix_manager"] = hotfix_manager

    return hotfix_manager, kwargs


class AttributeHandler:
    """
    TODO: if set, read stac_discovery/stac_extensions to automatically recognize stac properties.
    For examlple, if view is in stac_extension, help('view:incidence_angle') automatically understand that
    "view:incidence_angle" is equivalent to "stac_discovery/properties/view:incidence_angle"
    """

    _fixed_containers: set[int] = set()

    @classmethod
    def clear_cache(cls) -> None:
        """Reset the set of fixed containers."""
        cls._fixed_containers.clear()

    def __init__(self, container: T_ContainerWithAttributes | T_Attributes | None = None, **kwargs: Any):
        """
        Represents a class responsible for handling a container (DataTree, EOProduct, dict) to ease access to attributes
        and metadata. This class also provide an hotfix mecanism to fix metadata values on the fly and guess full paths
        from short names (ie: created -> stac_discover/properties/created).

        To manipulate metadata, see
          - get_attr
          - set_attr
          - set_stac_property, get_stac_property ...

        For hotfixes:

        By default, it use buitltins hotfix provided by sentineltoolbox and hotfix extensions, else you can:
          - disable builtin hotfix it by setting `builtins` to False.
          - choose hotfix explicitly using hotfix_list or hotfix_manager parameters


        Example values for `kwargs`:
        - "name": The name associated with the container (e.g., "example_name")
        - "builtins": Determines if built-in settings should be applied (e.g., True)
        - "hotfix_list": A list of hotfixes to apply.
        - "hotfix_manager": A class instance of a class that implements the interface
          :obj:`~sentineltoolbox.hotfix.HotfixManager` for applying hotfixes.

        :param container:
            Optional container with attributes, defaulting to an empty dictionary if None is provided.
        :param kwargs:
            Additional keyword arguments for customization. Includes a default "builtins" flag.
        """
        if container is None:
            container = {}
        self._container = container
        self.name = kwargs.get("name")
        kwargs["builtins"] = kwargs.get("builtins", True)
        _, kwargs = get_hotfix_manager(**kwargs)
        self._fixes: list[Any] = []
        self._kwargs = kwargs

    @property
    def datatype(self) -> str | None:
        ptype = self.get_attr("product:type", default=None)
        if ptype is None:
            from sentineltoolbox.metadata_utils import guess_product_type

            return guess_product_type(self._container, metadata_extractors=["filename"])
        else:
            return ptype

    def to_dict(self) -> MutableMapping[Any, Any]:
        """

        :return: convert it to dict. If container is a dict, return a copy of it
        """
        return copy.copy(_get_attr_dict(self._container))

    def container(self) -> Any:
        """
        Provides access to the internal container storing data.

        :rtype: Any
        """
        return self._container

    def append_log(self, log_data: Any, **kwargs: Any) -> None:
        """
        :param log_data: data you want to log
        :param kwargs:
          * name: processing unit name. Default: AttributeHandler.name or `"root"` if not set
          * namespace: group containing all logs. Default: `"processing_unit_history"`
        :return:
        """
        serialized_data = serialize_to_zarr_json(log_data, errors="replace", **kwargs)
        namespace, name = _extract_namespace_name(self.name, **kwargs)
        history = self.get_metadata(namespace, create=True, default={})
        history.setdefault(name, []).append(serialized_data)

    def get_logs(self, **kwargs: Any) -> list[Any]:
        """
        :param kwargs:
          * name: processing unit name. Default: AttributeHandler.name or `"root"` if not set
          * namespace: group containing all logs. Default: `"processing_unit_history"`
        :return: all logs registered in products
        """
        namespace, name = _extract_namespace_name(self.name, **kwargs)
        return self.get_metadata(f"{namespace}/{name}", default=[])

    def _update_kwargs(self, kwargs: Any) -> dict[str, Any]:
        final_kwargs: dict[str, Any] = {}
        final_kwargs.update(self._kwargs)
        final_kwargs.update(kwargs)
        if kwargs.get("raw", False):
            final_kwargs["format"] = False
            final_kwargs["fix"] = False
        return final_kwargs

    def set_property(self, path: str, value: Any, **kwargs: Any) -> None:
        """
        .. warning:: This method is deprecated. Use :meth:`set_stac_property` instead.

        :param path: Path to the property in the container attrs (e.g., "metadata/sensor").
        :param value: Value to set for the specified property (e.g., "Landsat-8").
        :param kwargs: Additional parameters for customization, passed to
                       :meth:`set_stac_property`.
        """
        warnings.warn("use set_stac_property instead", DeprecationWarning)
        self.set_stac_property(path, value, **kwargs)

    def set_stac_property(self, path: str, value: Any, **kwargs: Any) -> None:
        """
        Set a property in the STAC stac_discovery/properties dict. path is relative to properties.

        >>> d = {}
        >>> attrs = AttributeHandler(d)
        >>> attrs.set_stac_property("subgroup/a", 1)
        >>> attrs.set_stac_property("subgroup/b", 2)
        >>> d
        {'stac_discovery': {'properties': {'subgroup': {'a': 1, 'b': 2}}}}

        :param path: Key path to the STAC property (e.g., 'cloud_cover').
        :param value: Value to set for the property (e.g., 45 or "High").
        :param kwargs: Additional keyword arguments to provide to the fix method.
        """
        kwargs = self._update_kwargs(kwargs)
        set_attr(self._container, path, value, category="stac_properties", **kwargs)

    def set_metadata(self, path: str, value: Any, **kwargs: Any) -> None:
        """
        Set a value in the other_metadata dict. path is relative to this dict.
        Alias for :meth:`set_attr` with category="metadata".

        >>> d = {}
        >>> attrs = AttributeHandler(d)
        >>> attrs.set_metadata("subgroup/a", 1)
        >>> attrs.set_metadata("subgroup/b", 2)
        >>> d
        {'other_metadata': {'subgroup': {'a': 1, 'b': 2}}}

        :param path: Key path to the STAC property (e.g., 'cloud_cover').
        :param value: Value to set for the property (e.g., 45 or "High").
        :param kwargs: Additional keyword arguments to provide to the fix method.
        """
        kwargs = self._update_kwargs(kwargs)
        set_attr(self._container, path, value, category="metadata", **kwargs)

    def set_stac(self, path: str, value: Any, **kwargs: Any) -> None:
        """
        Set a value in the STAC stac_discovery dict. path is relative to stac_discovery.
        Alias for :meth:`set_attr` with category="stac_discovery".

        >>> d = {}
        >>> attrs = AttributeHandler(d)
        >>> attrs.set_stac("subgroup/a", 1)
        >>> attrs.set_stac("subgroup/b", 2)
        >>> d
        {'stac_discovery': {'subgroup': {'a': 1, 'b': 2}}}

        :param path: Key path to the STAC property (e.g., 'cloud_cover').
        :param value: Value to set for the property (e.g., 45 or "High").
        :param kwargs: Additional keyword arguments to provide to the fix method.
        """
        kwargs = self._update_kwargs(kwargs)
        set_attr(self._container, path, value, category="stac_discovery", **kwargs)

    def set_root_attr(self, path: str, value: Any, **kwargs: Any) -> None:
        """
        Set a value in the metadata.
        Alias for :meth:`set_attr` with category="root".

        >>> d = {}
        >>> attrs = AttributeHandler(d)
        >>> attrs.set_root_attr("a/b/c", 1)
        >>> d
        {'a': {'b': {'c': 1}}}

        :param path: Key path to the STAC property (e.g., 'cloud_cover').
        :param value: Value to set for the property (e.g., 45 or "High").
        :param kwargs: Additional keyword arguments to provide to the fix method.
        """
        kwargs = self._update_kwargs(kwargs)
        set_attr(self._container, path, value, category="root", **kwargs)

    def set_attr(self, path: str, value: Any, category: MetadataType_L | None = None, **kwargs: Any) -> None:
        """
        Set a value in the metadata. Category determines the group to set metadata. If category is not set the function
        tries to determine the right category thanks to hotfix.

        >>> d = {}
        >>> attrs = AttributeHandler(d)
        >>> attrs.set_attr("product:type", "S03OLCERR")
        >>> attrs.set_attr("root_prop", "R1")
        >>> attrs.set_attr("metadata_prop", "M1", category="metadata")
        >>> d
        {'stac_discovery': {'properties': {'product:type': 'S03OLCERR'}}, 'root_prop': 'R1', 'other_metadata': {'prop': 'M1'}}

        :param path: Key path to the STAC property (e.g., 'cloud_cover').
        :param value: Value to set for the property (e.g., 45 or "High").
        :param kwargs: Additional keyword arguments to provide to the fix method.
        """  # noqa: E501
        kwargs = self._update_kwargs(kwargs)
        set_attr(self._container, path, value, category=category, **kwargs)

    def get_attr(self, path: str | None = None, category: MetadataType_L | None = None, **kwargs: Any) -> Any:
        kwargs = self._update_kwargs(kwargs)
        return extract_attr(self._container, path, category=category, **kwargs)

    def get_stac_property(self, path: str | None = None, **kwargs: Any) -> Any:
        kwargs = self._update_kwargs(kwargs)
        return extract_attr(self._container, path, category="stac_properties", **kwargs)

    def get_metadata(self, path: str | None = None, **kwargs: Any) -> Any:
        kwargs = self._update_kwargs(kwargs)
        return extract_attr(self._container, path, category="metadata", **kwargs)

    def get_stac(self, path: str | None = None, **kwargs: Any) -> Any:
        kwargs = self._update_kwargs(kwargs)
        return extract_attr(self._container, path, category="stac_discovery", **kwargs)

    def get_root_attr(self, path: str | None = None, **kwargs: Any) -> Any:
        kwargs = self._update_kwargs(kwargs)
        return extract_attr(self._container, path, category="root", **kwargs)

    def search(
        self,
        path: str,
        *,
        category: MetadataType_L | None = None,
        **kwargs: Any,
    ) -> list[str]:
        kwargs = self._update_kwargs(kwargs)
        return search_attributes(self._container, path, category=category, **kwargs)

    def fix_path(self, path: str, **kwargs: Any) -> str:
        kwargs = self._update_kwargs(kwargs)
        return fix_attribute_path(path, **kwargs)[0]

    def _help(
        self,
        path: str,
        description_data: list[Any],
        documentation_data: list[Any],
        **kwargs: Any,
    ) -> dict[str, Any]:
        kwargs = self._update_kwargs(kwargs)
        help_data = {}
        attrs = _get_attr_dict(self._container)
        try:
            value, fixed, real = find_and_fix_attribute(attrs, path, **kwargs)
        except KeyError:
            pass
        else:

            help_data["value"] = value
            path = real
        category = guess_category(path, **kwargs)
        path = self.fix_path(path, category=category)
        name = Path(path).name
        if category:
            help_data["category"] = category
            help_data["path"] = path
        if category == "stac_properties":
            from sentineltoolbox.stacutils import STAC_PROPERTIES

            try:
                data, _, _ = find_and_fix_attribute(STAC_PROPERTIES, name, category=category, **kwargs)
            except KeyError:
                pass
            else:
                help_data.update(copy.copy(data))
        for field, field_dbs in [
            ("description", description_data),
            ("documentation", documentation_data),
        ]:
            for db in field_dbs:
                try:
                    found, _, _ = find_and_fix_attribute(db, name, **kwargs)
                except KeyError:
                    pass
                else:
                    if found is None:
                        continue
                    help_data[field] = found
                    break
        return help_data

    def apply_hotfix(self, hotfix: Hotfix, attrs: T_Attributes, **kwargs: Any) -> None:
        trace = kwargs.get("trace", False)
        if hotfix.hotfix_type == "path":
            for wrong_path, correct_data in hotfix.data.items():
                correct_cat, correct_rel_path = correct_data
                correct_path, correct_cat = fix_attribute_path(correct_rel_path, correct_cat, **kwargs)
                try:
                    value = _get_value_from_path(attrs, wrong_path)
                except KeyError:
                    pass
                else:
                    if correct_path != wrong_path:
                        if trace:
                            self._fixes.append((wrong_path, wrong_path, correct_path, hotfix))
                        pp = PurePosixPath(wrong_path)
                        parent = pp.parent.as_posix()
                        if parent == ".":
                            old_data = attrs
                            del old_data[pp.name]
                        else:
                            old_data = self.get_attr(parent)
                            del old_data[pp.name]
                    self.set_attr(correct_path, value, category=correct_cat, fix=False, format=False)

        elif hotfix.hotfix_type in ("value", "wrapper"):
            # thanks to dynamic fix done by get_attr, we can fix internal dict by getting value concerned by a hotfix
            # and set it back to dict directly. We set fix=False to setter to not fix it twice
            for category, attr_dict in hotfix.data.items():
                for attr_relpath, converter in attr_dict.items():
                    try:
                        current_value = self.get_attr(attr_relpath, category=category)
                    except KeyError:
                        pass
                    else:
                        old_value = self.get_attr(attr_relpath, category=category, fix=False, format=False)
                        try:
                            diff = bool(old_value != current_value)  # convert to bool to force evaluation here
                        except ValueError:
                            pass
                        else:
                            if diff:
                                if trace:
                                    self._fixes.append((attr_relpath, old_value, current_value, hotfix))
                                self.set_attr(
                                    attr_relpath,
                                    current_value,
                                    category=category,
                                    fix=False,
                                    format=False,
                                )  # already fixed by get_attr

        elif hotfix.hotfix_type == "attrs" and isinstance(hotfix.data, AttrsVisitor):
            visit_attrs(_get_attr_dict(self._container), hotfix.data)
        else:
            pass

    def fix(self, **kwargs: Any) -> None:
        from sentineltoolbox.metadata_utils import guess_product_type

        # apply hotfixes except if cache=True is specified
        container_id = id(self._container)
        cache = kwargs.get("cache", False)
        force = not cache or container_id not in self._fixed_containers
        if force:
            self._fixes.clear()
            kwargs = self._update_kwargs(kwargs)
            hotfix_manager, kwargs = get_hotfix_manager(**kwargs)
            attrs = _get_attr_dict(self._container)
            if attrs is None:
                attrs = {}
            for hotfix in hotfix_manager.hotfix_list:
                # compute product:type for each hotfix because a previous hotfix may have changed it
                product_type = guess_product_type(self._container)
                if not hotfix.is_applicable(attrs, product_type):
                    continue
                logger.info(f"apply hotfix <{hotfix.name}> {hotfix.description} (priority={hotfix.priority})")
                kwargs = copy.copy(kwargs)
                self.apply_hotfix(hotfix, attrs, **kwargs)
            AttributeHandler._fixed_containers.add(container_id)
        else:
            logger.info("fix skipped - already applied")

    def help_product(self, path: str, **kwargs: Any) -> dict[Any, Any]:
        from sentineltoolbox.resources.data import ProductMetadataResource

        kwargs = self._update_kwargs(kwargs)
        metadata = ProductMetadataResource(data=None, relpath="metadata/datafiles.json", **kwargs)
        description_data = [metadata.map("description")]
        documentation_data = [metadata.map("documentation")]

        return self._help(path, description_data, documentation_data, **kwargs)

    def help_attr(self, path: str, **kwargs: Any) -> dict[Any, Any]:
        from sentineltoolbox.resources.data import ResourceDb

        kwargs = self._update_kwargs(kwargs)
        properties = ResourceDb(relpath="metadata/properties.json", **kwargs)
        terms = ResourceDb(relpath="metadata/terms.json", **kwargs)

        description_data = [properties.map("description"), terms.map("description")]
        documentation_data = [properties.map("documentation"), terms.map("documentation")]

        return self._help(path, description_data, documentation_data, **kwargs)

    def help(self, path: str, **kwargs: Any) -> dict[Any, Any]:
        kwargs = self._update_kwargs(kwargs)
        return self.help_attr(path, **kwargs)
