from typing import List

from src.day_11.models import Category, Floor, State, Thing


class Parser(object):
    @classmethod
    def parse(cls, input: str) -> State:
        return State(floors=[cls.parse_line(line) for line in input.strip().splitlines()])

    @classmethod
    def parse_line(cls, line: str) -> Floor:
        if "nothing relevant" in line:
            return Floor(things=[])

        return Floor(things=set([cls.parse_piece(piece) for piece in line[:-1].split(",")]))

    @staticmethod
    def parse_piece(piece: str) -> Thing:
        words = piece.split(" ")
        category = words[-1]
        elementish = words[-2]
        match category:
            case "generator":
                return Thing(category=Category.Generator, element=elementish)
            case "microchip":
                return Thing(category=Category.Microchip, element=elementish.split("-")[0])
            case _:
                raise Exception(f"Unexpected category: {category}")

