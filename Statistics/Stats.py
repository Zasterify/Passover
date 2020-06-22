def total(Newlist):
    """ 
    To define the function 'Newlist'
    """

    total = 0   # To create the variable to store the total number

    for y in Newlist:  # for every number (y) in the list of numbers
        total += y  # To add 'y' to the total

    return total   # To return the total


# To put any number for total             ### This is not a sample list. To make a list you have to use "[ ]" Look up how to assign a list to a variable  ###
Newlist = [3, 6]
print(total(Newlist))  # To print the total


def multiply(Randomlist):
    '''
    To define the function 'multiply'
    '''

    total = 1  # To modify the variable to store the total

    for i in Randomlist:  # for every number 'i' in the list of number
        total *= i  # To multiply i to the total

    return total  # To return the total


# To put any number as you like             ### This is not a sample list. To make a list you have to use "[ ]" Look up how to assign a list to a variable  ###
Randomlist = [3, 6, 4]
print(total(Randomlist))  # To print the total
