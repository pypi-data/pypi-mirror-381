"""OWL vocabulary constants and axiom builders."""

from __future__ import annotations

from libraries.ontology.bnop.rdf_jena.constants.standard_namespaces import (
    OWL_NS,
    RDF_NS,
    RDFS_NS,
)
from libraries.ontology.bnop.rdf_jena.object_models.triples import Triple

# OWL entity declarations
CLASS = f"{OWL_NS}Class"
OBJECT_PROPERTY = f"{OWL_NS}ObjectProperty"
DATATYPE_PROPERTY = f"{OWL_NS}DatatypeProperty"
ANNOTATION_PROPERTY = f"{OWL_NS}AnnotationProperty"

# Common OWL axioms
EQUIVALENT_CLASS = f"{OWL_NS}equivalentClass"
SAME_AS = f"{OWL_NS}sameAs"
SUBCLASS_OF = f"{RDFS_NS}subClassOf"
RDF_TYPE = f"{RDF_NS}type"


def declare_class(uri: str) -> Triple:
    """Return a triple declaring ``uri`` as an OWL class."""
    return Triple(uri, RDF_TYPE, CLASS)


def declare_object_property(uri: str) -> Triple:
    """Return a triple declaring ``uri`` as an OWL object property."""
    return Triple(uri, RDF_TYPE, OBJECT_PROPERTY)


def declare_datatype_property(uri: str) -> Triple:
    """Return a triple declaring ``uri`` as an OWL datatype property."""
    return Triple(uri, RDF_TYPE, DATATYPE_PROPERTY)


def build_subclass_axiom(subclass: str, superclass: str) -> Triple:
    """Return a triple stating that ``subclass`` is a subclass of ``superclass``."""
    return Triple(subclass, SUBCLASS_OF, superclass)


def build_equivalent_class_axiom(first: str, second: str) -> Triple:
    """Return a triple stating that ``first`` is equivalent to ``second``."""
    return Triple(first, EQUIVALENT_CLASS, second)


def build_same_as_axiom(first: str, second: str) -> Triple:
    """Return a triple stating that ``first`` and ``second`` denote the same individual."""
    return Triple(first, SAME_AS, second)
