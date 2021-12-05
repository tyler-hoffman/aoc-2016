TEST_PART_TEMPLATE = """
import unittest

from .sample_data import SAMPLE_DATA
from src.day_{day_string}.{part} import solve


class TestDay{day_string}{part_upper}(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1)

"""
