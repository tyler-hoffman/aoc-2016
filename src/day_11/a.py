from dataclasses import dataclass

from src.day_11.parser import Parser
from src.day_11.solver import Solver


@dataclass
class Day11PartASolver(Solver):
    @property
    def solution(self) -> int:
        return self.determine_victory_time(self.start_state)


def solve(input: str) -> int:
    state = Parser.parse(input)
    solver = Day11PartASolver(start_state=state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_11/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
