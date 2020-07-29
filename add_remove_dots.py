# python challenge 7 #
# https://pythonprinciples.com/challenges/Adding-and-removing-dots/ #


def add_dots(str_in):
    dot_string = ""
    for i in range(len(str_in)):
        dot_string += str_in[i]
        if(i == len(str_in) - 1):
            pass
        else:
            dot_string += "."
    return dot_string


def remove_dots(str_in):
    return str_in.replace('.', '')
