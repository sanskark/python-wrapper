from typing import List


class Reward:
    def __init__(self, data: dict):
        self.type = data.get("type")
        self.uuid: str = data.get("uuid")
        self.amount: int = data.get("amount")
        self.is_highlighted: bool = data.get("isHighlighted")


class Level:
    def __init__(self, data: dict):
        self.reward: Reward = Reward(data.get("reward"))
        self.xp: int = data.get("xp")
        self.vp_cost = data.get("vpCost")
        self.is_purchasable_with_vp: bool = data.get("isPurchasableWithVP")


class Chapter:
    def __init__(self, data: dict):
        self.is_epilogue: bool = data.get("isEpilogue")
        self.levels: List[Level] = [Level(x) for x in data.get("levels")]
        self.free_rewards: List[Reward] = data.get("")


class Content:
    def __init__(self, data: dict):
        self.relation_type: str = data.get("relationType")
        self.relation_uuid: str = data.get("relationUuid")
        self.chapters: List[Chapter] = [Chapter(x) for x in data.get("chapters")]


class Contract:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.display_icon: str = data.get("displayIcon")
        self.ship_it: bool = data.get("shipIt")
        self.free_reward_schedule_uuid: str = data.get("freeRewardScheduleUuid")
        self.content: Content = Content(data.get("content"))
        self.asset_path: str = data.get("assetPath")