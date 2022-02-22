from typing import List


class Tier:
    def __init__(self, data: dict):
        self.tier: int = data.get("tier")
        self.tier_name: str = data.get("tierName")
        self.division: str
        self.division_name: str
        self.color: str
        self.background_color: str
        self.small_icon: str
        self.large_icon: str


class CompetitiveTier:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.asset_object_name = data.get("assetObjectName")
        self.tiers: List[Tier] = [Tier(x) for x in data.get("tiers")] if data.get("tiers") is not None else None
        self.asset_path: str = data.get("assetPath")
