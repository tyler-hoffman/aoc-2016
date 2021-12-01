import dataclasses
import re
from typing import List

from src.shared.functions import frequency_map



@dataclasses.dataclass
class Room(object):
    id: int
    characters: List[str]
    checksum: str

    @property
    def is_valid(self) -> bool:
        chars = frequency_map(self.characters)

        ordered = [k for k, _ in sorted(chars.items(), key=lambda x: (-x[1], x[0]))]

        return "".join(ordered[:5]) == self.checksum

def parse_line(line: str) -> Room:
    parts = line.split("-")
    characters: List[str] = []
    for part in parts[:-1]:
        characters = characters + list(part)

    match = re.search("(\d+)\[(\w+)\]", parts[-1])
    assert match is not None

    return Room(id=int(match.group(1)), characters=characters, checksum=match.group(2))

def parse(input: str) -> List[Room]:
    return [parse_line(line) for line in input.splitlines() if line]
