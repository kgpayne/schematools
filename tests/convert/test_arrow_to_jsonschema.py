import pyarrow as pa

from schematools.arrow import ArrowToJSONSchemaConverter
from schematools.jsonschema.parse import JSONSchemaParser


def test_arrow_array():
    """Test conversion of array."""
    arrow_schema = pa.schema([pa.field("root", pa.list_(pa.string()), nullable=False)])
    jsonschema = ArrowToJSONSchemaConverter.to_jsonschema(arrow_schema)
    expected_jsonschema = JSONSchemaParser.parse(
        {"type": "array", "items": {"type": "string"}}
    )
    assert jsonschema == expected_jsonschema


def test_arrow_array_nullable():
    """Test conversion of array."""
    arrow_schema = pa.schema([pa.field("root", pa.list_(pa.string()), nullable=True)])
    jsonschema = ArrowToJSONSchemaConverter.to_jsonschema(arrow_schema)
    expected_jsonschema = JSONSchemaParser.parse(
        {"type": ["array", "null"], "items": {"type": "string"}}
    )
    assert jsonschema == expected_jsonschema


def test_arrow_array_union_type():
    """Test ArrowSchema with array and union type."""
    arrow_schema = pa.schema(
        [
            pa.field(
                "root",
                pa.list_(
                    pa.dense_union(
                        [
                            pa.field("a", pa.string(), nullable=False),
                            pa.field("b", pa.int32(), nullable=False),
                        ]
                    )
                ),
                nullable=False,
            )
        ]
    )
    jsonschema = ArrowToJSONSchemaConverter.to_jsonschema(arrow_schema)
    assert jsonschema == JSONSchemaParser.parse(
        {"type": "array", "items": {"type": ["string", "integer"]}}
    )


def test_arrow_nullable():
    """Test conversion of nullable fields."""
    arrow_schema = pa.schema([pa.field("root", pa.string(), nullable=True)])
    jsonschema = ArrowToJSONSchemaConverter.to_jsonschema(arrow_schema)
    expected_jsonschema = JSONSchemaParser.parse({"type": ["string", "null"]})
    assert jsonschema == expected_jsonschema


def test_arrow_boolean():
    arrow_schema = pa.schema([pa.field("root", pa.bool_(), nullable=False)])
    jsonschema = ArrowToJSONSchemaConverter.to_jsonschema(arrow_schema)
    expected_jsonschema = JSONSchemaParser.parse({"type": "boolean"})
    assert jsonschema == expected_jsonschema


def test_arrow_null():
    arrow_schema = pa.schema([pa.field("root", pa.null())])
    jsonschema = ArrowToJSONSchemaConverter.to_jsonschema(arrow_schema)
    expected_jsonschema = JSONSchemaParser.parse({"type": "null"})
    assert jsonschema == expected_jsonschema


def test_arrow_integer():
    arrow_schema = pa.schema([pa.field("root", pa.int32(), nullable=False)])
    jsonschema = ArrowToJSONSchemaConverter.to_jsonschema(arrow_schema)
    expected_jsonschema = JSONSchemaParser.parse({"type": "integer"})
    assert jsonschema == expected_jsonschema


def test_arrow_number():
    arrow_schema = pa.schema([pa.field("root", pa.float64(), nullable=False)])
    jsonschema = ArrowToJSONSchemaConverter.to_jsonschema(arrow_schema)
    expected_jsonschema = JSONSchemaParser.parse({"type": "number"})
    assert jsonschema == expected_jsonschema


def test_arrow_number_nullable():
    arrow_schema = pa.schema([pa.field("root", pa.float64(), nullable=True)])
    jsonschema = ArrowToJSONSchemaConverter.to_jsonschema(arrow_schema)
    expected_jsonschema = JSONSchemaParser.parse({"type": ["number", "null"]})
    assert jsonschema == expected_jsonschema


def test_arrow_struct():
    arrow_schema = pa.schema(
        [
            pa.field(
                "root",
                pa.struct([pa.field("name", pa.string(), nullable=False)]),
                nullable=False,
            )
        ]
    )
    jsonschema = ArrowToJSONSchemaConverter.to_jsonschema(arrow_schema)
    expected_jsonschema = JSONSchemaParser.parse(
        {"type": "object", "properties": {"name": {"type": "string"}}}
    )
    assert jsonschema == expected_jsonschema
