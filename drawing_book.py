def pageCount(n, p):
    total_turns = int(n / 2)

    right_turns = int(p / 2)
        
    if right_turns > (total_turns - right_turns):
        min_turns = total_turns - right_turns
    else:
        min_turns = right_turns

    return min_turns 

print(pageCount(30, 30))

                    
