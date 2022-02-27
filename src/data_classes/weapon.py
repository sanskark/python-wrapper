from typing import List, Optional


class Levels:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.level_item: Optional[str] = data.get("levelItem")
        self.display_icon: Optional[str] = data.get("displayIcon")
        self.streamed_video: Optional[str] = data.get("streamedVideo")
        self.asset_path: str = data.get("assetPath")


class Chromas:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.display_icon: Optional[str] = data.get("displayIcon")
        self.full_render: Optional[str] = data.get("fullRender")
        self.swatch: Optional[str] = data.get("swatch")
        self.streamed_video: Optional[str]= data.get("streamedVideo")
        self.asset_path: str = data.get("assetPath")


class Skin:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.theme_uuid: str = data.get("themeUuid")
        self.content_tier_uuid: str = data.get("contentTierUuid")
        self.display_icon: str = data.get("displayIcon")
        self.wallpaper: Optional[str] = data.get("wallpaper")
        self.asset_path: str = data.get("assetPath")
        self.chromas: List[Chromas] = data.get("chromas")
        self.levels: List[Levels] = data.get("levels")


class GridPosition:
    def __init__(self, data: dict):
        self.row: int = data.get("row")
        self.column: int = data.get("column")


class ShopData:
    def __init__(self, data: dict):
        self.cost: int = data.get("cost")
        self.category: str = data.get("category")
        self.category_text: str = data.get("categoryText")
        self.grid_position: GridPosition = data.get("gridPosition")
        self.can_be_trashed: bool = data.get("canBeTrashed")
        self.image: Optional[str] = data.get("image")
        self.new_image: Optional[str] = data.get("newImage")
        self.new_image2: Optional[str] = data.get("newImage2")
        self.asset_path: str = data.get("assetPath")


class AdsStats:
    def __init__(self, data: dict):
        self.zoom_multiplier: float = data.get("zoomMultiplier")
        self.fire_rate: float = data.get("fireRate")
        self.run_speed_multiplier: float = data.get("runSpeedMultiplier")
        self.burst_count: int = data.get("burstCount")
        self.first_bullet_accuracy: float = data.get("firstBulletAccuracy")


class AltShotgunStats:
    def __init__(self, data: dict):
        self.shotgun_pellet_count: int = data.get("shotgunPelletCount")
        self.burst_rate: float = data.get("burstRate")


class DamageRange:
    def __init__(self, data: dict):
        self.range_start_meters: int = data.get("rangeStartMeters")
        self.range_end_meters: int = data.get("rangeEndMeters")
        self.head_damage: int = data.get("headDamage")
        self.body_damage: int = data.get("bodyDamage")
        self.leg_damage: float = data.get("legDamage")


class WeaponStats:
    def __init__(self, data: dict):
        self.fire_rate: int = data.get("fireRate")
        self.magazine_size: int = data.get("magazineSize")
        self.run_speed_multiplier: float = data.get("runSpeedMultiplier")
        self.equip_time_seconds: float = data.get("equipTimeSeconds")
        self.reload_time_seconds: float = data.get("reloadTimeSeconds")
        self.first_bullet_accuracy: float = data.get("firstBulletAccuracy")
        self.shotgun_pellet_count: int = data.get("shotgunPelletCount")
        self.wall_penetration: str = data.get("wallPenetration")
        self.feature: Optional[str] = data.get("feature")
        self.fire_mode: Optional[str] = data.get("fireMode")
        self.alt_fire_mode: Optional[str] = data.get("altFireType")
        self.ads_stats: Optional[AdsStats] = data.get("adsStats")
        self.alt_shotgun_stats: Optional[AltShotgunStats] = data.get("altShotgunStats")
        self.damage_ranges: List[DamageRange] = data.get("damageRanges")


class Weapon:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.category: str = data.get("category")
        self.default_skin_uuid: str = data.get("defaultSkinUuid")
        self.display_icon: str = data.get("displayIcon")
        self.kill_stream_icon: str = data.get("killStreamIcon")
        self.asset_path: str = data.get("assetPath")
        self.weapon_stats: WeaponStats = data.get("weaponStats")
        self.shop_data: ShopData = data.get("shopData")
        self.skins: List[Skin] = data.get("skins")
