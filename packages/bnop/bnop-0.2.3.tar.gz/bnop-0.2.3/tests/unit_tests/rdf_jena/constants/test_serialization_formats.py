import pytest
from bnop.rdf_jena.constants.serialization_formats import (
    EXTENSION_TO_FORMAT,
    MIME_TYPE_TO_FORMAT,
    SUPPORTED_FORMATS,
    detect_format_from_filename,
    detect_format_from_mime_type,
    get_mime_type,
)


def test_supported_formats_keys():
    assert set(SUPPORTED_FORMATS) == {
        "turtle",
        "rdf/xml",
        "json-ld",
        "n-triples",
    }


@pytest.mark.parametrize(
    ("format_name", "mime_type"),
    [
        ("turtle", "text/turtle"),
        ("rdf/xml", "application/rdf+xml"),
        ("json-ld", "application/ld+json"),
        ("n-triples", "application/n-triples"),
    ],
)
def test_get_mime_type(format_name, mime_type):
    assert get_mime_type(format_name) == mime_type


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("example.ttl", "turtle"),
        ("example.rdf", "rdf/xml"),
        ("example.xml", "rdf/xml"),
        ("example.jsonld", "json-ld"),
        ("example.json", "json-ld"),
        ("example.nt", "n-triples"),
    ],
)
def test_detect_format_from_filename(filename, expected):
    assert detect_format_from_filename(filename) == expected


def test_detect_format_from_filename_unknown():
    assert detect_format_from_filename("example.txt") is None


@pytest.mark.parametrize(
    ("mime_type", "expected"),
    [
        ("text/turtle", "turtle"),
        ("application/rdf+xml", "rdf/xml"),
        ("application/ld+json", "json-ld"),
        ("application/n-triples", "n-triples"),
    ],
)
def test_detect_format_from_mime_type(mime_type, expected):
    assert detect_format_from_mime_type(mime_type) == expected


def test_detect_format_from_mime_type_unknown():
    assert detect_format_from_mime_type("text/plain") is None
