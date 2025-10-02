"""Prefix mappings utilities for RDF output."""

from __future__ import annotations

from libraries.ontology.bnop.rdf_jena.constants.standard_namespaces import (
    STANDARD_NAMESPACES,
)

PREFIX_MAPPINGS: dict[str, str] = dict(STANDARD_NAMESPACES)


def register_prefix(prefix: str, namespace: str) -> None:
    """Register ``prefix`` for ``namespace``."""
    PREFIX_MAPPINGS[prefix] = namespace


def get_namespace(prefix: str) -> str | None:
    """Return namespace URI for ``prefix`` if registered."""
    return PREFIX_MAPPINGS.get(prefix)


def get_prefix(namespace: str) -> str | None:
    """Return prefix associated with ``namespace`` if registered."""
    for registered_prefix, registered_namespace in PREFIX_MAPPINGS.items():
        if registered_namespace == namespace:
            return registered_prefix
    return None
