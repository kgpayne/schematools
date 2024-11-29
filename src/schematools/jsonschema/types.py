from __future__ import annotations

import sys
import typing as t
from dataclasses import dataclass

if t.TYPE_CHECKING:

    if sys.version_info >= (3, 10):
        from typing import TypeAlias  # noqa: ICN003
    else:
        from typing_extensions import TypeAlias

_JsonValue: TypeAlias = t.Union[
    str,
    int,
    float,
    bool,
    list,
    dict,
    None,
]

T = t.TypeVar("T", bound=_JsonValue)


@dataclass(frozen=True)
class BaseJSONSchemaType:

    id: str | None = None
    schema: str | None = None
    comment: str | None = None
    type: str | list[str] | None = None
    title: str | None = None
    description: str | None = None
    default: T | None = None
    examples: t.List[T] | None = None
    readOnly: bool | None = None
    writeOnly: bool | None = None
    deprecated: bool | None = None
    enum: t.List[T] | None = None
    const: T | None = None


class UnionType(BaseJSONSchemaType):
    """Multi type."""

    type: t.List[str] | None = None

    def __post_init__(self):
        if self.type is None:
            raise ValueError("types must be provided")

    @classmethod
    def from_types(cls, types: t.List[t.Type[BaseJSONSchemaType]]) -> UnionType:
        """Create UnionType from types."""

        @dataclass(frozen=True, eq=False)
        class CustomUnionType(UnionType, *types):
            """Custom UnionType class."""

            type = [t.type for t in types]

        return CustomUnionType

    def is_nullable(self) -> bool:
        """Check if type is nullable."""
        return any(isinstance(t, NullType) for t in self.type)


@dataclass(frozen=True)
class BooleanType(BaseJSONSchemaType):
    """Boolean type."""

    type: str = "boolean"


@dataclass(frozen=True)
class NullType(BaseJSONSchemaType):
    """Null type."""

    type: str = "null"


############
# Object Type
############


@dataclass(frozen=True)
class ObjectType(BaseJSONSchemaType):
    """Object type."""

    type: str = "object"
    properties: t.Dict[str, BaseJSONSchemaType] | None = None
    additionalProperties: bool | BaseJSONSchemaType | None = None
    patternProperties: t.Dict[str, BaseJSONSchemaType] | None = None
    unevaluatedProperties: BaseJSONSchemaType | None = None
    required: t.List[str] | None = None
    minProperties: int | None = None
    maxProperties: int | None = None
    allOf: t.List[BaseJSONSchemaType] | None = None
    anyOf: t.List[BaseJSONSchemaType] | None = None
    oneOf: t.List[BaseJSONSchemaType] | None = None
    not_: BaseJSONSchemaType | None = None
    if_: BaseJSONSchemaType | None = None
    then: BaseJSONSchemaType | None = None
    else_: BaseJSONSchemaType | None = None
    propertyNames: BaseJSONSchemaType | None = None
    dependentRequired: t.Dict[str, t.List[str]] | None = None
    dependentSchemas: t.Dict[str, BaseJSONSchemaType] | None = None

    def has_properties(self) -> bool:
        """Check if object has properties."""
        return self.properties is not None


############
# Array Type
############


@dataclass(frozen=True)
class ArrayType(BaseJSONSchemaType):
    """Array type."""

    type: str = "array"
    items: BaseJSONSchemaType | bool | None = None
    prefixItems: t.List[BaseJSONSchemaType] | None = None
    additionalItems: BaseJSONSchemaType | bool | None = None
    unevaluatedItems: BaseJSONSchemaType | bool | None = None
    contains: BaseJSONSchemaType | None = None
    minContains: int | None = None
    maxContains: int | None = None
    minItems: int | None = None
    maxItems: int | None = None
    uniqueItems: bool | None = None


###############
# Numeric Types
###############


@dataclass(frozen=True)
class _NumericType(BaseJSONSchemaType):
    """Numeric type."""

    minimum: int | float | None = None
    maximum: int | float | None = None
    exclusiveMinimum: bool | None = None
    exclusiveMaximum: bool | None = None
    multipleOf: int | float | None = None


@dataclass(frozen=True)
class NumberType(_NumericType):
    """Number type."""

    type: str = "number"


@dataclass(frozen=True)
class IntegerType(_NumericType):
    """Integer type."""

    type: str = "integer"


##############
# String Types
##############


@dataclass(frozen=True)
class StringType(BaseJSONSchemaType):
    """String type."""

    type: str = "string"
    format: str | None = None
    minLength: int | None = None
    maxLength: int | None = None
    pattern: str | None = None

    @classmethod
    def from_jsonschema(cls, jsonschema: dict) -> StringType:
        string_format = jsonschema.get("format")
        if string_format is not None:
            return string_format_map[string_format](**jsonschema)
        return cls(**jsonschema)


@dataclass(frozen=True)
class DateTimeType(StringType):
    """DateTime type.

    Example: `2018-11-13T20:20:39+00:00`
    """

    format = "date-time"


@dataclass(frozen=True)
class TimeType(StringType):
    """Time type.

    Example: `20:20:39+00:00`
    """

    format = "time"


@dataclass(frozen=True)
class DateType(StringType):
    """Date type.

    Example: `2018-11-13`
    """

    format = "date"


@dataclass(frozen=True)
class DurationType(StringType):
    """Duration type.

    Example: `P3D`
    """

    format = "duration"


@dataclass(frozen=True)
class EmailType(StringType):
    """Email type."""

    format = "email"


@dataclass(frozen=True)
class HostnameType(StringType):
    """Hostname type."""

    format = "hostname"


@dataclass(frozen=True)
class IPv4Type(StringType):
    """IPv4 address type."""

    format = "ipv4"


@dataclass(frozen=True)
class IPv6Type(StringType):
    """IPv6 type."""

    format = "ipv6"


@dataclass(frozen=True)
class UUIDType(StringType):
    """UUID type.

    Example: `3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a`
    """

    format = "uuid"


@dataclass(frozen=True)
class URIType(StringType):
    """URI type."""

    format = "uri"


@dataclass(frozen=True)
class URIReferenceType(StringType):
    """URIReference type."""

    format = "uri-reference"


@dataclass(frozen=True)
class URITemplateType(StringType):
    """URITemplate type."""

    format = "uri-template"


@dataclass(frozen=True)
class JSONPointerType(StringType):
    """JSONPointer type."""

    format = "json-pointer"


@dataclass(frozen=True)
class RelativeJSONPointerType(StringType):
    """RelativeJSONPointer type."""

    format = "relative-json-pointer"


@dataclass(frozen=True)
class RegexType(StringType):
    """Regex type."""

    format = "regex"


string_format_map = {
    "date-time": DateTimeType,
    "time": TimeType,
    "date": DateType,
    "duration": DurationType,
    "email": EmailType,
    "hostname": HostnameType,
    "ipv4": IPv4Type,
    "ipv6": IPv6Type,
    "uuid": UUIDType,
    "uri": URIType,
    "uri-reference": URIReferenceType,
    "uri-template": URITemplateType,
    "json-pointer": JSONPointerType,
    "relative-json-pointer": RelativeJSONPointerType,
    "regex": RegexType,
}
