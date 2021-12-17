import unittest
from parameterized import parameterized

from src.day_17.a import solve


class TestDay17A(unittest.TestCase):
    @parameterized.expand([
        ('ihgpwlah', 'DDRRRD'),
        ('kglvqrro', 'DDUDRLRRUDRD'),
        ('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'),
    ])
    def test_solve(self, passcode: str, path: str):
        self.assertEqual(solve(passcode), path)

    def test_solution(self):
        with open("src/day_17/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), "DUDRLRRDDR")
