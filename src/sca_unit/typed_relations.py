"""Typed relation conflict detection for SCA-Unit.

This module provides a small deterministic engine for detecting conflicts
between typed relations represented as dictionaries.

The implementation is intentionally additive. It does not replace the
existing simple edge comparison model.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Tuple


Relation = Dict[str, Any]
Conflict = Dict[str, Any]


def _relation_key(relation: Relation) -> Tuple[str, str]:
    return (str(relation.get("source", "")), str(relation.get("target", "")))


def _relation_type(relation: Relation) -> str:
    return str(relation.get("type", ""))


def _required(relation: Relation) -> bool:
    return bool(relation.get("required", False))


def detect_typed_relation_conflicts(
    first_relations: Iterable[Relation],
    second_relations: Iterable[Relation],
) -> List[Conflict]:
    """Detect deterministic conflicts between two typed-relation lists.

    Supported conflict types:
    - relation_type_changed
    - relation_direction_reversed
    - required_relation_removed
    - required_status_changed
    """

    first = list(first_relations or [])
    second = list(second_relations or [])

    second_by_pair: Dict[Tuple[str, str], Relation] = {}
    second_by_reversed_pair_and_type: Dict[Tuple[str, str, str], Relation] = {}

    for relation in second:
        source, target = _relation_key(relation)
        relation_type = _relation_type(relation)
        second_by_pair[(source, target)] = relation
        second_by_reversed_pair_and_type[(target, source, relation_type)] = relation

    conflicts: List[Conflict] = []

    for relation in first:
        source, target = _relation_key(relation)
        relation_type = _relation_type(relation)
        same_pair = second_by_pair.get((source, target))

        if same_pair is not None:
            second_type = _relation_type(same_pair)

            if relation_type != second_type:
                conflicts.append(
                    {
                        "conflict_type": "relation_type_changed",
                        "source": source,
                        "target": target,
                        "first_relation": relation,
                        "second_relation": same_pair,
                        "explanation": (
                            f"Relation {source} -> {target} changed type "
                            f"from {relation_type} to {second_type}."
                        ),
                    }
                )

            if _required(relation) != _required(same_pair):
                conflicts.append(
                    {
                        "conflict_type": "required_status_changed",
                        "source": source,
                        "target": target,
                        "first_relation": relation,
                        "second_relation": same_pair,
                        "explanation": (
                            f"Relation {source} -> {target} changed required "
                            f"status from {_required(relation)} to {_required(same_pair)}."
                        ),
                    }
                )

            continue

        reversed_relation = second_by_reversed_pair_and_type.get((source, target, relation_type))

        if reversed_relation is not None:
            conflicts.append(
                {
                    "conflict_type": "relation_direction_reversed",
                    "source": source,
                    "target": target,
                    "first_relation": relation,
                    "second_relation": reversed_relation,
                    "explanation": (
                        f"Relation direction changed from {source} -> {target} "
                        f"to {target} -> {source}."
                    ),
                }
            )
            continue

        if _required(relation):
            conflicts.append(
                {
                    "conflict_type": "required_relation_removed",
                    "source": source,
                    "target": target,
                    "first_relation": relation,
                    "second_relation": None,
                    "explanation": (
                        f"Required relation {source} -> {target} is missing "
                        "from the second structure."
                    ),
                }
            )

    return conflicts


def count_typed_relation_conflicts(
    first_relations: Iterable[Relation],
    second_relations: Iterable[Relation],
) -> int:
    """Return the number of detected typed relation conflicts."""

    return len(detect_typed_relation_conflicts(first_relations, second_relations))

REQUIRED_RELATION_FIELDS = ("source", "target", "type", "required")


def validate_typed_relations(
    relations: Iterable[Relation],
) -> Dict[str, Any]:
    """Validate typed relation inputs without raising exceptions.

    Returns:
    - valid_relations
    - invalid_relations
    - validation_errors
    """

    valid_relations: List[Relation] = []
    invalid_relations: List[Relation] = []
    validation_errors: List[Dict[str, Any]] = []

    for index, relation in enumerate(list(relations or [])):
        missing_fields = [
            field for field in REQUIRED_RELATION_FIELDS if field not in relation
        ]

        if missing_fields:
            invalid_relations.append(relation)

            for field in missing_fields:
                validation_errors.append(
                    {
                        "relation_index": index,
                        "missing_field": field,
                        "message": (
                            "Typed relation is missing required field: "
                            f"{field}"
                        ),
                    }
                )

            continue

        valid_relations.append(relation)

    return {
        "valid_relations": valid_relations,
        "invalid_relations": invalid_relations,
        "validation_errors": validation_errors,
    }