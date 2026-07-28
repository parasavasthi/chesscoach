# ChessCoach Roadmap

## Milestone 1: ChessCoach v1 foundation

- Maintain a clean documentation-first repository.
- Provide a GPT Actions-ready Chess.com public API schema for profile, stats, and archive URLs.
- Provide coach instructions and example prompts.
- Document why monthly game and PGN analysis moves to the backend.

## Milestone 2: Custom GPT testing

- Import `openapi/chesscoach.yaml` into a Custom GPT Action.
- Test `getPlayer`, `getStats`, and `getArchives`.
- Confirm the GPT can analyse public stats, opponent profiles, rating trends, archive availability, and study advice prompts.

## Milestone 3: Backend design

- Define backend response contracts for compact coaching reports.
- Add `GET /players/{username}/analysis?month=YYYY-MM`.
- Fetch Chess.com monthly games server-side instead of through GPT Actions.
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
