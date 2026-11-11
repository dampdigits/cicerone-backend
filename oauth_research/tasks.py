import threading
import uuid
from typing import Any

from oauth_research.services import ResearchPipeline

JOB_STORE: dict[str, dict[str, Any]] = {}


def create_job(payload: dict[str, Any]) -> str:
    job_id = str(uuid.uuid4())
    JOB_STORE[job_id] = {
        "job_id": job_id,
        "status": "queued",
        "provider": payload.get("provider") or payload.get("provider_name") or "unknown",
        "payload": payload,
    }
    thread = threading.Thread(target=_run_job, args=(job_id, payload), daemon=True)
    thread.start()
    return job_id


def _run_job(job_id: str, payload: dict[str, Any]) -> None:
    JOB_STORE[job_id]["status"] = "running"
    try:
        pipeline = ResearchPipeline(
            provider_name=payload.get("provider") or payload.get("provider_name") or "unknown",
            document_url=payload.get("doc_url"),
            overrides={
                "domains": payload.get("domains") or [],
                "seeds": payload.get("seeds") or [],
                "select_paths": payload.get("select_paths") or [],
                "exclude_paths": payload.get("exclude_paths") or [],
                "max_urls": payload.get("max_urls"),
                "dry_run": payload.get("dry_run", False),
            },
        )
        result = pipeline.run()
        JOB_STORE[job_id]["status"] = "completed"
        JOB_STORE[job_id]["result"] = result
    except Exception as exc:  # pragma: no cover - defensive; job remains visible for debugging
        JOB_STORE[job_id]["status"] = "failed"
        JOB_STORE[job_id]["error"] = str(exc)


def get_job(job_id: str) -> dict[str, Any] | None:
    return JOB_STORE.get(job_id)
