"""Common RDF and BORO namespaces with helpers."""

from __future__ import annotations

# Standard RDF/OWL namespaces
RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
RDFS_NS = "http://www.w3.org/2000/01/rdf-schema#"
OWL_NS = "http://www.w3.org/2002/07/owl#"
SKOS_NS = "http://www.w3.org/2004/02/skos/core#"
DCTERMS_NS = "http://purl.org/dc/terms/"

# BORO namespace for bclearer ontology objects
BORO_NS = "http://bclearer.org/ontology#"

# Mapping of common prefix to namespace URI
STANDARD_NAMESPACES: dict[str, str] = {
    "rdf": RDF_NS,
    "rdfs": RDFS_NS,
    "owl": OWL_NS,
    "skos": SKOS_NS,
    "dcterms": DCTERMS_NS,
    "boro": BORO_NS,
}


def build_uri(namespace: str, name: str) -> str:
    """Return a URI within ``namespace`` for ``name``."""
    return f"{namespace}{name}"


def build_boro_uri(name: str) -> str:
    """Return a URI within the BORO namespace for ``name``."""
    return build_uri(BORO_NS, name)
