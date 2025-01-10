import pyarrow as pa

from schematools.arrow import ArrowToJSONSchemaConverter
from schematools.jsonschema.parse import JSONSchemaParser


def test_arrow_schema_null():
    """Test ArrowSchema."""
    jsonschema = JSONSchemaParser.parse({"type": "null"})
    arrow_schema = ArrowToJSONSchemaConverter.from_jsonschema(jsonschema)
    assert arrow_schema == pa.schema([pa.field("root", pa.null(), nullable=True)])


# TODO: This is actually wrong. Fix 'nullable' inference.
def test_arrow_schema_object():
    """Test ArrowSchema with object."""
    jsonschema = JSONSchemaParser.parse(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
            },
        }
    )
    arrow_schema = ArrowToJSONSchemaConverter.from_jsonschema(jsonschema)
    assert arrow_schema == pa.schema(
        [
            pa.field("name", pa.string(), nullable=False),
            pa.field("age", pa.int64(), nullable=False),
        ]
    )
