class ContentTier:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.dev_name: str = data.get("devName")
        self.highlight_color: str = data.get("highlightColor")
        self.display_icon: str = data.get("displayIcon")
        self.asset_path: str = data.get("assetPath")
