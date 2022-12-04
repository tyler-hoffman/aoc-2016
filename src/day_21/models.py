from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class Command(object):
    ...


@dataclass
class SwapPositions(Command):
    a: int
    b: int


@dataclass
class SwapLetters(Command):
    a: str
    b: str


@dataclass
class RotateDirection(Command):
    direction: Direction
    steps: int


@dataclass
class RotateBasedOn(Command):
    index: str


@dataclass
class ReversePositions(Command):
    start: int
    end: int


@dataclass
class MovePositions(Command):
    x: int
    y: int


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
