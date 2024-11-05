from schematools.jsonschema import JSONSchema, ObjectType


def test_object_type():
    """Test object type."""
    object_type = JSONSchema.parse({"type": "object"})
    assert isinstance(object_type, ObjectType)


def test_simple_object_properties():
    """Test object properties."""
    object_type = JSONSchema.parse(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
            },
        }
    )
    assert object_type.properties == {
        "name": JSONSchema.parse({"type": "string"}),
        "age": JSONSchema.parse({"type": "integer"}),
    }


def test_nested_object_properties():
    """Test nested object properties."""
    object_type = JSONSchema.parse(
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
        "address": JSONSchema.parse(
            {
                "type": "object",
                "properties": {
                    "street": {"type": "string"},
                    "city": {"type": "string"},
                    "house": JSONSchema.parse(
                        {
                            "type": "object",
                            "properties": {
                                "number": {"type": "integer"},
                                "owner": {"type": "string"},
                            },
                        }
                    ),
                },
            }
        )
    }
