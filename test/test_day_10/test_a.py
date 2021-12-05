import unittest

from .sample_data import SAMPLE_DATA
from src.day_10.a import solve


class TestDay10A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA, (5, 2)), 2)
