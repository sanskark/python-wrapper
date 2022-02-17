"""
    A python class that allows access to all of the functionality of
    the valorant-api(not an official API)

    This API allows a developer to build applications around the
    valorant-api without having deal with accessing and managing
    the requests and responses
"""


class EndPoints:
    """
        The class will handle of the endpoints. The purpose of this
        class is to store and serve all endpoint strings useful to
        the valorant-api .

        There is no processing of the endpoints int this class all of
        that logic is handles by ValorantAPI class
    """
    def __init__(self):
        self.base_url = "https://valorant-api.com/v1/"

        # Agents
        self.agents = "agents"
        self.agent = "agents/{uuid}".format(uuid="{uuid}")

        # Buddies
        self.buddies = "buddies"
        self.buddies_levels = "buddies/levels"

        self.buddy = "buddies/{uuid}".format(uuid="{uuid}")
        self.buddy_level = "buddies/levels/{uuid}".format(uuid="{uuid}")

        # Bundles
        self.bundles = "bundles"
        self.bundle = "bundles/{uuid}".format(uuid="{uuid}")

        # Ceremonies
        self.ceremonies = "ceremonies"
        self.ceremony = "ceremonies/{uuid}".format(uuid="{uuid}")

        # Competitive Tiers
        self.compi_tiers = "competitivetiers"
        self.compi_tier = "competitivetiers/{uuid}".format(uuid="{uuid}")

        # Content Tiers
        self.content_tiers = "contenttiers"
        self.content_tier = "contenttiers/{uuid}".format(uuid="{uuid}")

        # Contracts
        self.contracts = "contracts"
        self.contract = "contracts/{uuid}".format(uuid="{uuid}")

        # Currencies
        self.currencies = "currencies"
        self.currency = "currencies/{uuid}".format(uuid="{uuid}")

        # Events
        self.events = "events"
        self.event = "events/{uuid}".format(uuid="{uuid}")

        # Game Modes and its Equippables
        self.gamemodes = "gamemodes"
        self.gamemode = "gamemodes/{uuid}".format(uuid="{uuid}")
        self.equips = "gamemodes/equippables"
        self.equip = "gamemodes/equippables/{uuid}".format(uuid="{uuid}")

        # Gears
        self.gears = "gear"
        self.gear = "gear/{uuid}".format(uuid="{uuid}")

        # Maps
        self.maps = "maps"
        self.map = "maps/{uuid}".format(uuid="{uuid}")

        # Player Cards
        self.player_cards = "playercards"
        self.player_card = "playercards/{uuid}".format(uuid="{uuid}")

        # Player Titles
        self.player_titles = "playertitles"
        self.player_title = "playertitles/{uuid}".format(uuid="{uuid}")

        # Seasons and Competitive Seasons
        self.seasons = "seasons"
        self.season = "seasons/{uuid}".format(uuid="{uuid}")
        self.comp_seasons = "seasons/competitive"
        self.comp_season = "seasons/competitive/{uuid}".format(uuid="{uuid}")

        # Spray and its Levels
        self.sprays = "sprays"
        self.spray = "sprays/{uuid}".format(uuid="{uuid}")
        self.sprays_levels = "sprays/levels"
        self.spray_level = "sprays/levels/{uuid}".format(uuid="{uuid}")

        # Themes
        self.themes = "themes"
        self.theme = "themes/{uuid}".format(uuid="{uuid}")

        # Weapons, Skins, Chromas and Levels
        self.weapons = "weapons"
        self.weapon = "weapons/{uuid}".format(uuid="{uuid}")
        self.skins = "weapons/skins"
        self.skin = "weapons/skins/{uuid}".format(uuid="{uuid}")
        self.skins_chromas = "weapons/skinchromas"
        self.skin_chroma = "weapons/skinchromas/{uuid}".format(uuid="{uuid}")
        self.skins_levels = "weapons/levels"
        self.skin_level = "weapons/levels/{uuid}".format(uuid="{uuid}")

        self.version = "version"

    """
        Agents
    """
    def agents_url(self):
        """Combines the request endpoint and agents API URLs"""
        return self.base_url + self.agents

    def agent_url(self):
        """Combines the request endpoint and agent API URLs"""
        return self.base_url + self.agent

    """
        Buddies
    """
    def buddies_url(self):
        """Combines the request endpoint and buddies API URLs"""
        return self.base_url + self.buddies

    def buddies_levels_url(self):
        """Combines the request endpoint and buddy levels API URLs"""
        return self.base_url + self.buddies_levels

    def buddy_url(self):
        """Combines the request endpoint and buddy API URLs"""
        return self.base_url + self.buddy

    def buddy_level_url(self):
        """Combines the request endpoint and buddy level API URLs"""
        return self.base_url + self.buddy_level

    """
        Bundles
    """
    def bundles_url(self):
        """Combines the request endpoint and bundles API URLs"""
        return self.base_url + self.bundles

    def bundle_url(self):
        """Combines the request endpoint and bundle API URLs"""
        return self.base_url + self.bundle

    """
        Ceremonies
    """
    def ceremonies_url(self):
        """Combines the request endpoint and ceremonies API URLs"""
        return self.base_url + self.ceremonies

    def ceremony_url(self):
        """Combines the request endpoint and ceremony API URLs"""
        return self.base_url + self.ceremony

    """
        Competitive Tiers
    """
    def compitiers_url(self):
        """Combines the request endpoint and competitive tiers API URLs"""
        return self.base_url + self.compi_tiers

    def compitier_url(self):
        """Combines the request endpoint and competitive tier API URLs"""
        return self.base_url + self.compi_tier

    """
        Content Tiers
    """
    def content_tiers_url(self):
        """Combines the request endpoint and content tiers API URLs"""
        return self.base_url + self.content_tiers

    def content_tier_url(self):
        """Combines the request endpoint and content tier API URLs"""
        return self.base_url + self.content_tier

    """
        Contracts
    """
    def contracts_url(self):
        """Combines the request endpoint and contracts API URLs"""
        return self.base_url + self.contracts

    def contract_url(self):
        """Combines the request endpoint and contract API URLs"""
        return self.base_url + self.contract

    """
        Events
    """
    def events_url(self):
        """Combines the request endpoint and events API URLs"""
        return self.base_url + self.events

    def event_url(self):
        """Combines the request endpoint and event API URLs"""
        return self.base_url + self.event

    """
        Game Modes and Equippables
    """
    def gamemodes_url(self):
        """Combines the request endpoint and Game Modes API URLs"""
        return self.base_url + self.gamemodes

    def gamemode_url(self):
        """Combines the request endpoint and Game Mode API URLs"""
        return self.base_url + self.gamemode

    def equips_url(self):
        """Combines the request endpoint and Game mode equipments API URLs"""
        return self.base_url + self.equips

    def equip_url(self):
        """Combines the request endpoint and Game mode equipment API URLs"""
        return self.base_url + self.equip

    """
        Gears
    """
    def gears_url(self):
        """Combines the request endpoint and Gears API URLs"""
        return self.base_url + self.gears

    def gear_url(self):
        """Combines the request endpoint and Gear API URLs"""
        return self.base_url + self.gear

    """
        Maps
    """
    def maps_url(self):
        """Combines the request endpoint and Maps API URLs"""
        return self.base_url + self.maps

    def map_url(self):
        """Combines the request endpoint and map API URLs"""
        return self.base_url + self.map

    """
        Player Cards
    """
    def player_cards_url(self):
        """Combines the request endpoint and Player Cards API URLs"""
        return self.base_url + self.player_cards

    def player_card_url(self):
        """Combines the request endpoint and Player card API URLs"""
        return self.base_url + self.player_card

    """
        Player Titles
    """
    def player_titles_url(self):
        """Combines the request endpoint and player titles API URLs"""
        return self.base_url + self.player_titles

    def player_title_url(self):
        """Combines the request endpoint and player title API URLs"""
        return self.base_url + self.player_title

    """
        Seasons and Competitive Seasons
    """
    def seasons_url(self):
        """Combines the request endpoint and Seasons API URLs"""
        return self.base_url + self.seasons

    def season_url(self):
        """Combines the request endpoint and season API URLs"""
        return self.base_url + self.season

    def comp_seasons_url(self):
        """Combines the request endpoint and competitive seasons API URLs"""
        return self.base_url + self.comp_seasons

    def comp_season_url(self):
        """Combines the request endpoint and competitive season API URLs"""
        return self.base_url + self.comp_season

    """
        Sprays and its Levels
    """
    def sprays_url(self):
        """Combines the request endpoint and Sprays API URLs"""
        return self.base_url + self.sprays

    def spray_url(self):
        """Combines the request endpoint and spray API URLs"""
        return self.base_url + self.spray

    def sprays_levels_url(self):
        """Combines the request endpoint and sprays levels API URLs"""
        return self.base_url + self.sprays_levels

    def spray_level_url(self):
        """Combines the request endpoint and spray level API URLs"""
        return self.base_url + self.spray_level

    """
        Themes
    """
    def themes_url(self):
        """Combines the request endpoint and themes API URLs"""
        return self.base_url + self.themes

    def theme_url(self):
        """Combines the request endpoint and themes API URLs"""
        return self.base_url + self.theme

    """
        Weapons
    """
    def weapons_url(self):
        """Combines the request endpoint and weapons API URLs"""
        return self.base_url + self.weapons

    def weapon_url(self):
        """Combines the request endpoint and weapons API URLs"""
        return self.base_url + self.weapon

    def skins_url(self):
        """Combines the request endpoint and skins API URLs"""
        return self.base_url + self.skins

    def skin_url(self):
        """Combines the request endpoint and skin API URLs"""
        return self.base_url + self.skin

    def skins_levels_url(self):
        """Combines the request endpoint and skins levels API URLs"""
        return self.base_url + self.skins_levels

    def skin_level_url(self):
        """Combines the request endpoint and skin level API URLs"""
        return self.base_url + self.skin_level

    def skins_chromas_url(self):
        """Combines the request endpoint and skins chromas API URLs"""
        return self.base_url + self.skins_chromas

    def skin_chroma_url(self):
        """Combines the request endpoint and skin chroma API URLs"""
        return self.base_url + self.skin_chroma

    """
        Version of the API
    """
    def version_url(self):
        """Combines the request endpoint and version of the API URLs"""
        return self.base_url + self.version
