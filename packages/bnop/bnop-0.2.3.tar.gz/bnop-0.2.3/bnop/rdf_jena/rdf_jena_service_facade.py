from __future__ import annotations

"""Service facade for RDF-Jena operations."""

from collections.abc import Iterable
from typing import Self

from libraries.ontology.bnop.rdf_jena.converters.base_rdf_converter import (
    BaseRdfConverter,
)
from libraries.ontology.bnop.rdf_jena.object_models.jena_databases import (
    JenaDatabases,
)
from libraries.ontology.bnop.rdf_jena.object_models.jena_sessions import (
    JenaSessions,
)
from libraries.ontology.bnop.rdf_jena.object_models.query_results import (
    QueryResults,
)
from libraries.ontology.bnop.rdf_jena.orchestrators.jena_data_load_orchestrator import (
    JenaDataLoadOrchestrator,
)
from libraries.ontology.bnop.rdf_jena.orchestrators.sparql_query_orchestrator import (
    SparqlQueryOrchestrator,
)
from libraries.ontology.bnop.rdf_jena.rdf_jena_configuration_factory import (
    RdfJenaConfigurations,
    create_rdf_jena_configuration,
)


class RdfJenaServiceFacade:
    """Main entry point for RDF-Jena operations."""

    def __init__(
        self,
        configuration: RdfJenaConfigurations | None = None,
    ) -> None:
        self.configuration = configuration or create_rdf_jena_configuration()
        self.database = JenaDatabases(self.configuration.jena_config)
        self.session = JenaSessions(self.database)
        loader_cfg = self.configuration.loader_config
        self.data_loader = JenaDataLoadOrchestrator(
            self.session,
            batch_size=loader_cfg.batch_size,
            streaming_threshold=loader_cfg.streaming_threshold_mb,
        )
        self.query_runner = SparqlQueryOrchestrator(self.session)

    def load(
        self,
        source: Iterable[object],
        converter: BaseRdfConverter,
        *,
        strategy: str | None = None,
    ) -> None:
        """Convert *source* with *converter* and load into Jena."""
        self.data_loader.load_data(source, converter, strategy=strategy)

    def query(
        self,
        query: str,
        *,
        endpoints: Iterable[JenaSessions] | None = None,
    ) -> QueryResults:
        """Execute *query* and return structured results."""
        return self.query_runner.execute(query, endpoints=endpoints)

    def query_formatted(
        self,
        query: str,
        *,
        format: str = "json",
        endpoints: Iterable[JenaSessions] | None = None,
    ) -> str:
        """Execute *query* and return formatted results."""
        return self.query_runner.execute_formatted(
            query,
            format=format,
            endpoints=endpoints,
        )

    def close(self) -> None:
        """Close session and underlying database resources."""
        self.session.close()
        self.database.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # pragma: no cover - defensive
        self.close()
