import typing as t

from schematools.jsonschema.base import BaseJSONType
from schematools.jsonschema.object_ import ObjectType

DEFAULT_MAX_DEPTH = 10
DEFAULT_SEPARATOR = "__"


def flatten(
    jsonschema: BaseJSONType, max_depth: int | None = None, separator: str | None = None
) -> BaseJSONType:
    """Flatten JSON schema."""
    max_depth = max_depth or DEFAULT_MAX_DEPTH
    separator = separator or DEFAULT_SEPARATOR

    if max_depth <= 0:
        return jsonschema

    if isinstance(jsonschema, ObjectType) and jsonschema.has_properties():
        flattened_properties = {}
        max_depth -= 1  # first level of flattening is here
        for key, value in jsonschema.properties.items():
            if isinstance(value, ObjectType) and value.has_properties():
                flattened_properties.update(
                    {
                        f"{key}{separator}{k}": v
                        for k, v in flatten(
                            value, max_depth - 1, separator
                        ).properties.items()
                    }
                )
            else:
                flattened_properties[key] = value
        # TODO: return a copy of the object with the new properties, rather than modifying the original object
        jsonschema.properties = flattened_properties

    return jsonschema
