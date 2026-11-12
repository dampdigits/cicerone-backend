from django.http import JsonResponse
from django.urls import include, path


def healthz(request):
    return JsonResponse({"status": "ok", "service": "cicerone"})


urlpatterns = [
    path("healthz/", healthz, name="healthz"),
    path("api/", include("oauth_research.urls")),
]
