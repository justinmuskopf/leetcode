# This is a sample Python script.
from typing import List

class BoardCell:
    def __init__(self, row, col, value, can_go_up, can_go_down, can_go_left, can_go_right):
        self._row = row
        self._col = col
        self._value = value
        self._can_go_up = can_go_up
        self._can_go_down = can_go_down
        self._can_go_left = can_go_left
        self._can_go_right = can_go_right


class Board:
    def __init__(self, board: List[List[str]]):
        self._rows = len(board)
        self._max_row_idx = self._rows - 1
        self._cols = len(board[0])
        self._max_col_idx = self._cols - 1
        self._board = board

        self._cells = []
        self._cells_by_letter = {}
        for rowIdx, row in enumerate(board):
            self._cells.append([])

            can_go_up = rowIdx > 0
            can_do_down = rowIdx < self._max_row_idx
            for colIdx, col in enumerate(row):
                can_go_right = colIdx < self._max_col_idx
                can_go_left = colIdx != 0

                if col not in self._cells_by_letter:
                    self._cells_by_letter[col] = []

                cell = BoardCell(rowIdx, colIdx, col, can_go_up, can_do_down, can_go_left, can_go_right)
                self._cells[rowIdx].append(cell)
                self._cells_by_letter[col].append(cell)

    def get_neighbors(self, cell):
        row, col = cell._row, cell._col
        print(f'Getting Neighbors of [{row}, {col}]')

        left = self._cells[row][col-1] if cell._can_go_left else None
        right = self._cells[row][col + 1] if cell._can_go_right else None
        up = self._cells[row - 1][col] if cell._can_go_up else None
        down = self._cells[row + 1][col] if cell._can_go_down else None

        return [c for c in (left, right, up, down) if c is not None]

    def get(self, row, col):
        return self._board[row][col]

    def find(self, word: str) -> bool:
        first_letter = word[0]
        if first_letter not in self._cells_by_letter:
            return False

        for cell in self._cells_by_letter[first_letter]:
            if BoardSearch(self, word).search(cell):
                return True

        return False


class BoardSearch:
    def __init__(self, _board: Board, _word: str):
        self._board = _board
        self._word = _word
        self._word_len = len(_word)
        self._searched_cells = []

    def recurse(self, c, word_idx):
        if word_idx == self._word_len:
            return True

        letter = self._word[word_idx]
        for c in self._board.get_neighbors(c):
            if c in self._searched_cells:
                continue

            board_letter = c._value
            print(f'[{c._row}, {c._col}] - {word_idx}:{letter} = {board_letter}')
            if board_letter == letter:
                self._searched_cells.append(c)
                if self.recurse(c, word_idx + 1):
                    return True

        return False

    def search(self, c: BoardCell) -> bool:
        return self.recurse(c, 1)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return Board(board).find(word)


if __name__ == '__main__':
    # b = [
    #     ["A", "B", "C", "E"],
    #     ["S", "F", "C", "S"],
    #     ["A", "D", "E", "E"]
    # ]
    b = [["a","a"]]
    w = "aaa"

    print(Solution().exist(b, w))
