import json
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass(frozen=True, slots=True)
class AuditRecord:
    request_id: str
    timestamp_utc: str
    first_identity: str
    second_identity: str
    status: str


def create_audit_record(
    first_identity: str,
    second_identity: str,
    status: str,
) -> AuditRecord:
    return AuditRecord(
        request_id=str(uuid.uuid4()),
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
        first_identity=first_identity,
        second_identity=second_identity,
        status=status,
    )


def append_audit_record(
    record: AuditRecord,
    log_path: str | Path,
) -> None:
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(asdict(record), ensure_ascii=False))
        log_file.write("\n")