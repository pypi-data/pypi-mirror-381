from __future__ import annotations

from pathlib import Path

from defusedxml import ElementTree

from libraries.ontology.bnop.rdf_jena.converters.base_rdf_converter import (
    BaseRdfConverter,
)
from libraries.ontology.bnop.rdf_jena.converters.helpers.conversion_utils import (
    build_uri,
    map_literal,
)
from libraries.ontology.bnop.rdf_jena.object_models.rdf_graphs import (
    RdfGraph,
)
from libraries.ontology.bnop.rdf_jena.object_models.triples import (
    Triple,
)


class XmlToRdfConverter(BaseRdfConverter):
    """Convert XML elements to RDF triples."""

    def __init__(self, namespace: str) -> None:
        super().__init__()
        if not namespace:
            raise ValueError("namespace required")
        self._namespace = namespace
        self._blank_counter = 0

    def convert_file(self, path: str | Path) -> RdfGraph:
        """Convert XML file at *path* to RDF."""
        namespaces: dict[str, str] = {}
        for _, elem in ElementTree.iterparse(path, events=("start-ns",)):
            prefix, uri = elem
            namespaces[prefix] = uri
        tree = ElementTree.parse(path)
        root = tree.getroot()
        graph = self.convert([root])
        for prefix, uri in namespaces.items():
            graph.add_namespace(prefix, uri)
        return graph

    def _convert_item(self, item: ElementTree.Element, graph: RdfGraph) -> None:  # type: ignore[override]
        """Add triples for XML *item* to *graph*."""
        subject = self._element_uri(item)
        for attr, value in item.attrib.items():
            if attr == "id":
                continue
            predicate = build_uri(self._namespace, self._local_name(attr))
            obj = map_literal(value)
            graph.add_triple(Triple(subject, predicate, obj))
        text = (item.text or "").strip()
        if text:
            predicate = build_uri(self._namespace, "value")
            obj = map_literal(text)
            graph.add_triple(Triple(subject, predicate, obj))
        for child in list(item):
            child_subject = self._element_uri(child)
            predicate = build_uri(self._namespace, self._local_name(child.tag))
            graph.add_triple(Triple(subject, predicate, child_subject))
            self._convert_item(child, graph)

    def _element_uri(self, element: ElementTree.Element) -> str:
        identifier = element.attrib.get("id")
        if identifier:
            return build_uri(self._namespace, identifier)
        self._blank_counter += 1
        return f"_:b{self._blank_counter}"

    @staticmethod
    def _local_name(tag: str) -> str:
        return tag.split("}")[-1]
