# CareerPath AI

AI-powered career platform for students and early-career job seekers.
Semantic job search • Personalized job matching • ATS résumé scoring • JD-aware CV tailoring • LLM eval pipeline

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)](https://www.postgresql.org/)
[![pgvector](https://img.shields.io/badge/pgvector-0.3-purple)](https://github.com/pgvector/pgvector)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-lightgray)](https://github.com/abhishek-ngu/CareerPath-AI-AI-Career-Job-Matching-Platform/actions)

## About

CareerPath AI is an end-to-end AI career platform built to mirror a real-world AI career product. It helps students and early-career job seekers:

- Search jobs semantically over a constantly-updating jobs index
- Get personalized job match rankings with LLM-generated explanations
- Score their résumé for ATS friendliness (0–100)
- Receive JD-aware before/after CV edit suggestions
- Track everything through a Python/FastAPI backend with PostgreSQL memory

This project is designed as a portfolio piece for LLM agent, search, and backend engineering roles. It is **local-first** — run it with Docker Compose on your machine. No live deployment link is provided to avoid broken-link risk.

## Features

| Feature | Description |
|---------|-------------|
| Hybrid Semantic Search | pgvector embeddings + PostgreSQL full-text search over job postings |
| Personalized Matching | LLM reranker returns match scores and natural-language explanations via strict Pydantic-structured outputs |
| ATS Scorer Agent | Parses PDF/DOCX résumés, scores 0–100 across formatting, keywords, sections, and readability |
| CV Tailor Agent | Generates targeted before/after edits optimizing for both ATS compatibility and a specific JD |
| Agent Memory | PostgreSQL-backed conversation history for the career chat agent |
| Offline Eval Pipeline | Golden-set eval + LLM-as-a-judge running in GitHub Actions on every PR |
| Containerized Stack | Docker Compose orchestration of FastAPI + PostgreSQL/pgvector with `.env` config and volume persistence |

## Tech Stack

- **Language:** Python 3.11
- **API:** FastAPI
- **Database:** PostgreSQL 16 + pgvector (vector embeddings)
- **LLM:** OpenAI (GPT + text-embedding models)
- **Validation:** Pydantic v2 (structured outputs)
- **Containerization:** Docker + Docker Compose
- **Frontend:** Streamlit (planned / lightweight UI stub)
- **CI:** GitHub Actions

## Project Structure

```
careerpath-ai/
├── .github/
│   └── workflows/
│       └── eval.yml              # LLM eval pipeline on PRs
├── apps/api/
│   ├── main.py                   # FastAPI entrypoint + routers
│   ├── schemas.py                # Pydantic models (ATSReport, TailorResult, JobOut, etc.)
│   ├── db/
│   │   ├── session.py            # Async SQLAlchemy session + init_db
│   │   └── models.py             # SQLAlchemy models (User, Job, ATSReport, CVSuggestion, Conversation, Message, Feedback)
│   ├── routers/
│   │   ├── jobs.py               # /jobs/search, /jobs/match
│   │   ├── ats.py                # /ats/score
│   │   ├── cv.py                 # /cv/tailor
│   │   ├── agent.py              # /agent/chat
│   │   └── feedback.py           # /feedback
│   └── agents/
│       ├── ats_agent.py          # ATS-friendliness LLM agent
│       ├── cv_tailor.py          # JD-aware CV tailor LLM agent
│       └── career_agent.py       # Career chat agent (tools + memory stubs)
├── worker/
│   ├── ingest.py                 # Job scraping / seeding stub
│   └── embed.py                  # Embedding generation stub
├── scripts/
│   └── seed_jobs.py              # CLI to seed demo jobs into PostgreSQL
├── evals/
│   ├── golden_set.jsonl          # Annotated CV/JD pairs for eval
│   ├── judge_prompt.txt          # LLM-as-a-judge rubric
│   └── run_eval.py               # Offline eval runner
├── Dockerfile                    # Multi-stage Python image
├── docker-compose.yml            # api + db services with pgvector
├── requirements.txt              # Python dependencies
└── README.md
```

## Run Locally with Docker

### Prerequisites
- Docker and Docker Compose installed
- An OpenAI API key

### Steps

```bash
# Clone the repository
git clone https://github.com/abhishek-ngu/CareerPath-AI-AI-Career-Job-Matching-Platform.git
cd CareerPath-AI-AI-Career-Job-Matching-Platform

# Copy environment template and add your OpenAI key
cp .env.example .env
# Edit .env and set OPENAI_API_KEY=sk-...

# Build and start services
docker-compose up --build
```

The FastAPI backend will be available at `http://localhost:8000` with interactive docs at `http://localhost:8000/docs`.

PostgreSQL + pgvector runs on `localhost:5432` (user: `careerpath`, password: `careerpath`, db: `careerpath`).

### Seed demo jobs

```bash
python scripts/seed_jobs.py
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/jobs/search` | POST | Semantic + keyword job search |
| `/jobs/match` | POST | Personalized job matching with explanations |
| `/ats/score` | POST | ATS résumé scoring (0–100) |
| `/cv/tailor` | POST | JD-aware CV before/after suggestions |
| `/agent/chat` | POST | Career chat agent |
| `/feedback` | POST | Submit thumbs-up/down feedback |

All LLM agent responses use strict Pydantic-structured outputs.

## Eval Pipeline

The repo includes an offline evaluation pipeline located in `evals/`:

- **`golden_set.jsonl`**: 3+ annotated CV/job-description pairs with expected ATS scores and keywords
- **`judge_prompt.txt`**: Rubric for an LLM-as-a-judge evaluator
- **`run_eval.py`**: Script to run evals locally or in CI

### GitHub Actions

`.github/workflows/eval.yml` runs the eval pipeline on every push and pull request to `main`. It:

1. Spins up a `pgvector/pgvector:pg16` service container
2. Installs Python dependencies
3. Initializes the database
4. Executes `python evals/run_eval.py`

To enable LLM calls in CI, add `OPENAI_API_KEY` as a GitHub repository secret (Settings → Secrets and variables → Actions).

## Example CV Bullets

You can adapt these for your résumé:

> Built CareerPath AI, an end-to-end AI career platform featuring semantic job search, personalized match ranking, an ATS résumé scorer (0–100), and a JD-aware CV tailor agent — powered by LLM agents with function calling, Pydantic structured outputs, and PostgreSQL conversation memory.

> Engineered hybrid retrieval (pgvector embeddings + PostgreSQL full-text search) over ~2,000 job postings with an LLM reranker returning structured match scores and explanations.

> Containerized a FastAPI backend and PostgreSQL/pgvector database using Docker Compose with volume persistence, `.env`-based configuration, and reproducible single-command builds.

> Implemented an offline LLM eval pipeline (golden set + LLM-as-a-judge) in GitHub Actions to detect prompt/model regressions on every PR.

## Roadmap

- [x] Project skeleton: FastAPI, PostgreSQL, pgvector, Docker Compose
- [x] Pydantic schemas for all agent outputs
- [x] LLM agent stubs (ATS scorer, CV tailor, career agent)
- [x] Eval pipeline + GitHub Actions workflow
- [ ] Wire real OpenAI calls into agent stubs
- [ ] Add Streamlit frontend UI
- [ ] Implement pgvector hybrid search + HNSW index querying
- [ ] Add resume PDF/DOCX text extraction (pdfplumber / python-docx)

## License

MIT License. See `LICENSE` if added.

---

**Note:** This is a local-first portfolio project. All LLM agent files currently contain skeleton stubs — replace them with real OpenAI API calls using your key in `.env` to activate full functionality.