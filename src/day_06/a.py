from src.day_06.shared import parse
from src.shared.functions import frequency_map


def solve(input: str) -> str:
    lines = parse(input)
    line_len = len(lines[0])
    output = ""
    for i in range(line_len):
        freqs = frequency_map(line[i] for line in lines)
        keys = list(freqs.keys())
        values = list(freqs.values())
        max_index = values.index(max(values))
        output += keys[max_index]
    return output


if __name__ == "__main__":
    with open("src/day_06/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
