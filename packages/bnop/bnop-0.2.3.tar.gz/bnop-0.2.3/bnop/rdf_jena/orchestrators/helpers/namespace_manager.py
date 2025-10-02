"""Manage namespace prefixes and URIs."""

from __future__ import annotations

from dataclasses import dataclass, field

from libraries.ontology.bnop.rdf_jena.constants.standard_namespaces import (
    STANDARD_NAMESPACES,
    build_uri,
)


@dataclass
class NamespaceManager:
    """Register and resolve namespace prefixes."""

    namespaces: dict[str, str] = field(
        default_factory=lambda: dict(
            STANDARD_NAMESPACES,
        ),
    )

    def register(
        self,
        prefix: str,
        namespace: str,
    ) -> None:
        """Register ``prefix`` with ``namespace``.

        Raises
        ------
        ValueError
            If ``prefix`` already exists with a
            different ``namespace``.

        """
        if prefix in self.namespaces and self.namespaces[prefix] != namespace:
            raise ValueError(
                f"prefix {prefix!r} already registered",
            )
        self.namespaces[prefix] = namespace

    def get_namespace(
        self,
        prefix: str,
    ) -> str:
        """Return namespace for ``prefix``."""
        return self.namespaces[prefix]

    def resolve(
        self,
        prefixed_name: str,
    ) -> str:
        """Expand ``prefix:name`` to full URI."""
        prefix, _, name = prefixed_name.partition(
            ":",
        )
        if not name:
            raise ValueError(
                "missing ':' in prefixed name",
            )
        namespace = self.get_namespace(prefix)
        return build_uri(namespace, name)

    def shrink(
        self,
        uri: str,
    ) -> str:
        """Reduce full ``uri`` to ``prefix:name``.

        Selects the *longest* matching namespace to handle nested namespaces and
        ensure that ``shrink`` is the inverse of :meth:`resolve` for registered
        prefixes.
        """
        longest_prefix: str | None = None
        longest_namespace = ""
        for prefix, namespace in self.namespaces.items():
            if uri.startswith(namespace) and len(namespace) > len(longest_namespace):
                longest_prefix = prefix
                longest_namespace = namespace

        if longest_prefix is None:
            raise ValueError(
                "URI not in registered namespaces",
            )

        local = uri[len(longest_namespace) :]
        return f"{longest_prefix}:{local}"
