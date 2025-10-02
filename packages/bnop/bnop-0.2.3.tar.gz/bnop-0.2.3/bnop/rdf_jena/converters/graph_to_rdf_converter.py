from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import networkx as nx

from libraries.ontology.bnop.rdf_jena.converters.base_rdf_converter import (
    BaseRdfConverter,
)
from libraries.ontology.bnop.rdf_jena.converters.helpers.conversion_utils import (
    build_uri,
    map_literal,
)
from libraries.ontology.bnop.rdf_jena.object_models.rdf_graphs import (
    RdfGraph,
)
from libraries.ontology.bnop.rdf_jena.object_models.triples import (
    Triple,
)

try:  # pragma: no cover - optional dependency
    from libraries.interop_services.bclearer_interop_services.b_simple_graph_service.objects.b_simple_graphs import (
        BSimpleGraphs,
    )
except Exception:  # pragma: no cover

    class BSimpleGraphs:  # type: ignore[too-few-public-methods]
        """Fallback stand-in when b_simple_graphs is unavailable."""


class GraphToRdfConverter(BaseRdfConverter):
    """Convert graph structures to RDF triples."""

    def __init__(self, namespace: str) -> None:
        super().__init__()
        if not namespace:
            raise ValueError("namespace required")
        self._namespace = namespace

    def convert_graph(self, graph: nx.Graph | BSimpleGraphs) -> RdfGraph:
        """Convert *graph* to an RDF graph."""
        if graph is None:
            raise ValueError("graph cannot be None")

        nx_graph = graph.graph if isinstance(graph, BSimpleGraphs) else graph
        rdf_graph = self.convert(nx_graph.nodes(data=True))
        self._add_edges(nx_graph, rdf_graph)
        return rdf_graph

    def _convert_item(
        self,
        item: tuple[Any, Mapping[str, Any]],
        graph: RdfGraph,
    ) -> None:
        """Add triples for node *item* to *graph*."""
        node_id, attributes = item
        subject = build_uri(self._namespace, str(node_id))
        for key, value in attributes.items():
            if value is None:
                continue
            predicate = build_uri(self._namespace, key)
            obj = map_literal(value)
            graph.add_triple(Triple(subject, predicate, obj))

    def _add_edges(self, graph: nx.Graph, rdf_graph: RdfGraph) -> None:
        for source, target, data in graph.edges(data=True):
            predicate_name = data.get("label", "relatedTo")
            predicate = build_uri(self._namespace, str(predicate_name))
            subject = build_uri(self._namespace, str(source))
            obj = build_uri(self._namespace, str(target))
            rdf_graph.add_triple(Triple(subject, predicate, obj))
