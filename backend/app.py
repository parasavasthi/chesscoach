"""FastAPI application entrypoint for ChessCoach backend v1."""

from __future__ import annotations

from fastapi import FastAPI

from backend.api.routes import router

app = FastAPI(
    title="ChessCoach Backend",
    version="1.0.0",
    description="Compact Chess.com profile and stats analysis API. Stockfish is planned but not enabled yet.",
)
app.include_router(router)
