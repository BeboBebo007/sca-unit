"""SCA-Unit public package interface."""

try:
    from .typed_relations import (
        count_typed_relation_conflicts,
        detect_typed_relation_conflicts,
    )
except Exception:
    pass
