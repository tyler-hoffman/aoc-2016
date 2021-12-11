import re
from typing import List

from src.day_11.models import Category, Floor, State, Thing


class Parser(object):
    @classmethod
    def parse(cls, input: str) -> State:
        floors = [cls.parse_line(line) for line in input.strip().splitlines()]
        return State(floors=tuple(floors))

    @classmethod
    def parse_line(cls, line: str) -> Floor:
        if "nothing relevant" in line:
            return Floor(things=tuple([]))

        sans_period = line[:-1]
        return Floor(
            things=frozenset(
                [cls.parse_piece(piece) for piece in re.split(r", | and ", sans_period)]
            )
        )

    @staticmethod
    def parse_piece(piece: str) -> Thing:
        words = piece.split(" ")
        category = words[-1]
        elementish = words[-2]
        match category:
            case "generator":
                return Thing(category=Category.Generator, element=elementish)
            case "microchip":
                return Thing(
                    category=Category.Microchip, element=elementish.split("-")[0]
                )
            case _:
                raise Exception(f"Unexpected category: {category}")
