from schematools.jsonschema import BooleanType, JSONSchema


def test_boolean_type():
    """Test boolean type."""
    boolean_type = JSONSchema.parse({"type": "boolean"})
    assert isinstance(boolean_type, BooleanType)
