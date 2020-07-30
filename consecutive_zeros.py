# Python Challenge 14 #
# Alex Hill #
# https://pythonprinciples.com/challenges/Consecutive-zeros/ #

def consecutive_zeros(int_in):
    zeros, maxzero = 0,0
    str_in = str(int_in)
    print(str_in)
    for i in range(len(str_in)):
        if(str_in[i] == '1'):
            zeros = 0
        else:
            zeros += 1
            if(zeros > maxzero):
                maxzero = zeros
    return maxzero

