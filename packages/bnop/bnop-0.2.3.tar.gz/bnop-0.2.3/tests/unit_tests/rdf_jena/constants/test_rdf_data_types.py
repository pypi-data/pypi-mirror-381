from datetime import UTC, date, datetime, timezone

import pytest
from bnop.rdf_jena.constants.rdf_data_types import (
    RDF_LITERAL_URIS,
    get_literal_uri,
    is_valid_literal,
    is_valid_uri,
)


@pytest.mark.parametrize(
    "uri",
    [
        "http://example.org/one",
        "https://example.org/two",
    ],
)
def test_is_valid_uri_accepts(uri):
    assert is_valid_uri(uri)


@pytest.mark.parametrize(
    "uri",
    [
        "example.org",
        "http://exa mple.org",
    ],
)
def test_is_valid_uri_rejects(uri):
    assert not is_valid_uri(uri)


def test_is_valid_literal_accepts():
    assert is_valid_literal("a", "string")
    assert is_valid_literal(
        value=True,
        literal="boolean",
    )
    assert is_valid_literal(7, "integer")
    assert is_valid_literal(3.5, "float")
    assert is_valid_literal(date(2024, 1, 1), "date")
    assert is_valid_literal(
        datetime(2024, 1, 1, tzinfo=UTC),
        "dateTime",
    )


def test_is_valid_literal_rejects_bool_as_int():
    assert not is_valid_literal(
        value=True,
        literal="integer",
    )


def test_get_literal_uri_returns():
    assert get_literal_uri("a") == RDF_LITERAL_URIS["string"]
    assert get_literal_uri(value=True) == RDF_LITERAL_URIS["boolean"]
    assert get_literal_uri(7) == RDF_LITERAL_URIS["integer"]
    assert get_literal_uri(3.5) == RDF_LITERAL_URIS["float"]
    assert get_literal_uri(date(2024, 1, 1)) == RDF_LITERAL_URIS["date"]
    assert (
        get_literal_uri(
            datetime(2024, 1, 1, tzinfo=UTC),
        )
        == RDF_LITERAL_URIS["dateTime"]
    )


def test_get_literal_uri_rejects_unsupported():
    with pytest.raises(TypeError):
        get_literal_uri(object())
