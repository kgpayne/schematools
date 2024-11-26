from schematools.jsonschema import BooleanType, JSONSchemaParser


def test_boolean_type():
    """Test boolean type."""
    boolean_type = JSONSchemaParser.parse({"type": "boolean"})
    assert isinstance(boolean_type, BooleanType)
    assert boolean_type == BooleanType()
