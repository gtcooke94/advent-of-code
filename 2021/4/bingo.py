from os import sep
import personal_aoc_helpers as pah
from dataclasses import dataclass

class BingoBoard(pah.Grid):

    def __init__(self):
        self.number_to_pos = {}
    
    def __init__(self, grid, num_rows, num_cols):
        super().__init__(grid, num_rows, num_cols)
        self.number_to_pos = {}

    @classmethod
    def from_string(cls, string, separator):
        board = super().from_string(string, separator)
        for row, col, item in board:
            board[row, col] = BingoItem(item, False)
            board.number_to_pos[item] = (row, col)
        return board

    def number_called(self, number):
        if number in self.number_to_pos.keys():
            pos = self.number_to_pos[number]
            self[pos].selected = True

    def check_winning(self):
        for row in range(self.num_rows):
            if all(self[row, col].selected for col in range(self.num_cols)):
                return True
        for col in range(self.num_cols):
            if all(self[row, col].selected for row in range(self.num_rows)):
                return True
        return False

    def calculate_solution(self, last_number):
        return sum(item.value for _, _, item in self if not item.selected) * last_number


@dataclass
class BingoItem:
    value: int
    selected: bool