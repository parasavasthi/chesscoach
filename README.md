# ChessCoach

ChessCoach is a Custom GPT workflow for reviewing public Chess.com games like a practical chess coach. It uses the Chess.com Published Data API to fetch public profiles, stats, archive lists, and monthly games, then guides the GPT to explain recurring patterns, opening habits, rating trends, opponent tendencies, and study priorities.

This repository is intentionally documentation-first for v1: no unnecessary app code, no private-account access, and no backend implementation until the Custom GPT workflow is proven.

## Where to see the v1 changes

If the repository view still looks unchanged, check that you are on the branch containing commit `7c4750c` or open these files directly:

1. `openapi/chesscoach.yaml` — the GPT Actions schema.
2. `prompts/system_prompt.md` — the coach behavior instructions.
3. `docs/usage.md` — the step-by-step Custom GPT setup guide.
4. `backend/stockfish_plan.md` — the future engine-analysis plan.

## Available now

- A GPT Actions-ready OpenAPI schema for Chess.com public endpoints.
- A reusable system prompt that makes the GPT behave like a chess coach.
- Example user prompts for game review, opponent analysis, opening analysis, rating trends, and study advice.
- Usage, architecture, roadmap, backend, and Stockfish planning docs.

## How to use the Custom GPT

1. Open the Custom GPT builder.
2. Copy `prompts/system_prompt.md` into the GPT instructions field.
3. Add the OpenAPI schema from `openapi/chesscoach.yaml` as a new Action.
4. Ask a question from `prompts/example_queries.md`, or provide a Chess.com username and a goal.

Example:

```text
My Chess.com username is <username>. Look at my recent rapid games and tell me the top three recurring mistakes.
```

## How to import the OpenAPI schema

1. In the Custom GPT builder, open **Configure → Actions**.
2. Choose **Create new action**.
3. Paste the full contents of `openapi/chesscoach.yaml` into the schema editor.
4. Save the action.
5. Test `getPlayer`, then `getStats`, then `getArchives`, then `getMonthlyGames`.

The schema calls Chess.com's public API directly. It does not require or support Chess.com login credentials.

## What comes later

A future backend can make ChessCoach stronger by fetching several archives safely, parsing PGNs, caching responses, running Stockfish on selected positions, and returning structured engine-backed coaching reports. That future work is documented in `backend/README.md` and `backend/stockfish_plan.md`.

## Repository structure

```text
README.md
backend/README.md
backend/stockfish_plan.md
docs/architecture.md
docs/roadmap.md
docs/usage.md
openapi/chesscoach.yaml
prompts/example_queries.md
prompts/system_prompt.md
```
