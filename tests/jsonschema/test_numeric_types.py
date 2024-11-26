from schematools.jsonschema import IntegerType, JSONSchemaParser, NumberType


def test_number_type():
    """Test number type."""
    number_type = JSONSchemaParser.parse({"type": "number"})
    assert isinstance(number_type, NumberType)
    assert number_type == NumberType()


def test_integer_type():
    """Test integer type."""
    integer_type = JSONSchemaParser.parse({"type": "integer"})
    assert isinstance(integer_type, IntegerType)
    assert integer_type == IntegerType()
