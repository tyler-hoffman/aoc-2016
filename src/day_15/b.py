from src.day_15.models import Disk
from src.day_15.parser import Parser
from src.day_15.solver import Solver

class Day15PartBSolver(Solver):
    @property
    def solution(self) -> int:
        return -1


def solve(all_lines: str) -> int:
    disks = Parser.parse(all_lines)
    disks.append(Disk(positions=11, start=0, depth = disks[-1].depth + 1))
    solver = Solver(disks=disks)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_15/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
