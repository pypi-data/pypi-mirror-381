from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar

from bclearer_core.configurations.b_clearer_configurations.b_clearer_configurations import (
    BClearerConfigurations,
)


@dataclass
class SparqlConfigurations(BClearerConfigurations):
    """Settings controlling SPARQL query execution."""

    timeout_seconds: int = 30
    result_limit: int = 1000
    allow_federated_queries: bool = False
    service_endpoints: dict[str, str] = field(
        default_factory=dict,
    )

    VALID_URI_PREFIXES: ClassVar[tuple[str, ...]] = (
        "http://",
        "https://",
    )

    def __post_init__(self) -> None:
        self.validate()

    def add_endpoint(self, name: str, uri: str) -> None:
        """Add a federated SPARQL service endpoint."""
        self._validate_endpoint_uri(uri, f"service '{name}'")
        self.service_endpoints[name] = uri

    def validate(self) -> None:
        if self.timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        if self.result_limit <= 0:
            raise ValueError("result_limit must be positive")
        if not self.allow_federated_queries and self.service_endpoints:
            raise ValueError(
                "federated queries disabled but service_endpoints provided",
            )
        for name, uri in self.service_endpoints.items():
            self._validate_endpoint_uri(uri, f"service '{name}'")

    def _validate_endpoint_uri(self, uri: str, field_name: str) -> None:
        if not uri.startswith(self.VALID_URI_PREFIXES):
            raise ValueError(
                f"{field_name} must start with 'http://' or 'https://'",
            )
