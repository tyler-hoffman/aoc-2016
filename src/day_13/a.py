from dataclasses import dataclass
from src.day_13.solver import Solver
from src.shared.point import Point


@dataclass
class Day13PartASolver(Solver):
    goal: Point

    @property
    def solution(self) -> int:
        discoveries = self.board.discover()
        while True:
            data = next(discoveries)
            if data.point == self.goal:
                return data.steps


def solve(goal: Point, secret: int) -> int:
    solver = Day13PartASolver(goal=goal, secret=secret)

    return solver.solution


if __name__ == "__main__":
    goal = Point(x=31, y=39)
    secret = 1352
    print(solve(goal, secret))
