import unittest

from src.day_13.b import solve


class TestDay13B(unittest.TestCase):
    def test_solve(self):
        secret = 1352
        self.assertEqual(solve(target=50, secret=secret), 135)
