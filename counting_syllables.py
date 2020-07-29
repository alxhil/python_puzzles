#python challenge 8 #
# https://pythonprinciples.com/challenges/Counting-syllables/ #

def count(str_in):
    syllables = 0
    for i in range(len(str_in)):
        if('a' in str_in[i] or 'e' in str_in[i] or 'i' in str_in[i] or 'o' in str_in[i] or 'u' in str_in[i]):
            syllables += 1
        else:
            pass
    return syllables
