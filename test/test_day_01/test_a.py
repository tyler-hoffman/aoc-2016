import unittest

from parameterized import parameterized
from src.day_01.a import solve


class TestDay01A(unittest.TestCase):
    @parameterized.expand(
        [
            ("R2, L3", 5),
            ("R2, R2, R2", 2),
            ("R5, L5, R5, R3", 12),
        ]
    )
    def test_solve(self, input: str, expected: int):
        self.assertEqual(solve(input), expected)

    def test_solution(self):
        input = open("src/day_01/input.txt", "r").read()
        self.assertEqual(solve(input), 226)
