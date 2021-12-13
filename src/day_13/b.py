from dataclasses import dataclass
from src.day_13.solver import Solver
from src.shared.point import Point

@dataclass
class Day13PartbSolver(Solver):
    target: int

    @property
    def solution(self) -> int:
        discoveries = self.board.discover()
        count = 0
        while next(discoveries).steps <= self.target:
            count += 1
        return count


def solve(target: int, secret: int) -> int:
    solver = Day13PartbSolver(target=target, secret=secret)

    return solver.solution


if __name__ == "__main__":
    target = 50
    secret = 1352
    print(solve(target, secret))
