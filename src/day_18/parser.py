class Parser(object):
    @staticmethod
    def parse(first_row: str) -> list[bool]:
        return [char == "." for char in first_row.strip()]
