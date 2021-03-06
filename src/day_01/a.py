from src.day_01.shared import follow_instructions, parse


def solve(input: str) -> int:
    instructions = parse(input)
    for position in follow_instructions(instructions):
        pass

    return position.magnitude


if __name__ == "__main__":
    with open("src/day_01/input.txt", "r") as f:
        input = f.read()
    output = solve(input)
    print(output)
