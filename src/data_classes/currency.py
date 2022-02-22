class Currency:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.display_name_singular: str = data.get("displayNameSingular")
        self.display_icon: str = data.get("displayIcon")
        self.large_icon: str = data.get("largeIcon")
        self.asset_path: str = data.get("assetPath")
