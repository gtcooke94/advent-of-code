import personal_aoc_helpers as pah


class GridWithLines(pah.Grid):
    def __init__(self):
        super().__init__({}, 10, 10, 0)

    def mark_line(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            start, stop = min(x1, x2), max(x1, x2)
            for x in range(start, stop + 1):
                import pdb; pdb.set_trace()
                self[x, y1] += 1
        elif y1 == y2:
            start, stop = min(y1, y2), max(y1, y2)
            for y in range(start, stop + 1):
                self[x1, y] += 1
    
    def overlaps_count(self):
        return sum(1 for _, _, value in self if value >= 2)




