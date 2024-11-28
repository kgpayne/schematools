"""JSON Schema tools for Python."""

from .flatten import flatten
from .parse import JSONSchemaParser
from .types import (
    ArrayType,
    BaseJSONSchemaType,
    BooleanType,
    DateTimeType,
    DateType,
    DurationType,
    EmailType,
    HostnameType,
    IntegerType,
    IPv4Type,
    IPv6Type,
    JSONPointerType,
    NullType,
    NumberType,
    ObjectType,
    RegexType,
    RelativeJSONPointerType,
    StringType,
    TimeType,
    URIReferenceType,
    URITemplateType,
    URIType,
    UUIDType,
)

__all__ = [
    "ArrayType",
    "BaseJSONSchemaType",
    "BooleanType",
    "DateTimeType",
    "DateType",
    "DurationType",
    "EmailType",
    "flatten",
    "HostnameType",
    "IntegerType",
    "IPv4Type",
    "IPv6Type",
    "JSONPointerType",
    "JSONSchema",
    "NullType",
    "NumberType",
    "ObjectType",
    "RegexType",
    "RelativeJSONPointerType",
    "StringType",
    "TimeType",
    "URIReferenceType",
    "URITemplateType",
    "URIType",
    "UUIDType",
    "JSONSchemaParser",
]
