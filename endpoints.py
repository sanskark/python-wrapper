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
        """
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

        # Version
        self.version = "version"
        """

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
        return self.base_url + self.buddies_levels

    def buddy_url(self):
        return self.base_url + self.buddy

    def buddy_level_url(self):
        return self.base_url + self.buddy_level

    """
        Bundles
    """
    def bundles_url(self):
        return self.base_url + self.bundles

    def bundle_url(self):
        return self.base_url + self.bundle

    """
        Ceremonies
    """
    def ceremonies_url(self):
        return self.base_url + self.ceremonies

    def ceremony_url(self):
        return self.base_url + self.ceremony

    """
        Competitive Tiers
    """
    def compitiers_url(self):
        return self.base_url + self.compi_tiers

    def compitier_url(self):
        return self.base_url + self.compi_tier

    """
        Content Tiers
    """
    def contenttiers_url(self):
        return self.base_url + self.content_tiers

    def contenttier_url(self):
        return self.base_url + self.content_tier

    """
        Contracts
    """
    def contracts_url(self):
        return self.base_url + self.contracts

    def contract_url(self):
        return self.base_url + self.contract

    """
        Events
    """
    def events_url(self):
        return self.base_url + self.events

    def event_url(self):
        return self.base_url + self.event

    """
        Game Modes and Equippables
    """
    def gamemodes_url(self):
        return self.base_url + self.gamemodes

    def gamemode_url(self):
        return self.base_url + self.gamemode

    def equips_url(self):
        return self.base_url + self.equips

    def equip_url(self):
        return self.base_url + self.equip

    """
        Gears
    """
    def gears_url(self):
        return self.base_url + self.gears

    def gear_url(self):
        return self.base_url + self.gear

    """
        Maps
    """
    def maps_url(self):
        return self.base_url + self.maps

    def map_url(self):
        return self.base_url + self.map

    """
        Player Cards
    """
    def player_cards_url(self):
        return self.base_url + self.player_cards

    def player_card_url(self):
        return self.base_url + self.player_card

    """
        Player Titles
    """
    def player_titles_url(self):
        return self.base_url + self.player_titles

    def player_title_url(self):
        return self.base_url + self.player_title

    """
        Seasons and Competitive Seasons
    """
    def seasons_url(self):
        return self.base_url + self.seasons

    def season_url(self):
        return self.base_url + self.season

    def comp_seasons_url(self):
        return self.base_url + self.comp_seasons

    def comp_season_url(self):
        return self.base_url + self.comp_season

    """
        Sprays and its Levels
    """
    def sprays_url(self):
        return self.base_url + self.sprays

    def spray_url(self):
        return self.base_url + self.spray

    def sprays_levels_url(self):
        return self.base_url + self.sprays_levels

    def spray_level_url(self):
        return self.base_url + self.spray_level
