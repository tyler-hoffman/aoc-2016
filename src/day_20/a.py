from src.day_20.parser import Parser
from src.day_20.solver import Solver

class Day20PartASolver(Solver):

    @property
    def solution(self) -> int:
        max_blocked = -1

        for ip in self.ordered_ips:
            if ip.start > max_blocked + 1:
                return max_blocked + 1
            else:
                max_blocked = max([max_blocked, ip.end])
        return max_blocked + 1


def solve(input: str) -> int:
    ips = Parser.parse(input)
    solver = Day20PartASolver(ips=ips)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_20/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
