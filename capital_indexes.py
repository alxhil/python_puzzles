# python challenge 1 #
# solution is O(n) complexity #

# Write a function named capital_indexes. 
# The function takes a single parameter, 
# which is a string. Your function should return a list of 
# all the indexes in the string that have capital letters.

def capital_indexes(str_in):
    l = []
    str(str_in)
    for i in range(len(str_in)):
        if(str_in[i] == str_in[i].upper()):
            l.append(i)
    return l

capital_indexes("hElO")