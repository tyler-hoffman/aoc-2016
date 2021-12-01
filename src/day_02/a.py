from typing import List
from src.day_02.shared import move, number_at_point, parse
from src.shared.point import Point


def solve(input: str) -> str:
    directions = parse(input)
    numbers: List[int] = []

    pos = Point(x=1, y=1)
    for line in directions:
        pos = move(pos, line)
        numbers.append(number_at_point(pos))

    return "".join([f"{x}" for x in numbers])


if __name__ == "__main__":
    input = open("src/day_02/input.txt", "r").read()
    output = solve(input)
    print(output)
