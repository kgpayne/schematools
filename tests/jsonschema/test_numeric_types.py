from schematools.jsonschema import IntegerType, JSONSchema, NumberType


def test_number_type():
    """Test number type."""
    number_type = JSONSchema.parse({"type": "number"})
    assert isinstance(number_type, NumberType)


def test_integer_type():
    """Test integer type."""
    integer_type = JSONSchema.parse({"type": "integer"})
    assert isinstance(integer_type, IntegerType)
