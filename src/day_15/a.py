from dataclasses import dataclass
from src.day_15.models import Disk
from src.day_15.parser import Parser
from src.day_15.solver import Solver


@dataclass
class Day15PartASolver(Solver):
    disks: list[Disk]

    @property
    def solution(self) -> int:
        t = 0
        multiplier = 1
        for disk in self.disks:
            while (t + disk.superimposed_start) % disk.positions:
                t += multiplier
            multiplier *= disk.positions

        return t


def solve(all_lines: str) -> int:
    disks = Parser.parse(all_lines)
    solver = Day15PartASolver(disks=disks)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_15/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
