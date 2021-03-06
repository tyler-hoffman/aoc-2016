import unittest

from parameterized import parameterized
from src.day_04.shared import parse_line


class TestDay04Shared(unittest.TestCase):
    @parameterized.expand(
        [
            ("aaaaa-bbb-z-y-x-123[abxyz]", True),
            ("a-b-c-d-e-f-g-h-987[abcde]", True),
            ("not-a-real-room-404[oarel]", True),
            ("totally-real-room-200[decoy]", False),
        ]
    )
    def test_is_valid(self, line: str, expected: bool):
        room = parse_line(line)
        self.assertEqual(room.is_valid, expected)

    def test_rotate(self):
        room = parse_line("qzmt-zixmtkozy-ivhz-343[wat]")
        self.assertEqual(room.rotated_parts, "very encrypted name")
