import json
import typing as t

from .array import ArrayType
from .base import BaseJSONType, BooleanType, NullType
from .numeric import IntegerType, NumberType
from .object_ import ObjectType
from .parse import JSONSchemaParser
from .string import (
    DateTimeType,
    DateType,
    DurationType,
    EmailType,
    HostnameType,
    IPv4Type,
    IPv6Type,
    JSONPointerType,
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
    "BaseJSONType",
    "BooleanType",
    "DateTimeType",
    "DateType",
    "DurationType",
    "EmailType",
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
