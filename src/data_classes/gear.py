class ShopData:
    def __init__(self, data: dict):
        self.cost: str = data.get("cost")
        self.category: str = data.get("category")
        self.category_text: str = data.get("categoryText")
        self.can_be_trashed: bool = data.get("canBeTrashed")
        self.new_image: str = data.get("newImage")
        self.asset_path: str = data.get("assetPath")


class Gear:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.description: str = data.get("description")
        self.display_icon: str = data.get("displayIcon")
        self.asset_path: str = data.get("assetPath")
        self.shop_data: ShopData = data.get("shopData")
