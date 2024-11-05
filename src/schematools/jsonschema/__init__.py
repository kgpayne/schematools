import json
import typing as t

from .array import ArrayType
from .base import BaseJSONType, BooleanType, NullType
from .numeric import IntegerType, NumberType
from .object_ import ObjectType
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
]

json_schema_root_type_map = {
    None: BaseJSONType,
    "string": StringType,
    "number": NumberType,
    "integer": IntegerType,
    "boolean": BooleanType,
    "object": ObjectType,
    "null": NullType,
    "array": ArrayType,
}


class JSONSchema:

    @classmethod
    def parse(self, jsonschema: str | dict) -> t.Any:
        jsonschema = (
            json.loads(jsonschema) if isinstance(jsonschema, str) else jsonschema
        )
        simple_type_class = json_schema_root_type_map[jsonschema.get("type")]
        return simple_type_class.from_jsonschema(jsonschema)
