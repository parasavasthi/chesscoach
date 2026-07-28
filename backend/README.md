# ChessCoach Backend v1

ChessCoach Backend v1 is a small FastAPI service that fetches compact public Chess.com data and returns a coach-friendly summary. It does not run Stockfish yet and does not download full monthly PGN payloads through GPT Actions.

## Tech stack

- Python
- FastAPI
- Uvicorn
- python-chess
- requests
- pydantic

## Project structure

```text
backend/
  app.py
  requirements.txt
  api/
    routes.py
  chesscom/
    client.py
  models/
    responses.py
  services/
    analyzer.py
  stockfish_plan.md
```

## Setup

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

## Run locally

From the repository root:

```bash
uvicorn backend.app:app --reload
```

## Endpoints

### `GET /health`

Returns:

```json
{
  "status": "ok"
}
```

### `GET /analyzePlayer?username=<username>`

Fetches the player's public Chess.com profile and stats, then returns compact JSON with:

- player profile details
- rating summaries by time control
- a short non-engine coaching summary
- `stockfish: "not_enabled"`

Example:

```bash
curl "http://127.0.0.1:8000/analyzePlayer?username=bulletguy01"
```

## Future backend work

Later versions can add:

```http
GET /players/{username}/analysis?month=YYYY-MM
GET /players/{username}/analysis?month=YYYY-MM&timeClass=rapid
GET /players/{username}/openings?month=YYYY-MM&color=black
GET /players/{username}/trend?timeClass=rapid
GET /opponents/{username}/scout?month=YYYY-MM
```

Those future endpoints should fetch monthly Chess.com games server-side and return compact coaching reports instead of raw PGN payloads.

## Stockfish status

Stockfish is intentionally not implemented in backend v1. See `backend/stockfish_plan.md` for the future engine-analysis plan.
