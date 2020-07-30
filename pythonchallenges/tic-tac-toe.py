# Python Challenge 13 #
# Alex Hill #
# https://pythonprinciples.com/challenges/Tic-tac-toe-input/ #

def get_row_col(str_in):
    returnTupleList = []
    first = (int(str_in[1]) - 1)
    returnTupleList.append(first)
    if(str_in[0] == 'A'):
        returnTupleList.append(0)
    elif(str_in[0] == 'B'):
        returnTupleList.append(1)
    else:
        returnTupleList.append(2)
    return tuple(returnTupleList)

