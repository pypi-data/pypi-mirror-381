from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import date, datetime
from pathlib import Path

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


class JsonToRdfConverter(BaseRdfConverter):
    """Convert JSON objects to RDF triples."""

    def __init__(self, namespace: str) -> None:
        super().__init__()
        if not namespace:
            raise ValueError("namespace required")
        self._namespace = namespace
        self._blank_counter = 0

    def convert_file(self, path: str | Path) -> RdfGraph:
        """Convert JSON file at *path* to RDF."""
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
        items = data if isinstance(data, list) else [data]
        return self.convert(items)

    def _convert_item(
        self,
        item: Mapping[str, object],
        graph: RdfGraph,
    ) -> None:
        """Add triples for JSON *item* to *graph*."""
        if not isinstance(item, Mapping):
            raise TypeError("item must be mapping")
        identifier = str(item.get("id", self.processed))
        subject = build_uri(self._namespace, identifier)
        self._handle_mapping(subject, item, graph)

    def _handle_mapping(
        self,
        subject: str,
        mapping: Mapping[str, object],
        graph: RdfGraph,
    ) -> None:
        for key, value in mapping.items():
            if key == "id" or value is None:
                continue
            predicate = build_uri(self._namespace, key)
            self._handle_value(subject, predicate, value, graph)

    def _handle_value(
        self,
        subject: str,
        predicate: str,
        value: object,
        graph: RdfGraph,
    ) -> None:
        if isinstance(value, Mapping):
            blank = self._new_blank_node()
            graph.add_triple(Triple(subject, predicate, blank))
            self._handle_mapping(blank, value, graph)
        elif isinstance(value, list):
            for item in value:
                self._handle_value(subject, predicate, item, graph)
        else:
            if not isinstance(value, (str, bool, int, float, date, datetime)):
                value = str(value)
            obj = map_literal(value)  # type: ignore[arg-type]
            graph.add_triple(Triple(subject, predicate, obj))

    def _new_blank_node(self) -> str:
        self._blank_counter += 1
        return f"_:b{self._blank_counter}"
