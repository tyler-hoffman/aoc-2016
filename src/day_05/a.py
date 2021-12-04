from src.day_05.shared import get_hashes_for_prefix


def solve(input: str) -> str:
    output = ""

    for hash in get_hashes_for_prefix(input):
        output += hash[5]
        if len(output) == 8:
            break

    return output


if __name__ == "__main__":
    input = "ugkcyxxp"
    print(solve(input))
