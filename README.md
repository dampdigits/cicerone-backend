# Cicerone

Cicerone is a Django backend that researches how to set up an OAuth application with a third-party provider. It reads the provider's **official documentation** and turns it into a structured, evidence-backed setup guide.

Given a provider name (and optionally a documentation URL), it returns:

- a human-readable **Markdown guide**
- a **JSON payload** for a frontend to render

It is meant to sit behind a frontend that presents the guide with a richer interface.

## What it produces

For each provider, the guide covers:

- the **workflow**: ordered steps with sub-steps, dependencies between steps, and time estimates
- **approvals**: gates where someone other than the developer must approve something (admin consent, app review, publisher verification), with who approves and how long it may take
- **roadblocks** and their mitigations
- **dependencies**: accounts, permissions, tools and prior setup needed first
- a **difficulty** rating (1 to 5, the model's estimate; docs do not rate difficulty)
- **topic coverage** across nine OAuth topics, and an explicit list of **gaps** (things the sources do not say)

## Tech stack

- Python 3.13
- Django and Django REST Framework
- [Tavily](https://tavily.com) for search, site mapping and page extraction
- [OpenRouter](https://openrouter.ai) for model analysis

## Repository layout

- `cicerone/`: Django project settings and routing
- `oauth_research/services.py`: `ResearchPipeline`, the whole research flow
- `oauth_research/tasks.py`: job queue (`create_job`, `get_job`, `JobQueueFull`, `TERMINAL`)
- `oauth_research/views.py`: API views and request validation
- `provider_info.py`: built-in provider registry (official domains, seeds, path filters)
- `manage.py`: Django management entry point
- `.env`: API keys and model settings
- `Pipfile`: dependencies

## Local setup

### 1. Install dependencies

```bash
pipenv install
pipenv shell
```

### 2. Configure environment variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_key
OPENROUTER_API_KEY=your_openrouter_key
OPENROUTER_MODEL=openai/gpt-6-luna
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

| Variable | Required | Default |
|---|---|---|
| `TAVILY_API_KEY` | Yes | none |
| `OPENROUTER_API_KEY` | Yes, except for `dry_run` requests | none |
| `OPENROUTER_MODEL` | No | `openai/gpt-6-luna` |
| `OPENROUTER_BASE_URL` | No | `https://openrouter.ai/api/v1` |

Each value is read from the environment first, then from Django settings of the same name.

### 3. Configure a shared cache

Job state is stored in Django's cache, so every web worker can see it. This only works with a **shared** backend (Redis, Memcached, database or file cache). The default `LocMemCache` is per process: it works for a single local dev server but jobs will appear to vanish when more than one worker runs.

### 4. Start the backend

```bash
pipenv run python manage.py runserver 0.0.0.0:8000
```

No database migrations are needed for Cicerone itself. Run `migrate` only if your project's auth or other apps require it.

## Authentication and cost control

Every research run spends paid Tavily and OpenRouter credits.

> **Current state:** `ResearchAPIView` and `JobStatusView` both set `permission_classes = []`, and the throttle settings are commented out. Anyone who can reach the server can start runs. Before deploying, enable authentication (for example `IsAuthenticated` or an API-key permission) and DRF throttling (the code includes a commented `research_create` scope example, for instance `10/hour`).

Job ownership is keyed on `request.user.pk`. With anonymous access every caller shares the same owner value, so per-user job isolation only works once authentication is on.

## API

### Health check

```bash
curl http://127.0.0.1:8000/healthz/
```

```json
{ "status": "ok", "service": "cicerone" }
```

### Start a research job

```bash
curl -X POST http://127.0.0.1:8000/api/research/ \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "github",
    "doc_url": "https://docs.github.com/en/apps/oauth-apps"
  }'
```

Response `202 Accepted`:

```json
{
  "job_id": "7bba7f23-5ec1-4d86-bd03-a147f48f7ad6",
  "status": "queued",
  "poll_after_seconds": 2,
  "message": "Provider research job accepted."
}
```

Error responses:

| Status | When |
|---|---|
| `400` | Invalid body (per-field messages) or the pipeline rejected the provider name |
| `503` | Queue is full; includes a `Retry-After: 30` header |

### Request body

| Field | Type | Notes |
|---|---|---|
| `provider` | string, required | Provider name, max 80 characters (letters, digits, spaces and `. & + ' -`). `provider_name` is accepted as an alias. |
| `doc_url` | string, optional | Public `https` documentation URL, used as the first seed. |
| `domains` | list of strings, optional | Allowed official domains (max 10). Used for providers not in the registry. |
| `seeds` | list of URLs, optional | Extra seed URLs (max 10). |
| `select_paths` | list of regex strings, optional | Path filters for site mapping (max 10, each up to 200 characters). |
| `exclude_paths` | list of regex strings, optional | Path exclusions for site mapping (max 10). |
| `max_urls` | integer, optional | Pages to extract, 5 to 60. Default 30. |
| `dry_run` | boolean, optional | Runs discovery only and returns the URLs it would extract. No pages are fetched and no model calls are made, so `OPENROUTER_API_KEY` is not needed. |

Example with overrides for a provider not in the registry:

```json
{
  "provider": "acme",
  "doc_url": "https://docs.acme.com/oauth",
  "domains": ["docs.acme.com"],
  "seeds": ["https://docs.acme.com/oauth/apps"],
  "select_paths": ["/oauth/.*"],
  "exclude_paths": [".*pricing.*"],
  "max_urls": 30,
  "dry_run": false
}
```

### Check job status

```bash
curl http://127.0.0.1:8000/api/jobs/7bba7f23-5ec1-4d86-bd03-a147f48f7ad6/status/
```

While running:

```json
{
  "job_id": "7bba7f23-5ec1-4d86-bd03-a147f48f7ad6",
  "status": "running",
  "provider": "github",
  "stage": "extracting",
  "stage_detail": "pages 1-20 of 30",
  "finished": false,
  "poll_after_seconds": 3
}
```

When finished, the response has `"finished": true` and a `result` object. An unknown, expired or someone else's job returns `404`. Responses are sent with `Cache-Control: no-store`.

**Statuses:** `queued`, `running`, `completed`, `partial`, `failed`, `dry_run`. The last four are terminal.

- `completed`: everything ran without recorded errors
- `partial`: a result exists, but some part failed (see `errors`)
- `failed`: nothing usable, or the model provider rejected the credentials or credits (401, 402, 403)
- `dry_run`: discovery only

**Stages** (for a progress label): `resolving`, `discovering`, `extracting`, `analyzing topics`, `building workflow`.

If an internal error occurs, the status response carries a generic `error` message with a reference id; the traceback goes to the server log.

### Result shape

`result` contains:

```json
{
  "status": "completed",
  "provider": "github",
  "json": { "...": "see below" },
  "markdown": "# GitHub: OAuth app setup guide\n...",
  "errors": [],
  "warnings": []
}
```

`result.json` includes:

| Key | Contents |
|---|---|
| `provider`, `slug`, `display_name`, `status`, `model`, `retrieved_at` | Run identity and timing |
| `auto_detected` | `true` if the official domains were guessed rather than confirmed |
| `config` | Resolved `domains`, `seeds`, `select_paths`, `exclude_paths`, `domain_source` |
| `source_urls`, `discovery` | URLs selected, and counts for candidates, off-domain rejections and selected |
| `pages` | Each extracted page: `url`, `title`, `chars`, `sha256`, `last_updated_hint` |
| `failed_fetches`, `thin_pages` | Pages that could not be fetched, or had too little text |
| `facts` | `topics` (per-topic status and verified requirements) and `gaps` |
| `workflow` | `workflow` (steps), `approvals`, `difficulty`, `roadblocks`, `dependencies`, `gaps`, `totals` |
| `usage` | Prompt and completion token counts |
| `errors`, `warnings`, `markdown` | Problems, notes, and the rendered guide |

## How the pipeline works

1. **Resolve config.** Providers in `provider_info.py` use the registry's domains, seeds and path filters, and user input cannot widen them. Unknown providers use the supplied `domains`, `seeds` and `doc_url`. If none are given, Cicerone searches for the official docs site and flags the guess for a person to confirm.
2. **Discover URLs.** One Tavily search per topic, restricted to the allowed domains, plus a Tavily map of each seed. Anything outside the domain allowlist is dropped in code.
3. **Rank and cap.** Seeds first, then pages found by more topics, higher search score and more OAuth-related URL hints, up to `max_urls`.
4. **Extract.** Full page text via Tavily, in batches of 20. If a batch fails, each URL is retried on its own. Redirects that leave the allowlist are rejected, and pages under 300 characters are set aside.
5. **Analyze nine topics.** For each topic, the best-matching pages (3 per pass, up to 2 passes) go to the model with a strict evidence-first prompt. Topics: `account_requirements`, `registration`, `redirect_uri`, `credentials`, `scopes`, `consent`, `verification`, `production`, `limits`.
6. **Build the workflow.** The five most workflow-relevant pages and the already verified facts go to the model, which returns steps, approvals, difficulty, roadblocks and dependencies.
7. **Compute totals and render.** Time and wait totals are summed in code, and the Markdown guide is rendered.

### Evidence rules

The system is deliberately strict:

- The model may use only the supplied pages, never outside knowledge. Page text is treated as untrusted data.
- Every requirement must carry a quote copied verbatim from a cited page. The quote is checked in code against the fetched text (a loose match ignoring case and punctuation), and failures are rejected.
- Topic status comes from what was verified, not from the model's own claim: `confirmed`, `partial`, `not_found`, or `error`.
- Workflow items are labeled `verified` (a page quote checked out), `inferred` (the model reasoned beyond the pages) or `unverified` (it claimed a source that did not check out).
- Time and wait estimates are labeled `verified` only when a page states them; otherwise they are marked as estimates.
- Missing information is listed as a gap, never filled from memory. Pages that failed to fetch are listed, because related gaps may be unknown rather than absent.

### Totals

`workflow.totals` includes approval counts (always vs conditional), active time for the minimum setup and the full production path, and approval wait ranges. Sums assume steps run one after another, so treat them as rough bounds.

## Safety notes for user input

- Document URLs, seeds and domains must be public `https` URLs on real public hostnames (no IP literals, `localhost` or private suffixes such as `.internal`).
- Cicerone never fetches a user-supplied URL itself. Only Tavily does, so there is no server-side path to internal hosts.
- A `doc_url` outside a registry provider's official domains is ignored with a warning.

## Job queue behavior

Jobs run in an in-process thread pool (`oauth_research/tasks.py`):

| Setting | Value |
|---|---|
| Concurrent jobs | 2 |
| Running plus queued, maximum | 10 (then `503`) |
| Job retention in cache | 24 hours |
| Stale-job cutoff | 30 minutes without a progress update, then reported as `failed` |

Invalid input is rejected when the job is created, so the view can return `400` straight away.

## Current limitations

- **Process-local limits:** the pending-job counter is per process, so with N web workers the effective cap is N times higher.
- **Threads die with the process:** a restart loses running jobs, and they show as `failed` once the stale cutoff passes.
- **Cache size:** the whole result, Markdown included, is stored in the cache. Backends with small value limits (Memcached defaults to 1 MB) can silently drop large results.
- **Stale detection:** the timestamp only updates on stage changes, so a very slow model stage (up to 5 attempts of 180 seconds each) can approach the 30-minute cutoff.
- **No persistence:** results expire with the cache, and intermediate artifacts are not stored.
- **Auth and throttling are not enabled yet** (see above).

Future work could move `_run_job` into a Celery or RQ task for restart-safe, multi-machine execution (`create_job` and `get_job` can stay the same) and persist results to a database.

## Running tests

```bash
pipenv run python manage.py test oauth_research
```

## Example workflow

```bash
# start the server
pipenv run python manage.py runserver 0.0.0.0:8000

# preview what would be fetched, without model calls
curl -X POST http://127.0.0.1:8000/api/research/ \
  -H "Content-Type: application/json" \
  -d '{"provider":"github","dry_run":true}'

# run the full research
curl -X POST http://127.0.0.1:8000/api/research/ \
  -H "Content-Type: application/json" \
  -d '{"provider":"github"}'

# poll until "finished" is true
curl http://127.0.0.1:8000/api/jobs/<job_id>/status/
```

## License

This project is in active development and intended for internal use and experimentation.