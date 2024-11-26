from __future__ import annotations

import typing as t
from dataclasses import dataclass

from .base import BaseJSONType


@dataclass(frozen=True)
class ArrayType(BaseJSONType):
    """Array type."""

    type: str = "array"
    items: BaseJSONType | bool | None = None
    prefixItems: t.List[BaseJSONType] | None = None
    additionalItems: BaseJSONType | bool | None = None
    unevaluatedItems: BaseJSONType | bool | None = None
    contains: BaseJSONType | None = None
    minContains: int | None = None
    maxContains: int | None = None
    minItems: int | None = None
    maxItems: int | None = None
    uniqueItems: bool | None = None
