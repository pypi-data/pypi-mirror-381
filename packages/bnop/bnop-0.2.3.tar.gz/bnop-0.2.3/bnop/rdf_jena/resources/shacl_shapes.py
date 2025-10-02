from __future__ import annotations

from libraries.ontology.bnop.rdf_jena.constants.standard_namespaces import (
    RDF_NS,
)
from libraries.ontology.bnop.rdf_jena.object_models.triples import Triple

SHACL_NS = "http://www.w3.org/ns/shacl#"

NODE_SHAPE = f"{SHACL_NS}NodeShape"
PROPERTY_SHAPE = f"{SHACL_NS}PropertyShape"
PROPERTY = f"{SHACL_NS}property"
PATH = f"{SHACL_NS}path"
CLASS = f"{SHACL_NS}class"
MIN_COUNT = f"{SHACL_NS}minCount"
MAX_COUNT = f"{SHACL_NS}maxCount"


def build_node_shape(uri: str) -> Triple:
    """Return a triple declaring ``uri`` as a SHACL node shape."""
    return Triple(uri, f"{RDF_NS}type", NODE_SHAPE)


def link_property_shape(node_shape: str, prop_shape: str) -> Triple:
    """Return a triple linking ``prop_shape`` to ``node_shape``."""
    return Triple(node_shape, PROPERTY, prop_shape)


def build_property_shape(
    uri: str,
    path: str,
    *,
    class_uri: str | None = None,
    min_count: int | None = None,
    max_count: int | None = None,
) -> list[Triple]:
    """Return triples defining a SHACL property shape."""
    triples = [
        Triple(uri, f"{RDF_NS}type", PROPERTY_SHAPE),
        Triple(uri, PATH, path),
    ]
    if class_uri is not None:
        triples.append(Triple(uri, CLASS, class_uri))
    if min_count is not None:
        triples.append(Triple(uri, MIN_COUNT, str(min_count)))
    if max_count is not None:
        triples.append(Triple(uri, MAX_COUNT, str(max_count)))
    return triples
