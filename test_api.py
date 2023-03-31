import unittest

from api import API


class Test_API(unittest.TestCase):
    

    def test_call_get(self):
        self.api = API()
        self.assertEqual(self.api.call_get('https://zippopotam.us/us/90210').status_code, 200, "Should be 200")
        self.assertEqual(self.api.call_get('https://zippopotam.us/us/90215').status_code, 404, "Should be 404")

if __name__ == '__main__':
    unittest.main()