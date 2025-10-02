from __future__ import annotations

from collections.abc import Iterable
from typing import Any, Self

from .jena_databases import JenaDatabases


class TransactionError(Exception):
    """Raised when transaction operations fail."""


class JenaSessions:
    """Provide transactional operations for a Jena dataset."""

    def __init__(self, databases: JenaDatabases) -> None:
        self.databases = databases
        self._session: dict[str, Any] | None = None
        self._in_transaction = False
        self._snapshot: set[tuple[str, str, str]] | None = None

    def open(self) -> None:
        """Open a session if none is active."""
        if self._session is None:
            self._session = self.databases.create_session()
            dataset = self._session["dataset"]
            dataset.setdefault("data", set())

    def close(self) -> None:
        """Close the current session."""
        if self._session is not None:
            self.databases.close_session(self._session)
            self._session = None
            self._in_transaction = False
            self._snapshot = None

    def __enter__(self) -> Self:
        self.open()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def begin(self) -> None:
        """Begin a transaction."""
        if self._session is None:
            self.open()
        dataset = self._session["dataset"]
        self._snapshot = set(dataset["data"])
        self._in_transaction = True

    def commit(self) -> None:
        """Commit changes made during the transaction."""
        if not self._in_transaction:
            raise TransactionError("no active transaction")
        self._in_transaction = False
        self._snapshot = None

    def rollback(self) -> None:
        """Revert changes made during the transaction."""
        if not self._in_transaction:
            raise TransactionError("no active transaction")
        dataset = self._session["dataset"]
        dataset["data"] = self._snapshot or set()
        self._in_transaction = False
        self._snapshot = None

    def add_triple(self, subj: str, pred: str, obj: str) -> None:
        """Insert a triple into the dataset."""
        if self._session is None:
            self.open()
        dataset = self._session["dataset"]
        dataset["data"].add((subj, pred, obj))

    def delete_triple(self, subj: str, pred: str, obj: str) -> None:
        """Remove a triple from the dataset."""
        if self._session is None:
            self.open()
        dataset = self._session["dataset"]
        dataset["data"].discard((subj, pred, obj))

    def update_triple(
        self,
        old: tuple[str, str, str],
        new: tuple[str, str, str],
    ) -> None:
        """Replace one triple with another."""
        self.delete_triple(*old)
        self.add_triple(*new)

    def query(self, _sparql: str) -> Iterable[tuple[str, str, str]]:
        """Execute a SPARQL query and return results."""
        if self._session is None:
            self.open()
        dataset = self._session["dataset"]
        return set(dataset["data"])
