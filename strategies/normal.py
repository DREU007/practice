from strategies.easy import Easy


class Normal(Easy):
    def move(self, field):
        length = len(field)
        columns = list(zip(*field))
        for y in range(length):
            _y = y - length
            if self._check_line(field[_y]): 
                print(f"{y=}, {field[y]=}, {_y=}, {field[_y]=}")
                for x, char in enumerate(field[_y]):
                    if char is None:
                        return x, y
            elif self._check_line(columns[_y]):
                print(columns[_y])
                for x, char in enumerate(columns[_y]):
                    if char is None:
                        return y, x 

