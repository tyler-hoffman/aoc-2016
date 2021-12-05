def solve(input: str) -> int:
    return len(encrypt(input))


def encrypt(input: str) -> str:
    index = 0
    output = ""

    while index < len(input):
        char = input[index]
        if char == "(":
            end_index = input.index(")", index + 1)
            chars, repeat = [int(x) for x in input[index + 1 : end_index].split("x")]

            to_repeat = input[end_index + 1 : end_index + 1 + chars]

            output += to_repeat * repeat
            index = end_index + chars + 1
        else:
            output += char
            index += 1

    return output


if __name__ == "__main__":
    with open("src/day_09/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
