from datetime import datetime


class Event:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.short_display_name: str = data.get("shortDisplayName")
        self.start_time: datetime = data.get("startTime")
        self.end_time: datetime = data.get("endTime")
        self.asset_path: str = data.get("assetPath")
