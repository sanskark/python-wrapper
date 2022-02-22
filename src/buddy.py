from typing import List


class Level:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.charm_level: int = data.get("charmLevel")
        self.display_name: str = data.get("displayName")
        self.display_icon: str = data.get("displayIcon")
        self.asset_path: str = data.get("assetPath")


class Buddy:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.is_hidden_if_not_owned: bool = data.get("isHiddenIfNotOwned")
        self.theme_uuid: None = data.get("themeUuid")
        self.display_icon: str = data.get("displayIcon")
        self.asset_path: str = data.get("assetPath")
        self.levels: List[Level] = [Level(x) for x in data.get("levels")]

        self.raw_data = data

    def __str__(self):
        return f"{self.display_name}"
