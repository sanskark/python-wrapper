class PlayerTitle:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_text: str = data.get("displayText")
        self.title_text: str = data.get("titleText")
        self.is_hidden_if_not_owned: bool = data.get("isHiddenIfNotOwned")
        self.asset_path: str = data.get("assetPath")
