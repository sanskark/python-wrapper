from datetime import datetime
from typing import List, Optional


class Border:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.level: int = data.get("level")
        self.wins_required: int = data.get("winsRequired")
        self.display_icon: str = data.get("displayIcon")
        self.small_icon: Optional[str] = data.get("smallIcon")
        self.asset_path: str = data.get("assetPath")


class CompetitiveSeason:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.start_time: datetime = data.get("startTime")
        self.end_time: datetime = data.get("endTime")
        self.season_uuid: str = data.get("seasonUuid")
        self.competitive_tier_uuid: str = data.get("competitiveTiersUuid")
        self.borders: List[Border] = data.get("borders")
