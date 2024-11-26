from functools import singledispatchmethod

import pyarrow as pa

from schematools.jsonschema import (
    ArrayType,
    BaseJSONType,
    BooleanType,
    IntegerType,
    JSONSchemaParser,
    NullType,
    NumberType,
    ObjectType,
    StringType,
)


class JSONToArrowTypeMap:

    @singledispatchmethod
    def convert(self, jsontype: BaseJSONType) -> pa.DataType:
        """Convert JSON type to Apache Arrow type."""
        raise NotImplementedError(f"Conversion of {jsontype} is not supported")

    @convert.register
    def convert_integer(self, jsontype: IntegerType) -> pa.DataType:
        """Convert IntegerType to Apache Arrow type."""
        return pa.int64()

    @convert.register
    def convert_number(self, jsontype: NumberType) -> pa.DataType:
        """Convert NumberType to Apache Arrow type."""
        return pa.float64()

    @convert.register
    def convert_string(self, jsontype: StringType) -> pa.DataType:
        """Convert StringType to Apache Arrow type."""
        return pa.string()

    @convert.register
    def convert_boolean(self, jsontype: BooleanType) -> pa.DataType:
        """Convert BooleanType to Apache Arrow type."""
        return pa.bool_()

    @convert.register
    def convert_object(self, jsontype: ObjectType) -> pa.DataType:
        """Convert ObjectType to Apache Arrow type."""
        if jsontype.properties is not None:
            fields = [
                pa.field(
                    name=k,
                    type=self.convert(v),
                    # nullable=v.get("nullable", True),
                )
                for k, v in jsontype.properties.items()
            ]
            return pa.struct(fields)
        return pa.struct([])

    @convert.register
    def convert_array(self, jsontype: ArrayType) -> pa.DataType:
        """Convert ArrayType to Apache Arrow type."""
        return pa.list_(self.convert(jsontype.items))

    @convert.register
    def convert_null(self, jsontype: NullType) -> pa.DataType:
        """Convert NullType to Apache Arrow type."""
        return pa.null()


class ArrowSchema:
    """Apache Arrow schema representation."""

    @classmethod
    def from_jsonschema(cls, jsonschema: dict) -> pa.Schema:
        """Convert JSON schema to Apache Arrow schema."""
        json_schema = JSONSchemaParser.parse(jsonschema)
        if isinstance(json_schema, ObjectType) and json_schema.has_properties():
            return pa.schema(
                [
                    pa.field(
                        name=k,
                        type=JSONToArrowTypeMap().convert(v),
                        # nullable=jsonschema.get("nullable", True),
                    )
                    for k, v in json_schema.properties.items()
                ]
            )
        return pa.schema(
            [
                pa.field(
                    name="root",
                    type=JSONToArrowTypeMap().convert(json_schema),
                    # nullable=jsonschema.get("nullable", True),
                )
            ]
        )
