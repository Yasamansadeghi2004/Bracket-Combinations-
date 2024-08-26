def bracket_combinations(num, s="", curb=0):
    number = 0 
    if num == 0:
        if curb == 0:
            return[s]
        return bracket_combinations(num, s+")", curb-1)
    if curb == 0:
        return bracket_combinations(num-1, s+"(", curb+1)
    return bracket_combinations(num-1, s+"(", curb+1) + bracket_combinations(num, s+")", curb-1)
    
    




print(bracket_combinations(int(input(":"))))