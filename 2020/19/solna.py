from copy import deepcopy

def follows_rule(rules, rule_number, original_message):
    message = deepcopy(original_message)

    # I think this is a safe thing to do to guard from infinite recursion
    if len(message) == 0:
        raise Exception("lengths can't match")
    
    rule = rules[rule_number]
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
                this_follows, message = follows_rule(rules, num, message)
                follows &= this_follows
            return follows, message
        else:
            for sub_rule in rule:
                follows = True
                try_message = deepcopy(message)
                for num in sub_rule:
                    this_follows, try_message = follows_rule(rules, num, try_message)
                    follows &= this_follows
                if follows:
                    return True, try_message
            return False, message