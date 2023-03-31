import unittest

from api_sunrisesunset import SunriseSunset


class Test_SunriseSet_api(unittest.TestCase):

    def test_api(self):
        self.srs = SunriseSunset()
        self.assertEqual(self.srs.get_sun_rise_set(-118.4065, 34.0901, '2022-01-10'), True, "Should be True")
        self.assertEqual(self.srs.check_status(), True, "Should be True")
        self.assertEqual(self.srs.place_info['results']['sunrise'], '7:19:06 AM', "Should be 7:19:06 AM")
        self.assertEqual(self.srs.place_info['results']['sunset'], '12:23:07 PM', "Should be 12:23:07 PM")
        self.assertEqual(self.srs.place_info['results']['day_length'], '05:04:01', "Should be 05:04:01")
        self.assertEqual(self.srs.get_sun_rise_set(0, 0, '2022-01-41'), None, "Should be None")
        self.assertEqual(self.srs.place_info, None, "Should be None")



if __name__ == '__main__':
    unittest.main()