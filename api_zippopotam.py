from api import API


class Zippopotam:
    def __init__(self):
        super().__init__()
        self.url = 'https://api.zippopotam.us/'
        self.place_info = {}
        self.api = API()

    def store_place_info(self, place):
        self.place_info = place

    def get_place_result(self, country, zip_code):
        url = f'{self.url}{country}/{zip_code}'
        response = self.api.call_get(url)
        if response.status_code != 200:
            self.store_place_info(None)
            return
        self.store_place_info(response.json())
        return True