from schematools.jsonschema import JSONSchema, NullType


def test_null_type():
    """Test null type."""
    null_type = JSONSchema.parse({"type": "null"})
    assert isinstance(null_type, NullType)
