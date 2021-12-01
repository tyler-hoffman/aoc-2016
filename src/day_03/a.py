from src.day_03.shared import parse


def solve(input: str) -> int:
    triangles = parse(input)

    return len([t for t in triangles if t.is_valid])


if __name__ == "__main__":
    with open("src/day_03/input.txt", "r") as f:
        input = f.read()

    output = solve(input)
    print(output)
