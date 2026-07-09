import json
from pathlib import Path
from typing import Any

from private_server.audit import append_audit_record, create_audit_record
from sca_unit.assessment import assess_structures
from sca_unit.models import StructuralState


class InputValidationError(ValueError):
    """Raised when invalid structural input is rejected."""


def validate_structure_content(content: Any) -> dict[str, Any]:
    if not isinstance(content, dict):
        raise InputValidationError(
            "The structural payload must be a JSON object"
        )

    required_fields = {"identity", "nodes", "edges"}
    missing_fields = sorted(required_fields - content.keys())

    if missing_fields:
        raise InputValidationError(
            f"Missing required fields: {', '.join(missing_fields)}"
        )

    identity = content["identity"]
    nodes = content["nodes"]
    edges = content["edges"]

    if not isinstance(identity, str) or not identity.strip():
        raise InputValidationError(
            "The identity field must be a non-empty string"
        )

    if not isinstance(nodes, list):
        raise InputValidationError(
            "The nodes field must be a list"
        )

    if not isinstance(edges, list):
        raise InputValidationError(
            "The edges field must be a list"
        )

    return content


def validate_structure_file(
    file_path: str | Path,
) -> dict[str, Any]:
    path = Path(file_path)

    if not path.exists():
        raise InputValidationError(
            f"File does not exist: {path}"
        )

    if not path.is_file():
        raise InputValidationError(
            f"Path is not a file: {path}"
        )

    if path.suffix.lower() != ".json":
        raise InputValidationError(
            "Only JSON files are accepted"
        )

    try:
        content = json.loads(
            path.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError as exc:
        raise InputValidationError(
            "Invalid JSON content"
        ) from exc

    return validate_structure_content(content)


def create_structural_state(
    content: dict[str, Any],
) -> StructuralState:
    try:
        return StructuralState.create(
            identity=content["identity"],
            nodes=content["nodes"],
            edges=content["edges"],
        )
    except (TypeError, ValueError) as exc:
        raise InputValidationError(
            f"Invalid structural data: {exc}"
        ) from exc


def load_structural_state(
    file_path: str | Path,
) -> StructuralState:
    content = validate_structure_file(file_path)
    return create_structural_state(content)


def load_structural_state_from_payload(
    content: Any,
) -> StructuralState:
    validated_content = validate_structure_content(content)
    return create_structural_state(validated_content)


def build_drift_report(
    baseline: StructuralState,
    current: StructuralState,
) -> dict[str, Any]:
    added_nodes = sorted(current.nodes - baseline.nodes)
    removed_nodes = sorted(baseline.nodes - current.nodes)
    added_edges = [
        list(edge)
        for edge in sorted(current.edges - baseline.edges)
    ]
    removed_edges = [
        list(edge)
        for edge in sorted(baseline.edges - current.edges)
    ]

    total_changes = (
        len(added_nodes)
        + len(removed_nodes)
        + len(added_edges)
        + len(removed_edges)
    )

    if total_changes <= 1:
        severity = "low"
    elif total_changes <= 4:
        severity = "medium"
    else:
        severity = "high"

    if total_changes == 0:
        verdict = "no_drift"
    elif total_changes == 1:
        verdict = "minor_review"
    elif total_changes <= 4:
        verdict = "review_required"
    else:
        verdict = "urgent_review"


    human_messages = {
        "no_drift": "No structural drift detected.",
        "minor_review": "One structural change detected; minor review recommended.",
        "review_required": "Multiple structural changes detected; review required.",
        "urgent_review": "Extensive structural drift detected; urgent review required.",
    }
    human_summary = human_messages[verdict]

    return {
        "added_nodes": added_nodes,
        "removed_nodes": removed_nodes,
        "added_edges": added_edges,
        "removed_edges": removed_edges,
        "severity": severity,
        "verdict": verdict,
        "human_summary": human_summary,
        "total_changes": total_changes,
        "summary": {
            "added_node_count": len(added_nodes),
            "removed_node_count": len(removed_nodes),
            "added_edge_count": len(added_edges),
            "removed_edge_count": len(removed_edges),
        },
    }


def build_assessment_report(
    first: StructuralState,
    second: StructuralState,
    audit_log_path: str | Path | None = None,
) -> dict[str, Any]:
    assessment = assess_structures(first, second)

    audit_record = create_audit_record(
        first_identity=first.identity,
        second_identity=second.identity,
        status="completed",
    )

    report = {
        "request_id": audit_record.request_id,
        "schema_version": "1.0",
        "engine": {
            "name": "SCA-Unit Public Structural Assessment",
            "scope": "non-proprietary prototype",
            "version": "0.2.0",
        },
        "assessment": assessment.as_dict(),
        "drift": build_drift_report(first, second),
    }

    if audit_log_path is not None:
        append_audit_record(
            audit_record,
            audit_log_path,
        )

    return report


def assess_structure_files(
    first_file: str | Path,
    second_file: str | Path,
    audit_log_path: str | Path | None = None,
) -> dict[str, Any]:
    first = load_structural_state(first_file)
    second = load_structural_state(second_file)

    return build_assessment_report(
        first,
        second,
        audit_log_path=audit_log_path,
    )


def assess_structure_payloads(
    first_structure: Any,
    second_structure: Any,
    audit_log_path: str | Path | None = None,
) -> dict[str, Any]:
    first = load_structural_state_from_payload(
        first_structure
    )
    second = load_structural_state_from_payload(
        second_structure
    )

    return build_assessment_report(
        first,
        second,
        audit_log_path=audit_log_path,
    )