from schematools.jsonschema import JSONSchemaParser
from schematools.jsonschema.flatten import flatten


def test_flatten():
    """Test flatten."""
    schema = JSONSchemaParser.parse(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "address": {
                    "type": "object",
                    "properties": {
                        "number": {"type": "integer"},
                        "street": {"type": "string"},
                        "city": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "zip": {"type": "string"},
                            },
                        },
                    },
                },
            },
        }
    )
    flattened = flatten(schema)
    expected = JSONSchemaParser.parse(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "address__number": {"type": "integer"},
                "address__street": {"type": "string"},
                "address__city__name": {"type": "string"},
                "address__city__zip": {"type": "string"},
            },
        }
    )
    assert flattened == expected


def test_no_flatten():
    """Test no flatten."""
    schema = JSONSchemaParser.parse(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "address": {
                    "type": "object",
                    "properties": {
                        "number": {"type": "integer"},
                        "street": {"type": "string"},
                        "city": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "zip": {"type": "string"},
                            },
                        },
                    },
                },
            },
        }
    )
    flattened = flatten(schema, max_depth=0)
    assert flattened == schema


def test_flatten_max_depth():
    """Test flatten max depth."""
    schema = JSONSchemaParser.parse(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "address": {
                    "type": "object",
                    "properties": {
                        "number": {"type": "integer"},
                        "street": {"type": "string"},
                        "city": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "zip": {"type": "string"},
                            },
                        },
                    },
                },
            },
        }
    )
    flattened = flatten(schema, max_depth=1)
    expected = JSONSchemaParser.parse(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "address__number": {"type": "integer"},
                "address__street": {"type": "string"},
                "address__city": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "zip": {"type": "string"},
                    },
                },
            },
        }
    )
    assert flattened == expected
