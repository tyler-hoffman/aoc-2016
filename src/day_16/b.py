from src.day_16.solver import Solver


def solve(initial_state: str, disk_size: int = 35651584) -> int:
    initial_state = initial_state.strip()
    solver = Solver(disk_size=disk_size, initial_state=initial_state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_16/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
