from src.day_05.shared import get_hashes_for_prefix


BLANK = "_"


def solve(input: str) -> int:
    characters = [BLANK for _ in range(8)]

    for hash in get_hashes_for_prefix(input):
        index = int(hash[5], 16)
        if index < len(characters) and characters[index] == BLANK:
            characters[index] = hash[6]
        if not BLANK in characters:
            break

    return "".join(characters)


if __name__ == "__main__":
    input = "ugkcyxxp"
    print(solve(input))
