"""RDF graph validation utilities."""

from __future__ import annotations

from dataclasses import dataclass

from rdflib import Graph
from rdflib.namespace import OWL, RDF

try:  # pragma: no cover
    from pyshacl import validate as sh_validate
except ImportError:  # pragma: no cover
    sh_validate = None  # type: ignore[assignment]


@dataclass
class RdfValidator:
    """Validate graphs via SHACL and OWL."""

    def validate_shacl(
        self,
        data_graph: Graph,
        shacl_graph: Graph,
    ) -> None:
        """Validate with a SHACL shapes graph.

        Raises
        ------
        ImportError
            If pyshacl is missing.
        ValueError
            If validation fails.

        """
        if sh_validate is None:
            raise ImportError(
                "pyshacl is required",
            )
        conforms, _, report = sh_validate(
            data_graph,
            shacl_graph=shacl_graph,
        )
        if not conforms:
            raise ValueError(report)

    def validate_owl(
        self,
        graph: Graph,
    ) -> None:
        """Check basic OWL consistency."""
        for c1, _, c2 in graph.triples(
            (None, OWL.disjointWith, None),
        ):
            for inst in graph.subjects(
                RDF.type,
                c1,
            ):
                if (inst, RDF.type, c2) in graph:
                    raise ValueError(
                        "ontology inconsistent",
                    )
