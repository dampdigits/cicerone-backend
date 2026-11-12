from django.urls import path

from oauth_research.views import (
    HealthView,
    JobStatusView,
    ResearchAPIView,
)

urlpatterns = [
    path("healthz/", HealthView.as_view(), name="healthz"),
    path("research/", ResearchAPIView.as_view(), name="provider-research"),
    path("jobs/<str:job_id>/status/", JobStatusView.as_view(), name="provider-job-status"),
]
