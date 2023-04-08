from dataclasses import dataclass
from functools import cached_property
from typing import Mapping
from src.day_22.models import Node
from src.day_22.parser import Parser
from src.day_22.solver import Solver
from src.shared.point import Point


@dataclass
class Day22PartASolver(Solver):
    node_map: Mapping[Point, Node]

    @property
    def solution(self) -> int:
        return len(self.viable_pairs)

    @property
    def viable_pairs(self) -> set[tuple[Node, Node]]:
        output: set[tuple[Node, Node]] = set()
        for a in self.nodes:
            for b in self.nodes:
                if all([a != b, not a.empty, a.used <= b.avail, (b, a) not in output]):
                    output.add((a, b))
        return output

    @cached_property
    def nodes(self) -> list[Node]:
        return list(self.node_map.values())


def solve(input: str) -> int:
    solver = Day22PartASolver(Parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_22/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
