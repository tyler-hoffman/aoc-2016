from src.day_04.shared import parse


def solve(input: str) -> int:
    rooms = parse(input)

    return sum([r.id for r in rooms if r.is_valid])


if __name__ == "__main__":
    with open("src/day_04/input.txt", "r") as f:
        input = f.read()

    output = solve(input)
    print(output)
