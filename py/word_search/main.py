from typing import List, Tuple


class BoardSearch:
    def __init__(self, board: List[List[str]], word: str):
        self.__board = board
        self.__max_row_idx = len(board) - 1
        self.__max_col_idx = len(board[0]) - 1
        self.__visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        self.__word = word
        self.__word_len = len(word)

    def _valid_cell(self, row: int, col: int) -> bool:
        return (0 <= row <= self.__max_row_idx) and (0 <= col <= self.__max_col_idx)

    def _cell_value_is(self, row: int, col: int, value: str):
        return self._valid_cell(row, col) and self.__board[row][col] == value

    def _can_visit(self, row: int, col: int):
        return self.__visited[row][col] is False

    def _set_visited(self, row: int, col: int, visited: bool):
        self.__visited[row][col] = visited

    def _recurse(self, coordinate: Tuple[int, int], word_idx: int) -> bool:
        if word_idx == self.__word_len:
            return True

        row, col = coordinate

        # Either out of bounds or wrong character value
        if not self._cell_value_is(row, col, self.__word[word_idx]):
            return False

        # Already visited
        if not self._can_visit(row, col):
            return False

        self._set_visited(row, col, True)

        left, right = (row, col - 1), (row, col + 1)
        up, down = (row - 1, col), (row + 1, col)
        for coordinate in left, right, up, down:
            if self._recurse(coordinate, word_idx + 1):
                return True

        # Search unsuccessful, FALSIFY
        self._set_visited(row, col, False)
        return False

    def find(self) -> bool:
        for rowIdx, row in enumerate(self.__board):
            for colIdx, col in enumerate(row):
                if self._recurse((rowIdx, colIdx), 0):
                    return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str):
        return BoardSearch(board, word).find()
