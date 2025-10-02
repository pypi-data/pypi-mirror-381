from __future__ import annotations

"""Constants and utilities for common SPARQL query forms."""

import string

# Supported SPARQL query forms
SELECT = "SELECT"
CONSTRUCT = "CONSTRUCT"
ASK = "ASK"
DESCRIBE = "DESCRIBE"

QUERY_FORMS: set[str] = {SELECT, CONSTRUCT, ASK, DESCRIBE}

# Minimal query templates for each form
QUERY_TEMPLATES: dict[str, str] = {
    SELECT: "SELECT {select} WHERE {where}",
    CONSTRUCT: "CONSTRUCT {construct} WHERE {where}",
    ASK: "ASK WHERE {where}",
    DESCRIBE: "DESCRIBE {describe} WHERE {where}",
}


def detect_query_form(query: str) -> str | None:
    """Return the SPARQL form used by ``query`` if supported."""
    stripped = query.lstrip().upper()
    for form in QUERY_FORMS:
        if stripped.startswith(form):
            return form
    return None


def is_supported_query(query: str) -> bool:
    """Return ``True`` if ``query`` starts with a supported SPARQL form."""
    return detect_query_form(query) is not None


def bind_query_template(template: str, **params: str) -> str:
    """Fill a SPARQL query ``template`` with ``params``.

    Raises ``KeyError`` if required parameters are missing.
    """
    formatter = string.Formatter()
    required = {
        field_name for _, field_name, _, _ in formatter.parse(template) if field_name
    }
    missing = required - params.keys()
    if missing:
        raise KeyError(f"Missing parameters: {sorted(missing)}")
    return template.format(**params)
