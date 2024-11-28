from __future__ import annotations

import typing as t

from schematools.jsonschema import BaseJSONSchemaType


class SchemaConverterBase:

    @staticmethod
    def to_jsonschema(schema: t.Any) -> BaseJSONSchemaType:
        raise NotImplementedError

    @staticmethod
    def from_jsonschema(jsontype: BaseJSONSchemaType) -> t.Any:
        raise NotImplementedError
