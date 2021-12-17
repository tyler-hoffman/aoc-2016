from parameterized import parameterized
import unittest

from src.day_18.parser import Parser

from .sample_data import MEDIUM_INPUT, MEDIUM_ROWS, MEDIUM_SAFE_COUNT, SMALL_INPUT, SMALL_ROWS, SMALL_SAFE_COUNT
from src.day_18.a import solve


class TestDay18A(unittest.TestCase):
    @parameterized.expand([
        (SMALL_INPUT, SMALL_ROWS, SMALL_SAFE_COUNT),
        (MEDIUM_INPUT, MEDIUM_ROWS, MEDIUM_SAFE_COUNT),
    ])
    def test_solve(self, input: str, row_count: int, safe_count: int):
        self.assertEqual(solve(input, row_count), safe_count)

    def test_solution(self):
        with open("src/day_18/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input, 40), 1957)
