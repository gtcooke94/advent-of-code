from collections import defaultdict
import personal_aoc_helpers as pah

class TicketVerifier:
    def __init__(self, requirements: dict, your_ticket, nearby_tickets):
        self.requirements = requirements
        self.your_ticket = your_ticket
        self.nearby_tickets = nearby_tickets

    def CompletelyInvalidSum(self):
        all_ranges = [r for ranges in self.requirements.values() for r in ranges]
        valid_numbers = set()
        for r in all_ranges:
            valid_numbers.update(r)
        # Can't do full set, it loses out on duplicates here
        # all_ticket_numbers = set(num for ticket in self.nearby_tickets for num in ticket)
        # return all_ticket_numbers - valid_numbers
        # Let's just brute force!
        sum = 0
        for ticket in self.nearby_tickets:
            for num in ticket:
                if num not in valid_numbers:
                    sum += num

        return sum

    def SolveA(self):
        return self.CompletelyInvalidSum()

    def SolveB(self):
        valid_tickets = self.ValidTickets()
        requirement_sets = self.build_requirement_sets()
        requirement_to_index = {name: i for i, name in enumerate(self.requirements.keys())}
        index_to_requirement = {i: name for name, i in requirement_to_index.items()}
        requirement_to_index_soln = {}

        # (row, col) = (req_index, position)
        self.solution_matrix = defaultdict(lambda: True)

        for ticket in valid_tickets:
            for requirement, valid_numbers in requirement_sets.items():
                req_index = requirement_to_index[requirement]
                for position, number in enumerate(ticket):
                    if number in valid_numbers:
                        self.solution_matrix[(req_index, position)] &= True
                    else:
                        self.solution_matrix[(req_index, position)] = False


        self.mat_dim = len(self.requirements)

        while (len(requirement_to_index_soln) < len(self.requirements)):
            # Go and find single trues in each row and column, then clear that row/col
            """ Grid for inp1 X = True, . = False
            . X X
            X X X
            . . X
            So (1, 2), (2, 2) are hard requirements. Apply those, clear their rows/cols and you get
            . X .
            X . . 
            . . X
            which represents the final solution
            This assume we don't have to make then check assumptions and do a branch/check like a sudoku solver
            I haven't proved it, but I lean towards this being a fair assumption - otherwise, I think there could be multiple solutions?
            But, this is just intuition. It works for this problem anyways!
            """
            for row in range(self.mat_dim):
                row_true_count = 0
                row_true_pos = None
                for col in range(self.mat_dim):
                    if self.solution_matrix[(row, col)]:
                        row_true_count += 1
                        row_true_pos = (row, col)
                        if row_true_count > 1:
                            break 
                if row_true_count == 1:
                    requirement = index_to_requirement[row_true_pos[0]]
                    req_number = row_true_pos[1]
                    requirement_to_index_soln[requirement] = req_number 
                    # Clear the row and column
                    self._set_row_and_col_to_false(row_true_pos[0], row_true_pos[1])

            for col in range(self.mat_dim):
                col_true_count = 0
                col_true_pos = None
                for row in range(self.mat_dim):
                    if self.solution_matrix[(row, col)]:
                        col_true_count += 1
                        col_true_pos = (row, col)
                        if col_true_count > 1:
                            break 
                if col_true_count == 1:
                    requirement = index_to_requirement[col_true_pos[0]]
                    req_number = col_true_pos[1]
                    requirement_to_index_soln[requirement] = req_number 
                    # Clear the row and column
                    self._set_row_and_col_to_false(col_true_pos[0], col_true_pos[1])

        soln_mult = 1
        for requirement, index in requirement_to_index_soln.items():
            if requirement.startswith("departure"):
                soln_mult *= self.your_ticket[index]
        
        return soln_mult
            
    def _set_row_and_col_to_false(self, row, col):
        for r in range(self.mat_dim):
            self.solution_matrix[(r, col)] = False
        for c in range(self.mat_dim):
            self.solution_matrix[(row, c)] = False
        self.solution_matrix[(row, col)] = True
    
    def build_requirement_sets(self):
        requirement_sets = {}
        for name, ranges in self.requirements.items():
            requirement_sets[name] = set((num) for r in ranges for num in r)
        return requirement_sets

    def ValidTickets(self):
        all_ranges = [r for ranges in self.requirements.values() for r in ranges]
        valid_numbers = set()
        for r in all_ranges:
            valid_numbers.update(r)
        # Can't do full set, it loses out on duplicates here
        # all_ticket_numbers = set(num for ticket in self.nearby_tickets for num in ticket)
        # return all_ticket_numbers - valid_numbers
        # Let's just brute force!
        valid_tickets = []
        for ticket in self.nearby_tickets:
            valid = True
            for num in ticket:
                if num not in valid_numbers:
                    valid = False
                    break
            if valid:
                valid_tickets.append(ticket)
        return valid_tickets
    



