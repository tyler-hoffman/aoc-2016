from more_itertools import nth
from src.day_14.solver import Solver


class Day14PartASolver(Solver):
    @property
    def solution(self) -> int:
        return nth(self.get_keys(), 63).index


def solve(salt: str) -> int:
    solver = Day14PartASolver(salt=salt.strip())

    return solver.solution


if __name__ == "__main__":
    with open("src/day_14/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
