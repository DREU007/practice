class Easy():
    # BEGIN (write your solution here)
    def __init__(self, sym):
        self.sym = sym

    def move(self, field):
        length = len(field)
        columns = list(zip(*field))
        print(f"\n{field=}\n{columns=}")
        for y in range(length):
            if self._check_line(field[y]): 
                for x, char in enumerate(field[y]):
                    if char is None:
                        return y, x
            elif self._check_line(columns[y]):
                for x, char in enumerate(columns[y]):
                    if char is None:
                        return x, y

    def _check_line(self, line):
        return all(map(
            lambda char: char in (self.sym, None), line
        ))
    # END
