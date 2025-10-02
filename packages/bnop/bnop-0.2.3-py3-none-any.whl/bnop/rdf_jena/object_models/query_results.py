from __future__ import annotations

import csv
import io
import json
from dataclasses import dataclass, field
from typing import Any
from xml.etree.ElementTree import Element, SubElement, tostring


@dataclass
class QueryResults:
    """Structured SPARQL query results."""

    rows: list[dict[str, Any]] = field(default_factory=list)

    def add_row(self, row: dict[str, Any]) -> None:
        """Add a result row."""
        self.rows.append(row)

    def to_json(self) -> str:
        """Return results in JSON format."""
        return json.dumps({"results": self.rows})

    def to_csv(self) -> str:
        """Return results in CSV format."""
        if not self.rows:
            return ""
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=list(self.rows[0].keys()))
        writer.writeheader()
        writer.writerows(self.rows)
        return output.getvalue().strip()

    def to_xml(self) -> str:
        """Return results in XML format."""
        root = Element("results")
        for row in self.rows:
            result_el = SubElement(root, "result")
            for key, value in row.items():
                binding = SubElement(result_el, key)
                binding.text = str(value)
        return tostring(root, encoding="unicode")
