from __future__ import annotations

from collections.abc import Iterable, Mapping

from libraries.ontology.bnop.rdf_jena.converters.base_rdf_converter import (
    BaseRdfConverter,
)
from libraries.ontology.bnop.rdf_jena.object_models.jena_sessions import (
    JenaSessions,
)
from libraries.ontology.bnop.rdf_jena.object_models.rdf_graphs import RdfGraph
from libraries.ontology.bnop.rdf_jena.orchestrators.bulk_load_orchestrator import (
    BulkLoadOrchestrator,
)
from libraries.ontology.bnop.rdf_jena.orchestrators.streaming_orchestrator import (
    StreamingOrchestrator,
)


class JenaDataLoadOrchestrator:
    """Orchestrate conversion and loading of RDF data."""

    def __init__(
        self,
        session: JenaSessions,
        batch_size: int = 100,
        streaming_threshold: int = 1000,
    ) -> None:
        self.session = session
        self.bulk = BulkLoadOrchestrator(session, batch_size)
        self.streaming = StreamingOrchestrator(session, batch_size)
        self.streaming_threshold = streaming_threshold

    def load_data(
        self,
        source: Iterable[object],
        converter: BaseRdfConverter,
        *,
        strategy: str | None = None,
    ) -> None:
        """Convert *source* and load it with selected strategy."""
        graph = converter.convert(source)
        nodes, edges = self._graph_to_loadables(graph)
        if strategy is None:
            total = len(nodes) + len(edges)
            strategy = "streaming" if total > self.streaming_threshold else "bulk"
        if strategy == "streaming":
            self.streaming.stream(nodes=nodes, edges=edges)
        elif strategy == "bulk":
            self.bulk.load(nodes=nodes, edges=edges)
        else:  # pragma: no cover - defensive
            msg = "strategy must be 'bulk' or 'streaming'"
            raise ValueError(msg)

    def _graph_to_loadables(
        self,
        graph: RdfGraph,
    ) -> tuple[
        list[Mapping[str, Mapping[str, str]]],
        list[Mapping[str, str]],
    ]:
        nodes: dict[str, dict[str, object]] = {}
        edges: list[dict[str, str]] = []
        for triple in graph.triples:
            subj = triple.subject
            pred = triple.predicate
            obj = triple.object
            if obj.startswith('"'):
                node = nodes.setdefault(
                    subj,
                    {"uri": subj, "properties": {}},
                )
                props = node["properties"]
                props[pred] = obj
            else:
                edges.append(
                    {
                        "subject": subj,
                        "predicate": pred,
                        "object": obj,
                    },
                )
        return list(nodes.values()), edges
