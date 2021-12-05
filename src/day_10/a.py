from src.day_05.parser import Parser
from src.day_05.solver import Solver

class Day10PartaSolver(Solver):
    pass

def solve(input: str) -> int:
    parser = Parser()
    solver = Day10PartaSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_10/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
