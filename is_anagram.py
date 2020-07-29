# python challenge 9 #
# https://pythonprinciples.com/challenges/Anagrams/ #
# Alex Hill #


def is_anagram(in_1, in_2):
    if(len(in_1) != len(in_2)):
        return False
    for i in range(len(in_1)):
        if(in_1[i] in in_2):
            if(i == len(in_1)-1):
                return True
            else:
                in_2 = in_2.replace(in_1[i], '0', 1)
                in_1 = in_1.replace(in_1[i], '0', 1)
        else:
            return False


print(is_anagram('test', 'tess'))