class Easy():
    # BEGIN (write your solution here)
    def __init__(self, sym):
        self.sym = sym

    def move(self, field):
        length = len(field)
        columns = list(zip(*field))
        for line in range(length):
            if self._check_line(field[line]):
                for column, char in enumerate(field[line]):
                    if char is None:
                        return line, column
            elif self._check_line(columns[line]):
                for column, char in enumerate(columns[line]):
                    if char is None:
                        return column, line

    def _check_line(self, line):
        return all(map(
            lambda char: char in (self.sym, None), line
        ))
    # END
