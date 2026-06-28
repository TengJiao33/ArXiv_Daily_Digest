# ArXiv_Daily_Digest

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
![Dashboard](https://img.shields.io/badge/Dashboard-Static%20HTML%20%2B%20Local%20API-2f7d62)
![Automation](https://img.shields.io/badge/Automation-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

[中文](README.zh-CN.md)

ArXiv_Daily_Digest is a configurable pipeline for collecting, enriching, storing, and reviewing arXiv papers across predefined research directions. It combines arXiv search, optional citation expansion, metadata enrichment, structured extraction, generated Markdown artifacts, and a static dashboard.

The repository currently includes an Agent Reliability Radar configuration. The implementation itself is organized around direction-level configuration and can be adapted to other research scopes.

## Features

| Area | Description |
| --- | --- |
| Paper collection | Fetches papers from arXiv according to direction-specific queries. |
| Citation expansion | Uses seed papers for Semantic Scholar citation-based candidate expansion. |
| Relevance filtering | Applies configurable keyword and topic filters before enrichment. |
| Metadata enrichment | Adds code repository signals, Hugging Face activity, citation counts, and venue metadata where available. |
| Structured extraction | Extracts research problem, method, contribution, limitations, evaluation signals, risks, and follow-up questions. |
| Local storage | Writes direction- and week-scoped JSONL records under `data/`. |
| Static dashboard | Serves a filesystem-friendly dashboard generated from local data. |
| Markdown artifacts | Generates weekly digest, landscape, and review brief documents from stored records. |
| Scheduled automation | Supports daily GitHub Actions execution with repository updates. |

## Quick Start

```bash
git clone https://github.com/TengJiao33/ArXiv_Daily_Digest.git
cd ArXiv_Daily_Digest
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Open the static dashboard:

```text
index.html
```

The root entry redirects to:

```text
radar_dashboard/static/index.html
```

The dashboard reads `radar_dashboard/static/data.js` and can be opened directly from the local filesystem.

## Collection Pipeline

Run a full collection cycle:

```bash
python main.py
```

This command may call external services including arXiv, Semantic Scholar, GitHub, Hugging Face, venue lookup endpoints, and Doubao/Volcengine Ark. It may consume API quota depending on the configured credentials and the number of candidate papers.

After data changes, rebuild the static dashboard snapshot:

```bash
python radar_dashboard/build_static.py
```

## Local Dashboard Server

For API-backed local development:

```bash
python radar_dashboard/app.py
```

Default address:

```text
http://127.0.0.1:7860
```

## Configuration

Create a `.env` file in the repository root when external integrations are required:

```ini
DOUBAO_API_KEY=your_ark_api_key
DOUBAO_ENDPOINT_ID=your_endpoint_id
GITHUB_TOKEN=ghp_your_token
SEMANTIC_SCHOLAR_API_KEY=optional_s2_api_key
SERVERCHAN_SENDKEY=optional_serverchan_key
WXPUSHER_APP_TOKEN=optional_wxpusher_app_token
WXPUSHER_UIDS=optional_wxpusher_uids
```

GitHub Actions uses the same secret names. The scheduled workflow runs daily at 03:00 UTC.

## Research Directions

Research scope is defined in:

```text
config/directions.yaml
```

Each direction can define:

| Field | Purpose |
| --- | --- |
| `name` | Display name used by generated artifacts and the dashboard. |
| `description` | Scope description used for structured extraction context. |
| `arxiv_query` | arXiv search query. |
| `keywords` | Terms used by enrichment and filtering logic. |
| `relevance` | Required and topic-level terms for relevance filtering. |
| `max_papers` | Candidate limit for the direction. |
| `seed_papers` | arXiv IDs used for direct inclusion and citation expansion. |

The current configuration contains directions for editing reliability, model unlearning, agent harnesses, multi-agent consistency, agent policy optimization, and factuality-oriented applications.

## Authority Anchors

Published or otherwise curated high-priority papers can be maintained separately from the daily candidate queue:

```text
config/authority_anchors.yaml
```

These records are displayed in the dashboard and listed before ordinary reading queues in generated briefs. Current queue papers with recognized venue labels are also prioritized in the reading order.

## Manual Paper Injection

Use manual injection when a paper should pass through the enrichment pipeline but is not expected to match standing queries:

```text
config/manual_papers.yaml
```

Example:

```yaml
manual_papers:
  agent-skills-harness:
    - arxiv_id: "2404.07972"
      reason: "Agent harness benchmark reference."
  multi-agent-consistency:
    - "2308.07201"
```

Manual papers fetch the arXiv record directly and bypass keyword relevance filtering. They still pass through code checks, structured extraction, Hugging Face matching, venue annotation, and JSONL storage. Historical de-duplication prevents repeated extraction for papers already processed.

## Review Brief

Generate a local Markdown brief from stored records:

```bash
python mentor_brief.py
```

Default output:

```text
output/mentor_briefs/{ISO-week}.md
```

Useful variants:

```bash
python mentor_brief.py --week 2026-W23 --top 3
python mentor_brief.py --stdout
```

## Venue Backfill

Semantic Scholar venue lookup is rate-limited. The resolver supports `SEMANTIC_SCHOLAR_API_KEY` or `S2_API_KEY`, local response caching under `data/_cache/`, and 429 backoff.

Backfill venue labels for stored records:

```bash
python venue_backfill.py --week 2026-W23 --write
```

Dry run is the default:

```bash
python venue_backfill.py --week 2026-W23
```

## Repository Layout

```text
ArXiv_Daily_Digest/
  index.html                    # Static dashboard entry
  config/                       # Research directions, anchors, and overrides
  data/                         # JSONL records and generated research artifacts
  radar_dashboard/              # Static dashboard and optional local API server
  main.py                       # Collection pipeline entry point
  scraper_arxiv.py              # arXiv collection
  relevance_filter.py           # Candidate filtering
  citation_tracker.py           # Semantic Scholar citation expansion
  code_hunter.py                # Repository discovery
  processor.py                  # Structured extraction
  venue_resolver.py             # Venue metadata resolution
  digest_builder.py             # Weekly digest generation
  landscape_builder.py          # Weekly landscape generation
  mentor_brief.py               # Local review brief generation
  storage.py                    # JSONL persistence and de-duplication
  .github/workflows/daily.yml   # Scheduled collection workflow
```

## Data Outputs

Typical generated files include:

```text
data/{direction}/{ISO-week}/papers.jsonl
data/{direction}/{ISO-week}/weekly_digest.md
data/{direction}/{ISO-week}/landscape.md
radar_dashboard/static/data.js
output/mentor_briefs/{ISO-week}.md
```

## License

No license file is currently included.
