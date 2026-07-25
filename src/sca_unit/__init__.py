"""SCA-Unit public package interface."""

from .assessment import StructuralAssessment, assess_structures
from .models import StructuralState
from .typed_relations import (
    count_typed_relation_conflicts,
    detect_typed_relation_conflicts,
    validate_typed_relations,
)

__all__ = [
    "StructuralAssessment",
    "StructuralState",
    "assess_structures",
    "count_typed_relation_conflicts",
    "detect_typed_relation_conflicts",
    "validate_typed_relations",
]

__version__ = "0.4.0"
