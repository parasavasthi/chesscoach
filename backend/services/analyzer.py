"""Player analysis service for ChessCoach backend v1."""

from __future__ import annotations

from typing import Any, Dict

from backend.chesscom.client import ChessComClient
from backend.models.responses import AnalyzePlayerResponse, GameRecord, PlayerSummary, RatingSummary


RATING_CATEGORIES = {
    "chess_rapid": "rapid",
    "chess_blitz": "blitz",
    "chess_bullet": "bullet",
    "chess_daily": "daily",
}


class PlayerAnalyzer:
    """Build compact coaching summaries from Chess.com profile and stats data."""

    def __init__(self, chesscom_client: ChessComClient | None = None) -> None:
        self.chesscom_client = chesscom_client or ChessComClient()

    def analyze_player(self, username: str) -> AnalyzePlayerResponse:
        """Fetch public Chess.com data and return a compact player summary."""

        profile = self.chesscom_client.get_player(username)
        stats = self.chesscom_client.get_stats(username)
        ratings = self._summarize_ratings(stats)

        player = PlayerSummary(
            username=profile.get("username", username),
            profile_url=profile.get("url"),
            title=profile.get("title"),
            status=profile.get("status"),
            country=profile.get("country"),
            joined=profile.get("joined"),
            last_online=profile.get("last_online"),
            followers=profile.get("followers"),
        )

        return AnalyzePlayerResponse(
            player=player,
            ratings=ratings,
            coaching_summary=self._build_coaching_summary(player.username, ratings),
        )

    def _summarize_ratings(self, stats: Dict[str, Any]) -> Dict[str, RatingSummary]:
        """Extract compact rating summaries from Chess.com stats."""

        summaries: Dict[str, RatingSummary] = {}
        for chesscom_key, display_name in RATING_CATEGORIES.items():
            raw_category = stats.get(chesscom_key)
            if not isinstance(raw_category, dict):
                continue

            record = raw_category.get("record") or {}
            wins = int(record.get("win") or 0)
            losses = int(record.get("loss") or 0)
            draws = int(record.get("draw") or 0)

            summaries[display_name] = RatingSummary(
                current=self._nested_int(raw_category, "last", "rating"),
                best=self._nested_int(raw_category, "best", "rating"),
                games_played=wins + losses + draws,
                record=GameRecord(
                    win=wins,
                    loss=losses,
                    draw=draws,
                    timeout_percent=record.get("timeout_percent"),
                ),
            )
        return summaries

    def _build_coaching_summary(self, username: str, ratings: Dict[str, RatingSummary]) -> str:
        """Create a short, non-engine coaching summary."""

        if not ratings:
            return f"Found {username}'s profile, but no standard rating categories were available."

        active_modes = sorted(ratings.items(), key=lambda item: item[1].games_played, reverse=True)
        most_active_name, most_active = active_modes[0]
        best_modes = [item for item in ratings.items() if item[1].current is not None]
        best_text = ""
        if best_modes:
            best_name, best_rating = max(best_modes, key=lambda item: item[1].current or 0)
            best_text = f" Their highest current listed rating is {best_rating.current} in {best_name}."

        return (
            f"{username} is most active in {most_active_name} with "
            f"{most_active.games_played} recorded games in that category."
            f"{best_text} Stockfish analysis is not enabled yet, so this is a compact profile/stat summary."
        )

    @staticmethod
    def _nested_int(data: Dict[str, Any], *keys: str) -> int | None:
        """Read a nested integer from a dictionary."""

        current: Any = data
        for key in keys:
            if not isinstance(current, dict):
                return None
            current = current.get(key)
        return current if isinstance(current, int) else None
