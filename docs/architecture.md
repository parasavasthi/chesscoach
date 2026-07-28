# ChessCoach Architecture

## Goal

Keep ChessCoach v1 simple, professional, and ready for a Custom GPT workflow without adding unnecessary code or sending oversized monthly game payloads through ChatGPT Actions.

## Current v1 architecture

```text
User
  ↓
Custom GPT with ChessCoach prompt
  ↓
GPT Action using openapi/chesscoach.yaml
  ↓
Chess.com Published Data API
  ↓
Profile, stats, and archive URLs only
```

## Current responsibilities

### Custom GPT

- Ask for a username only when public Chess.com data is needed.
- Fetch public profile, stats, and archive URLs.
- Analyse rating trends, public records, account context, and available archive months.
- Support self-review planning, opponent analysis, rating trends, and study advice.
- Avoid raw monthly game downloads because they can exceed ChatGPT Actions response-size limits.

### OpenAPI schema

- Expose compact Chess.com public API endpoints only.
- Keep operations small enough for ChatGPT Actions execution.
- Define response schemas with explicit properties.
- Avoid private account access, authentication, write operations, and full monthly PGN payloads.

## Future backend architecture

```text
User
  ↓
Custom GPT
  ↓
ChessCoach backend
  ├─ Chess.com public API client
  ├─ Monthly archive fetcher
  ├─ PGN parser
  ├─ Stockfish analysis worker
  ├─ cache/storage layer
  └─ compact coaching report
```

The backend should be added after the direct Custom GPT workflow is stable. It will handle tasks that are too large or too deterministic for the GPT action alone: monthly game fetching, PGN parsing, caching, engine analysis, and repeated-mistake grouping.

## Future Stockfish role

Stockfish should not live in the prompt or OpenAPI schema. It should run in the backend and return objective data such as evaluation changes, best moves, blunder labels, and tactical motif candidates. The GPT can then explain those compact results in human language.
