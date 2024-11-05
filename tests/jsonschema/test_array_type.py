from schematools.jsonschema import ArrayType, JSONSchema


def test_array_type():
    """Test array type."""
    array_type = JSONSchema.parse({"type": "array"})
    assert isinstance(array_type, ArrayType)


def test_array_type_items():
    """Test array type items."""
    array_type = JSONSchema.parse({"type": "array", "items": {"type": "string"}})
    assert array_type.items.type == "string"
