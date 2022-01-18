import personal_aoc_helpers as pah


class GridWithLines(pah.Grid):
    def __init__(self):
        super().__init__({}, 0)
    
    def mark_line_a(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            start, stop = min(y1, y2), max(y1, y2)
            for y in range(start, stop + 1):
                self[x1, y] += 1
        elif y1 == y2:
            start, stop = min(x1, x2), max(x1, x2)
            for x in range(start, stop + 1):
                self[x, y1] += 1


    def mark_line_b(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            start, stop = min(y1, y2), max(y1, y2)
            for y in range(start, stop + 1):
                self[x1, y] += 1
        elif y1 == y2:
            start, stop = min(x1, x2), max(x1, x2)
            for x in range(start, stop + 1):
                self[x, y1] += 1
        else:
            # Lines exactly 45 degrees
            x_step = 1 if x2 > x1 else -1
            y_step = 1 if y2 > y1 else -1
            number_steps = abs(x2 - x1) + 1
            curx, cury = x1, y1
            for _ in range(number_steps):
                self[curx, cury] += 1
                curx += x_step
                cury += y_step

    
    def overlaps_count(self):
        return sum(1 for (_, _), value in self.iter_explicit_items() if value >= 2)




