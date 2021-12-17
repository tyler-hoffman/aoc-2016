from more_itertools import first
from src.day_17.parser import Parser
from src.day_17.solver import Solver


class Day17PartASolver(Solver):
    @property
    def solution(self) -> str:
        return first(self.get_paths())


def solve(input: str) -> str:
    passcode = Parser.parse(input)
    solver = Day17PartASolver(passcode=passcode)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_17/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
