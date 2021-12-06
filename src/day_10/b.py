from dataclasses import dataclass
from src.day_10.parser import Parser
from src.day_10.solver import Solver


@dataclass
class Day10PartBSolver(Solver):
    @property
    def solution(self) -> int:
        for _ in self.distribute_chips():
            pass

        product = 1
        for value in [
            output.value for output in self.outputs if output.id in {0, 1, 2}
        ]:
            product *= value
        return product


def solve(input: str) -> int:
    parser = Parser()
    data = parser.parse(input)
    solver = Day10PartBSolver(**data.__dict__)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_10/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
