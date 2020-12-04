from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah

need = set(
    (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        "cid",
    )
)


def soln_a(data):
    valid = 0
    for entry in parse(data):
        missing = need - entry.keys()
        if len(missing) == 0:
            valid += 1
        elif len(missing) == 1:
            if "cid" in missing:
                valid += 1
    return valid


""" Part B Validation Criteria
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


def height_validation(value):
    number = int(value[:-2])
    unit = value[-2:]
    if unit == "cm":
        return 150 <= int(number) <= 193
    elif unit == "in":
        return 59 <= int(number) <= 76


HCL_VALID_SET = set("0123456789abcdef")


def hcl_validation(value):
    if len(value) != 7:
        return False
    hashtag = value[0]
    if hashtag != "#":
        return False
    rest = set(value[1:])
    if rest - HCL_VALID_SET:
        return False
    return True


ECL_VALID_SET = set(("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))

valid_functions = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": height_validation,
    "hcl": hcl_validation,
    "ecl": lambda x: x in ECL_VALID_SET,
    "pid": lambda x: len(x) == 9 and (int(x) + 1),
    "cid": lambda x: True,
}


def is_valid(key, value):
    try:
        return valid_functions[key](value)
    except Exception:
        # Something went wrong in validation, it's bad
        return False


def soln_b(data):
    valid = 0
    for entry in parse(data):
        missing = need - entry.keys()
        if len(missing) > 1:
            continue
        elif len(missing) == 1:
            if "cid" not in missing:
                continue
        valid += all(is_valid(key, value) for key, value in entry.items())
    return valid


def parse(data):
    for _, set_of_creds in enumerate(data.split("\n\n")):
        this_entry = {}
        set_of_creds = set_of_creds.strip("\n")
        for line in set_of_creds.split("\n"):
            for field in line.split(" "):
                field_name, content = field.split(":")
                this_entry[field_name] = content
        yield this_entry


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=4)
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
