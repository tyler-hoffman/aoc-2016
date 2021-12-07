PART_TEMPLATE = """
from src.day_{day_string}.parser import Parser
from src.day_{day_string}.solver import Solver

class Day{day_string}Part{part_upper}Solver(Solver):
    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    parser = Parser()
    solver = Day{day_string}Part{part_upper}Solver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_{day_string}/input.txt", "r") as f:
        input = f.read()
    print(solve(input))

"""
