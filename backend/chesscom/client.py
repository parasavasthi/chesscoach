"""Small Chess.com Published Data API client."""

from __future__ import annotations

from typing import Any, Dict

import requests
from fastapi import HTTPException


class ChessComClient:
    """HTTP client for compact Chess.com public API calls."""

    BASE_URL = "https://api.chess.com/pub"

    def __init__(self, timeout_seconds: int = 10) -> None:
        self.timeout_seconds = timeout_seconds
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "ChessCoach/1.0 (contact: local-development)",
                "Accept": "application/json",
            }
        )

    def get_player(self, username: str) -> Dict[str, Any]:
        """Fetch a public Chess.com player profile."""

        return self._get_json(f"/player/{username}")

    def get_stats(self, username: str) -> Dict[str, Any]:
        """Fetch public Chess.com player stats."""

        return self._get_json(f"/player/{username}/stats")

    def _get_json(self, path: str) -> Dict[str, Any]:
        """Request JSON from Chess.com and translate failures to API errors."""

        url = f"{self.BASE_URL}{path}"
        try:
            response = self.session.get(url, timeout=self.timeout_seconds)
        except requests.RequestException as exc:
            raise HTTPException(status_code=502, detail="Chess.com request failed") from exc

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Chess.com player not found")
        if response.status_code == 429:
            raise HTTPException(status_code=429, detail="Chess.com rate limit reached")
        if not response.ok:
            raise HTTPException(status_code=502, detail="Chess.com returned an upstream error")

        try:
            data = response.json()
        except ValueError as exc:
            raise HTTPException(status_code=502, detail="Chess.com returned invalid JSON") from exc

        if not isinstance(data, dict):
            raise HTTPException(status_code=502, detail="Chess.com returned an unexpected payload")
        return data
