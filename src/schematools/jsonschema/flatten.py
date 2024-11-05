import typing as t


def flatten(jsonschema: BaseJSONType) -> t.List[BaseJSONType]:
    """Flatten JSON schema."""
    return [jsonschema]
