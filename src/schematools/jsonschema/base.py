from __future__ import annotations

import sys
import typing as t
from dataclasses import dataclass

if t.TYPE_CHECKING:

    if sys.version_info >= (3, 10):
        from typing import TypeAlias  # noqa: ICN003
    else:
        from typing_extensions import TypeAlias

_JsonValue: TypeAlias = t.Union[
    str,
    int,
    float,
    bool,
    list,
    dict,
    None,
]

T = t.TypeVar("T", bound=_JsonValue)


@dataclass(frozen=True)
class BaseJSONType:

    id: str | None = None
    schema: str | None = None
    comment: str | None = None
    type: str | None = None
    title: str | None = None
    description: str | None = None
    default: T | None = None
    examples: t.List[T] | None = None
    readOnly: bool | None = None
    writeOnly: bool | None = None
    deprecated: bool | None = None
    enum: t.List[T] | None = None
    const: T | None = None


@dataclass(frozen=True)
class BooleanType(BaseJSONType):
    """Boolean type."""

    type: str = "boolean"


@dataclass(frozen=True)
class NullType(BaseJSONType):
    """Null type."""

    type: str = "null"
