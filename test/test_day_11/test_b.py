import unittest

from .sample_data import SAMPLE_DATA
from src.day_11.b import solve


class TestDay11B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1)
