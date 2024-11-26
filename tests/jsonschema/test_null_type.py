from schematools.jsonschema import JSONSchemaParser, NullType


def test_null_type():
    """Test null type."""
    null_type = JSONSchemaParser.parse({"type": "null"})
    assert isinstance(null_type, NullType)
    assert null_type == NullType()
