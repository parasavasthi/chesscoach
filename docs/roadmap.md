# ChessCoach Roadmap

## Milestone 1: ChessCoach v1 foundation

- Maintain a clean documentation-first repository.
- Provide a GPT Actions-ready Chess.com public API schema.
- Provide coach instructions and example prompts.
- Document usage, architecture, roadmap, backend plans, and Stockfish plans.

## Milestone 2: Custom GPT testing

- Import `openapi/chesscoach.yaml` into a Custom GPT Action.
- Test `getPlayer`, `getStats`, `getArchives`, and `getMonthlyGames`.
- Confirm the GPT can analyse self-review, opponent analysis, opening analysis, rating trends, and study advice prompts.

## Milestone 3: Backend design

- Define backend response contracts for aggregated coaching reports.
- Add safe Chess.com request handling, caching, and rate-limit protection.
- Parse PGN data into positions, moves, openings, results, and time-control metadata.

## Milestone 4: Stockfish integration

- Add Stockfish analysis for selected positions.
- Detect evaluation drops, missed tactics, conversion problems, and repeated blunders.
- Store engine results so repeated analyses get faster.

## Milestone 5: Personalized improvement loop

- Track recurring mistakes over time.
- Recommend drills based on the user's most common losses.
- Compare progress between review sessions.
