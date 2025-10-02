"""Executable documentation examples for the RDF-Jena service."""

from __future__ import annotations

from collections.abc import Iterable

import networkx as nx

from libraries.ontology.bnop.rdf_jena.configurations import (
    JenaConfigurations,
    JenaLoaderConfigurations,
    RdfConfigurations,
    SparqlConfigurations,
)
from libraries.ontology.bnop.rdf_jena.converters.csv_to_rdf_converter import (
    CsvToRdfConverter,
)
from libraries.ontology.bnop.rdf_jena.converters.graph_to_rdf_converter import (
    GraphToRdfConverter,
)
from libraries.ontology.bnop.rdf_jena.converters.json_to_rdf_converter import (
    JsonToRdfConverter,
)
from libraries.ontology.bnop.rdf_jena.rdf_jena_configuration_factory import (
    create_rdf_jena_configuration,
)
from libraries.ontology.bnop.rdf_jena.rdf_jena_service_facade import (
    RdfJenaServiceFacade,
)

_SELECT_ALL_QUERY = (
    "SELECT ?subject ?predicate ?object WHERE { ?subject ?predicate ?object }"
)
_PEOPLE_NS = "http://example.org/people#"
_ORDERS_NS = "http://example.org/orders#"
_GRAPH_NS = "http://example.org/graph#"


def _create_service(
    *,
    namespace: str = _PEOPLE_NS,
    loader_threshold: int = 100,
    sparql: SparqlConfigurations | None = None,
) -> RdfJenaServiceFacade:
    """Return a service facade with in-memory configuration."""
    rdf_config = RdfConfigurations(default_namespace=namespace)
    loader_config = JenaLoaderConfigurations(
        streaming_threshold_mb=loader_threshold,
    )
    configuration = create_rdf_jena_configuration(
        jena_config=JenaConfigurations.create_in_memory(),
        rdf_config=rdf_config,
        loader_config=loader_config,
        sparql_config=sparql,
    )
    return RdfJenaServiceFacade(configuration)


def _sample_people() -> list[dict[str, str]]:
    return [
        {"id": "alice", "name": "Alice", "role": "Engineer"},
        {"id": "bob", "name": "Bob", "role": "Scientist"},
    ]


def load_csv_people_example() -> list[dict[str, str]]:
    """Load tabular records and return the resulting triples."""
    converter = CsvToRdfConverter(_PEOPLE_NS)
    with _create_service() as service:
        service.load(_sample_people(), converter)
        results = service.query(_SELECT_ALL_QUERY)
    return _sort_rows(results.rows)


def query_people_as_csv_example() -> str:
    """Run a SPARQL query and return CSV formatted results."""
    converter = CsvToRdfConverter(_PEOPLE_NS)
    with _create_service() as service:
        service.load(_sample_people(), converter)
        return service.query_formatted(
            _SELECT_ALL_QUERY,
            format="csv",
        )


def json_blank_nodes_example() -> list[dict[str, str]]:
    """Convert nested JSON structures and stream the load."""
    document = [
        {
            "id": "order-1",
            "customer": {"name": "Alice"},
            "items": [
                {"sku": "A1", "quantity": 2},
                {"sku": "B2", "quantity": 1},
            ],
        },
    ]
    converter = JsonToRdfConverter(_ORDERS_NS)
    with _create_service(
        namespace=_ORDERS_NS,
        loader_threshold=0,
    ) as service:
        service.load(
            document,
            converter,
            strategy="streaming",
        )
        results = service.query(_SELECT_ALL_QUERY)
    return _sort_rows(results.rows)


def graph_to_rdf_example() -> list[str]:
    """Create RDF triples from a NetworkX graph."""
    graph = nx.Graph()
    graph.add_node("A", label="Node A")
    graph.add_node("B", label="Node B")
    graph.add_edge("A", "B", label="connectedTo")
    converter = GraphToRdfConverter(_GRAPH_NS)
    rdf_graph = converter.convert_graph(graph)
    triples = rdf_graph.to_n_triples().splitlines()
    return sorted(triples)


def federated_query_example() -> dict[str, object]:
    """Return configured endpoints and combined query rows."""
    sparql_cfg = SparqlConfigurations(
        allow_federated_queries=True,
    )
    sparql_cfg.add_endpoint(
        "analytics",
        "http://analytics.example/sparql",
    )
    converter = CsvToRdfConverter(_PEOPLE_NS)
    with _create_service(sparql=sparql_cfg) as local:
        local.load(_sample_people(), converter)
        with _create_service() as remote:
            remote_converter = CsvToRdfConverter(_PEOPLE_NS)
            remote.load(
                [{"id": "carol", "name": "Carol"}],
                remote_converter,
            )
            results = local.query(
                _SELECT_ALL_QUERY,
                endpoints=[remote.session],
            )
    return {
        "endpoints": dict(
            local.configuration.sparql_config.service_endpoints,
        ),
        "rows": _sort_rows(
            results.rows,
            include_endpoint=True,
        ),
    }


def _sort_rows(
    rows: Iterable[dict[str, str]],
    *,
    include_endpoint: bool = False,
) -> list[dict[str, str]]:
    """Return rows sorted for deterministic documentation output."""
    key_fields = [
        "subject",
        "predicate",
        "object",
    ]
    if include_endpoint:
        key_fields.insert(0, "endpoint")
    return sorted(
        rows,
        key=lambda row: tuple(row.get(field, "") for field in key_fields),
    )


__all__ = [
    "federated_query_example",
    "graph_to_rdf_example",
    "json_blank_nodes_example",
    "load_csv_people_example",
    "query_people_as_csv_example",
]
