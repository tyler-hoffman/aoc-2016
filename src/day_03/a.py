import re
from typing import List
from src.day_03.shared import Triangle


def parse_triangle(line: str) -> Triangle:
    match = re.search("(\d+)\s+(\d+)\s+(\d+)", line)
    assert match is not None

    return Triangle(a=int(match.group(1)), b=int(match.group(2)), c=int(match.group(3)))


def parse(input: str) -> List[Triangle]:
    lines = [line for line in input.splitlines() if line]
    return [parse_triangle(line) for line in lines]


def solve(input: str) -> int:
    triangles = parse(input)

    return len([t for t in triangles if t.is_valid])


if __name__ == "__main__":
    with open("src/day_03/input.txt", "r") as f:
        input = f.read()

    output = solve(input)
    print(output)
