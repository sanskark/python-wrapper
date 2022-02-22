class Bundle:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.display_name_sub_text: str = data.get("displayNameSubText")
        self.description: str = data.get("description")
        self.extra_description: str = data.get("extraDescription")
        self.promo_description: str = data.get("promoDescription")
        self.display_icon: str = data.get("displayIcon")
        self.display_icon2: str = data.get("displayIcon2")
        self.vertical_promo_image: str = data.get("verticalPromoImage")
        self.asset_path: str = data.get("assetPath")

        self.raw_data = data

