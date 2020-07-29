#python challenge 8 #
# https://pythonprinciples.com/challenges/Counting-syllables/ #
# Alex Hill #

def count(str_in):
    syllables = 1
    for i in range(len(str_in)):
        if(str_in[i] == '-'):
            syllables += 1
    return syllables
