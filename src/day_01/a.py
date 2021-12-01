from src.day_01.shared import follow_instructions, parse
from src.shared.point import Point


def solve(input: str) -> int:
    instructions = parse(input)
    for position in follow_instructions(instructions):
        pass

    return position.magnitude


if __name__ == "__main__":
    input = open("src/day_01/input.txt", "r").read()
    output = solve(input)
    print(output)
