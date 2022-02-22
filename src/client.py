from requests import Session
from json import JSONDecodeError


class Client:
    def __init__(self):
        self.session = Session()

    def get(self, url: str):
        response = self.session.get(url)

        try:
            data = response.json()
        except JSONDecodeError:
            data = {'error': response.text}

        if response.status_code == 200:
            return data['data']
        else:
            return data
