import unittest

from src.day_05.b import solve


class TestDay05B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("abc"), "05ace8e3")
