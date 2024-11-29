import pyarrow as pa

from schematools.arrow import ArrowJSONSchemaConverter
from schematools.jsonschema.parse import JSONSchemaParser


def test_arrow_array():
    """Test conversion of array."""
    arrow_schema = pa.schema([pa.field("root", pa.list_(pa.string()))])
    jsonschema = ArrowJSONSchemaConverter.to_jsonschema(arrow_schema)
    assert jsonschema == JSONSchemaParser.parse(
        {"type": "array", "items": {"type": "string"}}
    )


def test_arrow_array_union_type():
    """Test ArrowSchema with array and union type."""
    arrow_schema = pa.schema(
        [
            pa.field(
                "root",
                pa.list_(
                    pa.dense_union(
                        [pa.field("a", pa.string()), pa.field("b", pa.int32())]
                    )
                ),
            )
        ]
    )
    jsonschema = ArrowJSONSchemaConverter.to_jsonschema(arrow_schema)
    assert (
        jsonschema.type
        == JSONSchemaParser.parse(
            {"type": "array", "items": {"type": ["string", "integer"]}}
        ).type
    )


def test_arrow_nullable():
    """Test conversion of nullable fields."""
    arrow_schema = pa.schema([pa.field("root", pa.string(), nullable=True)])
    jsonschema = ArrowJSONSchemaConverter.to_jsonschema(arrow_schema)
    expected_jsonschema = JSONSchemaParser.parse({"type": ["string", "null"]})
    # TODO: fix equality check between two constructs of the same class
    assert jsonschema.type == expected_jsonschema.type
