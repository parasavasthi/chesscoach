# Stockfish Integration Plan

## Purpose

Stockfish will make future ChessCoach analysis more objective. The GPT can explain chess patterns, but Stockfish should decide whether a move was actually a blunder, mistake, inaccuracy, missed tactic, or conversion error.

## Where Stockfish belongs

Stockfish should run in the future backend, not in the OpenAPI schema and not in the GPT prompt.

```text
Custom GPT → ChessCoach backend → Stockfish
```

## v1 backend analysis strategy

Do not analyse every move deeply at first. Start with selected positions:

- After the opening phase.
- Before and after captures.
- Before and after checks.
- Before major material swings.
- Near resignation, timeout, or checkmate.
- In endgames where the result changed sharply.

## Suggested engine result shape

Each flagged move should include:

- Game URL.
- Move number.
- Side to move.
- FEN before the move.
- Played move.
- Best engine move.
- Evaluation before the move.
- Evaluation after the move.
- Evaluation loss.
- Human-readable label.

## Pattern grouping

After individual move analysis, group mistakes into coachable themes:

- Hanging pieces.
- Missing opponent threats.
- Unsafe king.
- Poor opening development.
- Bad trades.
- Pawn-structure weaknesses.
- Endgame conversion problems.
- Time-pressure blunders.

## Later improvements

- Configurable depth and time limits.
- Cached FEN evaluations.
- Background analysis queue.
- Historical trend tracking.
- Tactical motif classification.
