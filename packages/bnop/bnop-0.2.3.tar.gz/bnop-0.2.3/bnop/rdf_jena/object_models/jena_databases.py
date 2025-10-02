from __future__ import annotations

from typing import Any, Self

from libraries.ontology.bnop.rdf_jena.configurations.jena_configurations import (
    JenaConfigurations,
)

from .jena_connections import JenaConnections


class JenaDatabases:
    """Handle dataset management and session
    creation for Jena stores.
    """

    def __init__(self, configuration: JenaConfigurations) -> None:
        self.configuration = configuration
        self.connections = JenaConnections(configuration)
        self._dataset: dict[str, str] | None = None

    def get_or_create_dataset(self) -> dict[str, str]:
        """Return existing dataset or create a
        new one.
        """
        if self._dataset is None:
            self._dataset = {
                "store_type": self.configuration.jena_store_type,
                "path": self.configuration.jena_store_path,
            }
        return self._dataset

    def create_session(self) -> dict[str, Any]:
        """Acquire a connection and bind it to the
        dataset.
        """
        dataset = self.get_or_create_dataset()
        connection = self.connections.acquire()
        return {"dataset": dataset, "connection": connection}

    def close_session(self, session: dict[str, Any]) -> None:
        """Release the session's connection."""
        connection = session.get("connection")
        if connection is not None:
            self.connections.release(connection)

    def close(self) -> None:
        """Close all database resources."""
        self.connections.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
