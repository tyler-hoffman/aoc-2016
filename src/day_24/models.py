from dataclasses import dataclass
from typing import Mapping
from src.shared.point import Point


@dataclass
class Map:
    spaces: set[Point]
    nodes: Mapping[int, Point]
