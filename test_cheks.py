import unittest

from checks import check_arguments, check_date


class CheckTest(unittest.TestCase):

    def test_check_args(self):
        self.assertEqual(check_arguments(['main.py']), False, "Should be False")
        self.assertEqual(check_arguments(['main.py', '2022-01-10', 90210, 'us']), True, "Should be True")
        self.assertEqual(check_arguments(['main.py', '2022-01-10', 90210, 'us', 'extra']), False, "Should be False")
        self.assertEqual(check_arguments(['main.py', '2022-01-10', 90210]), False, "Should be False")


    def test_check_date(self):
        self.assertEqual(check_date('2022-01-10'), True, "Should be True")
        self.assertEqual(check_date('2022-01-10-10'), False, "Should be False")

if __name__ == '__main__':
    unittest.main()