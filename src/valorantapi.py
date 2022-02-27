from .endpoints import EndPoints

from .data_classes.agent import Agent
from .data_classes.buddy import Buddy, Level as BuddyLevel
from .data_classes.bundle import Bundle
from .data_classes.ceremony import Ceremony
from .data_classes.competitivetier import CompetitiveTier
from .data_classes.contenttier import ContentTier
from .data_classes.contract import Contract
from .data_classes.currency import Currency
from .data_classes.event import Event
from .data_classes.gamemode import GameMode, Equippable
from .data_classes.gear import Gear
from .data_classes.map import Map
from .data_classes.playercard import PlayerCard
from .data_classes.playertitle import PlayerTitle
from .data_classes.season import Season
from .data_classes.competitiveseason import CompetitiveSeason
from .data_classes.spray import Spray, Level as SprayLevel
from .data_classes.theme import Theme
from .data_classes.weapon import Weapon, Skin as WeaponSkin, Chromas, Levels as WeaponSkinLevel
from .data_classes.version import Version

from .client import Client
from typing import List


class ValorantApi:
    def __init__(self):
        self.client = Client()

    """
        Agents
    """
    def get_agents(self) -> List[Agent]:
        data = self.client.get(EndPoints.agents)
        return [Agent(x) for x in data]

    def find_agent_by_uuid(self, uuid: str) -> Agent:
        data = self.client.get(f"{EndPoints.agents}/{uuid}")
        return Agent(data)

    """
        Buddies
    """
    def get_buddies(self) -> List[Buddy]:
        data = self.client.get(EndPoints.buddies)
        return [Buddy(x) for x in data]

    def find_buddy_by_uuid(self, uuid: str) -> Buddy:
        data = self.client.get(f"{EndPoints.buddies}/{uuid}")
        return Buddy(data)

    def get_buddy_levels(self) -> List[BuddyLevel]:
        data = self.client.get(EndPoints.buddy_levels)
        return [BuddyLevel(x) for x in data]

    def find_buddy_levels_by_uuid(self, uuid: str) -> BuddyLevel:
        data = self.client.get(f"{EndPoints.buddy_levels}/{uuid}")
        return BuddyLevel(data)

    """
        Bundles
    """
    def get_bundles(self) -> List[Bundle]:
        data = self.client.get(EndPoints.bundles)
        return [Bundle(x) for x in data]

    def find_bundle_by_uuid(self, uuid: str) -> Bundle:
        data = self.client.get(f"{EndPoints.bundles}/{uuid}")
        return Bundle(data)

    """
        Ceremonies
    """
    def get_ceremony(self) -> List[Ceremony]:
        data = self.client.get(EndPoints.ceremonies)
        return [Ceremony(x) for x in data]

    def find_ceremony_by_uuid(self, uuid: str) -> Ceremony:
        data = self.client.get(f"{EndPoints.ceremonies}/{uuid}")
        return Ceremony(data)

    """
        Competitive Tiers
    """
    def get_competitivetiers(self) -> List[CompetitiveTier]:
        data = self.client.get(EndPoints.competitive_tiers)
        return [CompetitiveTier(x) for x in data]

    def find_competitivetier_by_uuid(self, uuid: str) -> CompetitiveTier:
        data = self.client.get(f"{EndPoints.competitive_tiers}/{uuid}")
        return CompetitiveTier(data)

    """
        Content Tiers
    """
    def get_contenttiers(self) -> List[ContentTier]:
        data = self.client.get(EndPoints.content_tiers)
        return [ContentTier(x) for x in data]

    def find_contenttier_by_uuid(self, uuid: str) -> ContentTier:
        data = self.client.get(f"{EndPoints.content_tiers}/{uuid}")
        return ContentTier(data)
    """
        Contracts
    """
    def get_contracts(self) -> List[Contract]:
        data = self.client.get(EndPoints.contracts)
        return [Contract(x) for x in data]

    def find_contract_by_uuid(self, uuid: str) -> Contract:
        data = self.client.get(f"{EndPoints.contracts}/{uuid}")
        return Contract(data)

    """
        Currencies
    """
    def get_currencies(self) -> List[Currency]:
        data = self.client.get(EndPoints.currencies)
        return [Currency(x) for x in data]

    def find_currency_by_uuid(self, uuid: str) -> Currency:
        data = self.client.get(f"{EndPoints.currencies}/{uuid}")
        return Currency(data)

    """
        Events
    """
    def get_events(self) -> List[Event]:
        data = self.client.get(EndPoints.events)
        return [Event(x) for x in data]

    def find_event_by_uuid(self, uuid: str) -> Event:
        data = self.client.get(f"{EndPoints.events}/{uuid}")
        return Event(data)

    """
        GameMode and its Equippables
    """
    def get_gamemodes(self) -> List[GameMode]:
        data = self.client.get(EndPoints.gamemodes)
        return [GameMode(x) for x in data]

    def find_gamemode_by_uuid(self, uuid: str) -> GameMode:
        data = self.client.get(f"{EndPoints.gamemodes}/{uuid}")
        return GameMode(data)

    def get_gamemodes_equippables(self) -> List[Equippable]:
        data = self.client.get(EndPoints.gamemode_equip)
        return [Equippable(x) for x in data]

    def find_gamemode_equippables_by_uuid(self, uuid: str) -> Equippable:
        data = self.client.get(f"{EndPoints.gamemode_equip}/{uuid}")
        return Equippable(data)

    """
        Gear
    """
    def get_gears(self) -> List[Gear]:
        data = self.client.get(EndPoints.gear)
        return [Gear(x) for x in data]

    def find_gear_by_uuid(self, uuid: str) -> Gear:
        data = self.client.get(f"{EndPoints.gear}/{uuid}")
        return Gear(data)

    """
        Maps
    """
    def get_maps(self) -> List[Map]:
        data = self.client.get(EndPoints.maps)
        return [Map(x) for x in data]

    def find_map_by_uuid(self, uuid: str) -> Map:
        data = self.client.get(f"{EndPoints.maps}/{uuid}")
        return Map(data)

    """
        Player Cards
    """
    def get_playercards(self) -> List[PlayerCard]:
        data = self.client.get(EndPoints.player_cards)
        return [PlayerCard(x) for x in data]

    def find_playercard_by_uuid(self, uuid: str) -> PlayerCard:
        data = self.client.get(f"{EndPoints.player_cards}/{uuid}")
        return PlayerCard(data)

    """
        Player Titles
    """
    def get_playertitles(self) -> List[PlayerTitle]:
        data = self.client.get(EndPoints.player_titles)
        return [PlayerTitle(x) for x in data]

    def find_playertitle_by_uuid(self, uuid: str) -> PlayerTitle:
        data = self.client.get(f"{EndPoints.player_titles}/{uuid}")
        return PlayerTitle(data)

    """
        Seasons, Competitive Seasons
    """
    def get_seasons(self) -> List[Season]:
        data = self.client.get(EndPoints.seasons)
        return [Season(x) for x in data]

    def find_season_by_uuid(self, uuid: str) -> Season:
        data = self.client.get(f"{EndPoints.seasons}/{uuid}")
        return Season(data)

    def get_competitive(self) -> List[CompetitiveSeason]:
        data = self.client.get(EndPoints.competitive_seasons)
        return [CompetitiveSeason(x) for x in data]

    def find_competitive_by_uuid(self, uuid: str) -> CompetitiveSeason:
        data = self.client.get(f"{EndPoints.competitive_seasons}/{uuid}")
        return CompetitiveSeason(data)

    """
        Spray
    """
    def get_sprays(self) -> List[Spray]:
        data = self.client.get(EndPoints.sprays)
        return [Spray(x) for x in data]

    def find_spray_by_uuid(self, uuid: str) -> Spray:
        data = self.client.get(f"{EndPoints.sprays}/{uuid}")
        return Spray(data)

    def get_spray_levels(self) -> List[SprayLevel]:
        data = self.client.get(EndPoints.spray_levels)
        return [SprayLevel(x) for x in data]

    def find_spray_levels_by_uuid(self, uuid: str) -> SprayLevel:
        data = self.client.get(f"{EndPoints.spray_levels}/{uuid}")
        return SprayLevel(data)

    """
        Themes
    """
    def get_themes(self) -> List[Theme]:
        data = self.client.get(EndPoints.themes)
        return [Theme(x) for x in data]

    def find_theme_by_uuid(self, uuid: str) -> Theme:
        data = self.client.get(f"{EndPoints.themes}/{uuid}")
        return Theme(data)

    """
        Weapons
    """
    def get_weapons(self) -> List[Weapon]:
        data = self.client.get(EndPoints.weapons)
        return [Weapon(x) for x in data]

    def find_weapon_by_uuid(self, uuid: str) -> Weapon:
        data = self.client.get(f"{EndPoints.weapons}/{uuid}")
        return Weapon(data)

    def get_weapon_skins(self) -> List[WeaponSkin]:
        data = self.client.get(EndPoints.weapons_skins)
        return [WeaponSkin(x) for x in data]

    def find_weapon_skins_by_uuid(self, uuid: str) -> WeaponSkin:
        data = self.client.get(f"{EndPoints.weapons_skins}/{uuid}")
        return WeaponSkin(data)

    def get_weapon_skin_levels(self) -> List[WeaponSkinLevel]:
        data = self.client.get(EndPoints.weapons_skin_levels)
        return [WeaponSkinLevel(x) for x in data]

    def find_weapon_skin_levels_by_uuid(self, uuid: str) -> WeaponSkinLevel:
        data = self.client.get(f"{EndPoints.weapons_skin_levels}/{uuid}")
        return WeaponSkinLevel(data)

    def get_weapon_skinchromas(self) -> List[Chromas]:
        data = self.client.get(EndPoints.weapons_skinchromas)
        return [Chromas(x) for x in data]

    def find_weapon_skinchromas_by_uuid(self, uuid: str) -> Chromas:
        data = self.client.get(f"{EndPoints.weapons_skinchromas}/{uuid}")
        return Chromas(data)

    """
        Version
    """
    def get_version(self) -> Version:
        data = self.client.get(EndPoints.version)
        return Version(data)
