from __future__ import annotations

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from oauth_research.tasks import create_job, get_job


class HealthView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return Response({"status": "ok", "service": "cicerone"})


class ResearchAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        payload = request.data or {}
        provider_name = (payload.get("provider") or payload.get("provider_name") or "").strip()
        if not provider_name:
            return Response({"detail": "provider is required."}, status=status.HTTP_400_BAD_REQUEST)

        overrides = {
            "domains": payload.get("domains") or [],
            "seeds": payload.get("seeds") or [],
            "select_paths": payload.get("select_paths") or [],
            "exclude_paths": payload.get("exclude_paths") or [],
            "max_urls": payload.get("max_urls"),
            "dry_run": payload.get("dry_run", False),
        }

        job_payload = {
            "provider": provider_name,
            "doc_url": payload.get("doc_url"),
            **overrides,
        }
        job_id = create_job(job_payload)

        return Response(
            {
                "job_id": job_id,
                "status": "queued",
                "message": "Provider research job accepted and running.",
            },
            status=status.HTTP_202_ACCEPTED,
        )


class JobStatusView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, job_id, *args, **kwargs):
        job = get_job(job_id)
        if not job:
            return Response({"detail": "job not found."}, status=status.HTTP_404_NOT_FOUND)

        response = {
            "job_id": job["job_id"],
            "status": job["status"],
            "provider": job.get("provider"),
        }
        if "error" in job:
            response["error"] = job["error"]
        if "result" in job:
            response["result"] = job["result"]
        return Response(response)
