import random


class Sudoku:
    def __init__(self, name):
        self.name = name
        self.board = [[0] * 9 for _ in range(9)]
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(self.numbers)
        self.__fill(0, 0)
        self.player_board = [[0] * 9 for _ in range(9)]
        self.__place_numbers()

    @staticmethod
    def __is_valid_move(board, row, col, number) -> bool:
        valid_by_row = number not in board[row]
        valid_by_col = number not in [[board[r][c] for r in range(9)] for c in range(9)][col]
        square_row = row // 3
        square_col = col // 3
        numbers_in_square = set()

        for r in range(square_row * 3, square_row * 3 + 3):
            for c in range(square_col * 3, square_col * 3 + 3):
                numbers_in_square.add(board[r][c])

        valid_by_square = number not in numbers_in_square

        return all([valid_by_row, valid_by_col, valid_by_square])

    def __fill(self, row, col) -> bool:
        if col == 9:
            if row == 8:
                return True
            row += 1
            col = 0

        if self.board[row][col] != 0:
            return self.__fill(row, col + 1)

        for num in self.numbers:
            if self.__is_valid_move(self.board, row, col, num):
                self.board[row][col] = num

                if self.__fill(row, col + 1):
                    return True

            self.board[row][col] = 0

        return False

    @property
    def is_correct(self) -> bool:
        valid_rows = all(len(set(row)) == 9 and 0 not in row for row in self.board)
        valid_cols = all([len(set(row)) == 9 and 0 not in row for row in
                          [[self.board[r][c] for r in range(9)] for c in range(9)]])
        squares = []

        for r in range(3):
            for c in range(3):
                numbers_in_square = []
                for row in range(r * 3, r * 3 + 3):
                    for col in range(c * 3, c * 3 + 3):
                        numbers_in_square.append(self.board[row][col])
                square_is_valid = len(set(numbers_in_square)) == 9 and 0 not in numbers_in_square
                squares.append(square_is_valid)

        valid_squares = all(squares)

        return all([valid_rows, valid_cols, valid_squares])

    @property
    def possible_moves(self):
        possible_moves = 0
        for row in range(9):
            for col in range(9):
                field = self.player_board[row][col]
                if field != 0:
                    continue
                possible_numbers_in_field = 0
                for num in range(1, 10):
                    if self.__is_valid_move(self.player_board, row, col, num):
                        possible_numbers_in_field += 1
                        if possible_numbers_in_field > 1:
                            break
                else:
                    possible_moves += 1

        return possible_moves

    def __place_numbers(self):
        while self.possible_moves < 5:
            row = random.randint(0, 8)
            col = random.randint(0, 8)

            self.player_board[row][col] = self.board[row][col]

    def __repr__(self):
        result = '\n'.join(['  '.join([str(x) for x in row]) for row in self.board])
        return result
