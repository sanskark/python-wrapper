from typing import List


class Role:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.description: str = data.get("description")
        self.display_icon: str = data.get("displayIcon")
        self.asset_path: str = data.get("assetPath")


class Ability:
    def __init__(self, data: dict):
        self.slot: str = data.get("slot")
        self.display_name: str = data.get("displayName")
        self.description: str = data.get("description")
        self.display_icon: str = data.get("displayIcon")


class MediaList:
    def __init__(self, data: dict):
        self.id: int = data.get("id")
        self.wwise: str = data.get("wwise")
        self.wave: str = data.get("wave")


class VoiceLine:
    def __init__(self, data: dict):
        self.min_duration: float = data.get("minDuration")
        self.max_duration: float = data.get("maxDuration")
        self.media_list: List[MediaList] = [MediaList(x) for x in data.get("mediaList")]


class Agent:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.description: str = data.get("description")
        self.developer_name: str = data.get("developerName")
        self.character_tags: list = data.get("characterTags")
        self.display_icon: str = data.get("displayIcon")
        self.display_icon_small: str = data.get("displayIconSmall")
        self.bust_portrait: str = data.get("bustPortrait")
        self.full_portrait: str = data.get("fullPortrait")
        self.killfeed_portrait: str = data.get("killfeedPortrait")
        self.background: str = data.get("background")
        self.asset_path: str = data.get("assetPath")
        self.is_full_portrait_right_facing: bool = data.get("isFullPortraitRightFacing")
        self.is_playable_character: bool = data.get("isPlayableCharacter")
        self.is_available_for_test: bool = data.get("isAvailableForTest")
        self.is_base_content: bool = data.get("isBaseContent")
        self.role: Role = Role(data.get("role")) if data.get("role") is not None else None
        self.abilities: List[Ability] = [Ability(x) for x in data.get("abilities")] if data.get("abilities") is not None else None
        self.voice_line: VoiceLine = VoiceLine(data.get("voiceLine")) if data.get("voiceLine") is not None else None

        self.raw_data: dict = data

    def __str__(self):
        return f'{self.display_name} object'
