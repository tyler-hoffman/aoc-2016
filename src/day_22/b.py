from __future__ import annotations
from dataclasses import dataclass, field
from functools import cache, cached_property, total_ordering
from queue import PriorityQueue
from typing import Any, Generic, Iterator, Mapping, Optional, TypeVar
from src.day_22.models import Node
from src.day_22.parser import Parser
from src.day_22.solver import Solver
from src.shared.point import Point

T = TypeVar("T")

@dataclass(frozen=True)
class NodeMap:
    map: Mapping[Point, Node] = field(hash=False)

@dataclass(frozen=True)
class LinkedList(Generic[T]):
    value: T
    prev: Optional[LinkedList[T]]

    def __iter__(self) -> Iterator[T]:
        if self.prev:
            yield from self.prev.__iter__()
        yield self.value

    @cache
    def __len__(self) -> int:
        return 1 if self.prev is None else 1 + len(self.prev)

    def append(self, value: T) -> LinkedList[T]:
        return LinkedList[T](value, self)


@dataclass(frozen=True)
class Move:
    start: Point
    end: Point
    amt: int

    @property
    def reverse(self) -> Move:
        return Move(start=self.end, end=self.start, amt=self.amt)

def weight(value: int, offset: int = 0, weight: int = 1) -> int:
    return (value - offset) * weight

@total_ordering
@dataclass(frozen=True)
class State:
    node_map: NodeMap
    start: Point
    data_start: Point
    moves: Optional[LinkedList[Point]]

    @cache
    @staticmethod
    def make(
        node_map: NodeMap,
        start: Point,
        data_start: Point,
        moves: Optional[LinkedList[Point]],
    ) -> State:
        return State(node_map, start, data_start, moves)

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, State):
            return self.score < other.score
        else:
            raise Exception(f"{other} can't be compared to State")

    @cached_property
    def override_map(self) -> Mapping[Point, Node]:
        output: dict[Point, Node] = {}
        current = self.start
        for next_pos in self.moves or []:
            current_node = output.get(current, self.node_map.map[current])
            next_node = output.get(next_pos, self.node_map.map[next_pos])

            output[current] = current_node.with_used(next_node.used)
            output[next_pos] = next_node.with_used(0)

            current = next_pos
        return output

    @cached_property
    def data_point(self) -> Point:
        data_pos = self.data_start
        current_pos = self.start
        for next_pos in self.moves or []:
            if next_pos == data_pos:
                data_pos = current_pos
            current_pos = next_pos
        return data_pos

    def get_node(self, point: Point) -> Node:
        return self.override_map.get(point, self.node_map.map[point])

    @cached_property
    def score(self) -> int:
        return sum([
            weight(self.move_count, 0, 2),
            weight(self.pos.manhattan_dist(self.data_point), 1, 2),
            # weight(self.pos.manhattan_dist(Point(0, 0)), 1, 2),
            # weight(self.data_point.manhattan_dist(Point(0, 0)), 0, 2),
            # weight(self.pos.manhattan_dist(self.start), 0, -2),
            weight(self.loop_count, 0, 4),
            # weight(max(1, self.pos.y), 1, 1),
            # weight(max(1, self.pos.x), 1, 1),
        ])

    @cached_property
    def move_count(self) -> int:
        return len(self.moves) if self.moves else 0

    @cached_property
    def loop_count(self) -> int:
        output = 0
        pos = self.start
        for next_pos in self.moves or []:
            if next_pos == pos:
                output += 1
            pos = next_pos
        return output


    @cached_property
    def done(self) -> bool:
        return self.data_point == Point(0, 0)

    @property
    def pos(self) -> Point:
        return self.moves.value if self.moves else self.start

    # TODO: nah
    @property
    def prev(self) -> Optional[Point]:
        if self.moves and self.moves.prev:
            return self.moves.prev.value
        else:
            return None

    @cached_property
    def has_bad_loop(self) -> bool:
        return False

    def next_states(self) -> Iterator[State]:
        for neighbor in self.pos.manhattan_neighbors:
            if neighbor in self.node_map.map and self.get_node(neighbor).used <= self.get_node(self.pos).avail and neighbor != self.prev:
                yield self.move(neighbor)

    def move(self, pos: Point) -> State:
        new_moves = self.moves.append(pos) if self.moves else LinkedList(pos, None)
        return State.make(self.node_map, self.start, self.data_start, new_moves)


@dataclass
class Day22PartBSolver(Solver):
    node_map: Mapping[Point, Node]

    @cached_property
    def wrapped_node_map(self) -> NodeMap:
        return NodeMap(self.node_map)

    @property
    def solution(self) -> int:
        # a* to target coord (- 1x), 
        return self.find_the_only_empty_node().coords.manhattan_dist(self.entrance) + self.entrance.manhattan_dist(self.target_coord.add(Point(-1, 0))) + 5 * self.target_coord.x - 4
        self.print(set())
        q = PriorityQueue[State]()
        q.put(State.make(self.wrapped_node_map, self.find_the_only_empty_node().coords, self.target_coord, None))
        visited = set[Point]([self.find_the_only_empty_node().coords])

        dist = 0
        i = 0

        while True:
            i += 1
            state = q.get()
            for pos in state.moves or []:
                visited.add(pos)

            if i % 10000 == 0:
                print("=======")
                self.print(visited)
                print("=======")

            if state.move_count > dist:
                dist = state.move_count
                print(dist)

            if state.done:
                return state.move_count
            else:
                for next_state in state.next_states():
                    q.put(next_state)


    @property
    def entrance(self) -> Point:
        walls = [p for p, k in self.node_map.items() if k.used > 100]
        wall_xs = [w.x for w in walls]
        return Point(x = min(wall_xs) - 1, y = walls[0].y)


        # data_pos = self.target_coord
        # current_node = self.find_the_only_empty_node()
        # start_state = State(self.node_map, current_node.coords, data_pos, [])


        # max_depth = 1
        # while True:
        #     max_depth *= 2
        #     print(max_depth)
        #     fewest_steps = self.solve_for_remaining_depth(
        #         pos=current_node.coords,
        #         data_pos=data_pos,
        #         moves_so_far=[],
        #         remaining_depth=max_depth,
        #     )
        #     as_set = set(fewest_steps)
        #     if len(as_set) > 0:
        #         return min(as_set)

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

    def print(self, visited: set[Point]) -> None:
        for y in range(self.y_max + 1):
            line = ""
            for x in range(self.x_max + 1):
                pos = Point(x, y)
                if pos in visited:
                    line += " XXXXXX "
                else:
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
