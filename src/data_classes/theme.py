from typing import Optional


class Theme:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.display_icon: Optional[str] = data.get("displayIcon")
        self.store_featured_image: Optional[str] = data.get("storeFeaturedImage")
        self.asset_path: str = data.get("assetPath")
