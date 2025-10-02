from __future__ import annotations

from collections.abc import Iterable

from libraries.ontology.bnop.rdf_jena.object_models.jena_sessions import (
    JenaSessions,
)
from libraries.ontology.bnop.rdf_jena.object_models.query_results import (
    QueryResults,
)


class SparqlQueryError(Exception):
    """Raised when SPARQL query execution fails."""


class SparqlQueryOrchestrator:
    """Execute SPARQL queries and format results."""

    def __init__(self, session: JenaSessions) -> None:
        self.session = session

    def execute(
        self,
        query: str,
        *,
        endpoints: Iterable[JenaSessions] | None = None,
    ) -> QueryResults:
        """Run *query* against session and optional *endpoints*."""
        results = QueryResults()
        datasets = [self.session]
        if endpoints:
            datasets.extend(endpoints)
        for dataset in datasets:
            try:
                for subj, pred, obj in dataset.query(query):
                    row = {
                        "subject": subj,
                        "predicate": pred,
                        "object": obj,
                    }
                    if endpoints:
                        row["endpoint"] = (
                            "local" if dataset is self.session else "federated"
                        )
                    results.add_row(row)
            except Exception as exc:  # pragma: no cover - defensive
                raise SparqlQueryError("failed to execute query") from exc
        return results

    def execute_formatted(
        self,
        query: str,
        *,
        format: str = "json",
        endpoints: Iterable[JenaSessions] | None = None,
    ) -> str:
        """Run *query* and return results in selected *format*."""
        results = self.execute(query, endpoints=endpoints)
        if format == "json":
            return results.to_json()
        if format == "csv":
            return results.to_csv()
        if format == "xml":
            return results.to_xml()
        msg = "format must be 'json', 'csv', or 'xml'"
        raise ValueError(msg)
