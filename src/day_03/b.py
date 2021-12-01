import re
from typing import List, Tuple
from src.day_03.shared import Triangle


def parse(input: str) -> List[Triangle]:
    ints: List[Tuple[int, int, int]] = []
    lines = [line for line in input.splitlines() if line]
    for line in lines:
        match = re.search("(\d+)\s+(\d+)\s+(\d+)", line)
        assert match is not None
        ints.append(tuple([int(match.group(i)) for i in range(1, 4)]))

    list_a = [a for a, _, _ in ints]
    list_b = [b for _, b, _ in ints]
    list_c = [c for _, _, c in ints]

    big_list = list_a + list_b + list_c

    output: List[Triangle] = []

    return [
        Triangle(a=big_list[n], b=big_list[n + 1], c=big_list[n + 2])
        for n in range(0, len(big_list), 3)
    ]


def solve(input: str) -> int:
    triangles = parse(input)

    return len([t for t in triangles if t.is_valid])


if __name__ == "__main__":
    with open("src/day_03/input.txt", "r") as f:
        input = f.read()

    output = solve(input)
    print(output)
