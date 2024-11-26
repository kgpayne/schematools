from schematools.jsonschema import ArrayType, JSONSchemaParser, StringType


def test_array_type():
    """Test array type."""
    array_type = JSONSchemaParser.parse({"type": "array"})
    assert isinstance(array_type, ArrayType)


def test_array_type_items():
    """Test array type items."""
    array_type = JSONSchemaParser.parse({"type": "array", "items": {"type": "string"}})
    assert array_type.items == StringType()
