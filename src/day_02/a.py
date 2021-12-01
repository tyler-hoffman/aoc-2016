from typing import List
from src.day_02.shared import Keypad, parse

KEYPAD_INPUT = """
1 2 3
4 5 6
7 8 9
"""

def solve(input: str) -> str:
    directions = parse(input)
    characters: List[str] = []
    keypad = Keypad.from_string(KEYPAD_INPUT)

    pos = keypad.position_of("5")
    for line in directions:
        pos = keypad.move(pos, line)
        characters.append(keypad.char_at_point(pos))

    return "".join(characters)


if __name__ == "__main__":
    with open("src/day_02/input.txt", "r") as f:
        input = f.read()

    output = solve(input)
    print(output)
