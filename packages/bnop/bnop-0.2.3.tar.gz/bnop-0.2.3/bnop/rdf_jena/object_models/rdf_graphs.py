"""RDF graph container and namespace manager."""

from dataclasses import dataclass, field

from .triples import Triple


@dataclass
class RdfGraph:
    """Collection of RDF triples with namespace and metadata support."""

    triples: list[Triple] = field(default_factory=list)
    namespaces: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, str] = field(default_factory=dict)

    def add_triple(self, triple: Triple) -> None:
        """Append a triple to the graph."""
        self.triples.append(triple)

    def add_namespace(self, prefix: str, uri: str) -> None:
        """Register a namespace prefix."""
        self.namespaces[prefix] = uri

    def get_namespace(self, prefix: str) -> str:
        """Return the URI for a namespace prefix."""
        return self.namespaces[prefix]

    def to_n_triples(self) -> str:
        """Serialize all triples to N-Triples format."""
        return "\n".join(triple.to_n_triple() for triple in self.triples)
