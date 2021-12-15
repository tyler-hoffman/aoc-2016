from dataclasses import dataclass
from src.day_15.models import Disk
from src.day_15.parser import Parser
from src.day_15.solver import Solver


def solve(all_lines: str) -> int:
    disks = Parser.parse(all_lines)
    solver = Solver(disks=disks)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_15/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
