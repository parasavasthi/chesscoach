"""HTTP routes for ChessCoach backend v1."""

from __future__ import annotations

from fastapi import APIRouter, Query

from backend.models.responses import AnalyzePlayerResponse, HealthResponse
from backend.services.analyzer import PlayerAnalyzer

router = APIRouter()
analyzer = PlayerAnalyzer()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Return backend health status."""

    return HealthResponse()


@router.get("/analyzePlayer", response_model=AnalyzePlayerResponse)
def analyze_player(username: str = Query(..., min_length=1, description="Chess.com username")) -> AnalyzePlayerResponse:
    """Fetch public Chess.com profile and stats and return a compact summary."""

    return analyzer.analyze_player(username)
