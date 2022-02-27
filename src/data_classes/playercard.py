from typing import Optional


class PlayerCard:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.is_hidden_if_not_owned: bool = data.get("isHiddenIfNotOwned")
        self.theme_uuid: Optional[str] = data.get("themeUuid")
        self.display_icon: str = data.get("displayIcon")
        self.small_art: str = data.get("smallArt")
        self.wide_art: str = data.get("wideArt")
        self.wide_art: str = data.get("wideArt")
        self.asset_path: str = data.get("assetPath")
