def total(Newlist):
    """ 
    To define the function 'Newlist'
    Newlist is provided in the list of integer 
    The function return the total which is given the numbers in Newlist
    """

    total = 0   # This is a variable to store the total number

    for y in Newlist:  # for every number (y) in the list of numbers (Newlist)
        total += y  # Add 'y' to the total

    return total   # Return the total when done

Newlist = [9, 5, 2]  # i create a New list so that it may allow a user to pass in 

expectedAnswer = 16 # I also save my expected answer so i can use it later

print('The answer i expect is: ', expectedAnswer) # To print the answer what i expected is right

print('The answer my function is: ', total(Newlist)) # To print the function exactly the same as the above.




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



def length(givenlist):
    
    """ 
    To define the function 'length' with the parameter called givenlist
    Givenlist is shown in the list of integer that includes in parameter
    The function return the length which represents the whole number in givenlist
    """
    total = 0 # This is a variable that stores the total

    for num in givenlist: # for every number (num) in the list of numbers (givenlist)
        total += 1  # Add num to the total
        
    return total  # return the length when done

givenlist = [2, 4, 6, 8, 10] # I produce a given list so that it perhaps allow a user to pass in
expectedAnswer = 5
print('The answer i expect is: ', expectedAnswer) # To print the answer exactly is right
print('The answer my function shown is: ', length(givenlist)) # To make a similar to total and multiplication 


def LengthSquared(givenlist):

    '''
    To define the function 'LengthSquared'
    Givenlist is produced in the list of integer
    The function return the total which is given the numbers in givenlist 
    '''

    


