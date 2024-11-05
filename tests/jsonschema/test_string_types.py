from schematools.jsonschema import (
    BaseJSONType,
    DateTimeType,
    DateType,
    DurationType,
    EmailType,
    HostnameType,
    IPv4Type,
    IPv6Type,
    JSONPointerType,
    JSONSchema,
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
    string_type = JSONSchema.parse({})
    assert isinstance(string_type, BaseJSONType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": None,
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_basic_string_type():
    string_type = JSONSchema.parse(
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
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": None,
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_basic_string_type_with_values():
    string_type = JSONSchema.parse(
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
        "read_only": False,
        "write_only": False,
        "deprecated": False,
        "comment": "Test comment",
        "enum": ["a", "b"],
        "const": None,
        # string type specific attrs
        "format": None,
        "min_length": 1,
        "max_length": 1,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_date_time():
    string_type = JSONSchema.parse({"type": "string", "format": "date-time"})
    assert isinstance(string_type, DateTimeType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "date-time",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_time():
    string_type = JSONSchema.parse({"type": "string", "format": "time"})
    assert isinstance(string_type, TimeType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "time",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_date():
    string_type = JSONSchema.parse({"type": "string", "format": "date"})
    assert isinstance(string_type, DateType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "date",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_duration():
    string_type = JSONSchema.parse({"type": "string", "format": "duration"})
    assert isinstance(string_type, DurationType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "duration",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_email():
    string_type = JSONSchema.parse({"type": "string", "format": "email"})
    assert isinstance(string_type, EmailType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "email",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_hostname():
    string_type = JSONSchema.parse({"type": "string", "format": "hostname"})
    assert isinstance(string_type, HostnameType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "hostname",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_ipv4():
    string_type = JSONSchema.parse({"type": "string", "format": "ipv4"})
    assert isinstance(string_type, IPv4Type)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "ipv4",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_ipv6():
    string_type = JSONSchema.parse({"type": "string", "format": "ipv6"})
    assert isinstance(string_type, IPv6Type)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "ipv6",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_uuid():
    string_type = JSONSchema.parse({"type": "string", "format": "uuid"})
    assert isinstance(string_type, UUIDType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "uuid",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_uri():
    string_type = JSONSchema.parse({"type": "string", "format": "uri"})
    assert isinstance(string_type, URIType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "uri",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_uri_reference():
    string_type = JSONSchema.parse({"type": "string", "format": "uri-reference"})
    assert isinstance(string_type, URIReferenceType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "uri-reference",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_uri_template():
    string_type = JSONSchema.parse({"type": "string", "format": "uri-template"})
    assert isinstance(string_type, URITemplateType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "uri-template",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_json_pointer():
    string_type = JSONSchema.parse({"type": "string", "format": "json-pointer"})
    assert isinstance(string_type, JSONPointerType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "json-pointer",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_relative_json_pointer():
    string_type = JSONSchema.parse(
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
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "relative-json-pointer",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)


def test_regex():
    string_type = JSONSchema.parse({"type": "string", "format": "regex"})
    assert isinstance(string_type, RegexType)

    expected_attrs = {
        "id": None,
        "schema": None,
        "type": "string",
        "title": None,
        "description": None,
        "default": None,
        "examples": None,
        "read_only": None,
        "write_only": None,
        "deprecated": None,
        "comment": None,
        "enum": None,
        "const": None,
        # string type specific attrs
        "format": "regex",
        "min_length": None,
        "max_length": None,
        "pattern": None,
    }
    validate_attrs(string_type, expected_attrs)
