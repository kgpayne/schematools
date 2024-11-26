from schematools.jsonschema import JSONSchemaParser, ObjectType


def test_object_type():
    """Test object type."""
    object_type = JSONSchemaParser.parse({"type": "object"})
    assert isinstance(object_type, ObjectType)


def test_simple_object_properties():
    """Test object properties."""
    object_type = JSONSchemaParser.parse(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
            },
        }
    )
    assert object_type.properties == {
        "name": JSONSchemaParser.parse({"type": "string"}),
        "age": JSONSchemaParser.parse({"type": "integer"}),
    }


def test_nested_object_properties():
    """Test nested object properties."""
    object_type = JSONSchemaParser.parse(
        {
            "type": "object",
            "properties": {
                "address": {
                    "type": "object",
                    "properties": {
                        "street": {"type": "string"},
                        "city": {"type": "string"},
                        "house": {
                            "type": "object",
                            "properties": {
                                "number": {"type": "integer"},
                                "owner": {"type": "string"},
                            },
                        },
                    },
                }
            },
        }
    )
    assert object_type.properties == {
        "address": JSONSchemaParser.parse(
            {
                "type": "object",
                "properties": {
                    "street": {"type": "string"},
                    "city": {"type": "string"},
                    "house": {
                        "type": "object",
                        "properties": {
                            "number": {"type": "integer"},
                            "owner": {"type": "string"},
                        },
                    },
                },
            }
        )
    }
