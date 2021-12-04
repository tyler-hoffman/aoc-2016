from typing import List
from src.day_06.shared import Solver, parse


class SolverA(Solver):
    def get_character_index(self, values: List[str]) -> str:
        return values.index(max(values))

def solve(input: str) -> str:
    lines = parse(input)
    return SolverA(lines).get_solution()

if __name__ == "__main__":
    with open("src/day_06/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
