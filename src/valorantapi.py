from .endpoints import EndPoints

from .data_classes.agent import Agent
from .data_classes.buddy import Buddy


from .client import Client
from typing import List


class ValorantApi:
    def __init__(self):
        self.client = Client()

    def get_agents(self) -> List[Agent]:
        data = self.client.get(EndPoints.agents)
        return [Agent(x) for x in data]

    def find_agent_by_uuid(self, uuid: str):
        data = self.client.get(f"{EndPoints.agents}/{uuid}")
        return Agent(data)

    def get_buddies(self) -> List[Buddy]:
        data = self.client.get(EndPoints.buddies)
        return [Buddy(x) for x in data]

    def find_buddy_by_uuid(self, uuid: str):
        data = self.client.get(f"{EndPoints.buddies}/{uuid}")
        return Buddy(data)


