from __future__ import annotations

import typing as t

from .base import BaseJSONType


class StringType(BaseJSONType):
    """String type."""

    _plain_key_map = {
        "format": "format",
        "minLength": "min_length",
        "maxLength": "max_length",
        "pattern": "pattern",
        **BaseJSONType._plain_key_map,
    }

    def __init__(
        self,
        *,
        format: str | None = None,
        min_length: int | None = None,
        max_length: int | None = None,
        pattern: str | None = None,
        **kwargs: t.Any,
    ) -> None:
        """Initialize StringType.

        Args:
            minLength: Minimum length of the string. See the
                :jsonschema:`JSON Schema reference <string#length>` for details.
            maxLength: Maximum length of the string. See the
                :jsonschema:`JSON Schema reference <string#length>` for details.
            pattern: A regular expression pattern that the string must match. See the
                :jsonschema:`JSON Schema reference <string#regexp>` for details.
            **kwargs: Additional keyword arguments to pass to the parent class.
        """
        super().__init__(**kwargs)
        self.format = format
        self.min_length = min_length
        self.max_length = max_length
        self.pattern = pattern

    @classmethod
    def from_jsonschema(cls, jsonschema: dict) -> "StringType":
        kwargs = {
            cls._plain_key_map[k]: v
            for k, v in jsonschema.items()
            if k in cls._plain_key_map.keys()
        }
        kwargs.update(
            {k[1:]: v for k, v in jsonschema.items() if k in cls._special_keys}
        )
        if "format" in kwargs:
            string_class = string_format_map[kwargs["format"]]
            return string_class(**kwargs)
        return cls(**kwargs)

    def __eq__(self, value: object) -> bool:
        return super().__eq__(value) and all(
            [
                isinstance(value, StringType),
                self.format == value.format,
                self.min_length == value.min_length,
                self.max_length == value.max_length,
                self.pattern == value.pattern,
            ]
        )


class DateTimeType(StringType):
    """DateTime type.

    Example: `2018-11-13T20:20:39+00:00`
    """


class TimeType(StringType):
    """Time type.

    Example: `20:20:39+00:00`
    """


class DateType(StringType):
    """Date type.

    Example: `2018-11-13`
    """


class DurationType(StringType):
    """Duration type.

    Example: `P3D`
    """


class EmailType(StringType):
    """Email type."""


class HostnameType(StringType):
    """Hostname type."""


class IPv4Type(StringType):
    """IPv4 address type."""


class IPv6Type(StringType):
    """IPv6 type."""


class UUIDType(StringType):
    """UUID type.

    Example: `3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a`
    """


class URIType(StringType):
    """URI type."""


class URIReferenceType(StringType):
    """URIReference type."""


class URITemplateType(StringType):
    """URITemplate type."""


class JSONPointerType(StringType):
    """JSONPointer type."""


class RelativeJSONPointerType(StringType):
    """RelativeJSONPointer type."""


class RegexType(StringType):
    """Regex type."""


string_format_map = {
    "date-time": DateTimeType,
    "time": TimeType,
    "date": DateType,
    "duration": DurationType,
    "email": EmailType,
    "hostname": HostnameType,
    "ipv4": IPv4Type,
    "ipv6": IPv6Type,
    "uuid": UUIDType,
    "uri": URIType,
    "uri-reference": URIReferenceType,
    "uri-template": URITemplateType,
    "json-pointer": JSONPointerType,
    "relative-json-pointer": RelativeJSONPointerType,
    "regex": RegexType,
}
