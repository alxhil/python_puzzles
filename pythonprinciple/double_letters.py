# python challenge 6 #
# https://pythonprinciples.com/challenges/Double-letters/ #
# Alex Hill #

def double_letters(str_in):
    temp_str = ""
    for i in range(len(str_in)):
        if(temp_str == str_in[i]):
            return True
        else:
            temp_str = str_in[i]
    return False

