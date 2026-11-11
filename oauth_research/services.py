import json
import os
import re
from typing import Any
from urllib.parse import urlparse

import requests
from django.conf import settings
from tavily import TavilyClient

from provider_info import PROVIDERS

TOPIC_KEYWORDS = {
    "account_requirements": ["developer account", "tenant", "organization", "admin approval"],
    "registration": ["register", "create app", "application registration", "client id"],
    "redirect_uri": ["redirect uri", "callback url", "redirect url", "redirect_uri"],
    "credentials": ["client secret", "client id", "credentials", "certificate"],
    "scopes": ["scope", "permissions", "oauth scopes"],
    "consent": ["consent screen", "user consent", "admin consent", "approve access"],
    "verification": ["verification", "review", "publisher verification", "app review", "approval"],
    "production": ["production", "publish", "live app", "public app"],
    "limits": ["quota", "limit", "restriction", "threshold", "expiry"],
}


def _slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "provider"


def _normalize_url(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url)
    path = parsed.path.rstrip("/") or "/"
    return f"{parsed.scheme}://{parsed.netloc.lower()}{path}"


def _strip_code_block(text: str) -> str:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"\s*```\s*$", "", cleaned)
    return cleaned.strip()


def _env(name: str, default: str = "") -> str:
    return os.getenv(name) or getattr(settings, name, default) or default


class ResearchPipeline:
    def __init__(self, provider_name: str, document_url: str | None = None, overrides: dict[str, Any] | None = None):
        self.provider_name = (provider_name or "").strip()
        self.document_url = (document_url or "").strip() or None
        self.overrides = overrides or {}
        self.provider_config = self._resolve_provider_config()
        self.tavily_api_key = _env("TAVILY_API_KEY")
        self.openrouter_api_key = _env("OPENROUTER_API_KEY")
        self.model = _env("OPENROUTE_MODEL", _env("OPENROUTER_MODEL", "openai/gpt-4o-mini"))
        self.base_url = _env("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

    def _resolve_provider_config(self) -> dict[str, Any]:
        registry = {name.lower(): config for name, config in PROVIDERS.items()}
        provider_key = self.provider_name.lower()
        if provider_key in registry:
            config = dict(registry[provider_key])
            config.setdefault("domains", [])
            config.setdefault("seeds", [])
            config.setdefault("select_paths", [])
            config.setdefault("exclude_paths", [])
            config["auto_detected"] = False
            return config

        domains = self.overrides.get("domains") or []
        seeds = self.overrides.get("seeds") or []
        if self.document_url:
            seeds = [self.document_url] + seeds
        return {
            "domains": domains,
            "seeds": seeds,
            "select_paths": self.overrides.get("select_paths") or [],
            "exclude_paths": self.overrides.get("exclude_paths") or [],
            "auto_detected": True,
        }

    def _tavily_search(self, query: str, domains: list[str] | None = None, max_results: int = 5) -> list[dict[str, Any]]:
        if not self.tavily_api_key:
            return []
        try:
            client = TavilyClient(api_key=self.tavily_api_key)
            payload = {"query": query, "search_depth": "advanced", "max_results": max_results}
            if domains:
                payload["include_domains"] = domains
            result = client.search(**payload)
            items = result.get("results", []) if isinstance(result, dict) else []
            return [
                {
                    "url": item.get("url"),
                    "title": item.get("title"),
                    "score": item.get("score"),
                }
                for item in items
                if item.get("url")
            ]
        except Exception:
            return []

    def _discover_urls(self) -> list[dict[str, Any]]:
        domains = self.provider_config.get("domains") or []
        seed_urls = list(dict.fromkeys(self.provider_config.get("seeds") or []))
        discovered: list[dict[str, Any]] = []
        seen: set[str] = set()

        for topic, keywords in TOPIC_KEYWORDS.items():
            query = f"{self.provider_name} OAuth {' '.join(keywords[:3])} official documentation"
            for item in self._tavily_search(query, domains=domains or None, max_results=5):
                url = _normalize_url(item["url"])
                if not url or url in seen:
                    continue
                seen.add(url)
                discovered.append({
                    "url": url,
                    "title": item.get("title") or "",
                    "score": item.get("score"),
                    "sources": ["search"],
                    "topics": [topic],
                })

        for seed in seed_urls:
            url = _normalize_url(seed)
            if not url or url in seen:
                continue
            seen.add(url)
            discovered.append({
                "url": url,
                "title": self.provider_name,
                "score": None,
                "sources": ["seed"],
                "topics": ["registration"],
            })

        if not discovered and self.document_url:
            url = _normalize_url(self.document_url)
            discovered.append({
                "url": url,
                "title": self.provider_name,
                "score": None,
                "sources": ["document_url"],
                "topics": ["registration"],
            })

        if not discovered:
            search_results = self._tavily_search(f"{self.provider_name} OAuth app setup documentation", domains=domains or None, max_results=3)
            for item in search_results:
                url = _normalize_url(item["url"])
                if url and url not in seen:
                    discovered.append({
                        "url": url,
                        "title": item.get("title") or "",
                        "score": item.get("score"),
                        "sources": ["search"],
                        "topics": ["registration"],
                    })
                    seen.add(url)

        return discovered[:25]

    def _extract_pages(self, urls: list[dict[str, Any]]) -> dict[str, str]:
        extracted: dict[str, str] = {}
        page_urls = [item["url"] for item in urls if item.get("url")]
        if not page_urls:
            return extracted

        if self.tavily_api_key:
            try:
                client = TavilyClient(api_key=self.tavily_api_key)
                for index in range(0, len(page_urls), 20):
                    batch = page_urls[index : index + 20]
                    response = client.extract(urls=batch, extract_depth="advanced", format="markdown")
                    items = response.get("results", []) if isinstance(response, dict) else []
                    for entry in items:
                        url = entry.get("url")
                        text = entry.get("raw_content") or ""
                        if url and text:
                            extracted[_normalize_url(url)] = text.strip()
            except Exception:
                extracted = {}

        if not extracted:
            for url in page_urls:
                try:
                    response = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
                    if response.ok:
                        text = response.text
                        if len(text.strip()) >= 400:
                            extracted[_normalize_url(url)] = text
                except Exception:
                    continue

        return extracted

    def _call_openrouter(self, prompt: str, system_prompt: str) -> dict[str, Any]:
        if not self.openrouter_api_key:
            raise RuntimeError("OPENROUTER_API_KEY is not configured.")

        url = f"{self.base_url.rstrip('/')}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.1,
            "max_tokens": 4000,
        }
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {self.openrouter_api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://cicerone.local",
                "X-Title": "Cicerone",
            },
            json=payload,
            timeout=180,
        )
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"]
        return json.loads(_strip_code_block(content))

    def _analyze_pages(self, pages: dict[str, str]) -> dict[str, Any]:
        if not pages:
            return {"topics": [], "gaps": ["No pages were successfully extracted for this provider."]}

        topic_reports = []
        for topic, keywords in TOPIC_KEYWORDS.items():
            prompt_lines = [
                f"Provider: {self.provider_name}",
                "Return JSON with fields: status, requirements. Each requirement must include: statement, source_url, quote.",
                "Use only the facts in the supplied pages. Do not use memory. If the answer is not documented, use status='not_found'.",
                "",
            ]
            for page_url, page_text in pages.items():
                excerpt = page_text[:2500]
                prompt_lines.append(f"<page source_url='{page_url}'>\n{excerpt}\n</page>")
                prompt_lines.append("")
            prompt = "\n".join(prompt_lines + [f"Topic to answer: {topic}. Keywords: {keywords}"])
            system_prompt = (
                "You are a strict OAuth documentation analyst. "
                "Use only the supplied page content. "
                "Return valid JSON only. "
                "For each requirement, quote must be a verbatim phrase from the page and source_url must match the page. "
                "If no requirement is documented, return {'status':'not_found','requirements':[]}."
            )

            try:
                result = self._call_openrouter(prompt, system_prompt)
            except Exception:
                result = {"status": "not_found", "requirements": []}

            if not isinstance(result, dict):
                result = {"status": "not_found", "requirements": []}
            requirements = result.get("requirements", []) or []
            cleaned_requirements = []
            for item in requirements:
                if not isinstance(item, dict):
                    continue
                statement = str(item.get("statement") or "").strip()
                source_url = str(item.get("source_url") or "").strip()
                quote = str(item.get("quote") or "").strip()
                if source_url in pages and quote and quote in pages[source_url]:
                    cleaned_requirements.append({
                        "statement": statement or quote,
                        "source_url": source_url,
                        "quote": quote,
                    })
            topic_reports.append({
                "topic": topic,
                "status": "documented" if cleaned_requirements else result.get("status", "not_found"),
                "requirements": cleaned_requirements[:5],
            })

        gaps = [
            f"{issue['topic']}: not documented in the extracted pages."
            for issue in topic_reports
            if issue["status"] == "not_found"
        ]
        return {"topics": topic_reports, "gaps": gaps}

    def _build_workflow(self, facts: dict[str, Any], pages: dict[str, str]) -> dict[str, Any]:
        verified_facts = []
        for topic in facts.get("topics", []):
            for req in topic.get("requirements", []):
                verified_facts.append(f"{topic['topic']}: {req['statement']} | source={req['source_url']}")

        prompt = (
            "You are building an OAuth setup workflow for a provider. "
            "Use only the verified facts and source pages provided. "
            "Return valid JSON with keys: workflow, approvals, difficulty, roadblocks, dependencies, gaps. "
            "workflow contains ordered step objects with id/title/sub_steps/depends_on/estimated_minutes/time_reasoning/required_for. "
            "Each approval and dependency should include basis and evidence source if available. "
            "If something is not documented, say so in gaps rather than inventing it."
            + "\n\nVerified facts:\n"
            + "\n".join(verified_facts[:40])
            + "\n\nSource pages:\n"
            + "\n\n".join(f"<{url}>\n{page[:2500]}\n</{url}>" for url, page in list(pages.items())[:6])
        )

        system_prompt = (
            "You are a strict OAuth workflow analyst. Use exact source pages and verified facts only. "
            "Never fill missing information from memory. Output JSON only."
        )
        try:
            result = self._call_openrouter(prompt, system_prompt)
        except Exception:
            result = {
                "workflow": [],
                "approvals": [],
                "difficulty": {"score": 2, "label": "moderate", "reasoning": "No confirmed evidence available."},
                "roadblocks": [],
                "dependencies": [],
                "gaps": ["The workflow could not be generated from the available evidence."],
            }

        if not isinstance(result, dict):
            result = {
                "workflow": [],
                "approvals": [],
                "difficulty": {"score": 2, "label": "moderate", "reasoning": "No confirmed evidence available."},
                "roadblocks": [],
                "dependencies": [],
                "gaps": ["The workflow could not be generated from the available evidence."],
            }
        return result

    def _render_markdown(self, workflow_payload: dict[str, Any]) -> str:
        provider_name = self.provider_name.title()
        workflow = workflow_payload.get("workflow") or []
        lines = [
            f"# {provider_name} OAuth Setup Guide",
            "",
            "## Overview",
            "",
            "This guide was assembled from the provider's official documentation, using the extracted source pages and verified requirements only.",
            "",
            "## Workflow",
            "",
        ]
        for step in workflow:
            lines.append(f"### {step.get('id', '1')}. {step.get('title', 'Setup step')}")
            for sub in step.get("sub_steps", []) or []:
                lines.append(f"- {sub}")
            minutes = step.get("estimated_minutes") or {"min": 0, "max": 0}
            lines.append(f"- Estimated time: {minutes.get('min')} to {minutes.get('max')} minutes")
            lines.append("")

        approvals = workflow_payload.get("approvals") or []
        if approvals:
            lines.append("## Approvals")
            lines.append("")
            for approval in approvals:
                lines.append(f"- {approval.get('name', 'Approval')}: {approval.get('approver', 'required')}")
            lines.append("")

        if workflow_payload.get("gaps"):
            lines.append("## Gaps")
            lines.append("")
            for gap in workflow_payload["gaps"]:
                lines.append(f"- {gap}")
            lines.append("")

        return "\n".join(lines) + "\n"

    def run(self) -> dict[str, Any]:
        discovered_urls = self._discover_urls()
        extracted_pages = self._extract_pages(discovered_urls)
        analysis = self._analyze_pages(extracted_pages)
        workflow = self._build_workflow(analysis, extracted_pages)
        workflow_payload = {
            "provider": self.provider_name,
            "slug": _slugify(self.provider_name),
            "auto_detected": self.provider_config.get("auto_detected", False),
            "source_urls": [entry["url"] for entry in discovered_urls],
            "pages": [{"url": url, "chars": len(page)} for url, page in extracted_pages.items()],
            "facts": analysis,
            "workflow": workflow,
            "markdown": self._render_markdown(workflow),
        }
        return {
            "status": "completed",
            "provider": self.provider_name,
            "json": workflow_payload,
            "markdown": workflow_payload["markdown"],
        }
