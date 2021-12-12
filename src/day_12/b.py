from dataclasses import dataclass
from functools import cached_property
from src.day_12.fibonacci import fibonacci_sequence


@dataclass
class Day12PartBSolver(object):
    do_setup: bool

    @property
    def solution(self) -> int:
        a = 1
        fibs = fibonacci_sequence()
        for _ in range(self.fib_count):
            a += next(fibs)
        a += 14 * 14
        return a

    @cached_property
    def fib_count(self) -> int:
        output = 26
        if self.do_setup:
            output += 7
        return output


def solve(do_setup: bool = True) -> int:
    solver = Day12PartBSolver(do_setup=do_setup)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_12/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
