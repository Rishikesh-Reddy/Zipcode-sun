import unittest

from places import Place


class Test_Place(unittest.TestCase):

    def test_api(self):
        self.place = Place()
        self.assertEqual(self.place.extract_apis_information('us', '90210', '2022-01-10'), True, "Should be True")
        self.assertEqual(self.place.place_info['places'][0]['place name'], 'Beverly Hills', "Should be Beverly Hills")
        self.assertEqual(self.place.place_info['places'][0]['state'], 'California', "Should be California")
        self.assertEqual(self.place.place_info['places'][0]['longitude'], '-118.4065', "Should be -118.4065")
        self.assertEqual(self.place.place_info['places'][0]['latitude'], '34.0901', "Should be 34.0901")
        self.assertEqual(self.place.place_sun_information['results']['sunrise'], '7:19:06 AM', "Should be 7:19:06 AM")
        self.assertEqual(self.place.place_sun_information['results']['sunset'], '12:23:07 PM', "Should be 12:23:07 PM")
        self.assertEqual(self.place.place_sun_information['results']['day_length'], '05:04:01', "Should be 05:04:01")
        self.assertEqual(self.place.place_sun_information['date'], '2022-01-10', "Should be 2022-01-10")
        self.assertEqual(self.place.extract_apis_information('us', '90215', '2022-01-10'), None, "Should be None")
        self.assertEqual(self.place.place_info, None, "Should be None")
        self.assertEqual(self.place.place_sun_information, None, "Should be None")

if __name__ == '__main__':
    unittest.main()