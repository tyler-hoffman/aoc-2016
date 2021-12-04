from typing import List
from src.day_06.shared import Solver, parse


class SolverB(Solver):
    def get_character_index(self, values: List[str]) -> str:
        return values.index(min(values))


def solve(input: str) -> str:
    lines = parse(input)
    return SolverB(lines).get_solution()


if __name__ == "__main__":
    with open("src/day_06/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
