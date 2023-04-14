from dataclasses import dataclass
from functools import cached_property
from queue import PriorityQueue
from typing import Iterator, Mapping
from src.day_24.models import Map
from src.day_24.parser import Parser
from src.day_24.solver import Solver
from src.shared.point import Point

@dataclass
class Day24PartASolver(Solver):
    map: Map

    @property
    def solution(self) -> int:
        return min(self.best_dist([0]))

    def best_dist(self, path: list[int]) -> Iterator[int]:
        if set(path) == self.nodes:
            yield self.path_length(path)
        else:
            for n in self.nodes - set(path):
                path.append(n)
                yield from self.best_dist(path)
                path.pop()

    def path_length(self, path: list[int]) -> int:
        output = 0
        for i in range(1, len(path)):
            output += self.distances_between_nodes[path[i-1]][path[i]]
        return output

    @cached_property
    def distances_between_nodes(self) -> Mapping[int, Mapping[int, int]]:
        return {
            node: self.distances(node) for node in self.nodes
        }

    def distances(self, node: int) -> Mapping[int, int]:
        dist_map: dict[int, int] = {}
        queue = PriorityQueue[tuple[int, Point]]()

        start = self.map.nodes[node]
        checked = set[Point]([start])
        queue.put((0, start))
        while len(dist_map) < len(self.nodes):
            dist, point = queue.get()
            if (id := self.point_to_id_map.get(point)) is not None:
                dist_map[id] = dist
            for neighbor in point.manhattan_neighbors:
                if neighbor in self.map.spaces - checked:
                    checked.add(neighbor)
                    queue.put((dist + 1, neighbor))
        return dist_map


    @cached_property
    def id_to_point_map(self) -> Mapping[int, Point]:
        return {k:v for k, v in self.map.nodes.items()}

    @cached_property
    def point_to_id_map(self) -> Mapping[Point, int]:
        return {v:k for k, v in self.map.nodes.items()}

    @cached_property
    def nodes(self) -> set[int]:
        return {k for k, v in self.map.nodes.items()}




def solve(input: str) -> int:
    parser = Parser()
    solver = Day24PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_24/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
