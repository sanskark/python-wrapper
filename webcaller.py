from endpoints import EndPoints
import requests


class ValorantAPI:
    def __init__(self):
        self.url = EndPoints()
        self.format = "json"

    def __to_json_format(self, response):
        if self.format == "json":
            return response.json()
        return response.json()

    def __get_data(self, url):
        return self.__to_json_format(requests.get(url))

    def get_agents(self):
        """Returns data and assets of all agents and their abilities"""
        return self.__get_data(self.url.agents_url())

    def get_agent_by_uuid(self, uuid):
        """Returns data and assets of the requested agent"""
        return self.__get_data(self.url.agent_url().format(uuid=str(uuid)))

    def get_agent_by_name(self, name, is_playable=True):
        """Return the specific agent by name"""
        agents_data = list(self.__get_data(self.url.agents_url())['data'])

        uuid = None
        for agent in agents_data:
            """Iterate Over through all agents data list and find particular one"""
            agent_dict = dict(agent)
            display_name = agent_dict.get('displayName').lower()
            cur_uuid = agent_dict.get('uuid')

            if is_playable:
                if display_name == name.lower() and agent_dict.get('isPlayableCharacter'):
                    uuid = cur_uuid
                    break
            else:
                if display_name.lower() == name.lower():
                    uuid = agent_dict.get('uuid')
                    break

        if uuid is not None:
            return self.__get_data(self.url.agent_url().format(uuid=str(uuid)))
        return None

    def get_buddies(self):
        """Returns data and assets of all weapon buddies"""
        return self.__get_data(self.url.buddies_url())

    def get_buddy_levels(self):
        """Returns data and assets of all weapon buddy levels"""
        return self.__get_data(self.url.buddies_levels_url())

    def get_buddy_by_uuid(self, uuid: str):
        """Returns data and assets of the requested weapon buddy"""
        return self.__get_data(self.url.buddy_url().format(uuid=str(uuid)))

    def get_buddy_level_by_uuid(self, uuid: str):
        """Returns data and assets of the requested weapon buddy level"""
        return self.__get_data(self.url.buddy_level_url().format(uuid=str(uuid)))

    def get_bundles(self):
        """Returns data and assets of all bundles"""
        return self.__get_data(self.url.bundles_url())

    def get_bundle_by_uuid(self, uuid):
        """Returns data and assets of the requested bundle"""
        return self.__get_data(self.url.bundle_url().format(uuid=uuid))

    def get_ceremonies(self):
        """Returns data and assets of all ceremonies(ACE, CLOSER, CLUTCH, FLAWLESS, TEAM ACE, THRIFTY)"""
        return self.__get_data(self.url.ceremonies_url())

    def get_ceremony_by_uuid(self, uuid):
        """Returns data and assets of the requested ceremony"""
        return self.__get_data(self.url.ceremony_url().format(uuid=uuid))

    def get_compitiers(self):
        """Returns data and assets of all competitive tiers(IRON, BRONZE, SILVER and so on..)"""
        return self.__get_data(self.url.compitiers_url())

    def get_compitiers_by_uuid(self, uuid):
        """Returns data and assets the requested competitive tier table(IRON, BRONZE, SILVER and so on..)"""
        return self.__get_data(self.url.compitier_url().format(uuid=uuid))

    def get_content_tiers(self):
        """Returns data and assets of all content tiers(Deluxe, Exclusive, Premium, Select, Ultra)"""
        return self.__get_data(self.url.content_tiers_url())

    def get_content_tier_by_uuid(self, uuid):
        """Returns data and assets the requested content tier(Deluxe, Exclusive, Premium, Select, Ultra)"""
        return self.__get_data(self.url.content_tier_url().format(uuid=uuid))

    def get_contracts(self):
        """Returns data and assets of all contracts"""
        return self.__get_data(self.url.contracts_url())

    def get_contract_by_uuid(self, uuid):
        """Returns data and assets the requested contract"""
        return self.__get_data(self.url.contract_url().format(uuid=uuid))

    def get_events(self):
        """Returns data and assets of all events"""
        return self.__get_data(self.url.events_url())

    def get_event_by_uuid(self, uuid):
        """Returns data and assets the requested event"""
        return self.__get_data(self.url.event_url().format(uuid=uuid))

    def get_gamemodes(self):
        """Returns data and assets of all gamemodes"""
        return self.__get_data(self.url.gamemodes_url())

    def get_gamemode_by_uuid(self, uuid):
        """Returns data and assets the requested gamemode"""
        return self.__get_data(self.url.gamemode_url().format(uuid=uuid))

    def get_equips(self):
        """Returns data and assets of all gamemodes equippables(Classic or Golden Gun)"""
        return self.__get_data(self.url.equips_url())

    def get_equip_by_uuid(self, uuid):
        """Returns data and assets the requested gamemode equippables(Classic or Golden Gun)"""
        return self.__get_data(self.url.equip_url().format(uuid=uuid))

    def get_gears(self):
        """Returns data and assets of all Gears(Heavy Shields or Light Shields)"""
        return self.__get_data(self.url.gears_url())

    def get_gear_by_uuid(self, uuid):
        """Returns data and assets the requested gear(Heavy Shields or Light Shields)"""
        return self.__get_data(self.url.gear_url().format(uuid=uuid))

    def get_maps(self):
        """Returns data and assets of all Maps"""
        return self.__get_data(self.url.maps_url())

    def get_map_by_uuid(self, uuid):
        """Returns data and assets the requested map"""
        return self.__get_data(self.url.map_url().format(uuid=uuid))

    def get_player_cards(self):
        """Returns data and assets of all player cards"""
        return self.__get_data(self.url.player_cards_url())

    def get_player_card_by_uuid(self, uuid):
        """Returns data and assets of the requested player card"""
        return self.__get_data(self.url.player_card_url().format(uuid=uuid))

    def get_player_titles(self):
        """Returns data and assets of all player titles"""
        return self.__get_data(self.url.player_titles_url())

    def get_player_title_by_uuid(self, uuid):
        """Returns data and assets of the requested player title"""
        return self.__get_data(self.url.player_title_url().format(uuid=uuid))

    def get_seasons(self):
        """Returns data of all seasons"""
        return self.__get_data(self.url.seasons_url())

    def get_season_by_uuid(self, uuid):
        """Returns data of the requested season"""
        return self.__get_data(self.url.season_url().format(uuid=uuid))

    def get_comp_seasons(self):
        """Returns data of all competitive seasons"""
        return self.__get_data(self.url.comp_seasons_url())

    def get_comp_season_by_uuid(self, uuid):
        """Returns data of the requested competitive season"""
        return self.__get_data(self.url.comp_season_url().format(uuid=uuid))

    def get_sprays(self):
        """Returns data and assets of all sprays"""
        return self.__get_data(self.url.sprays_url())

    def get_spray_by_uuid(self):
        """Returns data and assets of the requested spray"""
        return self.__get_data(self.url.spray_url())

    def get_sprays_levels(self):
        """Returns data and assets of all spray levels"""
        return self.__get_data(self.url.sprays_levels_url())

    def get_spray_level_by_uuid(self):
        """Returns data and assets of the requested spray level"""
        return self.__get_data(self.url.spray_level_url())

    def get_themes(self):
        """Returns data and assets of all Themes"""
        return self.__get_data(self.url.themes_url())

    def get_theme_by_uuid(self, uuid):
        """Returns data and assets the requested theme"""
        return self.__get_data(self.url.theme_url().format(uuid=uuid))

    def get_weapons(self):
        """Returns data and assets of all Weapons"""
        return self.__get_data(self.url.weapons_url())

    def get_weapon_by_uuid(self, uuid):
        """Returns data and assets the requested weapon"""
        return self.__get_data(self.url.weapon_url().format(uuid=uuid))

    def get_skins(self):
        """Returns data and assets of all Skins"""
        return self.__get_data(self.url.skins_url())

    def get_skin_by_uuid(self, uuid):
        """Returns data and assets the requested skin"""
        return self.__get_data(self.url.skin_url().format(uuid=uuid))

    def get_skins_levels(self):
        """Returns data and assets of all Skins levels"""
        return self.__get_data(self.url.skins_levels_url())

    def get_skin_level_by_uuid(self):
        """Returns data and assets of the requested skin level"""
        return self.__get_data(self.url.skin_level_url())

    def get_skins_chromas(self):
        """Returns data and assets of all weapon skin chromas"""
        return self.__get_data(self.url.skins_chromas_url())

    def get_skins_chromas_by_uuid(self):
        """Returns data and assets of the requested weapon skin chromas"""
        return self.__get_data(self.url.skin_chroma_url())

    def get_current_version(self):
        """Returns data of the current manifest & version the API is running on"""
        return self.__get_data(self.url.version_url())
