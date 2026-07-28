# Future Backend Plan

No backend code is included in ChessCoach v1. This directory documents the future backend so the project stays simple now and grows cleanly later.

## Why add a backend later

A Custom GPT Action can call Chess.com public endpoints directly, but a backend is better for heavier work:

- Fetching several archive months safely.
- Caching Chess.com responses.
- Parsing PGNs into positions and metadata.
- Running Stockfish without blocking the GPT.
- Grouping recurring mistakes across many games.
- Returning a compact coaching report.

## Proposed future endpoints

```http
GET /health
GET /players/{username}/analysis?maxGames=20&timeClass=rapid
GET /players/{username}/openings?color=black&maxGames=50
GET /players/{username}/trend?timeClass=rapid
GET /opponents/{username}/scout?maxGames=20
```

These are future ChessCoach backend endpoints, not Chess.com public API endpoints.

## Backend output goal

The backend should return structured JSON that the GPT can explain, for example:

- Summary verdict.
- Category scores.
- Repeated mistake patterns.
- Example game URLs.
- Engine-confirmed blunders when Stockfish is available.
- Recommended study plan.

## Implementation principles

- Keep the API read-only.
- Use a clear user-agent when calling Chess.com.
- Avoid request bursts and unnecessary parallelism.
- Cache archive and engine results.
- Keep long-running engine analysis asynchronous if needed.
