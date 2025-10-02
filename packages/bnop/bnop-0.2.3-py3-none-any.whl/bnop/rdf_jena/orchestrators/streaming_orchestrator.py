from __future__ import annotations

import json
import tempfile
from collections.abc import Callable, Iterable, Mapping

from libraries.ontology.bnop.rdf_jena.object_models.jena_sessions import (
    JenaSessions,
)
from libraries.ontology.bnop.rdf_jena.orchestrators.rdf_edge_loader import (
    RdfEdgeLoader,
)
from libraries.ontology.bnop.rdf_jena.orchestrators.rdf_node_loader import (
    RdfNodeLoader,
)


class StreamingError(Exception):
    """Raised when streaming operations fail."""


class StreamingOrchestrator:
    """Stream large RDF datasets efficiently."""

    def __init__(
        self,
        session: JenaSessions,
        batch_size: int = 100,
        cache_size_mb: int = 10,
    ) -> None:
        self.session = session
        self.batch_size = batch_size
        self.cache_size = cache_size_mb * 1024 * 1024
        self.node_loader = RdfNodeLoader(session, batch_size)
        self.edge_loader = RdfEdgeLoader(session, batch_size)

    def stream(
        self,
        nodes: Iterable[Mapping[str, Mapping[str, str]]] | None = None,
        edges: Iterable[Mapping[str, str]] | None = None,
    ) -> None:
        """Stream nodes and edges from iterables."""
        try:
            with self.session:
                if nodes:
                    self._stream_iter(nodes, self.node_loader.load_nodes)
                if edges:
                    self._stream_iter(edges, self.edge_loader.load_edges)
        except Exception as exc:  # pragma: no cover - defensive
            raise StreamingError("failed to stream data") from exc

    def _stream_iter(
        self,
        iterable: Iterable[Mapping[str, object]],
        loader: Callable[[Iterable[Mapping[str, object]]], None],
    ) -> None:
        with tempfile.SpooledTemporaryFile(
            max_size=self.cache_size,
            mode="w+",
            encoding="utf-8",
        ) as spooled:
            count = 0
            for item in iterable:
                spooled.write(json.dumps(item) + "\n")
                count += 1
                if count >= self.batch_size:
                    self._flush(spooled, loader)
                    count = 0
            if count:
                self._flush(spooled, loader)

    def _flush(
        self,
        spooled: tempfile.SpooledTemporaryFile,
        loader: Callable[[Iterable[Mapping[str, object]]], None],
    ) -> None:
        spooled.seek(0)
        batch = [json.loads(line) for line in spooled]
        loader(batch)
        spooled.seek(0)
        spooled.truncate()
