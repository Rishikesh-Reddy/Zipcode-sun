import sys

from api import API


class SunriseSunset(API):
    def __init__(self):
        super().__init__()
        self.url = 'https://api.sunrise-sunset.org/json'
        self.place_info = {}

    def store_place_info(self, place):
        self.place_info = place

    def get_sun_rise_set(self, lat, lng, date):
        url = f'{self.url}?lat={lat}&lng={lng}&date={date}&formatted = 0'
        response = self.call_get(url)
        if response.status_code != 200:
            self.store_place_info(None)
            return
        self.store_place_info(response.json())
        return True

    def check_status(self):
        if self.place_info['status'] == "OK":
            return True
        else:
            return False