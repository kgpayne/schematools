from functools import singledispatchmethod

import pyarrow as pa

from schematools.jsonschema import (
    ArrayType,
    BaseJSONSchemaType,
    BooleanType,
    IntegerType,
    JSONSchemaParser,
    NullType,
    NumberType,
    ObjectType,
    StringType,
)

from .convert import SchemaConverterBase


class JSONSchemaToArrowTypeMap:

    @singledispatchmethod
    def convert(self, jsontype: BaseJSONSchemaType) -> pa.DataType:
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


class ArrowToJSONSchemaTypeMap:

    @singledispatchmethod
    def convert(self, arrowtype: pa.DataType) -> BaseJSONSchemaType:
        """Convert Apache Arrow type to JSON type."""
        raise NotImplementedError(f"Conversion of {arrowtype} is not supported")

    @convert.register
    def convert_int64(self, arrowtype: pa.Int64Type) -> IntegerType:
        """Convert Apache Arrow int64 type to JSON type."""
        return IntegerType()

    @convert.register
    def convert_float64(self, arrowtype: pa.Float64Type) -> NumberType:
        """Convert Apache Arrow float64 type to JSON type."""
        return NumberType()

    @convert.register
    def convert_string(self, arrowtype: pa.StringType) -> StringType:
        """Convert Apache Arrow string type to JSON type."""
        return StringType()

    @convert.register
    def convert_bool(self, arrowtype: pa.BooleanType) -> BooleanType:
        """Convert Apache Arrow bool type to JSON type."""
        return BooleanType()

    @convert.register
    def convert_struct(self, arrowtype: pa.StructType) -> ObjectType:
        """Convert Apache Arrow struct type to JSON type."""
        properties = {field.name: self.convert(field.type) for field in arrowtype}
        return ObjectType(properties=properties)

    @convert.register
    def convert_list(self, arrowtype: pa.ListType) -> ArrayType:
        """Convert Apache Arrow list type to JSON type."""
        return ArrayType(items=self.convert(arrowtype.value_type))

    @convert.register
    def convert_null(self, arrowtype: pa.NullType) -> NullType:
        """Convert Apache Arrow null type to JSON type."""
        return NullType()


class ArrowJSONSchemaConverter(SchemaConverterBase):
    """Apache Arrow schema representation."""

    @staticmethod
    def from_jsonschema(cls, jsonschema: BaseJSONSchemaType) -> pa.Schema:
        """Convert JSON schema to Apache Arrow schema."""
        if isinstance(jsonschema, ObjectType) and jsonschema.has_properties():
            return pa.schema(
                [
                    pa.field(
                        name=k,
                        type=JSONSchemaToArrowTypeMap().convert(v),
                        # nullable=jsonschema.get("nullable", True),
                    )
                    for k, v in jsonschema.properties.items()
                ]
            )
        return pa.schema(
            [
                pa.field(
                    name="root",
                    type=JSONSchemaToArrowTypeMap().convert(jsonschema),
                    # nullable=jsonschema.get("nullable", True),
                )
            ]
        )

    @staticmethod
    def to_jsonschema(cls, arrow_schema: pa.Schema) -> BaseJSONSchemaType:
        """Convert Apache Arrow schema to JSON schema."""
        if len(arrow_schema) == 1 and arrow_schema[0].name == "root":
            return ArrowToJSONSchemaTypeMap().convert(arrow_schema[0].type)
        properties = {
            field.name: ArrowToJSONSchemaTypeMap().convert(field.type)
            for field in arrow_schema
        }
        return ObjectType(properties=properties)
