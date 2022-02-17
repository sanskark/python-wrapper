class EndPoints:
    """Stores the all endpoints of the Valorant API"""
    def __init__(self):
        self.base_url = "https://valorant-api.com/v1/"

        # agents
        self.agents = "agents"
        self.agent = "agents/{uuid}".format(uuid="{uuid}")

    def agents_url(self):
        return self.base_url + self.agents

    def agent_url(self):
        return self.base_url + self.agent
