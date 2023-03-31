import unittest

from api_zippopotam import Zippopotam


class Test_Zippopotam(unittest.TestCase):

    def test_get_place_result(self):
        self.zip = Zippopotam()
        self.zip.get_place_result('us', 90210)
        self.assertEqual(self.zip.get_place_result('us', 90210), True, "Should be True")
        self.assertEqual(self.zip.place_info['country'], 'United States', "Should be United States")
        self.assertEqual(self.zip.place_info['places'][0]['longitude'], '-118.4065', "Should be -118.4065")
        self.assertEqual(self.zip.place_info['places'][0]['latitude'], '34.0901', "Should be 34.0901")
        self.assertEqual(self.zip.place_info['places'][0]['state'], 'California', "Should be California")
        self.assertEqual(self.zip.get_place_result('us', 00000), None, "Should be None")
        self.assertEqual(self.zip.place_info, None, "Should be None")
        

if __name__ == '__main__':
    unittest.main()