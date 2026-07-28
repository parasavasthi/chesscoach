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
5. Test the endpoints in this order: `getPlayer`, `getStats`, `getArchives`.

## Run a first analysis

Ask:

```text
My Chess.com username is <username>. Review my public stats and tell me what I should study first.
```

The GPT should fetch the public profile, fetch stats, inspect archive availability, and explain rating trends or study priorities without downloading raw monthly games.

## Useful workflows

- **Profile check**: username → profile → account context and public metadata.
- **Rating trends**: stats → compare rapid, blitz, bullet, daily, tactics, and records.
- **Opponent prep**: opponent username → profile and stats → likely strengths, weaknesses, and practical preparation ideas.
- **Archive planning**: archives → identify which month should be sent to the future backend for full game analysis.
- **Study plan**: convert public stats and user goals into a short training routine.

## Why monthly games are not in the GPT Action

Chess.com monthly game archives can contain many games and full PGN text. Those responses can exceed ChatGPT Actions response-size limits, causing `ResponseTooLargeError`. ChessCoach v1 therefore retrieves only safe, compact data through GPT Actions: profile, stats, and archive URLs.

Full monthly game analysis belongs in the future backend. The backend will fetch Chess.com game data server-side and return a compact coaching report instead of raw PGNs.

## Limits

- ChessCoach v1 uses public Chess.com data only.
- The GPT should not ask for Chess.com passwords or private account access.
- GPT Actions can safely retrieve profile, stats, and archive URLs.
- Monthly PGN/game analysis should wait for the future backend.
- Engine-level claims should wait for the future Stockfish backend.
