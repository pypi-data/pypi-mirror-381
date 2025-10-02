"""Factory for composing RDF-Jena configuration."""

from dataclasses import dataclass

from bclearer_core.configurations.b_clearer_configurations.b_clearer_configurations import (
    BClearerConfigurations,
)

from libraries.ontology.bnop.rdf_jena.configurations import (
    JenaConfigurations,
    JenaLoaderConfigurations,
    RdfConfigurations,
    SparqlConfigurations,
)


@dataclass
class RdfJenaConfigurations(BClearerConfigurations):
    """Combined configuration for RDF-Jena."""

    jena_config: JenaConfigurations
    rdf_config: RdfConfigurations
    sparql_config: SparqlConfigurations
    loader_config: JenaLoaderConfigurations


def create_rdf_jena_configuration(
    jena_config: JenaConfigurations | None = None,
    rdf_config: RdfConfigurations | None = None,
    sparql_config: SparqlConfigurations | None = None,
    loader_config: JenaLoaderConfigurations | None = None,
) -> RdfJenaConfigurations:
    """Create a complete RDF-Jena configuration."""
    jena_cfg = jena_config or JenaConfigurations.create_in_memory()
    rdf_cfg = rdf_config or RdfConfigurations()
    sparql_cfg = sparql_config or SparqlConfigurations()
    loader_cfg = loader_config or JenaLoaderConfigurations()

    return RdfJenaConfigurations(
        jena_config=jena_cfg,
        rdf_config=rdf_cfg,
        sparql_config=sparql_cfg,
        loader_config=loader_cfg,
    )
