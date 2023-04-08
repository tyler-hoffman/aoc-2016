from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property
from typing import Iterator, Mapping
from src.day_22.models import Node
from src.day_22.parser import Parser
from src.day_22.solver import Solver
from src.shared.point import Point


@dataclass
class Move:
    start: Point
    end: Point
    amt: int

    @property
    def reverse(self) -> Move:
        return Move(start=self.end, end=self.start, amt=self.amt)


@dataclass
class Day22PartBSolver(Solver):
    node_map: Mapping[Point, Node]

    @property
    def solution(self) -> int:
        data_pos = self.target_coord
        current_node = self.find_the_only_empty_node()
        max_depth = 1
        while True:
            max_depth *= 2
            print(max_depth)
            fewest_steps = self.solve_for_remaining_depth(
                pos=current_node.coords,
                data_pos=data_pos,
                moves_so_far=[],
                remaining_depth=max_depth,
            )
            as_set = set(fewest_steps)
            if len(as_set) > 0:
                return min(as_set)

    def solve_for_remaining_depth(
        self,
        pos: Point,
        data_pos: Point,
        moves_so_far: list[Move],
        remaining_depth: int,
    ) -> Iterator[int]:
        if data_pos == Point(0, 0):
            yield len(moves_so_far)
        elif remaining_depth > 0:
            for new_pos in self.usable_neighbors(pos, moves_so_far, data_pos):
                start_node = self.node_map[pos]
                end_node = self.node_map[new_pos]

                assert start_node.empty
                assert start_node.size >= end_node.used
                move = Move(start=pos, end=new_pos, amt=end_node.used)

                start_node.used += move.amt
                end_node.used -= move.amt
                moves_so_far.append(move)
                if new_pos == data_pos:
                    data_pos = pos
                    x = 0

                yield from self.solve_for_remaining_depth(
                    pos=new_pos,
                    data_pos=data_pos,
                    moves_so_far=moves_so_far,
                    remaining_depth=remaining_depth - 1,
                )

                if pos == data_pos:
                    data_pos = new_pos
                moves_so_far.pop()
                end_node.used += move.amt
                start_node.used -= move.amt

    def usable_neighbors(self, pos: Point, moves_so_far: list[Move], data_pos: Point) -> set[Point]:
        assert self.node_map[pos].used == 0
        last_pos = moves_so_far[-1].start if len(moves_so_far) > 0 else None
        return {
            n
            for n in self.neighbors(pos)
            if all(
                [
                    self.node_map[pos].avail >= self.node_map[n].used,
                    not self.has_bad_loop(n, moves_so_far, data_pos),
                ]
            )
        }

    def has_bad_loop(self, pos: Point, moves_so_far: list[Move], data_pos: Point) -> bool:
        for m in moves_so_far[::-1]:
            if m.end == data_pos:
                return False
            elif m.end == pos:
                return True
        return False

    def neighbors(self, pos: Point) -> set[Point]:
        output = set[Point]()
        for p in [
            Point(pos.x, pos.y - 1),
            Point(pos.x, pos.y + 1),
            Point(pos.x - 1, pos.y),
            Point(pos.x + 1, pos.y),
        ]:
            if p in self.node_map.keys():
                output.add(p)
        return output

    @cached_property
    def target_coord(self) -> Point:
        return Point(
            x=max([p.x for p in self.node_map.keys() if p.y == 0]),
            y=0,
        )

    @cached_property
    def x_max(self) -> int:
        return max([p.x for p in self.node_map.keys()])

    @cached_property
    def y_max(self) -> int:
        return max([p.y for p in self.node_map.keys()])

    def find_the_only_empty_node(self) -> Node:
        found: set[Node] = set()
        for n in self.node_map.values():
            if n.empty:
                found.add(n)
        assert len(found) == 1
        return list(found)[0]

    def print(self) -> None:
        for y in range(self.y_max + 1):
            line = ""
            for x in range(self.x_max + 1):
                node = self.node_map[Point(x=x, y=y)]
                line += f" {node.used : >3}/{node.size : >3}"
            print(line)
        print()


def solve(input: str) -> int:
    parser = Parser()
    solver = Day22PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_22/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
