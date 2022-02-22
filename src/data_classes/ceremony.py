class Ceremony:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.asset_path: str = data.get("assetPath")

        self.raw_data: dict = data