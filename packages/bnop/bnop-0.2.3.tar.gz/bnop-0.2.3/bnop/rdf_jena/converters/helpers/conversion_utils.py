from __future__ import annotations

from urllib.parse import quote, urljoin

from libraries.ontology.bnop.rdf_jena.constants.rdf_data_types import (
    ValueType,
    get_literal_uri,
    is_valid_uri,
)


def build_uri(namespace: str, identifier: str) -> str:
    """Return full URI for *identifier* in *namespace*."""
    if not namespace:
        raise ValueError("namespace required")
    if not identifier:
        raise ValueError("identifier required")
    base = namespace
    if not base.endswith(("/", "#")):
        base += "#"
    uri = urljoin(base, quote(identifier))
    if not is_valid_uri(uri):
        raise ValueError(f"invalid uri: {uri}")
    return f"<{uri}>"


def map_literal(value: ValueType) -> str:
    """Return N-Triples literal for *value*."""
    uri = get_literal_uri(value)
    return f'"{value}"^^<{uri}>'


def ensure_uri(uri: str) -> None:
    """Validate *uri* string."""
    if uri.startswith("<") and uri.endswith(">"):
        uri = uri[1:-1]
    if not is_valid_uri(uri):
        raise ValueError(f"invalid uri: {uri}")


def format_error(
    message: str,
    *,
    line: int | None = None,
    column: int | None = None,
) -> str:
    """Return error message with location info."""
    parts = [message]
    if line is not None:
        parts.append(f"line {line}")
    if column is not None:
        parts.append(f"column {column}")
    if len(parts) == 1:
        return message
    return f"{message} ({', '.join(parts[1:])})"


def report_progress(processed: int, total: int) -> str:
    """Return formatted progress string."""
    if total <= 0:
        return f"{processed}/?"
    percent = (processed / total) * 100
    return f"{processed}/{total} ({percent:.1f}%)"
