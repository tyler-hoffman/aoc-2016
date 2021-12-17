from more_itertools import last
from src.day_17.parser import Parser
from src.day_17.solver import Solver

class Day17PartBSolver(Solver):
    @property
    def solution(self) -> int:
        return len(last(self.get_paths()))


def solve(input: str) -> int:
    passcode = Parser.parse(input)
    solver = Day17PartBSolver(passcode=passcode)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_17/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
