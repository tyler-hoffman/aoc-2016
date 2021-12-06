from dataclasses import dataclass
from typing import Set, Tuple
from src.day_10.parser import Parser
from src.day_10.solver import Solver


@dataclass
class Day10PartASolver(Solver):
    target_values: Set[int]

    @property
    def solution(self) -> int:
        for distribution in self.distribute_chips():
            if set(distribution.given) == self.target_values:
                return distribution.giver.id


def solve(input: str, values: Tuple[int, int]) -> int:
    parser = Parser()
    data = parser.parse(input)
    solver = Day10PartASolver(**data.__dict__, target_values=set(values))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_10/input.txt", "r") as f:
        input = f.read()
    print(solve(input, (61, 17)))
