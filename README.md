# Cicerone

Cicerone is a Django backend that researches a provider's OAuth setup requirements from official documentation and turns that research into a clear, structured guide.

The API accepts a provider name and optional documentation URL, runs the research pipeline, and returns:

- a human-readable Markdown guide
- a JSON payload for frontend rendering

## Project goal

Given a provider name or documentation URL, Cicerone:

- discovers official documentation pages
- extracts relevant page content
- analyzes the content for OAuth-specific requirements
- builds a setup workflow with dependencies, approvals, and gaps
- returns both a Markdown guide and machine-readable JSON

This project is intended to be the backend behind a frontend that presents the resulting guide with a richer interface.

## Tech stack

- Django
- Django REST Framework
- Tavily API
- OpenRouter API
- Python 3.13

## Repository layout

- `cicerone/` — Django project settings and routing
- `oauth_research/` — API views, async job queue, and research pipeline
- `provider_info.py` — built-in provider registry and domain metadata
- `manage.py` — Django management entry point
- `.env` — environment variables for Tavily and OpenRouter
- `Pipfile` — Python dependency declaration

## Local setup

### 1) Create and activate the environment

```bash
cd /home/dampdigits/projects/dampdigits/cicerone
pipenv install
pipenv shell
```

### 2) Configure environment variables

Create or update a `.env` file in the project root with:

```env
TAVILY_API_KEY=your_tavily_key
OPENROUTER_API_KEY=your_openrouter_key
OPENROUTE_MODEL=GPT-6-Luna
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

The app also supports the fallback variable name `OPENROUTER_MODEL` if used elsewhere.

### 3) Apply Django database migrations

```bash
pipenv run python manage.py migrate
```

### 4) Start the backend

```bash
pipenv run python manage.py runserver 0.0.0.0:8000
```

## API endpoints

### Health check

```bash
curl http://127.0.0.1:8000/healthz/
```

Example response:

```json
{
  "status": "ok",
  "service": "cicerone"
}
```

### Research request

```bash
curl -X POST http://127.0.0.1:8000/api/research/ \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "github",
    "doc_url": "https://docs.github.com/en/apps/oauth-apps"
  }'
```

Example response:

```json
{
  "job_id": "7bba7f23-5ec1-4d86-bd03-a147f48f7ad6",
  "status": "queued",
  "message": "Provider research job accepted and running."
}
```

### Check job status

```bash
curl http://127.0.0.1:8000/api/jobs/7bba7f23-5ec1-4d86-bd03-a147f48f7ad6/status/
```

Example response:

```json
{
  "job_id": "7bba7f23-5ec1-4d86-bd03-a147f48f7ad6",
  "status": "completed",
  "provider": "github",
  "result": {
    "status": "completed",
    "provider": "github",
    "json": {
      "provider": "github",
      "slug": "github",
      "workflow": {
        "workflow": [],
        "approvals": [],
        "gaps": []
      }
    },
    "markdown": "# GitHub OAuth Setup Guide\n..."
  }
}
```

## Request contract

The main request body to `POST /api/research/` accepts:

```json
{
  "provider": "github",
  "doc_url": "https://docs.github.com/en/apps/oauth-apps",
  "domains": ["docs.github.com"],
  "seeds": ["https://docs.github.com/en/apps/oauth-apps"],
  "select_paths": ["/en/apps/.*"],
  "exclude_paths": [".*pricing.*"],
  "max_urls": 30,
  "dry_run": false
}
```

### Fields

- `provider` (required): provider name such as `github`, `google`, `microsoft`, or a custom provider name
- `doc_url` (optional): direct documentation URL to use as an initial seed
- `domains` (optional): allowed official domains for the provider
- `seeds` (optional): explicit seed URLs to include for discovery
- `select_paths` (optional): path filters for search/crawl logic
- `exclude_paths` (optional): path exclusions for search/crawl logic
- `max_urls` (optional): cap the number of pages extracted
- `dry_run` (optional): if enabled, the job can prepare the research without finalizing the full output path

## Backend behavior

The backend is designed to process a single-provider request in a single orchestrated flow:

1. Discover candidate URLs using Tavily search
2. Extract the relevant pages and their full content
3. Analyze the extracted pages with the OpenRouter model using a strict evidence-first prompt
4. Build the final workflow and return JSON + Markdown output

The system is intentionally strict:

- no memory-only filling of missing facts
- missing information is tracked as a gap
- verification checks ensure quoted evidence matches the extracted page content before it is accepted

## Current limitations

- This is a backend-only implementation
- No persistent database storage is used yet
- The job runner is in-process and designed for local or lightweight async processing
- Future improvements may include Celery, Redis, and scheduled job persistence

## Development notes

The app currently keeps only the final output in memory for the request lifecycle and does not persist intermediate artifacts.

## Running tests

```bash
pipenv run python manage.py test oauth_research
```

## Example workflow

```bash
# start the server
pipenv run python manage.py runserver 0.0.0.0:8000

# request a job
curl -X POST http://127.0.0.1:8000/api/research/ \
  -H "Content-Type: application/json" \
  -d '{"provider":"github"}'

# poll the job status
curl http://127.0.0.1:8000/api/jobs/<job_id>/status/
```

## License

This project is currently in active development and is intended for internal use and experimentation.
