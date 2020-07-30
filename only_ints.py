#python challenge 5 #
# https://pythonprinciples.com/challenges/Type-check/ #
# Alex Hill #

def only_ints(int_1, int_2):
    if(type(int_1) == int and type(int_2) == int):
        return True
    else:
        return False
