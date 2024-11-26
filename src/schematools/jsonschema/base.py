from __future__ import annotations

import sys
import typing as t

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


class BaseJSONType:

    _special_keys = ["$id", "$schema", "$comment"]

    _plain_key_map = {
        "type": "type",
        "title": "title",
        "description": "description",
        "default": "default",
        "examples": "examples",
        "readOnly": "read_only",
        "writeOnly": "write_only",
        "deprecated": "deprecated",
        "enum": "enum",
        "const": "const",
    }

    def __init__(
        self,
        *,
        id: str | None = None,
        schema: str | None = None,
        type: str | None = None,
        title: str | None = None,
        description: str | None = None,
        default: T | None = None,
        examples: t.List[T] | None = None,
        read_only: bool | None = None,
        write_only: bool | None = None,
        deprecated: bool | None = None,
        comment: str | None = None,
        enum: t.List[T] | None = None,
        const: T | None = None,
    ):
        self.id = id
        self.schema = schema
        self.comment = comment
        self.type = type
        self.title = title
        self.description = description
        self.default = default
        self.examples = examples
        self.read_only = read_only
        self.write_only = write_only
        self.deprecated = deprecated
        self.enum = enum
        self.const = const

    @classmethod
    def from_jsonschema(cls, jsonschema: dict) -> BaseJSONType:
        kwargs = {
            cls._plain_key_map[k]: v
            for k, v in jsonschema.items()
            if k in cls._plain_key_map.keys()
        }
        kwargs.update(
            {k[1:]: v for k, v in jsonschema.items() if k in cls._special_keys}
        )
        return cls(**kwargs)

    @property
    def _class_properties(self) -> set[str]:
        """Return class properties."""
        return set(
            list(self._plain_key_map.values()) + [k[1:] for k in self._special_keys]
        )

    def __eq__(self, value: object) -> bool:
        return all(
            [
                isinstance(value, type(self)),
                *[
                    getattr(self, k) == getattr(value, k)
                    for k in self._class_properties
                ],
            ]
        )


class BooleanType(BaseJSONType):
    """Boolean type."""


class NullType(BaseJSONType):
    """Null type."""
