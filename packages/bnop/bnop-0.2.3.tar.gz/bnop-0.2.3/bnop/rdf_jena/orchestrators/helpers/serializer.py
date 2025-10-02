"""RDF graph serialization helper."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph

from libraries.ontology.bnop.rdf_jena.constants.serialization_formats import (
    SUPPORTED_FORMATS,
    detect_format_from_filename,
)
from libraries.ontology.bnop.rdf_jena.object_models.rdf_graphs import RdfGraph

_FORMAT_TO_RDFLIB = {
    "turtle": "turtle",
    "rdf/xml": "pretty-xml",
    "json-ld": "json-ld",
    "n-triples": "nt",
}


@dataclass
class Serializer:
    """Serialize :class:`RdfGraph` to various formats."""

    def _build_graph(self, graph: RdfGraph) -> Graph:
        rdflib_graph = Graph()
        for prefix, uri in graph.namespaces.items():
            rdflib_graph.bind(prefix, uri)
        data = graph.to_n_triples()
        if data:
            rdflib_graph.parse(data=data, format="nt")
        return rdflib_graph

    def to_string(self, graph: RdfGraph, format_name: str) -> str:
        """Return ``graph`` serialized to ``format_name``.

        Raises
        ------
        ValueError
            If ``format_name`` is unsupported.

        """
        if format_name not in SUPPORTED_FORMATS:
            raise ValueError("unsupported format")
        rdflib_graph = self._build_graph(graph)
        rdflib_format = _FORMAT_TO_RDFLIB[format_name]
        return rdflib_graph.serialize(format=rdflib_format)

    def to_file(
        self,
        graph: RdfGraph,
        path: str | Path,
        *,
        format_name: str | None = None,
    ) -> None:
        """Write ``graph`` to ``path`` using ``format_name``.

        If ``format_name`` is ``None`` it is inferred from ``path``.
        """
        fmt = format_name or detect_format_from_filename(str(path))
        if fmt is None:
            raise ValueError("format could not be inferred")
        data = self.to_string(graph, fmt)
        Path(path).write_text(data, encoding="utf-8")
