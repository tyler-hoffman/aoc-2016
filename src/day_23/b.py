from dataclasses import dataclass
from functools import cached_property
from src.day_23.parser import Parser
from src.day_23.solver import Solver
from src.shared.machine import Instruction, Machine

@dataclass
class Day23PartASolver(Solver):
    instructions: list[Instruction]

    @property
    def solution(self) -> int:
        a, b, c, d = 12, 0, 0, 0

        b = a - 1

        while b > 0:
            a *= b
            b -= 1
        
        c = 84
        d = 71

        a += c * d

        return a

        # b = a - 1

        # while b >= 0:
        #     a *= b
        #     b -= 1
        #     c = 2*b
        #     d = 0

        # c = 84
        # d = 71
        # a += c * d

        # return a

def solve(input: str) -> int:
    solver = Day23PartASolver(Parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_23/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
