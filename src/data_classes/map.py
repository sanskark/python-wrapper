class Location:
    def __init__(self, data: dict):
        self.x: float = data.get("x")
        self.y: float = data.get("y")


class Callouts:
    def __init__(self, data: dict):
        self.region_name: str = data.get("regionName")
        self.super_region_name: str = data.get("superRegionName")
        self.location: Location = data.get("location")


class Map:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.coordinates: str = data.get("coordinates")
        self.display_icon: str = data.get("displayIcon")
        self.list_view_icon: str = data.get("listViewIcon")
        self.splash: str = data.get("splash")
        self.asset_path: str = data.get("assetPath")
        self.map_url: str = data.get("mapUrl")
        self.x_multiplier: float = data.get("xMultiplier")
        self.y_multiplier: float = data.get("yMultiplier")
        self.x_scalar_to_add: float = data.get("xScalarToAdd")
        self.y_scalar_to_add: float = data.get("yScalarToAdd")
