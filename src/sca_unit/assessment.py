from __future__ import annotations

from dataclasses import dataclass
from typing import AbstractSet, Literal, TypeVar

from .models import Edge, StructuralState


T = TypeVar("T")

Verdict = Literal[
    "identical",
    "compatible",
    "partial",
    "conflicting",
    "unrelated",
]


def jaccard_similarity(
    first: AbstractSet[T],
    second: AbstractSet[T],
) -> float:
    """Return Jaccard similarity in the range 0.0 to 1.0."""
    union = first | second

    if not union:
        return 1.0

    return len(first & second) / len(union)


def shared_domain_conflict(
    first: StructuralState,
    second: StructuralState,
) -> float:
    """
    Measure edge disagreement inside the node domain shared
    by both structures.
    """
    shared_nodes = first.nodes & second.nodes

    if not shared_nodes:
        return 0.0

    first_shared_edges: set[Edge] = {
        edge
        for edge in first.edges
        if edge[0] in shared_nodes and edge[1] in shared_nodes
    }

    second_shared_edges: set[Edge] = {
        edge
        for edge in second.edges
        if edge[0] in shared_nodes and edge[1] in shared_nodes
    }

    edge_union = first_shared_edges | second_shared_edges

    if not edge_union:
        return 0.0

    disagreement = first_shared_edges ^ second_shared_edges

    return len(disagreement) / len(edge_union)


@dataclass(frozen=True, slots=True)
class StructuralAssessment:
    first_identity: str
    second_identity: str
    node_similarity: float
    edge_similarity: float
    compatibility: float
    conflict: float
    verdict: Verdict

    def as_dict(self) -> dict[str, str | float]:
        return {
            "first_identity": self.first_identity,
            "second_identity": self.second_identity,
            "node_similarity": round(self.node_similarity, 6),
            "edge_similarity": round(self.edge_similarity, 6),
            "compatibility": round(self.compatibility, 6),
            "conflict": round(self.conflict, 6),
            "verdict": self.verdict,
        }


def assess_structures(
    first: StructuralState,
    second: StructuralState,
) -> StructuralAssessment:
    """Produce a deterministic, non-proprietary structural assessment."""
    node_similarity = jaccard_similarity(first.nodes, second.nodes)
    edge_similarity = jaccard_similarity(first.edges, second.edges)

    compatibility = (
        0.5 * node_similarity
        + 0.5 * edge_similarity
    )

    conflict = shared_domain_conflict(first, second)

    if first.nodes == second.nodes and first.edges == second.edges:
        verdict: Verdict = "identical"
    elif not first.nodes.intersection(second.nodes):
        verdict = "unrelated"
    elif conflict >= 0.5:
        verdict = "conflicting"
    elif compatibility >= 0.65:
        verdict = "compatible"
    else:
        verdict = "partial"

    return StructuralAssessment(
        first_identity=first.identity,
        second_identity=second.identity,
        node_similarity=node_similarity,
        edge_similarity=edge_similarity,
        compatibility=compatibility,
        conflict=conflict,
        verdict=verdict,
    )