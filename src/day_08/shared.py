import dataclasses
import re


class Command(object):
    pass


@dataclasses.dataclass
class Rect(Command):
    width: int
    height: int


@dataclasses.dataclass
class RotateRow(Command):
    row: int
    amt: int


@dataclasses.dataclass
class RotateCol(Command):
    col: int
    amt: int


class Screen(object):
    width: int
    height: int
    pixels: list[list[bool]]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.pixels = [[False for _ in range(self.width)] for _ in range(self.height)]

    @property
    def count_on_pixels(self) -> int:
        output = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.pixels[y][x]:
                    output += 1
        return output

    def do_commands(self, cmds: list[Command]) -> None:
        for cmd in cmds:
            self.do_command(cmd)

    def do_command(self, cmd: Command) -> None:
        match cmd:
            case Rect(width=width, height=height):
                for y in range(height):
                    for x in range(width):
                        self.pixels[y][x] = True
            case RotateRow(row=row, amt=amt):
                new_row = self._rotate_array(self.pixels[row], amt)

                self.pixels[row] = new_row
            case RotateCol(col=col, amt=amt):
                old_col = [self.pixels[y][col] for y in range(self.height)]
                new_col = self._rotate_array(old_col, amt)

                for y, value in enumerate(new_col):
                    self.pixels[y][col] = value

    def _rotate_array(self, items: list[bool], amt: int) -> list[bool]:
        size = len(items)
        return [items[(x - amt) % size] for x in range(size)]


def parse_line(line: str) -> Command:
    if match := re.search("rect (\d+)x(\d)+", line):
        return Rect(width=int(match.group(1)), height=int(match.group(2)))
    elif match := re.search("rotate row y=(\d+) by (\d+)", line):
        return RotateRow(row=int(match.group(1)), amt=int(match.group(2)))
    elif match := re.search("rotate column x=(\d+) by (\d+)", line):
        return RotateCol(col=int(match.group(1)), amt=int(match.group(2)))
    else:
        raise Exception(f"Unhandled line: {line}")


def parse(input: str) -> list[Command]:
    return [parse_line(line) for line in input.strip().splitlines()]
