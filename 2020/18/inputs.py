inp0 = """1 + 2 * 3"""
inp1 = """1 + (2 * 3)"""
inp2 = """1 + (2 * 3) + (4 * (5 + 6))"""
inp3 = """1 + 2 * 3
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""
inputs = [inp0, inp1, inp2, inp3]