from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, TypeAlias


Node: TypeAlias = str
Edge: TypeAlias = tuple[Node, Node]


def normalize_edge(source: Node, target: Node) -> Edge:
    """Normalize an undirected edge into a stable representation."""
    if source == target:
        raise ValueError("Self-referencing edges are not supported.")

    return tuple(sorted((source, target)))


@dataclass(frozen=True, slots=True)
class StructuralState:
    """Immutable representation of a simple structural state."""

    identity: str
    nodes: frozenset[Node]
    edges: frozenset[Edge]

    @classmethod
    def create(
        cls,
        identity: str,
        nodes: Iterable[Node],
        edges: Iterable[tuple[Node, Node]],
    ) -> "StructuralState":
        if not identity.strip():
            raise ValueError("Structural identity must not be empty.")

        normalized_nodes = frozenset(str(node) for node in nodes)

        normalized_edges = frozenset(
            normalize_edge(str(source), str(target))
            for source, target in edges
        )

        referenced_nodes = {
            node
            for edge in normalized_edges
            for node in edge
        }

        unknown_nodes = referenced_nodes - normalized_nodes

        if unknown_nodes:
            unknown = ", ".join(sorted(unknown_nodes))
            raise ValueError(
                f"Edges reference nodes not present in the structure: {unknown}"
            )

        return cls(
            identity=identity,
            nodes=normalized_nodes,
            edges=normalized_edges,
        )