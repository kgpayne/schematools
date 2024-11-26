from __future__ import annotations

import typing as t
from dataclasses import dataclass

from .base import BaseJSONType


@dataclass(frozen=True)
class StringType(BaseJSONType):
    """String type."""

    type: str = "string"
    format: str | None = None
    minLength: int | None = None
    maxLength: int | None = None
    pattern: str | None = None

    @classmethod
    def from_jsonschema(cls, jsonschema: dict) -> StringType:
        string_format = jsonschema.get("format")
        if string_format is not None:
            return string_format_map[string_format](**jsonschema)
        return cls(**jsonschema)


@dataclass(frozen=True)
class DateTimeType(StringType):
    """DateTime type.

    Example: `2018-11-13T20:20:39+00:00`
    """

    format = "date-time"


@dataclass(frozen=True)
class TimeType(StringType):
    """Time type.

    Example: `20:20:39+00:00`
    """

    format = "time"


@dataclass(frozen=True)
class DateType(StringType):
    """Date type.

    Example: `2018-11-13`
    """

    format = "date"


@dataclass(frozen=True)
class DurationType(StringType):
    """Duration type.

    Example: `P3D`
    """

    format = "duration"


@dataclass(frozen=True)
class EmailType(StringType):
    """Email type."""

    format = "email"


@dataclass(frozen=True)
class HostnameType(StringType):
    """Hostname type."""

    format = "hostname"


@dataclass(frozen=True)
class IPv4Type(StringType):
    """IPv4 address type."""

    format = "ipv4"


@dataclass(frozen=True)
class IPv6Type(StringType):
    """IPv6 type."""

    format = "ipv6"


@dataclass(frozen=True)
class UUIDType(StringType):
    """UUID type.

    Example: `3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a`
    """

    format = "uuid"


@dataclass(frozen=True)
class URIType(StringType):
    """URI type."""

    format = "uri"


@dataclass(frozen=True)
class URIReferenceType(StringType):
    """URIReference type."""

    format = "uri-reference"


@dataclass(frozen=True)
class URITemplateType(StringType):
    """URITemplate type."""

    format = "uri-template"


@dataclass(frozen=True)
class JSONPointerType(StringType):
    """JSONPointer type."""

    format = "json-pointer"


@dataclass(frozen=True)
class RelativeJSONPointerType(StringType):
    """RelativeJSONPointer type."""

    format = "relative-json-pointer"


@dataclass(frozen=True)
class RegexType(StringType):
    """Regex type."""

    format = "regex"


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
