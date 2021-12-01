import unittest

from src.day_04.a import solve

SAMPLE_DATA = """
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""


class TestDay04A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1514)

    def test_solution(self):
        with open("src/day_04/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 185371)
