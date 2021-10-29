from collections.abc import MutableMapping
from typing import Dict
import copy

ADJACENT_26_3D = [
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (-1, -1, 0),
    (-1, 1, 0),
    (1, -1, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1),
    (0, -1, 1),
    (-1, 0, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    (1, -1, 1),
    (0, 1, -1),
    (1, 0, -1),
    (1, 1, -1),
    (0, -1, -1),
    (-1, 0, -1),
    (-1, -1, -1),
    (-1, 1, -1),
    (1, -1, -1),
    (0, 0, 1),
    (0, 0, -1),
]

ADJACENT_80_4D = [
    (0, 0, 0, -1),
    (0, 0, 0, 1),
]

for entry in ADJACENT_26_3D:
    ADJACENT_80_4D.append((entry[0], entry[1], entry[2], -1))
    ADJACENT_80_4D.append((entry[0], entry[1], entry[2], 0))
    ADJACENT_80_4D.append((entry[0], entry[1], entry[2], 1))

class ConwayCubes(MutableMapping):
    def __init__(self, grid_dict: Dict, default_char="."):
        self.grid_dict = grid_dict
        self.default_char = default_char
        """ We are only looking for the 6th iteration, can only go in any direction +-6 at max. Be lazy and just add and subtract 6 from the max """
        self.min_x = min((i) for i, _, _ in self.grid_dict.keys()) - 6
        self.max_x = max((i) for i, _, _ in self.grid_dict.keys()) + 6
        self.min_y = min((i) for i, _, _ in self.grid_dict.keys()) - 6
        self.max_y = max((i) for i, _, _ in self.grid_dict.keys()) + 6
        self.min_z = -6
        self.max_z = 6

    def simulate(self):
        new = copy.deepcopy(self)
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                for z in range(self.min_z, self.max_z + 1):
                    pos = (x, y, z)
                    num_active_neighbors = self._get_num_active_neighbors(pos)
                    if self._is_active(pos) and not (num_active_neighbors == 2 or num_active_neighbors == 3):
                        new[pos] = "."
                    elif not self._is_active(pos) and num_active_neighbors == 3:
                        new[pos] = "#"
        self.grid_dict = new.grid_dict

    def total_active_cubes(self):
        return sum(value == "#" for value in self.grid_dict.values())


    def _is_active(self, pos):
        return self[pos] == "#"
    
    def _get_num_active_neighbors(self, pos):
        active_neighbors = 0
        for movement in ADJACENT_26_3D:
            if self._is_active((pos[0] + movement[0], pos[1] + movement[1], pos[2] + movement[2])):
                active_neighbors += 1
        return active_neighbors

    def __getitem__(self, pos):
        return self.grid_dict.get(pos, None)

    def __setitem__(self, pos, value):
        self.grid_dict[pos] = value

    def __delitem__(self, pos):
        del self.grid_dict[pos]

    def __len__(self):
        return len(self.grid_dict)

    def __eq__(self, other):
        if isinstance(other, ConwayCubes):
            return self.grid_dict == other.grid_dict
        else:
            return self.grid_dict == other

    def __iter__(self):
        yield from self.grid_dict.items()

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
        for row, line in enumerate(rows):
            for col, character in enumerate(line):
                # Treat the starting grid as the zero z-index in the infinite grid
                grid[(row, col, 0)] = character
        return cls(grid)





class ConwayCubes4D(MutableMapping):
    def __init__(self, grid_dict: Dict, default_char="."):
        self.grid_dict = grid_dict
        self.default_char = default_char
        """ We are only looking for the 6th iteration, can only go in any direction +-6 at max. Be lazy and just add and subtract 6 from the max """
        self.min_x = min((i) for i, *_ in self.grid_dict.keys()) - 6
        self.max_x = max((i) for i, *_ in self.grid_dict.keys()) + 6
        self.min_y = min((i) for i, *_ in self.grid_dict.keys()) - 6
        self.max_y = max((i) for i, *_ in self.grid_dict.keys()) + 6
        self.min_z = -6
        self.max_z = 6
        self.min_w = -6
        self.max_w = 6

    def simulate(self):
        new = copy.deepcopy(self)
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                for z in range(self.min_z, self.max_z + 1):
                    for w in range(self.min_w, self.max_w + 1):
                        pos = (x, y, z, w)
                        num_active_neighbors = self._get_num_active_neighbors(pos)
                        if self._is_active(pos) and not (num_active_neighbors == 2 or num_active_neighbors == 3):
                            new[pos] = "."
                        elif not self._is_active(pos) and num_active_neighbors == 3:
                            new[pos] = "#"
        self.grid_dict = new.grid_dict

    def total_active_cubes(self):
        return sum(value == "#" for value in self.grid_dict.values())


    def _is_active(self, pos):
        return self[pos] == "#"
    
    def _get_num_active_neighbors(self, pos):
        active_neighbors = 0
        for movement in ADJACENT_80_4D:
            if self._is_active((
                pos[0] + movement[0],
                pos[1] + movement[1],
                pos[2] + movement[2],
                pos[3] + movement[3]
            )):
                active_neighbors += 1
        return active_neighbors

    def __getitem__(self, pos):
        return self.grid_dict.get(pos, None)

    def __setitem__(self, pos, value):
        self.grid_dict[pos] = value

    def __delitem__(self, pos):
        del self.grid_dict[pos]

    def __len__(self):
        return len(self.grid_dict)

    def __eq__(self, other):
        if isinstance(other, ConwayCubes):
            return self.grid_dict == other.grid_dict
        else:
            return self.grid_dict == other

    def __iter__(self):
        yield from self.grid_dict.items()

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
        for row, line in enumerate(rows):
            for col, character in enumerate(line):
                # Treat the starting grid as the zero z-index in the infinite grid
                grid[(row, col, 0, 0)] = character
        return cls(grid)
