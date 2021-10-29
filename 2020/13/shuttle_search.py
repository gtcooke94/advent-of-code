from collections import defaultdict

class ShuttleSearch:
    def __init__(self, arrival_time, busses) -> None:
        self.arrival_time = arrival_time
        self.busses = busses
        self.partial_solutions = defaultdict(list)
        self.timeskip = self.busses[0]

    def _get_earliest_bus(self):
        earliest_bus = None
        current_time = self.arrival_time
        while earliest_bus is None:
            for bus in self.busses:
                if current_time % bus == 0:
                    earliest_bus = bus
                    return earliest_bus, current_time
            current_time += 1
    
    def solve(self):
        bus, time = self._get_earliest_bus()
        return (time - self.arrival_time) * bus

    def solve_b(self):
        # self.arrival_time doesn't matter for b
        # Let's try to brute force
        successes_needed = sum(b != "x" for b in self.busses)
        time = self.busses[0]
        while True:
            # Has to at least be a multiple of time
            works = 0
            for i, bus in enumerate(self.busses):
                if bus == "x":
                    continue
                if (time + i) % bus != 0:
                    break
                works += 1
            if works == successes_needed:
                return time
            else:
                # timeskipping
                # If we have two solutions that work for n busses, we know we have to skip by at least that amount, for the greatest n
                self.update_timeskip(time, works)

            time += self.timeskip
        
    # Inspired by looking at the subreddit. Keeping an increasingly large timeskip vs. just updating by the first number is the difference in solving quickly or very slowly
    def update_timeskip(self, time, partial_solution_size):
        self.partial_solutions[partial_solution_size].append(time)
        if len(self.partial_solutions[partial_solution_size]) >= 2:
            potential_timeskip = self.partial_solutions[partial_solution_size][-1] - self.partial_solutions[partial_solution_size][-2]
            self.timeskip = max(self.timeskip, potential_timeskip)