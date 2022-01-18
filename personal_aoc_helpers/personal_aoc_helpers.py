from collections.abc import MutableMapping



def print_grid(dictionary, rows=None, cols=None, default_char="."):
    """Print conents of an mxn grid."""
    if rows is None:
        rows = max(row_value for row_value, _ in dictionary.keys()) + 1
    if cols is None:
        cols = max(col_value for _, col_value in dictionary.keys()) + 1
    grid = [[default_char] * cols for _ in range(rows)]
    max_entry_length = max(len(str(entry)) for entry in dictionary.values()) + 1
    #  import pdb; pdb.set_trace()
    for row, col in dictionary:
        grid[row][col] = dictionary[(row, col)]
    str_rows = []
    for row in grid:
        str_row = ""
        for entry in row:
            str_entry = str(entry).strip(" ")
            str_row += " " * (max_entry_length - len(str_entry)) + str_entry
        str_rows.append(str_row)
    str_grid = "\n".join(str_row for str_row in str_rows)
    print("==== Printing Grid ====\n")
    print(str_grid)
    print("\n==== Done Printing Grid ====\n")


class Grid(MutableMapping):
    def __init__(self, grid_dict, default_char="."):
        self.grid_dict = grid_dict
        self.default_char = default_char

    def __getitem__(self, pos):
        return self.grid_dict.get(pos, self.default_char)

    def __setitem__(self, pos, value):
        self.grid_dict[pos] = value

    def __delitem__(self, pos):
        del self.grid_dict[pos]

    def __len__(self):
        return len(self.grid_dict)

    def __iter__(self):
        for row in range(self._min_row, self._max_row + 1):
            for col in range(self._min_col, self._max_col + 1):
                yield row, col, self[row, col]

    def iter_explicit_items(self):
        yield from self.grid_dict.items()
    
    def __repr__(self):
        """ TODO won't work with negative grid entries"""
        rows = self._max_row + 1
        cols = self._max_col + 1
        grid = [[self.default_char] * cols for _ in range(rows)]
        max_entry_length = max(len(str(entry)) for entry in self.grid_dict.values()) + 1
        for row, col, value in self:
            grid[row][col] = value
        str_rows = []
        for row in grid:
            str_row = ""
            for entry in row:
                str_entry = str(entry).strip(" ")
                str_row += " " * (max_entry_length - len(str_entry)) + str_entry
            str_rows.append(str_row)
        str_grid = "\n".join(str_row for str_row in str_rows)
        return str_grid

    
    @property
    def _max_row(self):
        return max(row for row, col in self.grid_dict.keys())

    @property
    def _min_row(self):
        return min(row for row, col in self.grid_dict.keys())

    @property
    def _max_col(self):
        return max(col for row, col in self.grid_dict.keys())

    @property
    def _min_col(self):
        return min(col for row, col in self.grid_dict.keys())

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.grid_dict == other.grid_dict
        else:
            return self.grid_dict == other

    def to_dict(self):
        return self.grid_dict



LR_GRID_MOVEMENTS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

LR_AND_DIAG_MOVEMENTS = [
    (0, 1),
    (1, 0),
    (1, 1),
    (0, -1),
    (-1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
]

class FiniteGrid(Grid):
    def __init__(self, num_rows, num_cols, default_char="."):
        super().__init__(self, default_char)
        self.num_rows = num_rows
        self.num_cols = num_cols
    
    def __repr__(self):
        """Print conents of an mxn grid."""
        grid = [[self.default_char] * self.num_cols for _ in range(self.num_rows)]
        max_entry_length = max(len(str(entry)) for entry in self.grid_dict.values()) + 1
        for row, col in self.grid_dict:
            grid[row][col] = self.grid_dict[(row, col)]
        str_rows = []
        for row in grid:
            str_row = ""
            for entry in row:
                str_entry = str(entry).strip(" ")
                str_row += " " * (max_entry_length - len(str_entry)) + str_entry
            str_rows.append(str_row)
        str_grid = "\n".join(str_row for str_row in str_rows)
        return str_grid

    @classmethod
    def from_string(cls, string):
        """
        Make a grid object from a string grid like:
        ..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#..
        """
        grid = {}
        rows = string.split("\n")
        num_rows = len(rows)
        num_cols = len(rows[0])
        for row, line in enumerate(rows):
            for col, character in enumerate(line):
                grid[(row, col)] = character
        return cls(grid, num_rows, num_cols)

    @classmethod
    def from_string(cls, string, separator):
        """
        Make a grid object from a string grid like:
        22 13 17 11  0
        8  2 23  4 24
        21  9 14 16  7
        6 10  3 18  5
        1 12 20 15 19
        """
        grid = {}
        rows = string.split("\n")
        num_rows = len(rows)
        num_cols = len(rows[0].strip().split(separator))
        for row, line in enumerate(rows):
            for col, item in enumerate(line.strip().split(separator)):
                item = item.strip()
                grid[(row, col)] = int(item)
        return cls(grid, num_rows, num_cols)

