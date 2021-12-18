import unittest

from src.day_19.b import solve


class TestDay19B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("5"), 2)
