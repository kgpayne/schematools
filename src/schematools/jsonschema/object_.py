from __future__ import annotations

import typing as t

from .base import BaseJSONType

if t.TYPE_CHECKING:
    from schematools.jsonschema import JSONSchema


class ObjectType(BaseJSONType):
    """Object type."""

    _plain_key_map = {
        "properties": "properties",
        "additionalProperties": "additional_properties",
        "patternProperties": "pattern_properties",
        "unevaluatedProperties": "unevaluated_properties",
        "required": "required",
        "minProperties": "min_properties",
        "maxProperties": "max_properties",
        "allOf": "all_of",
        "anyOf": "anyOf",
        "oneOf": "oneOf",
        "not": "not_",
        "if": "if_",
        "then": "then",
        "else": "else_",
        "propertyNames": "property_names",
        "dependentRequired": "dependent_required",
        "dependentSchemas": "dependent_schemas",
        **BaseJSONType._plain_key_map,
    }

    def __init__(
        self,
        *,
        properties: t.Dict[str, JSONSchema] | None = None,
        additional_properties: bool | JSONSchema | None = None,
        pattern_properties: t.Dict[str, JSONSchema] | None = None,
        unevaluated_properties: JSONSchema | None = None,
        required: t.List[str] | None = None,
        min_properties: int | None = None,
        max_properties: int | None = None,
        all_of: t.List[JSONSchema] | None = None,
        any_of: t.List[JSONSchema] | None = None,
        one_of: t.List[JSONSchema] | None = None,
        not_: JSONSchema | None = None,
        if_: JSONSchema | None = None,
        then: JSONSchema | None = None,
        else_: JSONSchema | None = None,
        property_names: JSONSchema | None = None,
        dependent_required: t.Dict[str, t.List[str]] | None = None,
        dependent_schemas: t.Dict[str, JSONSchema] | None = None,
        **kwargs: t.Any,
    ) -> None:
        """Initialize ObjectType.

        Args:
            properties: A dictionary of property names and their corresponding JSON types.
            required: A list of required property names.
            additional_properties: A boolean indicating whether additional properties are allowed,
                or a JSON type to use for additional properties.
            min_properties: Minimum number of properties.
            max_properties: Maximum number of properties.
            **kwargs: Additional keyword arguments to pass to the parent class.
        """
        super().__init__(**kwargs)
        self._properties = properties
        self.additional_properties = additional_properties
        self.pattern_properties = pattern_properties
        self.unevaluated_properties = unevaluated_properties
        self.required = required
        self.min_properties = min_properties
        self.max_properties = max_properties
        self.all_of = all_of
        self.any_of = any_of
        self.one_of = one_of
        self.not_ = not_
        self.if_ = if_
        self.then = then
        self.else_ = else_
        self.property_names = property_names
        self.dependent_required = dependent_required
        self.dependent_schemas = dependent_schemas

    @property
    def properties(self) -> t.Dict[str, JSONSchema] | None:
        """Return the properties."""
        if self._properties is not None:
            from schematools.jsonschema import JSONSchema

            return {k: JSONSchema.parse(v) for k, v in self._properties.items()}
        return self._properties
