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


# i create a New list so that it may allow a user to pass in
Newlist = [9, 5, 2]
expectedAnswer = 16  # I also save my expected answer so i can use it later
# To print the answer what i expected is right
print('The answer i expect is: ', expectedAnswer)
# To print the function exactly the same as the above.
print('The answer my function is: ', total(Newlist))


def multiplication(pinlist):
    '''
    To define the function which multiplies to a given number
    Pinlist is given in the list of integer that consists of parameter
    The function return the product which is given the whole numbers in pinlist
    '''
    total = 1  # This is a variable that stores the product.

    for s in pinlist:  # For every number (s) in the list of numbers (pinist)
        total *= s  # Multiply total to the given number

    return total  # To return the total when done


# i produce a pin list so that it might permit a user to pass in
pinlist = [7, 1, 2]
consideredAnswer = 14  # Also i save my considered answer so that i can use it again later
# To print the answer exactly is correct
print('The answer i consider is ', consideredAnswer)
# To make a comparison between total and multiplication
print('The answer my function given is ', multiplication(pinlist))


def length(givenlist):
    """ 
    To define the function 'length' with the parameter called givenlist
    Givenlist is shown in the list of integer that includes in parameter
    The function return the length which represents the whole number in givenlist
    """
    total = 0  # This is a variable that stores the total

    # for every number (num) in the list of numbers (givenlist)
    for num in givenlist:
        total += 1  # Add num to the total

    return total  # return the length when done

<<<<<<< Updated upstream

# I produce a given list so that it perhaps allow a user to pass in
givenlist = [2, 4, 6, 8, 10]
expectedAnswer = 5
# To print the answer exactly is right
print('The answer i expect is: ', expectedAnswer)
# To make a similar to total and multiplication
print('The answer my function shown is: ', length(givenlist))
=======
givenlist = [2, 4, 6, 8, 10] # I produce a given list so that it perhaps allow a user to pass in
expectedAnswer = 5  # I also save my expected answer so i can use it later
print('The answer i expect is: ', expectedAnswer) # To print the answer exactly is right
print('The answer my function shown is: ', length(givenlist)) # To make a similar to total and multiplication 
>>>>>>> Stashed changes


def LengthSquared(givenlist):
    '''
    To define the function 'LengthSquared'
    Givenlist is produced in the list of integer
    The function return the total which is given the numbers in givenlist 
    '''

    total = 0  # This is a variable to store the total number

    # for every number (t) in the list of numbers (givenlist)
    for t in givenlist:
        total += 1  # Add t to the total
<<<<<<< Updated upstream
=======
        
    return total ** 2  # To return the total by exponent of two

givenlist = [1, 3, 5, 4, 7, 5]  # i create a givenlist so that it may allow a user to pass in

consideredAnswer = 36 # Also i save my considered answer so that i can use it again later
>>>>>>> Stashed changes

    return total * total  # To return the total

<<<<<<< Updated upstream

# i create a givenlist so that it may allow a user to pass in
givenlist = [1, 3, 5, 4, 7, 5]
consideredAnswer = 36  # Also i save my considered answer so that i can use it again later
# To print the answer what i considered is correct
print("The answer i considered is: ", consideredAnswer)
# To print the function exactly the same as the above.
print("The answer my function is: ", LengthSquared(givenlist))
=======
print("The answer my function is: ", LengthSquared(givenlist)) # To print the function exactly the same as the above


def LengthHalved(givenlist):

    """
    To define the function 'LengthHalved'
    Givenlist is produced in the list of integer
    The function return half of the length of the list
    """

    total = 0  # This is a variable that stores the total

    for f in givenlist: # for every numbeers 'm' in the list of numbers (givenlist)
        total += 1  # Add m to the total

    if total % 2 == 0: 
        return total / 2 # if the length is even   
    else:   
        return (total // 2) + 1 # if the length is odd

givenlist = [3, 2, 1] # I produce a given list so that it perhaps allow a user to pass in
expectedAnswer = 3  # I also save my expected answer so i can use it later3
print("The answer i expected is: ", expectedAnswer)  # To print the answer exactly is right
print("The answer my function is: ", LengthHalved(givenlist)) # To print the function exactly the same as the above
>>>>>>> Stashed changes
