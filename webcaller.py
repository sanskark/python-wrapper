from endpoints import EndPoints
import requests
import json


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
        """Returns the all agents data"""
        return self.__get_data(self.url.agents_url())

    def get_agent_by_uuid(self, uuid):
        """Return the specific agent by uuid"""
        return self.__get_data(self.url.agent_url().format(uuid=str(uuid)))

    # def get_agent_by_name(self, name):

