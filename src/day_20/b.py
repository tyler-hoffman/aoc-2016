from dataclasses import dataclass, field
from src.day_20.parser import Parser
from src.day_20.solver import Solver


@dataclass
class Day20PartBSolver(Solver):
    tippy_top: int

    @property
    def solution(self) -> int:
        max_blocked = -1

        count = 0
        for ip in self.ordered_ips:
            if ip.start > max_blocked:
                count += ip.start - max_blocked - 1
                max_blocked = ip.end
            else:
                max_blocked = max([max_blocked, ip.end])
        count += self.tippy_top - max_blocked
        return count


def solve(input: str, tippy_top: int = 4294967295) -> int:
    ips = Parser.parse(input)
    solver = Day20PartBSolver(ips=ips, tippy_top=tippy_top)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_20/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
