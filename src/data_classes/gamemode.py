from typing import List, Optional


class GameFeatureOverrides:
    def __init__(self, data: dict):
        self.feature_name: str = data.get("featureName")
        self.state: bool = data.get("state")


class GameRuleBoolOverrides:
    def __init__(self, data: dict):
        self.rule_name: str = data.get("ruleName")
        self.state: bool = data.get("state")


class GameMode:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.duration: str = data.get("duration")
        self.allowed_match_timeouts: bool = data.get("allowsMatchTimeouts")
        self.is_team_voice_allowed: bool = data.get("isTeamVoiceAllowed")
        self.is_minimap_hidden: bool = data.get("isMinimapHidden")
        self.orb_count: int = data.get("orbCount")
        self.team_role: list = data.get("teamRole")
        self.game_feature_overrides: List[GameFeatureOverrides] = data.get("gameFeatureOverrides")
        self.game_rule_bool_overrides: List[GameRuleBoolOverrides] = data.get("gameRuleBoolOverrides")
        self.display_icon: str = data.get("displayIcon")
        self.asset_path: str = data.get("assetPath")


class Equippable:
    def __init__(self, data: dict):
        self.uuid: str = data.get("uuid")
        self.display_name: str = data.get("displayName")
        self.category: str = data.get("category")
        self.display_icon: str = data.get("displayIcon")
        self.kill_stream_icon: str = data.get("killStreamIcon")
        self.asset_path: str = data.get("assetPath")
