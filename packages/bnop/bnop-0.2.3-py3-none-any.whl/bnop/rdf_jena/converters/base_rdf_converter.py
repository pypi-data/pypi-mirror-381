from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable

from libraries.ontology.bnop.rdf_jena.object_models.rdf_graphs import (
    RdfGraph,
)


class BaseRdfConverter(ABC):
    """Abstract converter producing RDF graphs."""

    def __init__(self) -> None:
        self._processed = 0

    @property
    def processed(self) -> int:
        """Number of items converted."""
        return self._processed

    def convert(self, source: Iterable[object]) -> RdfGraph:
        """Convert items from *source* to RDF."""
        if source is None:
            raise ValueError("source cannot be None")

        graph = RdfGraph()
        for item in source:
            try:
                self._convert_item(item, graph)
            except Exception as exc:  # pragma: no cover
                msg = f"Failed at item {self._processed}: {exc}"
                raise RuntimeError(msg) from exc
            self._processed += 1
        return graph

    @abstractmethod
    def _convert_item(self, item: object, graph: RdfGraph) -> None:
        """Add triples for *item* to *graph*."""
