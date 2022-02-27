from typing import Optional, List


class Level:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.spray_level: int = data.get("sprayLevel")
        self.display_name: str = data.get("displayName")
        self.display_icon: str = data.get("displayIcon")
        self.asset_path: str = data.get("assetPath")


class Spray:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.category: Optional[str] = data.get("category")
        self.theme_uuid: Optional[str] = data.get("themeUuid")
        self.display_icon: str = data.get("displayIcon")
        self.full_icon: str = data.get("fullIcon")
        self.full_transparent_icon: str = data.get("fullTransparentIcon")
        self.asset_path: str = data.get("assetPath")
        self.levels: List[Level] = data.get("levels")
