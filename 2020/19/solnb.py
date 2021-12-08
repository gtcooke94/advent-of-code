from copy import deepcopy

def follows_rule_b(rules, rule_number, original_message, depth, original_message_length):
    message = deepcopy(original_message)

    # if depth > original_message_length * 2:
    #     return False, message
    if len(message) == 0:
        return False, message
    
    rule = rules[rule_number]
    # print("==========")
    # print(rule_number)
    # print(rule)
    # print(message)
    # print(depth)
    # print(original_message_length)
    if rule == "a":
        # check it
        if message[0] == "a":
            return True, message[1:]
        else:
            return False, message
    elif rule == "b":
        if message[0] == "b":
            return True, message[1:]
        else:
            return False, message
    else:
        if len(rule) == 1:
            follows = True
            for num in rule[0]:
                depth += 1
                this_follows, message = follows_rule_b(rules, num, message, depth, original_message_length)
                follows &= this_follows
            return follows, message
        else:
            compound_rule_helper(TODO)

def compound_rule_helper(TODO):
    follows_list = [False, False]
    messages = ["", ""]
    depths = [0, 0]
    for i, sub_rule in enumerate(rule):
        follows = True
        try_depth = depth
        try_message = deepcopy(message)
        for num in sub_rule:
            try_depth += 1
            this_follows, try_message = follows_rule_b(rules, num, try_message, try_depth, original_message_length)
            follows &= this_follows
            if not follows:
                break
        # Issue - we never explore the other branch if this one works, it's returned out
        # But, we might want to because of the loop
        # if follows:
        #     return True, try_message
        follows_list[i] = follows
        messages[i] = try_message
        depths[i] = try_depth
    if all(follows_list):
        # TODO - what do I do if it succeeds at both sub rules?
        # Soln 1 let it greedily follow the first rule, then second, but with loops now what?
        # How can I continue to explore both of these?
        import pdb; pdb.set_trace()
        a = 5
    if follows_list[0]:
        return True, messages[0]
    elif follows_list[1]:
        return True, messages[1]
    else:
        return False, message
