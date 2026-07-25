"""SCA-Unit public package interface."""

from .assessment import StructuralAssessment, assess_structures
from .models import StructuralState
from .typed_relations import (
    count_typed_relation_conflicts,
    detect_typed_relation_conflicts,
)

__all__ = [
    "StructuralAssessment",
    "StructuralState",
    "assess_structures",
    "count_typed_relation_conflicts",
    "detect_typed_relation_conflicts",
]

__version__ = "0.4.0"
