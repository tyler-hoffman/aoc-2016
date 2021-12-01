import dataclasses
from functools import cache, cached_property
import re
import string
from typing import Dict, List

from src.shared.functions import frequency_map

string.ascii_lowercase


@cache
def letter_indices() -> Dict[str, int]:
    output: Dict[str, int] = dict()
    for i, char in enumerate(string.ascii_lowercase):
        output[char] = i
    return output


@dataclasses.dataclass(frozen=True)
class Room(object):
    id: int
    parts: List[str]
    checksum: str

    @cached_property
    def characters(self) -> List[str]:
        output: List[str] = []
        for part in self.parts:
            for char in part:
                output.append(char)
        return output

    @cached_property
    def is_valid(self) -> bool:
        chars = frequency_map(self.characters)

        ordered = [k for k, _ in sorted(chars.items(), key=lambda x: (-x[1], x[0]))]

        return "".join(ordered[:5]) == self.checksum

    @cached_property
    def rotated_parts(self) -> str:
        return " ".join([self._rotate_part(part) for part in self.parts])

    def _rotate_part(self, part: str) -> str:
        rotated_characters: List[str] = []
        for char in part:
            index = letter_indices()[char]
            rotated_index = (index + self.id) % len(string.ascii_lowercase)
            rotated_characters.append(string.ascii_lowercase[rotated_index])

        return "".join(rotated_characters)


def parse_line(line: str) -> Room:
    parts = line.split("-")

    match = re.search("(\d+)\[(\w+)\]", parts[-1])
    assert match is not None

    return Room(id=int(match.group(1)), parts=parts[:-1], checksum=match.group(2))


def parse(input: str) -> List[Room]:
    return [parse_line(line) for line in input.splitlines() if line]
