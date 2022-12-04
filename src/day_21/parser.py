import re
from functools import cache, cached_property
from typing import List

from src.day_21.models import Command, Direction, MovePositions, ReversePositions, RotateBasedOn, RotateDirection, SwapLetters, SwapPositions


class Parser(object):
    swap_positions_regex = re.compile(r"swap position (\d+) with position (\d+)")
    swap_letters_regex= re.compile(r"swap letter (\w) with letter (\w)")
    rotate_direction_regex= re.compile(r"rotate (left|right) (\d+) steps?")
    rotate_based_on_regex= re.compile(r"rotate based on position of letter (\w)")
    reverse_positions_regex= re.compile(r"reverse positions (\d+) through (\d+)")
    move_positions_regex = re.compile(r"move position (\d+) to position (\d+)")

    @staticmethod
    def parse(input: str) -> List[Command]:
        return [Parser.parse_line(line) for line in input.strip().splitlines()]

    @classmethod
    def parse_line(cls, line: str) -> Command:
        if (match := cls.swap_positions_regex.search(line)):
            return SwapPositions(a=int(match.group(1)), b=int(match.group(2)))
        elif (match := cls.swap_letters_regex.search(line)):
            return SwapLetters(match.group(1), match.group(2))
        elif (match := cls.rotate_direction_regex.search(line)):
            return RotateDirection(Direction[match.group(1).upper()], int(match.group(2)))
        elif (match := cls.rotate_based_on_regex.search(line)):
            return RotateBasedOn(match.group(1))
        elif (match := cls.reverse_positions_regex.search(line)):
            return ReversePositions(int(match.group(1)), int(match.group(2)))
        elif (match := cls.move_positions_regex.search(line)):
            return MovePositions(int(match.group(1)), int(match.group(2)))
        else:
            raise Exception(f"Unexpected pattern: {line}")



