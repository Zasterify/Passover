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


def multiply(randomlist):
    '''
    Defines a function that multiplies a series of numbers provided. 
    Randomlist is a list of integer numbers passed in as a parameter
    The function returns a number that is the product of all the numbers in Randomlist
    '''

    total = 1  # A variable to keep track of the running product

    for i in randomlist:  # Iterator to go through every number passed in from the list
        total *= i  # Multiplies the running total by the given number

    return total  # When done, returns the product


## --------------------- Everything below this line is to test my code in order to make sure it works  -----------------------##

# I create an example list that a user may pass in.
exampleList = [1, 2, 3]
expectedAnswer = 6      # I save my expected answer in a variable so i can use it later

# I then print my function with my example list passed in to compare with an answer i know is right
print("The answer i expect is", expectedAnswer,
      "and the answer my function gives is", total(exampleList))




def multiplication(pinlist): 
    '''
    To define the function which multiplies to a given number
    Pinlist is given in the list of integer that consists of parameter
    The function return the product which is given the whole numbers in pinlist
    '''
    total = 1 # This is a variable that stores the product.
    
    for s in pinlist: # For every number (s) in the list of numbers (pinist)
        total *= s  # Multiply total to the given number

    return total # To return the total when done

pinlist = [7, 1, 2]  # i produce a pin list so that it might permit a user to pass in 

consideredAnswer = 14  # Also i save my considered answer so that i can use it again later 

print('The answer i consider is ', consideredAnswer) # To print the answer exactly is correct
    

