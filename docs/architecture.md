# ChessCoach Architecture

## Goal

Keep ChessCoach v1 simple, professional, and ready for a Custom GPT workflow without adding unnecessary code.

## Current v1 architecture

```text
User
  ↓
Custom GPT with ChessCoach prompt
  ↓
GPT Action using openapi/chesscoach.yaml
  ↓
Chess.com Published Data API
```

## Current responsibilities

### Custom GPT

- Ask for a username only when public Chess.com data is needed.
- Fetch public profile, stats, archives, and monthly games.
- Analyse recurring patterns rather than only one move or one game.
- Support self-review, opponent analysis, opening analysis, rating trends, and study advice.
- Explain findings in practical chess language.

### OpenAPI schema

- Expose Chess.com public API endpoints only.
- Keep operations small enough for GPT Actions import.
- Define response schemas with explicit properties.
- Avoid private account access, authentication, and write operations.

## Future backend architecture

```text
User
  ↓
Custom GPT
  ↓
ChessCoach backend
  ├─ Chess.com public API client
  ├─ PGN parser
  ├─ Stockfish analysis worker
  ├─ cache/storage layer
  └─ structured coaching report
```

The backend should be added after the direct Custom GPT workflow is stable. It will handle tasks that are too heavy or too deterministic for the GPT action alone: multi-month aggregation, PGN parsing, caching, engine analysis, and repeated-mistake grouping.

## Future Stockfish role

Stockfish should not live in the prompt or OpenAPI schema. It should run in the backend and return objective data such as evaluation changes, best moves, blunder labels, and tactical motif candidates. The GPT can then explain those results in human language.
