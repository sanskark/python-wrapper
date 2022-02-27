from datetime import datetime


class Version:
    def __init__(self, data: dict):
        self.manifest_id: str = data.get("manifestId")
        self.branch: str = data.get("branch")
        self.version: str = data.get("version")
        self.build_version: int = data.get("buildVersion")
        self.riot_client_version: str = data.get("riotClientVersion")
        self.build_date: datetime = data.get("buildDate")
