# Usage Guide

## Create the Custom GPT

1. Open the Custom GPT builder.
2. Paste `prompts/system_prompt.md` into the instruction area.
3. Save the GPT name and description.

## Import the OpenAPI schema

1. Open **Configure → Actions**.
2. Select **Create new action**.
3. Paste the contents of `openapi/chesscoach.yaml`.
4. Save the action.
5. Test the endpoints in this order: `getPlayer`, `getStats`, `getArchives`, `getMonthlyGames`.

## Run a first analysis

Ask:

```text
My Chess.com username is <username>. Review my recent rapid games and find the top three recurring mistakes.
```

The GPT should fetch public profile and stats, choose recent archive months, fetch monthly games, then summarize patterns.

## Useful workflows

- **Self-review**: username → stats → archives → monthly games → coaching report.
- **Opponent prep**: opponent username → stats → recent games → likely openings and tendencies.
- **Opening review**: monthly games → filter by color and opening tags in PGN/ECO data.
- **Rating trends**: stats → compare rapid, blitz, bullet, daily, tactics, and records.
- **Study plan**: convert repeated mistakes into a short training routine.

## Limits

- ChessCoach v1 uses public Chess.com data only.
- The GPT should not ask for Chess.com passwords or private account access.
- Monthly game responses can be large, so start with recent months.
- Engine-level claims should wait for the future Stockfish backend.
