import re
from collections import deque

ops = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}

def addition_equal_with_multiplication(expr):
    words = expr.split(" ")
    stack = deque()
    for word in words:
        if word == ")":
            word = stack.pop()
            while stack.pop() != "(":
                continue
        stack.append(word)
        stack = eval_stack_a(stack)
    assert len(stack) == 1
    return stack[0]

def eval_stack_a(stack):
    if len(stack) < 3:
        return stack
    valid = True
    while True:
        try:
            right = int(stack[-1])
            assert stack[-2] == "+" or stack[-2] == "*"
            left = int(stack[-3])
        except:
            break

        right = int(stack.pop())
        op = stack.pop()
        left = int(stack.pop())
        stack.append(ops[op](left, right))
    return stack

def addition_before_multiplication(expr):
    words = expr.split(" ")
    stack = deque()
    for word in words:
        if word == ")":
            stack = eval_inside_paren(stack)
        else:
            stack.append(word)
        stack = try_eval(stack, set("+"))
    stack = try_eval(stack, set("*"))
    assert len(stack) == 1
    return stack[0]

def try_eval(stack, check_set):
    if len(stack) < 3:
        return stack
    while True:
        try:
            right = int(stack[-1])
            assert stack[-2] in check_set
            left = int(stack[-3])
        except:
            break
        right = int(stack.pop())
        op = stack.pop()
        left = int(stack.pop())
        stack.append(ops[op](left, right))
    return stack

def eval_inside_paren(stack):
    # The way try-eval is written, we'll end up with 1 number before the opening paren
    while stack[-2] != "(":
        # addition is evaluated greedily, there should not be any addition in here, and we can eval all multiplication
        stack = try_eval(stack, set("*"))
    # remove the parent and put the number back on
    num = stack.pop()
    stack.pop()
    stack.append(num)
    return stack

