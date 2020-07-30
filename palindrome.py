#python challenge 13 #
# Alex Hill #
# https://pythonprinciples.com/challenges/Palindrome/ #

def palindrome(str_in):
    return (str_in == str_in[::-1])