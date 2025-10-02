"""Reusable SPARQL query templates."""

from libraries.ontology.bnop.rdf_jena.constants.sparql_query_forms import (
    ASK,
    CONSTRUCT,
    DESCRIBE,
    QUERY_TEMPLATES,
    SELECT,
    bind_query_template,
)


def build_select_query(select: str, where: str) -> str:
    """Return a SELECT query with ``select`` and ``where``."""
    template = QUERY_TEMPLATES[SELECT]
    return bind_query_template(template, select=select, where=where)


def build_construct_query(construct: str, where: str) -> str:
    """Return a CONSTRUCT query."""
    template = QUERY_TEMPLATES[CONSTRUCT]
    return bind_query_template(template, construct=construct, where=where)


def build_ask_query(where: str) -> str:
    """Return an ASK query."""
    template = QUERY_TEMPLATES[ASK]
    return bind_query_template(template, where=where)


def build_describe_query(describe: str, where: str) -> str:
    """Return a DESCRIBE query."""
    template = QUERY_TEMPLATES[DESCRIBE]
    return bind_query_template(template, describe=describe, where=where)
