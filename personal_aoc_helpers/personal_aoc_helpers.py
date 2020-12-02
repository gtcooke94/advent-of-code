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
