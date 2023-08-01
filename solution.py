from strategies.easy import Easy
from strategies.normal import Normal


class TicTacToe():
    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
# BEGIN (write your solution here)
        self.symbols = {
            'player1': 'x',
            'player2': 'o'
        }

        Difficulty = {
            'easy': Easy,
            'normal': Normal
        }.get(level)

        self.computer = Difficulty(self.symbols['player2'])

    def go(self, y=None, x=None):
        if x == y is None:
            y, x = self.computer.move(self.field)
            sym = self.symbols['player2']
        else:
            sym = self.symbols['player1']
        self._set_char(y, x, sym)
        return self._is_winner()

    def _set_char(self, y, x, sym):
        self.field[y][x] = sym

    def _is_winner(self):
        return any((
            *map(self._check_line, self.field),
            *map(self._check_line, zip(*self.field)),
            *map(self._check_line, self._get_diagonal_lines())
        ))

    def _check_line(self, line):
        return (line.count(self.symbols['player1']) == len(line)
                or line.count(self.symbols['player2']) == len(line))

    def _get_diagonal_lines(self):
        fdiag = [line[i] for i, line in enumerate(self.field)]
        bdiag = [line[-i-1] for i, line in enumerate(self.field)]
        return [fdiag, bdiag]

    def __repr__(self):
        output = '\n'.join([' '.join(map(str, line)) for line in self.field])
        return '\n' + output + '\n'
# END
