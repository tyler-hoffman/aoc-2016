from itertools import islice
from src.day_18.parser import Parser
from src.day_18.solver import Solver

class Day18PartASolver(Solver):
    @property
    def solution(self) -> int:
        safe_count = 0
        for row in islice(self.rows(), self.row_count):
            safe_count += self.row_safe_count(row)
        return safe_count

def solve(input: str, length: int) -> int:
    first_row = Parser.parse(input)
    solver = Day18PartASolver(first_row=first_row, row_count=length)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_18/input.txt", "r") as f:
        input = f.read()
        print(solve(input, 40))
