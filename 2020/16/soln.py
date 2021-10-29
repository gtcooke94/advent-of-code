from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from ticket_verifier import TicketVerifier


def soln_a(data):
    ticket_verifier = TicketVerifier(*parse(data))
    return ticket_verifier.SolveA()


def soln_b(data):
    parsed_data = parse(data)
    ticket_verifier = TicketVerifier(*parse(data))
    return ticket_verifier.SolveB()

def parse(data):
    requirements, your_ticket, nearby_tickets = data.split("\n\n")
    all_reqs = {}
    for type_req in requirements.split("\n"):
        name, type_req = type_req.split(":")
        reqs = type_req.split(" or ")
        reqs = [convert_to_range(req) for req in reqs]
        all_reqs[name] = reqs

    _, your_ticket = your_ticket.split("\n")
    your_ticket = [int(i) for i in your_ticket.split(",")]

    _, nearby_tickets = nearby_tickets.split("\n", 1)
    tickets = []
    for line in nearby_tickets.split("\n"):
        ticket = [int(i) for i in line.split(",")]
        tickets.append(ticket)

    nearby_tickets = tickets

    return all_reqs, your_ticket, nearby_tickets


def convert_to_range(str):
    i, j = (int(i) for i in str.split("-"))
    j += 1
    return range(i, j)


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=16)
    answer = soln(puzzle.input_data)
    print(answer)
    if a_or_b == "a":
        puzzle.answer_a = answer
    else:
        puzzle.answer_b = answer


if __name__ == "__main__":
    a_or_b = sys.argv[1]
    soln = soln_a if a_or_b == "a" else soln_b
    inp = sys.argv[2]
    if inp == "solve":
        solve_puzzle(soln, a_or_b)
    else:
        data = inputs.inputs[int(inp)]
        print(soln(data))
