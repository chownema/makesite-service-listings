import unittest
import sys
import makesite


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_params(self):
        makesite.build_site()


if __name__ == '__main__':
        unittest.main()
