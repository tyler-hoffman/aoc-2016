from dataclasses import dataclass

from more_itertools.more import chunked
from src.day_16.solver import Solver


def solve(initial_state: str, disk_size: int = 272) -> int:
    initial_state = initial_state.strip()
    solver = Solver(disk_size=disk_size, initial_state=initial_state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_16/input.txt", "r") as f:
        initial_state = f.read()
        print(solve(initial_state))
