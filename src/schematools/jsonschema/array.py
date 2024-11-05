from __future__ import annotations

import typing as t

from .base import BaseJSONType


class ArrayType(BaseJSONType):
    """Array type."""

    _plain_key_map = {
        "items": "items",
        "prefixItems": "prefix_items",
        "additionalItems": "additional_items",
        "unevaluatedItems": "unevaluated_items",
        "contains": "contains",
        "minContains": "min_contains",
        "maxContains": "max_contains",
        "minItems": "min_items",
        "maxItems": "max_items",
        "uniqueItems": "unique_items",
        **BaseJSONType._plain_key_map,
    }

    def __init__(
        self,
        *,
        items: BaseJSONType | bool | None = None,
        prefix_items: t.List[BaseJSONType] | None = None,
        additional_items: BaseJSONType | bool | None = None,
        unevaluated_items: BaseJSONType | bool | None = None,
        contains: BaseJSONType | None = None,
        min_contains: int | None = None,
        max_contains: int | None = None,
        min_items: int | None = None,
        max_items: int | None = None,
        unique_items: bool | None = None,
        **kwargs: t.Any,
    ) -> None:
        """Initialize ArrayType."""
        super().__init__(**kwargs)
        self._items = items
        self.prefix_items = prefix_items
        self.additional_items = additional_items
        self.unevaluated_items = unevaluated_items
        self.contains = contains
        self.min_contains = min_contains
        self.max_contains = max_contains
        self.min_items = min_items
        self.max_items = max_items
        self.unique_items = unique_items

    @property
    def items(self) -> BaseJSONType | bool | None:
        """Get the items attribute."""
        if isinstance(self._items, bool):
            return self._items

        from schematools.jsonschema import JSONSchema

        return JSONSchema.parse(self._items)
