from __future__ import annotations

from collections.abc import Mapping
from csv import DictReader
from pathlib import Path

from libraries.ontology.bnop.rdf_jena.constants.rdf_data_types import (
    ValueType,
)
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


class CsvToRdfConverter(BaseRdfConverter):
    """Converter turning CSV rows into RDF."""

    def __init__(self, namespace: str) -> None:
        super().__init__()
        if not namespace:
            raise ValueError("namespace required")
        self._namespace = namespace

    def convert_file(self, path: str | Path) -> RdfGraph:
        """Convert CSV file at *path* to RDF."""
        with open(path, newline="", encoding="utf-8") as handle:
            reader = DictReader(handle)
            return self.convert(reader)

    def _convert_item(
        self,
        item: Mapping[str, ValueType],
        graph: RdfGraph,
    ) -> None:
        """Add triples for CSV *item* to *graph*."""
        if not isinstance(item, Mapping):
            raise TypeError("item must be mapping")
        identifier = str(item.get("id", self.processed))
        subject = build_uri(self._namespace, identifier)
        for column, value in item.items():
            if column == "id" or value is None:
                continue
            predicate = build_uri(self._namespace, column)
            obj = map_literal(value)
            graph.add_triple(Triple(subject, predicate, obj))
