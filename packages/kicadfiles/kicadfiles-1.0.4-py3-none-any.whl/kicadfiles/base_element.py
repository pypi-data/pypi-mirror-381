"""Optimized S-expression parser for KiCad objects with cursor-based approach."""

from __future__ import annotations

import logging
from abc import ABC
from dataclasses import MISSING, dataclass, field, fields
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
    cast,
    get_args,
    get_origin,
    get_type_hints,
)

from .sexpdata import Symbol
from .sexpr_parser import SExpr, SExprParser, str_to_sexpr

T = TypeVar("T", bound="KiCadObject")


@dataclass(eq=False)
class KiCadPrimitive(ABC):
    """Base class for KiCad primitive values - simplified like OptionalFlag."""

    base_type: ClassVar[type] = object  # To be overridden in subclasses

    token_name: str
    value: Any = None
    required: bool = True
    __found__: bool = field(default=False, init=False)

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        parts = [repr(self.value)]
        if self.token_name:
            parts.append(f"token={repr(self.token_name)}")
        parts.append(f"found={self.__found__}")
        return f"{self.__class__.__name__}({', '.join(parts)})"

    def __bool__(self) -> bool:
        """Boolean conversion - returns True if found and has truthy value."""
        return self.__found__

    def __call__(self, value: Any) -> "KiCadPrimitive":
        """Set value using function call syntax: primitive(new_value)."""
        self.value = value
        self.__found__ = True
        return self

    def is_optional(self) -> bool:
        """Check if this primitive is optional (not required)."""
        return not self.required

    def to_sexpr(self) -> Optional[List[Any]]:
        """Convert to S-expression format."""
        if not self.__found__ and not self.required:
            return None

        return [self.token_name, self.value]

    def __eq__(self, other: object) -> bool:
        """Equality comparison excluding __found__ and required fields."""
        if not isinstance(other, KiCadPrimitive):
            return False

        return (
            self.__class__ == other.__class__
            and self.token_name == other.token_name
            and self.value == other.value
        )


@dataclass(eq=False)
class KiCadStr(KiCadPrimitive):
    """String wrapper for KiCad values."""

    base_type: ClassVar[type] = str

    token_name: str = ""
    value: str = ""
    required: bool = True


@dataclass(eq=False)
class KiCadInt(KiCadPrimitive):
    """Integer wrapper for KiCad values."""

    base_type: ClassVar[type] = int

    token_name: str = ""
    value: int = 0
    required: bool = True


@dataclass(eq=False)
class KiCadFloat(KiCadPrimitive):
    """Float wrapper for KiCad values."""

    base_type: ClassVar[type] = float

    token_name: str = ""
    value: float = 0.0
    required: bool = True


@dataclass
class ParseCursor:
    """Lightweight cursor for tracking position in S-expression."""

    sexpr: SExpr  # Current S-expression
    parser: SExprParser  # Single parser (passed through)
    path: List[str]  # Path for debugging
    strictness: ParseStrictness  # Parse strictness level

    def enter(self, sexpr: SExpr, name: str) -> "ParseCursor":
        """Create new cursor for nested object."""
        # Create new parser for nested object to track usage independently
        nested_parser = SExprParser(sexpr)
        return ParseCursor(
            sexpr=sexpr,
            parser=nested_parser,  # New parser for nested object
            path=self.path + [name],
            strictness=self.strictness,  # Pass through strictness
        )

    def get_path_str(self) -> str:
        return " > ".join(self.path)


class ParseStrictness(Enum):
    """Parser strictness levels for error handling."""

    STRICT = "strict"  # Raise exceptions for all parsing errors
    SILENT = "silent"  # Silently use defaults for missing fields
    FAILSAFE = "failsafe"  # Log warnings and use defaults for missing fields


class FieldType(Enum):
    """Optimized classification with correct Optional/Required handling."""

    PRIMITIVE = "primitive"  # str, int, float (required)
    OPTIONAL_PRIMITIVE = "optional_primitive"  # Optional[str], etc. (optional)
    KICAD_PRIMITIVE = "kicad_primitive"  # KiCadStr, KiCadInt, KiCadFloat (required)
    OPTIONAL_KICAD_PRIMITIVE = (
        "optional_kicad_primitive"  # Optional[KiCadStr], etc. (optional)
    )
    LIST = "list"  # List[T] AND Optional[List[T]] - both treated equally!
    KICAD_OBJECT = "kicad_object"  # KiCadObject (required)
    OPTIONAL_KICAD_OBJECT = "optional_kicad_object"  # Optional[KiCadObject] (optional)
    OPTIONAL_FLAG = "optional_flag"  # OptionalFlag (always optional by definition)
    OPTIONAL_SIMPLE_FLAG = "optional_simple_flag"  # OptionalSimpleFlag (always optional, simple symbols only)


@dataclass
class FieldInfo:
    """Complete field information for optimized parsing."""

    name: str
    field_type: FieldType
    inner_type: Type[Any]
    position_index: int
    token_name: Optional[str] = None


@dataclass
class KiCadObject(ABC):
    """Base class for KiCad S-expression objects with cursor-based parsing."""

    __token_name__: ClassVar[str] = ""
    __legacy_token_names__: ClassVar[List[str]] = []
    _field_info_cache: ClassVar[List[FieldInfo]]
    _field_defaults_cache: ClassVar[Dict[str, Any]]

    def __post_init__(self) -> None:
        """Validate token name is defined."""
        if not self.__token_name__:
            raise ValueError(
                f"Class {self.__class__.__name__} must define __token_name__"
            )

    @classmethod
    def _log_parse_issue(cls, cursor: ParseCursor, message: str) -> None:
        """Log parsing issues based on strictness level from cursor."""
        if cursor.strictness == ParseStrictness.STRICT:
            raise ValueError(message)
        elif cursor.strictness == ParseStrictness.FAILSAFE:
            logging.warning(message)
        # SILENT mode: do nothing

    @classmethod
    def from_sexpr(
        cls: Type[T],
        sexpr: Union[str, SExpr],
        strictness: ParseStrictness = ParseStrictness.STRICT,
    ) -> T:
        """Single public entry point - parser created once here."""

        # Create parser only once here
        if isinstance(sexpr, str):
            parser = SExprParser.from_string(sexpr)
            sexpr = parser.sexpr
        else:
            parser = SExprParser(sexpr)

        # Create cursor with parser and parse directly
        cursor = ParseCursor(
            sexpr=sexpr, parser=parser, path=[cls.__name__], strictness=strictness
        )
        return cls._parse_recursive(cursor)

    @classmethod
    def from_str(
        cls: Type[T],
        sexpr_string: str,
        strictness: ParseStrictness = ParseStrictness.STRICT,
    ) -> T:
        """Parse from S-expression string - convenience method for better clarity."""
        sexpr = str_to_sexpr(sexpr_string)
        return cls.from_sexpr(sexpr, strictness)

    @classmethod
    def _parse_recursive(cls: Type[T], cursor: ParseCursor) -> T:
        """Internal recursive parse function - uses existing parser."""

        token = str(cursor.sexpr[0]) if cursor.sexpr else "empty"
        valid_tokens = [cls.__token_name__] + (cls.__legacy_token_names__ or [])

        if not cursor.sexpr or token not in valid_tokens:
            raise ValueError(
                f"Token mismatch at {cursor.get_path_str()}: "
                f"expected '{cls.__token_name__}', got '{token}'"
            )

        field_infos = cls._classify_fields()
        field_defaults = cls._get_field_defaults()
        parsed_values = {}

        for field_info in field_infos:
            value = cls._parse_field_recursive(field_info, cursor, field_defaults)
            if value is not None:
                parsed_values[field_info.name] = value
            elif field_info.name in field_defaults:
                parsed_values[field_info.name] = field_defaults[field_info.name]

        # Check for unused parameters and warn
        unused = cursor.parser.get_unused_parameters()
        if unused and cursor.strictness != ParseStrictness.SILENT:
            unused_summary = cls._format_unused_parameters(unused)
            cls._log_parse_issue(
                cursor,
                f"{cursor.get_path_str()}: Unused parameters in {cls.__name__}: {unused_summary}",
            )

        return cls(**parsed_values)

    @classmethod
    def _format_unused_parameters(cls, unused: List[Any]) -> str:
        """Format unused parameters for concise logging.

        Args:
            unused: List of unused S-expression parameters

        Returns:
            Concise string representation of unused parameters
        """
        if not unused:
            return "[]"

        # Create short representations of each unused parameter
        short_params = []
        for param in unused:
            if isinstance(param, list) and len(param) > 0:
                # For lists, show first element (token name) and count
                token_name = param[0] if param else "unknown"
                short_params.append(f"{token_name}[{len(param) - 1} params]")
            else:
                # For simple values, show them directly but truncate if too long
                param_str = str(param)
                if len(param_str) > 30:
                    short_params.append(f"{param_str[:27]}...")
                else:
                    short_params.append(param_str)

        return f"[{', '.join(short_params)}] ({len(unused)} total)"

    @classmethod
    def _classify_fields(cls) -> List[FieldInfo]:
        """Pre-classify all fields for optimized parsing with caching."""
        if not hasattr(cls, "_field_info_cache"):
            field_types = get_type_hints(cls)
            field_infos: List[FieldInfo] = []
            position_index = 0

            for dataclass_field in fields(cls):
                if dataclass_field.name.startswith("_"):
                    continue

                field_type = field_types[dataclass_field.name]
                field_info = cls._classify_field(
                    dataclass_field.name, field_type, position_index
                )
                field_infos.append(field_info)

                # OptionalSimpleFlag doesn't consume positional slots
                if field_info.field_type != FieldType.OPTIONAL_SIMPLE_FLAG:
                    position_index += 1

            cls._field_info_cache = field_infos

        return cls._field_info_cache

    @classmethod
    def _get_field_defaults(cls) -> Dict[str, Any]:
        """Get field defaults with caching."""
        if not hasattr(cls, "_field_defaults_cache"):
            result = {}
            for f in fields(cls):
                if f.default != MISSING:
                    result[f.name] = f.default
                elif f.default_factory != MISSING:  # type: ignore
                    # Call default_factory to get the actual default instance
                    result[f.name] = f.default_factory()  # type: ignore
            cls._field_defaults_cache = result
        return cls._field_defaults_cache

    @classmethod
    def _classify_field(
        cls, name: str, field_type: Type[Any], position: int
    ) -> FieldInfo:
        """Correct classification with list simplification."""

        is_optional = get_origin(field_type) is Union and type(None) in get_args(
            field_type
        )
        inner_type = field_type
        if is_optional:
            inner_type = next(
                arg for arg in get_args(field_type) if arg is not type(None)
            )

        # Lists are ALWAYS treated equally - Optional[List] = List
        if get_origin(inner_type) in (list, List):
            list_element_type = get_args(inner_type)[0] if get_args(inner_type) else str

            # Handle Union types in lists (e.g., List[Union[Arc, Circle, ...]])
            if get_origin(list_element_type) is Union:
                # For Union types, we'll use a special marker to indicate multi-token parsing
                return FieldInfo(
                    name=name,
                    field_type=FieldType.LIST,
                    inner_type=list_element_type,
                    position_index=position,
                    token_name="__UNION__",  # Special marker for union types
                )

            return FieldInfo(
                name=name,
                field_type=FieldType.LIST,  # Always LIST, never optional
                inner_type=list_element_type,
                position_index=position,
                token_name=(
                    getattr(list_element_type, "__token_name__", None)
                    if hasattr(list_element_type, "__token_name__")
                    else None
                ),
            )

        # OptionalSimpleFlag (check before OptionalFlag since it's more specific)
        try:
            if isinstance(inner_type, type) and issubclass(
                inner_type, OptionalSimpleFlag
            ):
                return FieldInfo(
                    name=name,
                    field_type=FieldType.OPTIONAL_SIMPLE_FLAG,
                    inner_type=inner_type,
                    position_index=position,
                )
        except TypeError:
            pass

        # OptionalFlag
        try:
            if isinstance(inner_type, type) and issubclass(inner_type, OptionalFlag):
                return FieldInfo(
                    name=name,
                    field_type=FieldType.OPTIONAL_FLAG,
                    inner_type=inner_type,
                    position_index=position,
                )
        except TypeError:
            pass

        # KiCadPrimitive
        try:
            if isinstance(inner_type, type) and issubclass(inner_type, KiCadPrimitive):
                # Check default value to see if it's optional
                field_defaults = cls._get_field_defaults()
                default_value = field_defaults.get(name)

                # Determine if optional based on:
                # 1. Type hint is Optional[]
                # 2. Default value exists and is_optional() returns True
                is_kicad_optional = is_optional or (
                    default_value is not None
                    and hasattr(default_value, "is_optional")
                    and default_value.is_optional()
                )

                field_type_enum = (
                    FieldType.OPTIONAL_KICAD_PRIMITIVE
                    if is_kicad_optional
                    else FieldType.KICAD_PRIMITIVE
                )
                return FieldInfo(
                    name=name,
                    field_type=field_type_enum,
                    inner_type=inner_type,
                    position_index=position,
                    token_name=name,  # Use field name as token name by default
                )
        except TypeError:
            pass

        # KiCadObject
        try:
            if isinstance(inner_type, type) and issubclass(inner_type, KiCadObject):
                field_type_enum = (
                    FieldType.OPTIONAL_KICAD_OBJECT
                    if is_optional
                    else FieldType.KICAD_OBJECT
                )
                return FieldInfo(
                    name=name,
                    field_type=field_type_enum,
                    inner_type=inner_type,
                    position_index=position,
                    token_name=getattr(inner_type, "__token_name__", None),
                )
        except TypeError:
            pass

        # Primitive
        field_type_enum = (
            FieldType.OPTIONAL_PRIMITIVE if is_optional else FieldType.PRIMITIVE
        )
        return FieldInfo(
            name=name,
            field_type=field_type_enum,
            inner_type=inner_type,
            position_index=position,
        )

    @classmethod
    def _parse_field_recursive(
        cls,
        field_info: FieldInfo,
        cursor: ParseCursor,
        field_defaults: Dict[str, Any],
    ) -> Any:
        """Simplified logic with correct Required/Optional handling."""

        if field_info.field_type == FieldType.LIST:
            return cls._parse_list_with_cursor(field_info, cursor)

        elif field_info.field_type == FieldType.OPTIONAL_FLAG:
            return cls._parse_optional_flag_with_cursor(field_info, cursor)

        elif field_info.field_type == FieldType.OPTIONAL_SIMPLE_FLAG:
            return cls._parse_optional_simple_flag_with_cursor(field_info, cursor)

        elif field_info.field_type in (
            FieldType.KICAD_OBJECT,
            FieldType.OPTIONAL_KICAD_OBJECT,
        ):
            result = cls._parse_nested_object(field_info, cursor)
            # Validation: Required objects must be found
            if result is None and field_info.field_type == FieldType.KICAD_OBJECT:
                cls._log_parse_issue(
                    cursor,
                    f"{cursor.get_path_str()}: Required object '{field_info.name}' not found",
                )
            return result

        elif field_info.field_type in (
            FieldType.KICAD_PRIMITIVE,
            FieldType.OPTIONAL_KICAD_PRIMITIVE,
        ):
            primitive_result = cls._parse_kicad_primitive_with_cursor(
                field_info, cursor, field_defaults
            )
            # Validation: Required KiCad primitives must be found
            if (
                primitive_result is None
                and field_info.field_type == FieldType.KICAD_PRIMITIVE
            ):
                cls._log_parse_issue(
                    cursor,
                    f"{cursor.get_path_str()}: Required KiCad primitive '{field_info.name}' not found",
                )
            return primitive_result

        else:  # PRIMITIVE or OPTIONAL_PRIMITIVE
            result = cls._parse_primitive_with_cursor(
                field_info, cursor, field_defaults
            )
            # Validation: Required primitives must be found
            if result is None and field_info.field_type == FieldType.PRIMITIVE:
                cls._log_parse_issue(
                    cursor,
                    f"{cursor.get_path_str()}: Required field '{field_info.name}' not found",
                )
            return result

    @classmethod
    def _parse_list_with_cursor(
        cls,
        field_info: FieldInfo,
        cursor: ParseCursor,
    ) -> List[Any]:
        """Parse list of values with cursor tracking."""
        result: List[Any] = []
        _ = cursor.sexpr[0]  # Token at index 0, skip in enumeration

        if field_info.token_name:  # List of KiCadObjects
            if field_info.token_name == "__UNION__":  # Special handling for Union types
                # Get all possible types from the Union
                union_types = get_args(field_info.inner_type)
                # Create a mapping from token_name to type
                token_to_type = {}
                for union_type in union_types:
                    if hasattr(union_type, "__token_name__"):
                        token_to_type[union_type.__token_name__] = union_type

                # Parse items by matching their token names
                for token_idx, item in enumerate(cursor.sexpr[1:], 1):
                    if isinstance(item, list) and item:
                        item_token = str(item[0])
                        if item_token in token_to_type:
                            cursor.parser.mark_used(token_idx)
                            item_cursor = cursor.enter(
                                item, f"{item_token}[{len(result)}]"
                            )
                            parsed_item = token_to_type[item_token]._parse_recursive(
                                item_cursor
                            )
                            result.append(parsed_item)
            else:
                # Original single-type parsing
                for token_idx, item in enumerate(cursor.sexpr[1:], 1):
                    if (
                        isinstance(item, list)
                        and item
                        and str(item[0]) == field_info.token_name
                    ):
                        cursor.parser.mark_used(token_idx)  # Mark in main parser
                        item_cursor = cursor.enter(
                            item, f"{field_info.token_name}[{len(result)}]"
                        )
                        parsed_item = field_info.inner_type._parse_recursive(
                            item_cursor
                        )
                        result.append(parsed_item)
        else:  # List of primitives
            list_fields = [
                fi for fi in cls._classify_fields() if fi.field_type == FieldType.LIST
            ]
            if len(list_fields) == 1:
                for token_idx, item in enumerate(cursor.sexpr[1:], 1):
                    if token_idx not in cursor.parser.used_indices and not isinstance(
                        item, list
                    ):
                        cursor.parser.mark_used(token_idx)
                        converted = cls._convert_value(item, field_info.inner_type)
                        result.append(converted)

        return result  # Always list, never None

    @classmethod
    def _parse_nested_object(
        cls,
        field_info: FieldInfo,
        cursor: ParseCursor,
    ) -> Optional[KiCadObject]:
        """Parse nested KiCadObject using token name."""
        if not field_info.token_name:
            return None

        _ = cursor.sexpr[0]  # Token at index 0, skip in enumeration
        for token_idx, item in enumerate(cursor.sexpr[1:], 1):
            if (
                isinstance(item, list)
                and item
                and str(item[0]) == field_info.token_name
            ):
                cursor.parser.mark_used(token_idx)  # Mark in main parser
                nested_cursor = cursor.enter(item, field_info.token_name)
                return cast(
                    KiCadObject,
                    field_info.inner_type._parse_recursive(nested_cursor),
                )

        return None

    @classmethod
    def _parse_optional_flag_with_cursor(
        cls,
        field_info: FieldInfo,
        cursor: ParseCursor,
    ) -> Optional[OptionalFlag]:
        """Parse OptionalFlag with cursor tracking."""
        _ = cursor.sexpr[0]  # Token at index 0, skip in enumeration

        for token_idx, item in enumerate(cursor.sexpr[1:], 1):
            # Handle both simple flags and flags with values
            if (
                isinstance(item, list)
                and len(item) >= 1
                and str(item[0]) == field_info.name
            ):
                cursor.parser.mark_used(token_idx)  # Mark in main parser
                token_value = str(item[1]) if len(item) > 1 else None
                result = OptionalFlag(
                    field_info.name, is_token=True, token_value=token_value
                )
                result.__found__ = True
                return result
            elif str(item) == field_info.name:
                cursor.parser.mark_used(token_idx)  # Mark in main parser
                result = OptionalFlag(field_info.name, is_token=True)
                result.__found__ = True
                return result

        # Not found - return None for optional fields
        return None

    @classmethod
    def _parse_optional_simple_flag_with_cursor(
        cls,
        field_info: FieldInfo,
        cursor: ParseCursor,
    ) -> Optional[OptionalSimpleFlag]:
        """Parse OptionalSimpleFlag with cursor tracking.

        Only matches simple symbols (not S-expressions).
        """
        _ = cursor.sexpr[0]  # Token at index 0, skip in enumeration

        for token_idx, item in enumerate(cursor.sexpr[1:], 1):
            # Only match simple symbols, NOT lists
            if not isinstance(item, list) and str(item) == field_info.name:
                cursor.parser.mark_used(token_idx)  # Mark in main parser
                result = OptionalSimpleFlag(field_info.name)
                result.__found__ = True
                return result

        # Not found - return None for optional fields
        return None

    @classmethod
    def _parse_kicad_primitive_with_cursor(
        cls,
        field_info: FieldInfo,
        cursor: ParseCursor,
        field_defaults: Dict[str, Any],
    ) -> Optional[KiCadPrimitive]:
        """Parse KiCad primitive value."""
        is_required = field_info.field_type == FieldType.KICAD_PRIMITIVE

        def create_instance(
            raw_value: Any, token_name: str, found: bool = True
        ) -> KiCadPrimitive:
            """Helper to create and configure KiCadPrimitive instance."""
            instance = field_info.inner_type(token_name, raw_value, is_required)
            instance.__found__ = found
            return cast(KiCadPrimitive, instance)

        # Determine the token name to search for
        # If there's a default value with a token_name, use that
        # Otherwise use the field name
        search_token_name = field_info.name
        default_value = field_defaults.get(field_info.name)
        if default_value is not None and isinstance(default_value, KiCadPrimitive):
            if default_value.token_name:
                search_token_name = default_value.token_name

        # Search for field in S-expression
        for token_idx, item in enumerate(cursor.sexpr[1:], 1):
            # Named form: (token_name value)
            if (
                isinstance(item, list)
                and len(item) >= 2
                and str(item[0]) == search_token_name
            ):
                cursor.parser.mark_used(token_idx)
                raw_value = cls._convert_value(item[1], field_info.inner_type.base_type)
                return create_instance(raw_value, search_token_name)

            # Positional form: plain value at expected position
            # Skip Symbol objects as they should be handled by OptionalFlag parsing
            if (
                not isinstance(item, list)
                and not isinstance(item, Symbol)
                and field_info.position_index == (token_idx - 1)
            ):
                cursor.parser.mark_used(token_idx)
                raw_value = cls._convert_value(item, field_info.inner_type.base_type)
                return create_instance(raw_value, "")

        # Field not found - handle defaults and missing values
        default_value = field_defaults.get(field_info.name)
        if default_value is not None:
            if is_required:
                cls._log_parse_issue(
                    cursor,
                    f"{cursor.get_path_str()}: Missing required field '{field_info.name}', using default",
                )
            return cast(Optional[KiCadPrimitive], default_value)

        # No default value available
        if is_required:
            cls._log_parse_issue(
                cursor,
                f"{cursor.get_path_str()}: Required KiCad primitive field '{field_info.name}' not found",
            )

        return None

    @classmethod
    def _parse_primitive_with_cursor(
        cls,
        field_info: FieldInfo,
        cursor: ParseCursor,
        field_defaults: Dict[str, Any],
    ) -> Any:
        """Parse primitive value with cursor tracking."""
        _ = cursor.sexpr[0]  # Token at index 0, skip in enumeration

        # Try named field first: (field_name value)
        for token_idx, item in enumerate(cursor.sexpr[1:], 1):
            if (
                isinstance(item, list)
                and len(item) >= 2
                and str(item[0]) == field_info.name
            ):
                cursor.parser.mark_used(token_idx)  # Mark in main parser
                try:
                    return cls._convert_value(item[1], field_info.inner_type)
                except ValueError as e:
                    cls._log_parse_issue(
                        cursor,
                        f"{cursor.get_path_str()}: Conversion failed for '{field_info.name}': {e}",
                    )

        # Try positional access
        # Check if there are any OPTIONAL_SIMPLE_FLAG fields that might have consumed positions
        field_infos = cls._classify_fields()
        has_preceding_simple_flags = any(
            fi.field_type == FieldType.OPTIONAL_SIMPLE_FLAG
            and fi.position_index == field_info.position_index
            for fi in field_infos
        )

        if has_preceding_simple_flags:
            # Use loop-based parsing to skip values consumed by OptionalSimpleFlags
            positional_count = 0
            for token_idx, value in enumerate(cursor.sexpr[1:], 1):
                if isinstance(value, list):
                    continue
                if token_idx in cursor.parser.used_indices:
                    continue

                if positional_count == field_info.position_index:
                    cursor.parser.mark_used(token_idx)
                    try:
                        return cls._convert_value(value, field_info.inner_type)
                    except ValueError as e:
                        cls._log_parse_issue(
                            cursor,
                            f"{cursor.get_path_str()}: Positional conversion failed for '{field_info.name}': {e}",
                        )
                        break
                positional_count += 1
        else:
            # Use simple direct access for normal fields
            if field_info.position_index < len(cursor.sexpr[1:]):
                value = cursor.sexpr[1:][field_info.position_index]
                if not isinstance(value, list):
                    cursor.parser.mark_used(field_info.position_index + 1)
                    try:
                        return cls._convert_value(value, field_info.inner_type)
                    except ValueError as e:
                        cls._log_parse_issue(
                            cursor,
                            f"{cursor.get_path_str()}: Positional conversion failed for '{field_info.name}': {e}",
                        )

        # Handle missing values
        is_optional_field = field_info.field_type in (
            FieldType.OPTIONAL_PRIMITIVE,
            FieldType.OPTIONAL_KICAD_OBJECT,
            FieldType.OPTIONAL_FLAG,
        )

        default_value = field_defaults.get(field_info.name)
        if default_value is not None:
            if not is_optional_field:
                cls._log_parse_issue(
                    cursor,
                    f"{cursor.get_path_str()}: Missing field '{field_info.name}' (using default: {default_value})",
                )
            return default_value

        if not is_optional_field:
            cls._log_parse_issue(
                cursor,
                f"{cursor.get_path_str()}: Missing required field '{field_info.name}', returning None",
            )

        return None

    @classmethod
    def _convert_value(cls, value: Any, target_type: Type[Any]) -> Any:
        """Convert value to target type with error handling."""
        if value is None:
            raise ValueError(f"Cannot convert None to {target_type.__name__}")

        try:
            if target_type == int:
                return int(value)
            elif target_type == str:
                return str(value)
            elif target_type == float:
                return float(value)
            elif target_type == bool:
                return str(value).lower() in ("yes", "true", "1")
            elif isinstance(target_type, type) and issubclass(target_type, Enum):
                # Handle enum conversion - try by value first, then by name
                if isinstance(value, target_type):
                    return value
                try:
                    return target_type(value)
                except ValueError:
                    # Try by name if value lookup failed
                    return target_type[str(value).upper()]
            else:
                raise ValueError(f"Unsupported type: {target_type}")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Cannot convert '{value}' to {target_type.__name__}: {e}")

    def is_optional(self) -> bool:
        """Check if this object is optional (default: False for KiCadObject).

        Can be overridden in subclasses if needed.
        """
        return False

    def to_sexpr(self) -> SExpr:
        """Convert to S-expression using simple field iteration."""
        result: SExpr = [self.__token_name__]
        field_infos = self._classify_fields()
        field_defaults = self._get_field_defaults()

        for field_info in field_infos:
            value = getattr(self, field_info.name)

            # Lists are never None - always serialize (even if empty)
            if field_info.field_type == FieldType.LIST:
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, KiCadObject):
                            result.append(item.to_sexpr())
                        elif isinstance(item, Enum):
                            result.append(item.value)
                        else:
                            result.append(item)
                # Empty lists are serialized as empty, not skipped

            elif value is None:
                is_optional_field = field_info.field_type in (
                    FieldType.OPTIONAL_PRIMITIVE,
                    FieldType.OPTIONAL_KICAD_OBJECT,
                    FieldType.OPTIONAL_KICAD_PRIMITIVE,
                    FieldType.OPTIONAL_FLAG,
                    FieldType.OPTIONAL_SIMPLE_FLAG,
                )
                has_default = field_info.name in field_defaults

                if is_optional_field or has_default:
                    continue  # Skip optional None fields
                else:
                    raise ValueError(
                        f"Required field '{field_info.name}' is None in {self.__class__.__name__}. "
                        f"Field type: {field_info.field_type}"
                    )
            else:
                # Normal serialization for primitives/objects
                if isinstance(value, KiCadObject):
                    result.append(value.to_sexpr())
                elif isinstance(value, KiCadPrimitive):
                    # Serialize KiCad primitives using their to_sexpr method
                    # Only serialize if the primitive was actually found in parsing
                    if value.__found__:
                        sexpr = value.to_sexpr()
                        if sexpr is not None:
                            result.append(sexpr)
                elif isinstance(value, OptionalFlag):
                    # Only add the flag to the result if it was found
                    if value.__found__:
                        if value.token_value:
                            result.append([value.token, value.token_value])
                        else:
                            result.append([value.token])
                elif isinstance(value, OptionalSimpleFlag):
                    # Only add the simple flag if it was found
                    if value.__found__:
                        result.append(value.token)
                else:
                    # Primitives are added directly, not as named fields
                    # Convert enum to its value for serialization
                    if isinstance(value, Enum):
                        result.append(value.value)
                    else:
                        result.append(value)

        return result

    # def __eq__(self, other: object) -> bool:
    #     """Fast and robust equality comparison for KiCadObjects."""
    #     if not isinstance(other, KiCadObject):
    #         return False

    #     if self.__class__ != other.__class__:
    #         return False

    #     field_infos = self._classify_fields()

    #     for field_info in field_infos:
    #         self_value = getattr(self, field_info.name)
    #         other_value = getattr(other, field_info.name)

    #         if (self_value is None) != (other_value is None):
    #             return False

    #         if self_value is None and other_value is None:
    #             continue

    #         if not isinstance(other_value, type(self_value)):
    #             return False

    #         if isinstance(self_value, list):
    #             if len(self_value) != len(other_value):
    #                 return False

    #             for self_item, other_item in zip(self_value, other_value):
    #                 if isinstance(self_item, KiCadObject):
    #                     if not self_item.__eq__(other_item):  # Recursive comparison
    #                         return False
    #                 else:
    #                     if self_item != other_item:
    #                         return False

    #         elif isinstance(self_value, KiCadObject):
    #             if not self_value.__eq__(other_value):  # Recursive comparison
    #                 return False

    #         else:
    #             if self_value != other_value:
    #                 return False

    #     return True

    # def __hash__(self) -> int:
    #     """Hash implementation - required when implementing __eq__."""
    #     return hash((self.__class__.__name__, self.__token_name__))

    def to_sexpr_str(self, _indent_level: int = 0) -> str:
        """Convert to KiCad-formatted S-expression string using to_sexpr() with custom formatting.

        Args:
            _indent_level: Internal parameter for recursion depth

        Returns:
            Formatted S-expression string
        """
        sexpr = self.to_sexpr()
        return self._format_sexpr_kicad_style(sexpr, _indent_level)

    def _format_sexpr_kicad_style(self, sexpr: Any, indent_level: int = 0) -> str:
        """Format S-expression in KiCad style with tabs and unquoted tokens."""
        if not isinstance(sexpr, list):
            return self._format_primitive_value(sexpr)

        if not sexpr:
            return "()"

        current_indent = "\t" * indent_level
        token_name = str(sexpr[0])

        if len(sexpr) == 1:
            return f"{current_indent}({token_name})"

        # Separate primitives and nested lists
        primitive_values = []
        nested_lists = []

        for item in sexpr[1:]:
            if isinstance(item, list):
                nested_lists.append(item)
            else:
                if token_name in ("type") and isinstance(item, str):
                    primitive_values.append(item)  # No quotes for Type/Uuid values
                else:
                    primitive_values.append(self._format_primitive_value(item))

        # Check for single line format: only primitives and short enough
        if not nested_lists and len(sexpr) <= 4:
            all_items = [token_name] + primitive_values
            return f"{current_indent}({' '.join(all_items)})"

        # Multi-line format: primitives on first line, nested lists indented
        primitive_part = f" {' '.join(primitive_values)}" if primitive_values else ""
        lines = [f"{current_indent}({token_name}{primitive_part}"]

        for nested_item in nested_lists:
            nested_formatted = self._format_sexpr_kicad_style(
                nested_item, indent_level + 1
            )
            lines.append(nested_formatted)

        lines.append(f"{current_indent})")
        return "\n".join(lines)

    def _format_primitive_value(self, value: Any) -> str:
        """Format primitive values for S-expression serialization."""
        if isinstance(value, bool):
            return "yes" if value else "no"
        elif isinstance(value, Enum):
            return str(value.value)  # Enum values without quotes
        elif isinstance(value, str):
            # Check if this is a boolean-like token value (yes/no) - don't quote these
            if value in ("yes", "no"):
                return value
            # Escape backslashes first, then quotes (order is important!)
            escaped_value = value.replace("\\", "\\\\").replace('"', '\\"')
            return f'"{escaped_value}"'  # Regular strings are quoted
        else:
            return str(value)  # Numbers and other values as-is

    def __str__(self) -> str:
        """String representation showing only non-None values (except for required fields)."""
        field_infos = self._classify_fields()
        field_defaults = self._get_field_defaults()

        non_none_fields = []

        for field_info in field_infos:
            value = getattr(self, field_info.name)

            # Check if field is optional
            is_optional_field = field_info.field_type in (
                FieldType.OPTIONAL_PRIMITIVE,
                FieldType.OPTIONAL_KICAD_OBJECT,
                FieldType.OPTIONAL_KICAD_PRIMITIVE,
                FieldType.OPTIONAL_FLAG,
            )
            has_default = field_info.name in field_defaults

            # Show field if:
            # 1. Value is not None (for any field), OR
            # 2. Field is required (not optional and no default) even if None
            # Skip optional fields that are None
            if is_optional_field and value is None:
                continue
            elif value is not None or (not is_optional_field and not has_default):
                # Format value for display
                if isinstance(value, list) and len(value) == 0:
                    # Skip empty lists for optional fields
                    if is_optional_field or has_default:
                        continue
                    display_value = "[]"
                elif isinstance(value, OptionalFlag):
                    # Use OptionalFlag's own __str__ method
                    if value.__found__:
                        display_value = str(value)
                    else:
                        continue
                elif isinstance(value, KiCadObject):
                    # Use the custom __str__ for nested KiCadObjects
                    display_value = str(value)
                elif isinstance(value, KiCadPrimitive):
                    # Show KiCad primitive value with type info
                    display_value = f"{value.__class__.__name__}({value.value!r})"
                elif isinstance(value, list):
                    # Handle lists of KiCadObjects recursively
                    if value and isinstance(value[0], KiCadObject):
                        formatted_items = [str(item) for item in value]
                        display_value = f"[{', '.join(formatted_items)}]"
                    else:
                        display_value = repr(value)
                else:
                    display_value = repr(value)

                non_none_fields.append(f"{field_info.name}={display_value}")

        return f"{self.__class__.__name__}({', '.join(non_none_fields)})"


@dataclass
class OptionalFlag:
    """Enhanced flag container for optional tokens in S-expressions.

    Can handle:
    1. Simple presence flags: (locked) -> token="locked", is_token=True, token_value=None
    2. Tokens with values: (locked yes) -> token="locked", is_token=True, token_value="yes"
    3. Simple strings: "locked" -> token="locked", is_token=False, token_value=None
    """

    token: str
    token_value: Optional[str] = (
        None  # Additional value after token like "yes" in (locked yes)
    )
    is_token: bool = (
        True  # True if it was a token like (locked), False if simple string
    )
    __found__: bool = False

    def __str__(self) -> str:
        """Clean string representation."""
        if self.is_token:
            if self.token_value:
                return (
                    f"OptionalFlag(({self.token} {self.token_value})={self.__found__})"
                )
            else:
                return f"OptionalFlag(({self.token})={self.__found__})"
        else:
            return f"OptionalFlag({self.token}={self.__found__})"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        parts = [f"'{self.token}'"]

        if self.token_value is not None:
            parts.append(f"value={repr(self.token_value)}")

        if not self.is_token:
            parts.append("string")

        # Always show found status for consistency
        parts.append(f"found={self.__found__}")

        return f"OptionalFlag({', '.join(parts)})"

    def __eq__(self, other: object) -> bool:
        """Equality comparison excluding __found__ field."""
        if not isinstance(other, OptionalFlag):
            return False
        return (
            self.token == other.token
            and self.is_token == other.is_token
            and self.token_value == other.token_value
        )

    def __hash__(self) -> int:
        """Hash implementation - required when implementing __eq__."""
        return hash((self.token, self.is_token, self.token_value))

    def __call__(self, value: Optional[str] = None) -> "OptionalFlag":
        """Set token_value and mark as found using function call syntax: flag(value).

        Args:
            value: Optional token value to set

        Returns:
            self for chaining
        """
        if value is not None:
            self.token_value = value
        self.__found__ = True
        return self

    def __bool__(self) -> bool:
        """Boolean conversion - returns the logical boolean value based on token_value."""
        if not self.__found__:
            return False
        # If there's a token_value, interpret yes/no
        if self.token_value:
            return self.token_value.lower() in ("yes", "true", "1")
        # If no token_value, the presence of the flag means True
        return True

    def is_optional(self) -> bool:
        """Check if this flag is optional (always True for OptionalFlag)."""
        return True

    def to_sexpr(self) -> str:
        """Convert back to S-expression format for round-trip."""
        if not self.__found__:
            return ""

        if self.is_token:
            if self.token_value:
                return f"({self.token} {self.token_value})"
            else:
                return f"({self.token})"
        else:
            return self.token


@dataclass(eq=False)
class OptionalSimpleFlag:
    """Simple flag for optional symbol tokens (not S-expressions).

    This flag matches only simple symbols like 'oval', 'locked', etc.
    Unlike OptionalFlag, it does NOT match S-expressions like (locked yes).

    Used for flags that should NOT consume positional argument slots,
    like 'oval' in (drill oval 4 1.5).

    Args:
        token: The token name to match
        __found__: Whether the token was found during parsing
    """

    token: str
    __found__: bool = False

    def __str__(self) -> str:
        """Clean string representation."""
        return f"OptionalSimpleFlag({self.token}={self.__found__})"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"OptionalSimpleFlag('{self.token}', found={self.__found__})"

    def __eq__(self, other: object) -> bool:
        """Equality comparison excluding __found__ field."""
        if not isinstance(other, OptionalSimpleFlag):
            return False
        return self.token == other.token

    def __hash__(self) -> int:
        """Hash implementation."""
        return hash(self.token)

    def __bool__(self) -> bool:
        """Boolean conversion - returns True if found."""
        return self.__found__

    def __call__(self) -> "OptionalSimpleFlag":
        """Mark as found using function call syntax: flag()."""
        self.__found__ = True
        return self

    def is_optional(self) -> bool:
        """Check if this flag is optional (always True)."""
        return True

    def to_sexpr(self) -> str:
        """Convert back to S-expression format."""
        if not self.__found__:
            return ""
        return self.token
