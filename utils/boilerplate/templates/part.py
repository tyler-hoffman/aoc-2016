PART_TEMPLATE = """
def solve(input: str) -> int:
    return -1


if __name__ == "__main__":
    with open("src/day_{day_string}/input.txt", "r") as f:
        input = f.read()

    output = solve(input)
    print(output)

"""
