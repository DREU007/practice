from strategies.easy import Easy


class Normal(Easy):
    def move(self, field):
        length = len(field)
        columns = list(zip(*field))

        for line_y, column_y in zip(range(length - 1, -1, -1), range(length)):
            if self._check_line(field[line_y]):
                for column_x, char in enumerate(field[line_y]):
                    if char is None:
                        return line_y, column_x
            elif self._check_line(columns[column_y]):
                for line_x, char in enumerate(columns[column_y]):
                    if char is None:
                        return column_y, line_x
