from src.day_08.shared import Screen, parse


def solve(input: str, width=50, height=6) -> int:
    commands = parse(input)
    screen = Screen(width=width, height=height)
    screen.do_commands(commands)
    return screen.count_on_pixels


if __name__ == "__main__":
    with open("src/day_08/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
