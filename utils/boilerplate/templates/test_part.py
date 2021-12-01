TEST_PART_TEMPLATE = """
import unittest

from src.day_{day_string}.{part} import solve


class TestDay{day_string}{part_upper}(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(input), 1)

"""
