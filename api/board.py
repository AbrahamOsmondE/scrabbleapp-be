class Board:
    def __init__(self, size):
        self.size = size
        self._tiles = []

        for _ in range(size):
            row = []

            for _ in range(size):
                row.append(None)

            self._tiles.append(row)
        self.point_board = []
        tempList = ["T..d...T...d..T",
                    ".D...t...t...D.",
                    "..D...d.d...D..",
                    "d..D...d...D..d",
                    "....D.....D....",
                    ".t...t...t...t.",
                    "..d...d.d...d..",
                    "T..d...X...d..T",
                    "..d...d.d...d..",
                    ".t...t...t...t.",
                    "....D.....D....",
                    "d..D...d...D..d",
                    "..D...d.d...D..",
                    ".D...t...t...D.",
                    "T..d...T...d..T"]

        for string in tempList:
            temp = []

            for char in string:
                if char == 'T':
                    temp.append('TW')
                elif char == 'd':
                    temp.append('DL')
                elif char == 't':
                    temp.append('TL')
                elif char == 'D' or char == 'X':
                    temp.append('DW')
                else:
                    temp.append('')

            self.point_board.append(temp)

        self.point_table = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5,
                            'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, }

    def __str__(self):
        return '\n'.join(''.join(char if char is not None else '_' for char in row) for row in self._tiles)

    def all_positions(self):
        result = []

        for row in range(self.size):
            for col in range(self.size):
                result.append((row, col))

        return result

    def get_tile(self, pos):
        row, col = pos

        return self._tiles[row][col]

    def set_tile(self, pos, tile):
        row, col = pos
        self._tiles[row][col] = tile
        self.point_board[row][col] = tile

    def in_bounds(self, pos):
        row, col = pos

        return row >= 0 and row < self.size and col >= 0 and col < self.size

    def is_empty(self, pos):
        return self.in_bounds(pos) and self.get_tile(pos) is None

    def is_filled(self, pos):
        return self.in_bounds(pos) and self.get_tile(pos) is not None

    def copy(self):
        result = Board(self.size)

        for pos in self.all_positions():
            result.set_tile(pos, self.get_tile(pos))

        return result

    def count_sideway_points(self, letter_score, board_symbol, direction, pos):
        moving_index = 1 if direction == 'down' else 0
        point = 0
        row, col = pos
        word_multiplier = 1

        if board_symbol == 'TW':
            word_multiplier *= 3

        elif board_symbol == 'DW':
            word_multiplier *= 2

        if self.point_board[row][col] in set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            return point

        start, end = pos.copy(), pos.copy()

        while start[moving_index] > 0:
            start[moving_index] -= 1

            if start[0] >= 0 and start[1] >= 0 and self.point_board[start[0]][start[1]] not in set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                start[moving_index] += 1
                break

        while end[moving_index] < self.size:
            end[moving_index] += 1

            if end[0] < self.size and end[1] < self.size and self.point_board[end[0]][end[1]] not in set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                end[moving_index] -= 1
                break

        if start[moving_index] == end[moving_index]:
            return point

        if end[moving_index] == self.size:
            end[moving_index] -= 1

        if start[moving_index] == self.size:
            start[moving_index] -= 1
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                board_character = self.point_board[i][j]

                if board_character in self.point_table:
                    point += self.point_table[board_character]

        return (point + letter_score)*word_multiplier

    def count_points(self, word, direction, start, end):
        points = 0
        sideway_points = 0
        multiplier = 1
        index = 0
        word_length = len(word)
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):

                board_symbol = self.point_board[i][j]
                letter_score = self.point_table[word[index]]

                if board_symbol == 'TW':
                    multiplier *= 3

                elif board_symbol == 'DW':
                    multiplier *= 2

                elif board_symbol == 'TL':
                    letter_score *= 3

                elif board_symbol == 'DL':
                    letter_score *= 2

                elif board_symbol != '':
                    word_length -= 1

                points += letter_score

                sideway_points += self.count_sideway_points(
                    letter_score, board_symbol, direction, [i, j])

                index += 1

        bingo = 50 if word_length == 7 else 0

        return points*multiplier + bingo + sideway_points
