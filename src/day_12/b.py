from src.day_12.machine import Instruction, Machine
from src.day_12.parser import Parser
from src.day_12.solver import Solver


class Day12PartBSolver(Solver):
    @property
    def solution(self) -> int:
        machine = Machine(
            instructions=self.instructions,
            registers={"a": 0, "b": 0, "c": 1, "d": 0},
        )
        machine.run()

        return machine.registers["a"]


def solve(input: str) -> int:
    instructions = Parser.parse(input)
    solver = Day12PartBSolver(instructions)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_12/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
