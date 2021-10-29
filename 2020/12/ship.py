class Ship:

    def __init__(self):
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.x = 0
        self.y = 0

        self.OPTIONS = {
            "N": self._move_north,
            "S": self._move_south,
            "E": self._move_east,
            "W": self._move_west,
            "F": self._move_forward,
            "R": self._rotate_cw,
            "L": self._rotate_ccw,
        } 

    def manhatten_distance(self):
        return abs(self.x) + abs(self.y)

    def move(self, option, number):
        self.OPTIONS[option](number)

    def _rotate_cw(self, degrees):
        for _ in range(degrees // 90):
            self._rotate_cw_90()

    def _rotate_ccw(self, degrees):
        for _ in range(degrees // 90):
            self._rotate_ccw_90()

    def _move_north(self, distance):
        self.waypoint_y += distance

    def _move_south(self, distance):
        self.waypoint_y -= distance

    def _move_east(self, distance):
        self.waypoint_x += distance

    def _move_west(self, distance):
        self.waypoint_x -= distance

    def _move_forward(self, times):
        # move to the waypoint times
        for _ in range(times):
            self.x += self.waypoint_x
            self.y += self.waypoint_y

    def _rotate_cw_90(self):
        # waypoint coordinates are really always treating the ship as (0, 0). Easy to rotate around
        self.waypoint_x = -self.waypoint_x
        self.waypoint_x, self.waypoint_y = self.waypoint_y, self.waypoint_x

    def _rotate_ccw_90(self):
        self.waypoint_x, self.waypoint_y = self.waypoint_y, self.waypoint_x
        self.waypoint_x = -self.waypoint_x