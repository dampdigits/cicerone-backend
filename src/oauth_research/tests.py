from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse


class CiceroneApiTests(TestCase):
    def test_healthz(self):
        response = self.client.get("/healthz/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    @patch("oauth_research.views.create_job")
    def test_research_endpoint_accepts_provider_request(self, mock_create_job):
        mock_create_job.return_value = "job-123"

        response = self.client.post(
            reverse("oauth_research:provider-research"),
            {"provider": "github", "doc_url": "https://docs.github.com/en/apps/oauth-apps"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.json()["job_id"], "job-123")
        self.assertEqual(response.json()["status"], "queued")
        # Verify anonymous user passes owner=None
        mock_create_job.assert_called_once()
        call_kwargs = mock_create_job.call_args
        self.assertIsNone(call_kwargs[1].get("owner") if call_kwargs[1] else call_kwargs[0][1])

    @patch("oauth_research.views.get_job")
    def test_job_status_anonymous_user(self, mock_get_job):
        mock_get_job.return_value = {
            "job_id": "job-123",
            "status": "running",
            "provider": "github",
            "stage": "discovering",
            "stage_detail": "searching official docs",
        }

        response = self.client.get(
            reverse("oauth_research:provider-job-status", kwargs={"job_id": "job-123"}),
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "running")
        # Verify anonymous user passes owner=None
        mock_get_job.assert_called_once_with("job-123", owner=None)
