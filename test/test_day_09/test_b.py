import unittest
from parameterized import parameterized

from src.day_09.b import solve


class TestDay09B(unittest.TestCase):
    @parameterized.expand(
        [
            ("(3x3)XYZ", len("XYZXYZXYZ")),
            ("X(8x2)(3x3)ABCY", len("XABCABCABCABCABCABCY")),
            ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
            ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
        ]
    )
    def test_solve(self, input: str, expected: str):
        self.assertEqual(solve(input), expected)
