"""Batch loader for RDF resources."""

from __future__ import annotations

from collections.abc import Iterable, Mapping

from libraries.ontology.bnop.rdf_jena.object_models.jena_sessions import (
    JenaSessions,
)


class NodeLoadError(Exception):
    """Raised when node loading fails."""


class RdfNodeLoader:
    """Load RDF nodes into a Jena session."""

    def __init__(
        self,
        session: JenaSessions,
        batch_size: int = 100,
    ) -> None:
        self.session = session
        self.batch_size = batch_size

    def load_nodes(
        self,
        nodes: Iterable[Mapping[str, Mapping[str, str]]],
    ) -> None:
        """Load nodes with batch processing."""
        node_list = list(nodes)
        for i in range(0, len(node_list), self.batch_size):
            batch = node_list[i : i + self.batch_size]
            self._load_batch(batch)

    def _load_batch(
        self,
        batch: list[Mapping[str, Mapping[str, str]]],
    ) -> None:
        self.session.begin()
        try:
            for node in batch:
                self._validate_node(node)
                uri = node["uri"]
                props = node.get("properties", {})
                for predicate, obj in props.items():
                    self.session.add_triple(
                        uri,
                        predicate,
                        obj,
                    )
            self.session.commit()
        except Exception as exc:
            self.session.rollback()
            raise NodeLoadError(
                "failed to load nodes",
            ) from exc

    def _validate_node(
        self,
        node: Mapping[str, Mapping[str, str]],
    ) -> None:
        uri = node.get("uri")
        if not isinstance(uri, str):
            msg = "node 'uri' must be a string"
            raise TypeError(msg)
        if not uri:
            msg = "node 'uri' required"
            raise ValueError(msg)
        props = node.get("properties", {})
        if not isinstance(props, Mapping):
            msg = "'properties' must be a mapping"
            raise TypeError(msg)
        for pred, obj in props.items():
            if not pred or not obj:
                msg = "invalid predicate or object"
                raise ValueError(msg)
