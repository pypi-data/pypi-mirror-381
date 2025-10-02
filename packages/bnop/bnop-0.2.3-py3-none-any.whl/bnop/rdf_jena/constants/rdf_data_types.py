"""RDF data type constants and utilities."""

import re
from datetime import date, datetime

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
RDFS_NS = "http://www.w3.org/2000/01/rdf-schema#"
OWL_NS = "http://www.w3.org/2002/07/owl#"
XSD_NS = "http://www.w3.org/2001/XMLSchema#"

URI_PATTERN = re.compile(
    r"^[a-zA-Z][a-zA-Z0-9+.-]*://"
    r"[^\s<>\"{}|^`\\]*$",
)

RDF_LITERAL_URIS: dict[str, str] = {
    "string": f"{XSD_NS}string",
    "boolean": f"{XSD_NS}boolean",
    "integer": f"{XSD_NS}integer",
    "float": f"{XSD_NS}double",
    "date": f"{XSD_NS}date",
    "dateTime": f"{XSD_NS}dateTime",
}

PYTHON_TYPE_MAP: dict[type, str] = {
    str: "string",
    bool: "boolean",
    int: "integer",
    float: "float",
    datetime: "dateTime",
    date: "date",
}

ValueType = str | bool | int | float | date | datetime


def is_valid_uri(uri: str) -> bool:
    return bool(URI_PATTERN.match(uri))


def is_valid_literal(
    value: ValueType,
    literal: str,
) -> bool:
    expected = {
        "string": str,
        "boolean": bool,
        "integer": int,
        "float": float,
        "date": date,
        "dateTime": datetime,
    }[literal]
    if expected is int and isinstance(value, bool):
        return False
    return isinstance(value, expected)


def get_literal_uri(value: ValueType) -> str:
    for py, name in PYTHON_TYPE_MAP.items():
        if isinstance(value, py):
            if py is int and isinstance(value, bool):
                continue
            return RDF_LITERAL_URIS[name]
    raise TypeError("unsupported literal")
