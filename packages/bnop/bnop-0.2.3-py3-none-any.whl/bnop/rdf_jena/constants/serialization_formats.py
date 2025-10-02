"""Constants and utilities for RDF serialization formats."""

from __future__ import annotations

from os import path

# Supported serialization formats mapped to their MIME types
SUPPORTED_FORMATS: dict[str, str] = {
    "turtle": "text/turtle",
    "rdf/xml": "application/rdf+xml",
    "json-ld": "application/ld+json",
    "n-triples": "application/n-triples",
}

# File extensions mapped to serialization formats
EXTENSION_TO_FORMAT: dict[str, str] = {
    ".ttl": "turtle",
    ".rdf": "rdf/xml",
    ".xml": "rdf/xml",
    ".jsonld": "json-ld",
    ".json": "json-ld",
    ".nt": "n-triples",
}

# MIME types mapped to serialization formats
MIME_TYPE_TO_FORMAT: dict[str, str] = {
    mime: fmt for fmt, mime in SUPPORTED_FORMATS.items()
}


def get_mime_type(format_name: str) -> str:
    """Return the MIME type for a supported serialization format."""
    return SUPPORTED_FORMATS[format_name]


def detect_format_from_filename(filename: str) -> str | None:
    """Return the serialization format inferred from a file name.

    Returns ``None`` if the extension is not recognized.
    """
    _, ext = path.splitext(filename.lower())
    return EXTENSION_TO_FORMAT.get(ext)


def detect_format_from_mime_type(mime_type: str) -> str | None:
    """Return the serialization format for a MIME type.

    Returns ``None`` if the MIME type is not supported.
    """
    return MIME_TYPE_TO_FORMAT.get(mime_type.lower())
