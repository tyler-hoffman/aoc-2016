import dataclasses
from abc import ABC, abstractmethod
from typing import List

from src.shared.functions import frequency_map


@dataclasses.dataclass
class Solver(ABC):
    lines: List[str]

    @property
    def line_length(self) -> int:
        return len(self.lines[0])

    @abstractmethod
    def get_character_index(self, values: List[str]) -> str:
        ...

    def get_solution(self) -> str:
        output = ""
        for i in range(self.line_length):
            freqs = frequency_map(line[i] for line in self.lines)
            keys = list(freqs.keys())
            values = list(freqs.values())
            index = self.get_character_index(values)
            output += keys[index]
        return output


def parse(input: str) -> List[str]:
    return [line for line in input.splitlines() if line]
