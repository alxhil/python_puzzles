# Python Challenge 11 #
# Alex Hill #
# https://pythonprinciples.com/challenges/Minmaxing/ #

def largest_difference(list_in):
    min = 1e10
    max = 0
    for i in range(len(list_in)):
        if(list_in[i] > max):
            max = list_in[i]
        if(list_in[i] < min):
            min = list_in[i]
    return max-min