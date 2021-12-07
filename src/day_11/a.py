from src.day_11.parser import Parser
from src.day_11.solver import Solver

class Day11PartASolver(Solver):
    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    parser = Parser()
    solver = Day11PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_11/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
