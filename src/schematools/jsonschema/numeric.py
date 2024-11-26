from __future__ import annotations

from .base import BaseJSONType


class _NumericType(BaseJSONType):

    _plain_key_map = {
        **BaseJSONType._plain_key_map,
        "minimum": "minimum",
        "maximum": "maximum",
        "exclusiveMinimum": "exclusive_minimum",
        "exclusiveMaximum": "exclusive_maximum",
        "multipleOf": "multiple_of",
    }

    def __init__(
        self,
        *,
        minimum: int | float | None = None,
        maximum: int | float | None = None,
        exclusive_minimum: bool | None = None,
        exclusive_maximum: bool | None = None,
        multiple_of: int | float | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.minimum = minimum
        self.maximum = maximum
        self.exclusive_minimum = exclusive_minimum
        self.exclusive_maximum = exclusive_maximum
        self.multiple_of = multiple_of


class NumberType(_NumericType):
    """Number type."""


class IntegerType(_NumericType):
    """Integer type."""
