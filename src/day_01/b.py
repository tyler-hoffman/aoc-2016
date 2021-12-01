from unittest.case import addModuleCleanup
from src.day_01.shared import follow_instructions, parse
from src.shared.point import Point


def solve(input: str) -> int:
    instructions = parse(input)
    visited = set[Point]()

    for point in follow_instructions(instructions):
        if point in visited:
            return point.magnitude
        else:
            visited.add(point)

    assert False, "We shouldn't have gotten here"


if __name__ == "__main__":
    with open("src/day_01/input.txt", "r") as f:
        input = f.read()
    output = solve(input)
    print(output)
