from dataclasses import dataclass
from src.day_11.parser import Parser
from src.day_11.solver import Solver

@dataclass
class Day11PartASolver(Solver):
    @property
    def solution(self) -> int:
        elements = self.all_elements
        return -1


def solve(input: str) -> int:
    state = Parser.parse(input)
    solver = Day11PartASolver(state=state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_11/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
