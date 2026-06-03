# ArXiv_Daily_Digest

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
![Dashboard](https://img.shields.io/badge/Dashboard-Static%20HTML%20%2B%20Local%20API-2f7d62)
![Automation](https://img.shields.io/badge/Automation-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
![Scope](https://img.shields.io/badge/Scope-Agent%20Reliability%20Radar-3867a6)

[中文](README.zh-CN.md)

ArXiv_Daily_Digest is a research radar and dashboard project. Its current core surface is the **Agent Reliability Radar**, focused on LLM agents, harnesses, reliability, factuality, model control, and safety intervention. It collects recent papers, enriches them with reproducibility and venue signals, extracts structured research fields, and exposes the result through a local dashboard and mentor-alignment brief.

## Core Features

| Feature | Role |
| --- | --- |
| Static dashboard | Primary reading surface. Open `index.html` from the repository root, no server required. |
| Daily collection | Scheduled GitHub Actions workflow for ArXiv search, citation expansion, relevance filtering, and storage. |
| Direction radar | Active scope is defined in `config/directions.yaml`. The current setup keeps 2 legacy reliability lines and adds 4 agent/factuality lines. |
| Authority anchors | `config/authority_anchors.yaml` keeps manually curated A-conference backbone papers for each direction. These papers are highlighted separately from the daily queue. |
| Structured extraction | Converts abstracts into problem, method, key finding, method family, control mechanism, evaluation environment, reliability risk, feasibility, and mentor questions. |
| Mentor brief | `mentor_brief.py` turns local JSONL data into a compact discussion brief for periodic advisor alignment. |

## Dashboard

Open:

```text
index.html
```

The root entry redirects to:

```text
radar_dashboard/static/index.html
```

The static dashboard reads `radar_dashboard/static/data.js`, so it works directly from the filesystem. After new data is collected, refresh the static snapshot with:

```bash
python radar_dashboard/build_static.py
```

For API-backed local development:

```bash
python radar_dashboard/app.py
```

Default URL:

```text
http://127.0.0.1:7860
```

## Active Research Scope

The active directions are:

| Direction ID | Role |
| --- | --- |
| `editing-reliability-evaluation` | Legacy continuity line for editing reliability, steering side effects, model control, and mechanistic intervention. |
| `model-unlearning` | Legacy continuity line expanded to unlearning, backdoor defense, jailbreak defense, and safety intervention. |
| `agent-skills-harness` | Agent skills, executable skill libraries, harnesses, tool-use control, workflow constraints, and execution-based evaluation. |
| `multi-agent-consistency` | Multi-agent collaboration, disagreement, consensus, debate, judge/verifier mechanisms, and behavioral consistency. |
| `agent-policy-optimization` | Policy optimization, online distillation, teacher-student learning, reward learning, RLVR, and test-time scaling. |
| `factuality-rule-guided-apps` | Factuality, rule-guided reasoning, hallucination detection, benchmark contamination, and application benchmarks. |

## Authority Anchors

Published A-conference papers are treated as direction anchors rather than ordinary daily queue items. The dashboard shows them in the Authority Anchors panel, and the mentor brief lists them before the weekly reading queue.

Update the manual backbone here:

```text
config/authority_anchors.yaml
```

Current queue papers with recognized A-conference labels are also boosted in the reading order and marked as `A会重点`.

For the main collection pipeline, `seed_papers` in `config/directions.yaml` now has two roles: the seed papers themselves are fetched from arXiv and prioritized for extraction, and the same IDs are used for Semantic Scholar citation expansion.

## Mentor Brief

Generate a local discussion brief without calling external APIs:

```bash
python mentor_brief.py
```

By default it writes:

```text
output/mentor_briefs/{ISO-week}.md
```

Useful variants:

```bash
python mentor_brief.py --week 2026-W23 --top 3
python mentor_brief.py --stdout
```

## Quick Start

```bash
git clone https://github.com/TengJiao33/ArXiv_Daily_Digest.git
cd ArXiv_Daily_Digest
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run a collection cycle only when you intend to call external APIs:

```bash
python main.py
```

`python main.py` calls ArXiv, Semantic Scholar, GitHub, Hugging Face, venue lookup, and Doubao/Ark. It may consume API quota. Opening the dashboard and generating a mentor brief only read local files.

## Configuration

Create `.env` in the repository root:

```ini
DOUBAO_API_KEY=your_ark_api_key
DOUBAO_ENDPOINT_ID=your_endpoint_id
GITHUB_TOKEN=ghp_your_token
SEMANTIC_SCHOLAR_API_KEY=optional_s2_api_key
SERVERCHAN_SENDKEY=optional_serverchan_key
WXPUSHER_APP_TOKEN=optional_wxpusher_app_token
WXPUSHER_UIDS=optional_wxpusher_uids
```

GitHub Actions uses the same secret names. The scheduled workflow runs daily at 03:00 UTC, which is 11:00 in Asia/Shanghai.

## Venue Backfill

Semantic Scholar venue lookup is rate-limited. The resolver supports `SEMANTIC_SCHOLAR_API_KEY` or `S2_API_KEY`, local response caching under `data/_cache/`, and 429 backoff.

Backfill venue labels without running the main collection pipeline:

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
  index.html                    # Click-to-open dashboard entry
  config/                       # Active directions, authority anchors, and venue overrides
  data/                         # JSONL records and generated research artifacts
  radar_dashboard/              # Static dashboard and optional local API server
  main.py                       # Daily collection pipeline
  authority_anchors.py          # Manual A-conference anchor loader
  processor.py                  # Structured extraction
  mentor_brief.py               # Local mentor-alignment brief generator
  storage.py                    # JSONL persistence and direction-level deduplication
  digest_builder.py             # Weekly digest generation
  landscape_builder.py          # Weekly landscape generation
  .github/workflows/daily.yml   # Scheduled collection workflow
```

## License

No license file is currently included.
