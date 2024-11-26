from __future__ import annotations

import typing as t
from dataclasses import dataclass

from .base import BaseJSONType


@dataclass(frozen=True)
class ObjectType(BaseJSONType):
    """Object type."""

    type: str = "object"
    properties: t.Dict[str, BaseJSONType] | None = None
    additionalProperties: bool | BaseJSONType | None = None
    patternProperties: t.Dict[str, BaseJSONType] | None = None
    unevaluatedProperties: BaseJSONType | None = None
    required: t.List[str] | None = None
    minProperties: int | None = None
    maxProperties: int | None = None
    allOf: t.List[BaseJSONType] | None = None
    anyOf: t.List[BaseJSONType] | None = None
    oneOf: t.List[BaseJSONType] | None = None
    not_: BaseJSONType | None = None
    if_: BaseJSONType | None = None
    then: BaseJSONType | None = None
    else_: BaseJSONType | None = None
    propertyNames: BaseJSONType | None = None
    dependentRequired: t.Dict[str, t.List[str]] | None = None
    dependentSchemas: t.Dict[str, BaseJSONType] | None = None

    def has_properties(self) -> bool:
        """Check if object has properties."""
        return self.properties is not None
