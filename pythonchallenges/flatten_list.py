# Python Challenge 10 #
# Alex Hill #
# https://pythonprinciples.com/challenges/Flatten-a-list/ #
def flatten(list_in):
    flattenedList = []
    for i in range(len(list_in)):
        for n in range(len(list_in[i])):
            flattenedList.append(list_in[i][n])
    return flattenedList