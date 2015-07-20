__author__ = 'Elena'
from random import randint

def generate_list(n, min, max):
    """
    Generates list of N integers in range from x to y
    """
    l = []

    for i in range(n):
        num = randint(min, max)
        l.append(num)

    return l


def find(l, sum):
    """
    Finds all pairs of elements from the list, whose sum equals a given value

    :param my_list:
    :param sum:
    :return: the whole pair combinations
    """
    my_dictionary = {}
    result = {}

    for i in range(len(l)):
        if l[i] in my_dictionary.keys():
            result[l[i]] = my_dictionary[l[i]]
        else:
            my_dictionary[sum - l[i]] = l[i]

    return result

if __name__ == '__main__':

    print(find(generate_list(10, 3, 10), 12))