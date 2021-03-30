from typing import List, Tuple


class BoardSearch:
    def __init__(self, board: List[List[str]], word: str):
        self.__board = board

        self.__word = word
        self.__word_len = len(word)
        self.__cells_by_value = {}
        self.__initialize_value_map()

        num_rows, num_cols = len(board), len(board[0])
        self.__max_row_idx = num_rows - 1
        self.__max_col_idx = num_cols - 1
        self.__num_cells = num_rows * num_cols
        self.__visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    def __initialize_value_map(self):
        for rowIdx, row in enumerate(self.__board):
            for colIdx, col in enumerate(row):
                if col not in self.__cells_by_value:
                    self.__cells_by_value[col] = []

                self.__cells_by_value[col].append((rowIdx, colIdx))

    def _valid_cell(self, row: int, col: int) -> bool:
        return (0 <= row <= self.__max_row_idx) and (0 <= col <= self.__max_col_idx)

    def _cell_value_is(self, row: int, col: int, value: str) -> bool:
        return self._valid_cell(row, col) and self.__board[row][col] == value

    def _can_visit(self, row: int, col: int) -> bool:
        return self.__visited[row][col] is False

    def _set_visited(self, row: int, col: int, visited: bool):
        self.__visited[row][col] = visited

    def _recurse(self, coordinate: Tuple[int, int], word_idx=0) -> bool:
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
        # Not enough letters to make 'er happen cap'n
        if len(self.__word) > self.__num_cells:
            return False

        # Not all letters are present
        unique_letters = set(self.__word)
        for letter in unique_letters:
            if letter not in self.__cells_by_value:
                return False

        # Get cells matching the first letter of the word
        matching_cells = self.__cells_by_value[self.__word[0]]
        if matching_cells is None:
            return False

        # Try to match for each cell with the first letter
        for coordinate in matching_cells:
            if self._recurse(coordinate):
                return True


class Solution:
    def exist(self, board: List[List[str]], word: str):
        return BoardSearch(board, word).find()
