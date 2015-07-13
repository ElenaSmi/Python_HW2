__author__ = 'Elena'
from random import randint
"""
Generates list 'l' with 200 random elements from 0 to 99 each;
Takes an input from user. Input should be a number from 0 to 99;
If user provides non-number prints an error;
If user provides number less then 0 or bigger then 99 prints an error;
Finds all instances of that number in a list and prints the amount and indexes of those instances.
If nothing found - prints it.

"""
def my_function():

    l = []

    for i in range(0, 200):
        number = randint(0, 99)
        l.append(number)
    print l
    condition = True
    while condition:
        try:
            x = int(raw_input("Please, enter a number from  0 to 99: "))
            if x < 0 or x > 99:
                print("Your number is out of range, try again.")
            else:
                condition = False
        except ValueError:
            print("Wrong input, try again")

    amount = 0
    for j in range(0,len(l)):
        if l[j] == x:
            print("Index is: %s") %(j)
            amount += 1

    if amount == 0:
        print("The number is not in list")
    else:
        print("Amount is: %s") %amount

if __name__ == '__main__':
    my_function()
