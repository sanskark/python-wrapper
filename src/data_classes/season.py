from typing import Optional
from datetime import datetime


class Season:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.type: Optional[str] = data.get("type")
        self.start_time: datetime = data.get("startTime")
        self.end_time: datetime = data.get("endTime")
        self.parent_uuid: Optional[str] = data.get("parentUuid")
        self.asset_path: str = data.get("assetPath")
