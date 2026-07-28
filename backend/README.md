# Future Backend Plan

No backend code is included in ChessCoach v1. This directory documents the future backend so the project stays simple now and grows cleanly later.

## Why add a backend later

A Custom GPT Action can safely call compact Chess.com public endpoints for profile, stats, and archive URLs. Full monthly game archives can be too large for ChatGPT Actions and may trigger `ResponseTooLargeError`, so monthly game analysis should happen in a backend.

The backend is better for heavier work:

- Fetching monthly Chess.com game archives server-side.
- Returning compact coaching reports instead of raw PGNs.
- Caching Chess.com responses.
- Parsing PGNs into positions and metadata.
- Running Stockfish without blocking the GPT.
- Grouping recurring mistakes across many games.

## Proposed future endpoints

```http
GET /health
GET /players/{username}/analysis?month=YYYY-MM
GET /players/{username}/analysis?month=YYYY-MM&timeClass=rapid
GET /players/{username}/openings?month=YYYY-MM&color=black
GET /players/{username}/trend?timeClass=rapid
GET /opponents/{username}/scout?month=YYYY-MM
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
- Return compact JSON reports, not full monthly PGN payloads.
- Keep long-running engine analysis asynchronous if needed.
