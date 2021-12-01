import unittest

from src.shared.functions import frequency_map


class TestShared(unittest.TestCase):
    def test_frequency_map(self):
        input = ["a", "a", "a", "b", "c", "c"]
        mapped = frequency_map(input)
        self.assertEqual(
            mapped,
            {
                "a": 3,
                "b": 1,
                "c": 2,
            },
        )
