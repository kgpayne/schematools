import pyarrow as pa

from schematools.apache_arrow import ArrowSchema


def test_arrow_schema_null():
    """Test ArrowSchema."""
    arrow_schema = ArrowSchema.from_jsonschema({"type": "null"})
    assert arrow_schema == pa.schema([pa.field("root", pa.null())])


# TODO: This is actually wrong. Fix 'nullable' inference.
def test_arrow_schema_object():
    """Test ArrowSchema with object."""
    arrow_schema = ArrowSchema.from_jsonschema(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
            },
        }
    )
    assert arrow_schema == pa.schema(
        [
            pa.field(
                "root",
                pa.struct(
                    [
                        pa.field("name", pa.string(), nullable=True),
                        pa.field("age", pa.int64(), nullable=True),
                    ]
                ),
                nullable=True,
            )
        ]
    )
