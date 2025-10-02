from __future__ import annotations

from collections.abc import Iterable, Mapping

from libraries.ontology.bnop.rdf_jena.object_models.jena_sessions import (
    JenaSessions,
)


class EdgeLoadError(Exception):
    """Raised when edge loading fails."""


class RdfEdgeLoader:
    """Load RDF edges into a Jena session."""

    def __init__(
        self,
        session: JenaSessions,
        batch_size: int = 100,
    ) -> None:
        self.session = session
        self.batch_size = batch_size

    def load_edges(
        self,
        edges: Iterable[Mapping[str, str]],
    ) -> None:
        """Load edges with batch processing."""
        edge_list = list(edges)
        for i in range(0, len(edge_list), self.batch_size):
            batch = edge_list[i : i + self.batch_size]
            self._load_batch(batch)

    def _load_batch(
        self,
        batch: list[Mapping[str, str]],
    ) -> None:
        self.session.begin()
        try:
            existing = set(self.session.query(""))
            for edge in batch:
                self._validate_edge(edge)
                subj = edge["subject"]
                pred = edge["predicate"]
                obj = edge["object"]
                triple = (subj, pred, obj)
                if triple in existing:
                    continue
                self.session.add_triple(
                    subj,
                    pred,
                    obj,
                )
                existing.add(triple)
            self.session.commit()
        except Exception as exc:
            self.session.rollback()
            raise EdgeLoadError(
                "failed to load edges",
            ) from exc

    def _validate_edge(
        self,
        edge: Mapping[str, str],
    ) -> None:
        for key in ("subject", "predicate", "object"):
            value = edge.get(key)
            if not isinstance(value, str):
                msg = f"edge '{key}' must be a string"
                raise TypeError(msg)
            if not value:
                msg = f"edge '{key}' required"
                raise ValueError(msg)
