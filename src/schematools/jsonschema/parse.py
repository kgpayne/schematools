from __future__ import annotations

import json
import typing as t
from copy import deepcopy

from class_singledispatch import class_singledispatch

from .types import (
    ArrayType,
    BaseJSONType,
    BooleanType,
    IntegerType,
    NullType,
    NumberType,
    ObjectType,
    StringType,
)

json_schema_root_type_map = {
    "array": ArrayType,
    "boolean": BooleanType,
    "integer": IntegerType,
    "null": NullType,
    "number": NumberType,
    "object": ObjectType,
    "string": StringType,
    None: BaseJSONType,
}


def _handle_special_keys(jsonschema: dict) -> dict:
    for key in list(jsonschema.keys()):
        if key in ["$id", "$schema", "$comment"]:
            value = jsonschema.pop(key)
            jsonschema[key.lstrip("$")] = value
        if key in ["if", "not", "else"]:
            value = jsonschema.pop(key)
            jsonschema[key + "_"] = value
    return jsonschema


@class_singledispatch
def parse_type(jsontype: t.Type[BaseJSONType], jsonschema: dict | None = None) -> t.Any:
    raise NotImplementedError(f"Parsing of {jsontype} is not supported.")


@parse_type.register
def parse_array(
    jsontype: t.Type[ArrayType], jsonschema: dict | None = None
) -> ArrayType:
    kwargs = deepcopy(jsonschema)
    kwargs = _handle_special_keys(kwargs)
    item_type = kwargs.pop("items", {})
    if item_type:
        kwargs["items"] = parse_type(
            json_schema_root_type_map[item_type["type"]], item_type
        )
    return ArrayType(**kwargs)


@parse_type.register
def parse_boolean(jsontype: t.Type[BooleanType], jsonschema: dict) -> t.Any:
    return BooleanType(**jsonschema)


@parse_type.register
def parse_integer(jsontype: t.Type[IntegerType], jsonschema: dict) -> t.Any:
    return IntegerType(**jsonschema)


@parse_type.register
def parse_null(jsontype: t.Type[NullType], jsonschema: dict) -> t.Any:
    return NullType(**jsonschema)


@parse_type.register
def parse_number(jsontype: t.Type[NumberType], jsonschema: dict) -> t.Any:
    return NumberType(**jsonschema)


@parse_type.register
def parse_object(jsontype: t.Type[ObjectType], jsonschema: dict) -> t.Any:
    kwargs = deepcopy(jsonschema)
    kwargs = _handle_special_keys(kwargs)
    # handle properties
    properties = kwargs.get("properties")
    if properties:
        kwargs["properties"] = {
            k: parse_type(json_schema_root_type_map[v["type"]], v)
            for k, v in properties.items()
        }
    # TODO: handle patternProperties, additionalProperties etc.
    return ObjectType(**kwargs)


@parse_type.register
def parse_string(jsontype: t.Type[StringType], jsonschema: dict) -> t.Any:
    return StringType.from_jsonschema(jsonschema)


class JSONSchemaParser:

    @classmethod
    def parse(cls, jsonschema: dict | str) -> BaseJSONType:
        jsonschema = (
            json.loads(jsonschema) if isinstance(jsonschema, str) else jsonschema
        )
        jsonschema = _handle_special_keys(jsonschema)
        simple_type_class = json_schema_root_type_map[jsonschema.get("type")]
        return parse_type(simple_type_class, jsonschema=jsonschema)
