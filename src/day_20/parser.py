from src.day_20.models import Range


class Parser(object):
    @staticmethod
    def parse(input: str) -> set[Range]:
        return {Parser.parse_line(line) for line in input.strip().splitlines()}

    @staticmethod
    def parse_line(line: str) -> Range:
        a, b = line.split("-")
        return Range(start=int(a), end=int(b))
