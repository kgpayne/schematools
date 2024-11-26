from __future__ import annotations

import typing as t
from dataclasses import dataclass

from .base import BaseJSONType

if t.TYPE_CHECKING:
    from schematools.jsonschema import JSONSchema


@dataclass(frozen=True)
class ObjectType(BaseJSONType):
    """Object type."""

    type: str = "object"
    properties: t.Dict[str, JSONSchema] | None = None
    additionalProperties: bool | JSONSchema | None = None
    patternProperties: t.Dict[str, JSONSchema] | None = None
    unevaluatedProperties: JSONSchema | None = None
    required: t.List[str] | None = None
    minProperties: int | None = None
    maxProperties: int | None = None
    allOf: t.List[JSONSchema] | None = None
    anyOf: t.List[JSONSchema] | None = None
    oneOf: t.List[JSONSchema] | None = None
    not_: JSONSchema | None = None
    if_: JSONSchema | None = None
    then: JSONSchema | None = None
    else_: JSONSchema | None = None
    propertyNames: JSONSchema | None = None
    dependentRequired: t.Dict[str, t.List[str]] | None = None
    dependentSchemas: t.Dict[str, JSONSchema] | None = None

    def has_properties(self) -> bool:
        """Check if object has properties."""
        return self.properties is not None
