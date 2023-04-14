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
        self.machine.run()

        return self.machine.registers["a"]

    @cached_property
    def machine(self) -> Machine:
        return Machine(self.instructions, {"a": 7, "b": 0, "c": 0, "d": 0})


def solve(input: str) -> int:
    solver = Day23PartASolver(Parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_23/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
