import requests


class API:
    def __init__(self):
        pass

    def call_get(self, url):
        response = requests.get(url)
        return response