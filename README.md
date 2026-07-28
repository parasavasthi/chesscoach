# ChessCoach

ChessCoach is a Custom GPT workflow for reviewing public Chess.com profiles and stats like a practical chess coach. In v1, the GPT Action safely retrieves public player profiles, rating stats, and archive URLs. Full monthly game and PGN analysis is intentionally deferred to a future backend because raw monthly game responses can exceed ChatGPT Actions response-size limits.

This repository is documentation-first for v1: no unnecessary app code, no private-account access, and no backend implementation until the Custom GPT workflow is proven.

## Where to see the v1 changes

If the repository view still looks unchanged, check that you are on the branch containing commit `7c4750c` or open these files directly:

1. `openapi/chesscoach.yaml` — the GPT Actions schema.
2. `prompts/system_prompt.md` — the coach behavior instructions.
3. `docs/usage.md` — the step-by-step Custom GPT setup guide.
4. `backend/stockfish_plan.md` — the future engine-analysis plan.

## Available now

- A GPT Actions-ready OpenAPI schema for safe Chess.com public profile, stats, and archive URL endpoints.
- A reusable system prompt that makes the GPT behave like a chess coach while respecting Actions limits.
- Example user prompts for rating review, opponent analysis, opening planning from available metadata, and study advice.
- Usage, architecture, roadmap, backend, and Stockfish planning docs.

## How to use the Custom GPT

1. Open the Custom GPT builder.
2. Copy `prompts/system_prompt.md` into the GPT instructions field.
3. Add the OpenAPI schema from `openapi/chesscoach.yaml` as a new Action.
4. Ask a question from `prompts/example_queries.md`, or provide a Chess.com username and a goal.

Example:

```text
My Chess.com username is <username>. Review my public stats and tell me what I should study first.
```

## How to import the OpenAPI schema

1. In the Custom GPT builder, open **Configure → Actions**.
2. Choose **Create new action**.
3. Paste the full contents of `openapi/chesscoach.yaml` into the schema editor.
4. Save the action.
5. Test `getPlayer`, then `getStats`, then `getArchives`.

The schema calls Chess.com's public API directly. It does not require or support Chess.com login credentials. It does not fetch monthly game archives directly because those responses can be too large for ChatGPT Actions.

## What comes later

A future backend will fetch monthly Chess.com game data server-side, parse PGNs, cache responses, run Stockfish on selected positions, and return compact coaching reports such as `GET /players/{username}/analysis?month=YYYY-MM`. That backend design avoids sending raw monthly PGN payloads through ChatGPT Actions.

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
