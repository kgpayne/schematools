from __future__ import annotations

from dataclasses import dataclass

from .base import BaseJSONType


@dataclass(frozen=True)
class _NumericType(BaseJSONType):
    """Numeric type."""

    minimum: int | float | None = None
    maximum: int | float | None = None
    exclusiveMinimum: bool | None = None
    exclusiveMaximum: bool | None = None
    multipleOf: int | float | None = None


@dataclass(frozen=True)
class NumberType(_NumericType):
    """Number type."""

    type: str = "number"


@dataclass(frozen=True)
class IntegerType(_NumericType):
    """Integer type."""

    type: str = "integer"
