# python challenge 2 #
# Write a function named mid that 
# takes a string as its parameter. 
# Your function should extract and return the middle letter. 
# If there is no middle letter, your function should 
# return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa")
# should return "".
# Alex Hill #

def mid(str_in):
    if(len(str_in) % 2 == 0):
        return ""
    else:
        return str_in[round(len(str_in)/2)-1]