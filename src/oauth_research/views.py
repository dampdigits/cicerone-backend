from __future__ import annotations

from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView

# tasks.py should now hold the code from jobs.py (create_job, get_job, JobQueueFull, TERMINAL).
from oauth_research.tasks import TERMINAL, JobQueueFull, create_job, get_job


class HealthView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return Response({"status": "ok", "service": "cicerone"})


class ResearchRequestSerializer(serializers.Serializer):
    """Validates the request body: types, lengths and counts. Anything else is a 400, not a 500."""

    provider = serializers.CharField(max_length=80, required=False)
    provider_name = serializers.CharField(max_length=80, required=False)
    doc_url = serializers.URLField(max_length=500, required=False, allow_null=True)
    domains = serializers.ListField(child=serializers.CharField(max_length=253), max_length=10, required=False)
    seeds = serializers.ListField(child=serializers.URLField(max_length=500), max_length=10, required=False)
    select_paths = serializers.ListField(child=serializers.CharField(max_length=200), max_length=10, required=False)
    exclude_paths = serializers.ListField(child=serializers.CharField(max_length=200), max_length=10, required=False)
    max_urls = serializers.IntegerField(min_value=5, max_value=60, required=False, allow_null=True)
    dry_run = serializers.BooleanField(required=False, default=False)

    def validate(self, attrs):
        name = (attrs.get("provider") or attrs.get("provider_name") or "").strip()
        if not name:
            raise serializers.ValidationError({"provider": "This field is required."})
        attrs["provider"] = name  # keep the caller's casing; the pipeline looks up the registry case-insensitively
        return attrs


class ResearchAPIView(APIView):
    # Every run spends paid Tavily and OpenRouter credits, so this must not be anonymous.
    # Swap IsAuthenticated for your own API-key permission if only a service calls it.
    permission_classes = []
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = "research_create"  # needs REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"]["research_create"] = "10/hour"

    def post(self, request, *args, **kwargs):
        serializer = ResearchRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # 400 with per-field messages
        data = serializer.validated_data

        # Registry domains/seeds are applied inside ResearchPipeline, so they are not merged here.
        job_payload = {k: data.get(k) for k in (
            "provider", "doc_url", "domains", "seeds", "select_paths", "exclude_paths", "max_urls", "dry_run")}
        try:
            job_id = create_job(job_payload, owner=str(request.user.pk))
        except ValueError as exc:  # the pipeline rejected the provider name or similar
            return Response({"detail": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        except JobQueueFull as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_503_SERVICE_UNAVAILABLE,
                            headers={"Retry-After": "30"})

        return Response(
            {"job_id": job_id, "status": "queued", "poll_after_seconds": 2,
             "message": "Provider research job accepted."},
            status=status.HTTP_202_ACCEPTED,
        )


class JobStatusView(APIView):
    permission_classes = []

    def get(self, request, job_id, *args, **kwargs):
        job = get_job(str(job_id), owner=str(request.user.pk))  # None for unknown, expired or someone else's job
        if not job:
            return Response({"detail": "job not found."}, status=status.HTTP_404_NOT_FOUND)

        body = {
            "job_id": job["job_id"],
            "status": job["status"],          # queued | running | completed | partial | failed | dry_run
            "provider": job.get("provider"),
            "stage": job.get("stage"),         # for a progress label, e.g. "extracting"
            "stage_detail": job.get("stage_detail"),
            "finished": job["status"] in TERMINAL,
        }
        if not body["finished"]:
            body["poll_after_seconds"] = 3
        if job.get("error"):
            body["error"] = job["error"]
        if "result" in job:
            body["result"] = job["result"]
        return Response(body, headers={"Cache-Control": "no-store"})
