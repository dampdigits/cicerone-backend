"""
oauth_research/tasks.py

Runs ResearchPipeline jobs in a small background thread pool.

Differences from the in-memory version:
  * job state lives in Django's cache, so every web worker sees it. This only works
    with a SHARED cache backend (Redis, Memcached, database or file cache). The
    default LocMemCache is per process and behaves like the old dict.
  * at most MAX_WORKERS jobs run at once and at most MAX_PENDING wait, so users
    cannot start unlimited paid API runs. Add per-user throttling in the view too
    (for example DRF throttling).
  * bad input is rejected when the job is created, so the view can return 400.
  * internal errors are logged with a traceback; the user sees a generic message.
  * a job that stops reporting progress (worker restarted, thread died) is shown as
    failed instead of "running" forever.

Threads die when the process restarts. If you need jobs to survive restarts or run on
another machine, move _run_job into a Celery/RQ task; create_job/get_job stay the same.
"""
from __future__ import annotations

import logging
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from django.core.cache import cache

from oauth_research.services import ResearchPipeline

logger = logging.getLogger(__name__)

MAX_WORKERS = 2
MAX_PENDING = 10          # running + queued
JOB_TTL_SECONDS = 24 * 3600
STALE_AFTER_SECONDS = 30 * 60  # no progress update for this long -> treat as dead

_executor = ThreadPoolExecutor(max_workers=MAX_WORKERS, thread_name_prefix="oauth-research")
_lock = threading.Lock()
_pending = 0

TERMINAL = ("completed", "partial", "failed", "dry_run")

class JobQueueFull(Exception):
    """Too many jobs are running or waiting. The view should answer 429/503."""


def _cache_key(job_id: str) -> str:
    return f"oauth_research:job:{job_id}"


def _save(job: dict[str, Any]) -> None:
    job["updated_at"] = time.time()
    cache.set(_cache_key(job["job_id"]), job, JOB_TTL_SECONDS)


def _update(job_id: str, **fields: Any) -> None:
    with _lock:
        job = cache.get(_cache_key(job_id))
        if job is not None:
            job.update(fields)
            _save(job)


def create_job(payload: dict[str, Any], owner: str | None = None) -> str:
    """Validate, queue and return the job id. Raises ValueError (bad input) or JobQueueFull."""
    global _pending
    payload = payload if isinstance(payload, dict) else {}
    provider = str(payload.get("provider") or payload.get("provider_name") or "").strip()
    job_id = str(uuid.uuid4())

    def progress(stage: str, detail: str = "") -> None:
        _update(job_id, stage=stage, stage_detail=detail)

    # Built here so invalid provider names fail immediately. Construction makes no network calls.
    pipeline = ResearchPipeline(
        provider_name=provider,
        document_url=payload.get("doc_url"),
        overrides={
            "domains": payload.get("domains"),
            "seeds": payload.get("seeds"),
            "select_paths": payload.get("select_paths"),
            "exclude_paths": payload.get("exclude_paths"),
            "max_urls": payload.get("max_urls"),
            "dry_run": bool(payload.get("dry_run", False)),
        },
        progress=progress,
    )

    with _lock:
        if _pending >= MAX_PENDING:
            raise JobQueueFull("Too many research jobs are in progress. Try again later.")
        _pending += 1
        _save({"job_id": job_id, "status": "queued", "stage": None, "stage_detail": "",
               "provider": provider, "owner": owner, "created_at": time.time()})
    try:
        _executor.submit(_run_job, job_id, pipeline)
    except Exception:
        with _lock:
            _pending -= 1
        raise
    return job_id


def _run_job(job_id: str, pipeline: ResearchPipeline) -> None:
    global _pending
    _update(job_id, status="running")
    try:
        result = pipeline.run()
        # status is one of: completed, partial, failed, dry_run
        _update(job_id, status=result["status"], result=result, finished_at=time.time())
    except Exception:  # noqa: BLE001 - keep the worker thread alive; details go to the log
        logger.exception("oauth_research job %s crashed", job_id)
        _update(job_id, status="failed", finished_at=time.time(),
                error=f"Internal error while running the research job (reference {job_id}).")
    finally:
        with _lock:
            _pending -= 1


def get_job(job_id: str, owner: str | None = None) -> dict[str, Any] | None:
    """Return the job, or None if unknown, expired, or owned by someone else."""
    job = cache.get(_cache_key(job_id))
    if job is None or (owner is not None and job.get("owner") != owner):
        return None
    if job.get("status") in ("queued", "running") and time.time() - job.get("updated_at", 0) > STALE_AFTER_SECONDS:
        job = {**job, "status": "failed", "error": "The job stopped reporting progress (the server may have restarted)."}
    return job
