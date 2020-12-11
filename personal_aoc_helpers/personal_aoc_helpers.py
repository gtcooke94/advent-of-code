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
            str_row += (" " * (max_entry_length - len(str_entry)) + str_entry)
        str_rows.append(str_row)
    str_grid = "\n".join(str_row for str_row in str_rows)
    print("==== Printing Grid ====\n")
    print(str_grid)
    print("\n==== Done Printing Grid ====\n")


class Grid(MutableMapping):
    def __init__(self, grid_dict, num_rows, num_cols, default_char="."):
        self.grid_dict = grid_dict
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.default_char = default_char

    def __getitem__(self, pos):
        return self.grid_dict.get(pos, None)
    
    def __setitem__(self, pos, value):
        self.grid_dict[pos] = value

    def __delitem__(self, pos):
        del self.grid_dict[pos]

    def __len__(self):
        return len(self.grid_dict)

    def __iter__(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                yield row, col, self[row, col]

    def __str__(self):
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
                str_row += (" " * (max_entry_length - len(str_entry)) + str_entry)
            str_rows.append(str_row)
        str_grid = "\n".join(str_row for str_row in str_rows)
        return str_grid

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.grid_dict == other.grid_dict
        else:
            return self.grid_dict == other

    def to_dict(self):
        return self.grid_dict

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

