def total(Newlist):
    """ 
    To define the function 'Newlist'
    Newlist is provided in the list of integer 
    The function return the total which is given the numbers in Newlist
    """

    total = 0   # This is a variable to store the total number

    for y in Newlist:  # for every number (y) in the list of numbers (Newlist)
        total += y  # Add 'y' to the total




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
print('The answer my function given is ', multiplication(pinlist)) # To make a comparison between total and multiplication
