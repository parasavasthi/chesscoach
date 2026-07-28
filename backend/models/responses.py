"""Pydantic response models for the ChessCoach backend."""

from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, Field, HttpUrl


class HealthResponse(BaseModel):
    """Simple health-check response."""

    status: str = Field(default="ok", description="Service health status.")


class GameRecord(BaseModel):
    """Win/loss/draw record for a Chess.com time control."""

    win: int = 0
    loss: int = 0
    draw: int = 0
    timeout_percent: Optional[float] = None


class RatingSummary(BaseModel):
    """Compact rating summary for one Chess.com stats category."""

    current: Optional[int] = None
    best: Optional[int] = None
    games_played: int = 0
    record: GameRecord = Field(default_factory=GameRecord)


class PlayerSummary(BaseModel):
    """Compact profile details used by the coach."""

    username: str
    profile_url: Optional[HttpUrl] = None
    title: Optional[str] = None
    status: Optional[str] = None
    country: Optional[str] = None
    joined: Optional[int] = None
    last_online: Optional[int] = None
    followers: Optional[int] = None


class AnalyzePlayerResponse(BaseModel):
    """Response returned by GET /analyzePlayer."""

    player: PlayerSummary
    ratings: Dict[str, RatingSummary]
    coaching_summary: str
    stockfish: str = "not_enabled"
