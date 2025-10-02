from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping

from libraries.ontology.bnop.rdf_jena.object_models.jena_sessions import JenaSessions
from libraries.ontology.bnop.rdf_jena.orchestrators.rdf_edge_loader import RdfEdgeLoader
from libraries.ontology.bnop.rdf_jena.orchestrators.rdf_node_loader import RdfNodeLoader


class BulkLoadError(Exception):
    """Raised when bulk loading fails."""


class BulkLoadOrchestrator:
    """Coordinate high-performance RDF node and edge loading."""

    def __init__(self, session: JenaSessions, batch_size: int = 100) -> None:
        self.session = session
        self.node_loader = RdfNodeLoader(session, batch_size)
        self.edge_loader = RdfEdgeLoader(session, batch_size)

    def load(
        self,
        nodes: Iterable[Mapping[str, Mapping[str, str]]] | None = None,
        edges: Iterable[Mapping[str, str]] | None = None,
        progress: Callable[[int, int], None] | None = None,
    ) -> None:
        """Load nodes and edges with progress tracking."""
        node_list = list(nodes) if nodes is not None else []
        edge_list = list(edges) if edges is not None else []
        total = len(node_list) + len(edge_list)
        loaded = 0

        try:
            with self.session:
                if node_list:
                    self.node_loader.load_nodes(node_list)
                    loaded += len(node_list)
                    if progress:
                        progress(loaded, total)
                if edge_list:
                    self.edge_loader.load_edges(edge_list)
                    loaded += len(edge_list)
                    if progress:
                        progress(loaded, total)
        except Exception as exc:  # pragma: no cover - defensive programming
            raise BulkLoadError("failed to bulk load data") from exc
