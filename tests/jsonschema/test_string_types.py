import pytest

from schematools.jsonschema import (
    BaseJSONSchemaType,
    DateTimeType,
    DateType,
    DurationType,
    EmailType,
    HostnameType,
    IPv4Type,
    IPv6Type,
    JSONPointerType,
    JSONSchemaParser,
    RegexType,
    RelativeJSONPointerType,
    StringType,
    TimeType,
    URIReferenceType,
    URITemplateType,
    URIType,
    UUIDType,
)


def validate_attrs(obj, attrs: dict):
    for key, value in attrs.items():
        assert (
            getattr(obj, key) == value
        ), f"Expected {key} to be {value}, got {getattr(obj, key)}"


def test_empty_type():
    empty_type = JSONSchemaParser.parse({})
    assert empty_type is None


def test_basic_string_type():
    string_type = JSONSchemaParser.parse(
        {
            "type": "string",
        }
    )
    assert isinstance(string_type, StringType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": None,
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_basic_string_type_with_values():
    string_type = JSONSchemaParser.parse(
        {
            "type": "string",
            "title": "Test",
            "description": "Test description",
            "default": "a",
            "examples": ["a", "b"],
            "readOnly": False,
            "writeOnly": False,
            "deprecated": False,
            "$comment": "Test comment",
            "enum": ["a", "b"],
            "minLength": 1,
            "maxLength": 1,
            "pattern": None,
        }
    )
    assert isinstance(string_type, StringType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": "Test",
        "description": "Test description",
        "default": "a",
        "examples": ["a", "b"],
        "readOnly": False,
        "writeOnly": False,
        "deprecated": False,
        "comment": "Test comment",
        "enum": ["a", "b"],
        "const": None,
        # string type specific attrs
        "format": None,
        "minLength": 1,
        "maxLength": 1,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_date_time():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "date-time"})
    assert isinstance(string_type, DateTimeType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "date-time",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_time():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "time"})
    assert isinstance(string_type, TimeType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "time",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_date():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "date"})
    assert isinstance(string_type, DateType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "date",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_duration():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "duration"})
    assert isinstance(string_type, DurationType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "duration",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_email():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "email"})
    assert isinstance(string_type, EmailType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "email",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_hostname():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "hostname"})
    assert isinstance(string_type, HostnameType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "hostname",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_ipv4():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "ipv4"})
    assert isinstance(string_type, IPv4Type)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "ipv4",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_ipv6():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "ipv6"})
    assert isinstance(string_type, IPv6Type)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "ipv6",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_uuid():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "uuid"})
    assert isinstance(string_type, UUIDType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "uuid",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_uri():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "uri"})
    assert isinstance(string_type, URIType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "uri",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_uri_reference():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "uri-reference"})
    assert isinstance(string_type, URIReferenceType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "uri-reference",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_uri_template():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "uri-template"})
    assert isinstance(string_type, URITemplateType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "uri-template",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_json_pointer():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "json-pointer"})
    assert isinstance(string_type, JSONPointerType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "json-pointer",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_relative_json_pointer():
    string_type = JSONSchemaParser.parse(
        {"type": "string", "format": "relative-json-pointer"}
    )
    assert isinstance(string_type, RelativeJSONPointerType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "relative-json-pointer",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_regex():
    string_type = JSONSchemaParser.parse({"type": "string", "format": "regex"})
    assert isinstance(string_type, RegexType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "readOnly": None,
        "writeOnly": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "regex",
        "minLength": None,
        "maxLength": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)
    validate_attrs(string_type, expected_attrs)
