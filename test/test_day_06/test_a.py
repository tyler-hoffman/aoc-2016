import unittest

from src.day_06.a import solve


SAMPLE_DATA = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"""


class TestDay06A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), "easter")

    def test_solution(self):
        with open("src/day_06/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), "tzstqsua")
