from src.day_08.shared import Screen, parse


def solve(input_string: str, width=50, height=6) -> str:
    commands = parse(input_string)
    screen = Screen(width=width, height=height)
    screen.do_commands(commands)

    print()
    for line in screen.pixels:
        print("".join("#" if x else " " for x in line))
    print()

    answer = input("What's that look like to you? ")
    return answer


if __name__ == "__main__":
    with open("src/day_08/input.txt", "r") as f:
        input_string = f.read()
    print(solve(input_string))
