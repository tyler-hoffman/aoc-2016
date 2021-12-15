from src.day_16.parser import Parser
from src.day_16.solver import Solver

class Day16PartASolver(Solver):
    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    parser = Parser()
    solver = Day16PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_16/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
