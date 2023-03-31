from api_sunrisesunset import SunriseSunset
from api_zippopotam import Zippopotam


class Place:
    def __init__(self):
        self.sunrise_sunset = SunriseSunset()
        self.zippopotam = Zippopotam()
        self.place_info = {}
        self.place_sun_information = {}

    def extract_apis_information(self, country, zip_code, date):
        if self.zippopotam.get_place_result(country, zip_code) == None:
            print('There is an error with Zippopotam API')
            self.place_info = None
            self.place_sun_information = None
            return
        self.place_info = self.zippopotam.place_info
        if self.sunrise_sunset.get_sun_rise_set(self.place_info['places'][0]['longitude'], self.place_info['places'][0]['latitude'], date) == None:
            print('There is an error with Sunrise-Sunset API')
            return
        self.sunrise_sunset.place_info['date'] = date
        self.place_sun_information = self.sunrise_sunset.place_info
        return True


    def display_output(self):
        if self.sunrise_sunset.check_status():
            print(f"On {self.place_sun_information['date']}, the sunrise and sunset times from {self.place_info['places'][0]['place name']} ({self.place_info['post code']}) in {self.place_info['places'][0]['state']}, {self.place_info['country']} were respectively at {self.place_sun_information['results']['sunrise']} and {self.place_sun_information['results']['sunset']} (UTC time)")
        else:
            raise Exception('There is an error with Sunrise-Sunset API')