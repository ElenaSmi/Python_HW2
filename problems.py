__author__ = 'Elena'
from random import randint

def my_function():
    """
    1. Generates list 'l' with 30 random int elements in range from 0 to 99;
    2. Computes the number of even ints in the given list 'l'; print the result.
    3. Computes the difference between the largest and smallest values in the list, without using min(), max().
    """
    l = []

    for i in range(0, 30):
        number = randint(0, 99)
        l.append(number)

    sum = 0 # sum of even numbers
    for j in range(0, len(l)):
        if l[j] % 2 == 0:
            sum += l[j]

    print "Sum of even numbers is: %s" %sum
    l.sort()
    print "Difference between max and min is: %s" %(l[-1] - l[0])

def string_parser(s, sub):
    """
    Returns the number of times that the string 'qa' appears anywhere in the given string include
    upper case letters. For example 'Qa' and 'QA' count.
    """
    low_s = s.lower()
    sub = sub.lower()
    number = low_s.count(sub, 0, len(s))


    return number

if __name__ == '__main__':
    my_function()
    print "'QA' appears in string: %s times" %string_parser("fwerfgwfqawefwQafgeQfwefaqfeq", "qa")

