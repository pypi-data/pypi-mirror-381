from __future__ import annotations

from typing import Any

from libraries.ontology.bnop.rdf_jena.constants.standard_namespaces import (
    OWL_NS,
    RDF_NS,
    RDFS_NS,
)
from libraries.ontology.bnop.rdf_jena.converters.base_rdf_converter import (
    BaseRdfConverter,
)
from libraries.ontology.bnop.rdf_jena.converters.helpers.conversion_utils import (
    build_uri,
    map_literal,
)
from libraries.ontology.bnop.rdf_jena.object_models.rdf_graphs import RdfGraph
from libraries.ontology.bnop.rdf_jena.object_models.triples import Triple

try:  # pragma: no cover
    from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_ids import (
        BieIds,
    )

    from libraries.interop_services.bclearer_interop_services.b_dictionary_service.objects.row_b_dictionaries import (
        RowBDictionaries,
    )
    from libraries.interop_services.bclearer_interop_services.b_dictionary_service.objects.table_b_dictionaries import (
        TableBDictionaries,
    )
except Exception:  # pragma: no cover
    TableBDictionaries = Any  # type: ignore[misc]
    RowBDictionaries = Any  # type: ignore[misc]

    class BieIds:  # type: ignore[too-few-public-methods]
        def __init__(self, value: object = "") -> None:
            self.value = str(value)

        def __str__(self) -> str:
            return self.value


class DatabaseToRdfConverter(BaseRdfConverter):
    """Convert database table schemas to RDF classes."""

    def __init__(self, namespace: str) -> None:
        super().__init__()
        if not namespace:
            raise ValueError("namespace required")
        self._namespace = namespace

    def _convert_item(self, item: TableBDictionaries, graph: RdfGraph) -> None:
        """Add schema triples for *item* to *graph*."""
        self._map_table_schema(item, graph)
        self._map_table_rows(item, graph)

    def _map_table_schema(self, table: TableBDictionaries, graph: RdfGraph) -> None:
        """Map *table* definition to an RDF class."""
        class_uri = build_uri(self._namespace, table.table_name)
        graph.add_triple(
            Triple(class_uri, build_uri(RDF_NS, "type"), build_uri(OWL_NS, "Class")),
        )

        rows = getattr(table, "dictionary", {})
        if not rows:
            return
        first_row = next(iter(rows.values()))
        columns = getattr(first_row, "dictionary", {})
        for column in columns:
            predicate = build_uri(self._namespace, column)
            graph.add_triple(
                Triple(
                    predicate,
                    build_uri(RDF_NS, "type"),
                    build_uri(RDF_NS, "Property"),
                ),
            )
            graph.add_triple(
                Triple(predicate, build_uri(RDFS_NS, "domain"), class_uri),
            )

    def _map_table_rows(
        self,
        table: TableBDictionaries,
        graph: RdfGraph,
    ) -> None:
        """Map *table* rows to RDF instances."""
        class_uri = build_uri(self._namespace, table.table_name)
        rows: dict[object, RowBDictionaries] = getattr(
            table,
            "dictionary",
            {},
        )
        for row_id, row in rows.items():
            subject = build_uri(self._namespace, str(row_id))
            graph.add_triple(
                Triple(
                    subject,
                    build_uri(RDF_NS, "type"),
                    class_uri,
                ),
            )
            columns = getattr(row, "dictionary", {})
            for column, value in columns.items():
                if value is None:
                    continue
                predicate = build_uri(self._namespace, column)
                if isinstance(value, BieIds):
                    obj = build_uri(self._namespace, str(value))
                else:
                    obj = map_literal(value)
                graph.add_triple(Triple(subject, predicate, obj))
