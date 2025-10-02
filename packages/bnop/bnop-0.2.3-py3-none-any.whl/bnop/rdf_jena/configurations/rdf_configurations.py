from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar

from bclearer_core.configurations.b_clearer_configurations.b_clearer_configurations import (
    BClearerConfigurations,
)

from libraries.ontology.bnop.rdf_jena.constants.serialization_formats import (
    SUPPORTED_FORMATS,
)
from libraries.ontology.bnop.rdf_jena.constants.standard_namespaces import (
    BORO_NS,
    STANDARD_NAMESPACES,
)


@dataclass
class RdfConfigurations(BClearerConfigurations):
    """Settings controlling RDF generation and namespaces."""

    default_namespace: str = BORO_NS
    generate_blank_nodes: bool = True
    preserve_boro_uuids: bool = True
    namespaces: dict[str, str] = field(
        default_factory=lambda: STANDARD_NAMESPACES.copy(),
    )
    supported_formats: list[str] = field(
        default_factory=lambda: list(SUPPORTED_FORMATS.keys()),
    )

    VALID_NAMESPACE_PREFIXES: ClassVar[tuple[str, ...]] = ("http://", "https://")
    _NS_SUFFIXES: ClassVar[tuple[str, ...]] = ("#", "/")

    def __post_init__(self) -> None:
        self.validate()

    def add_namespace(self, prefix: str, uri: str) -> None:
        """Add a custom namespace mapping after validation."""
        self._validate_namespace_uri(uri, f"namespace '{prefix}'")
        self.namespaces[prefix] = uri

    def validate(self) -> None:
        if not self.default_namespace:
            raise ValueError("default_namespace must not be empty")
        self._validate_namespace_uri(self.default_namespace, "default_namespace")
        if self.default_namespace not in self.namespaces.values():
            self.namespaces.setdefault("default", self.default_namespace)
        for prefix, uri in self.namespaces.items():
            self._validate_namespace_uri(uri, f"namespace '{prefix}'")
        for fmt in self.supported_formats:
            if fmt not in SUPPORTED_FORMATS:
                raise ValueError(f"unsupported format: {fmt}")

    def _validate_namespace_uri(self, uri: str, field_name: str) -> None:
        if not uri.startswith(self.VALID_NAMESPACE_PREFIXES):
            raise ValueError(
                f"{field_name} must start with 'http://' or 'https://'",
            )
        if not uri.endswith(self._NS_SUFFIXES):
            raise ValueError(
                f"{field_name} must end with '#' or '/'",
            )
