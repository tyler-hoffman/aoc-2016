from src.day_04.shared import parse


def solve(input: str) -> int:
    rooms = parse(input)

    contendor_ids = [r.id for r in rooms if r.is_valid if "north" in r.rotated_parts]

    assert (
        len(contendor_ids) == 1
    ), f"We found the wrong number of contendors: {len(contendor_ids)}"

    return contendor_ids[0]


if __name__ == "__main__":
    with open("src/day_04/input.txt", "r") as f:
        input = f.read()

    output = solve(input)
    print(output)
