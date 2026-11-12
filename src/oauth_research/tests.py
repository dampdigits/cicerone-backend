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
            reverse("provider-research"),
            {"provider": "github", "doc_url": "https://docs.github.com/en/apps/oauth-apps"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.json()["job_id"], "job-123")
        self.assertEqual(response.json()["status"], "queued")
