def total(Newlist):  

    """ 
    To define the function 'Newlist'
    """

    total = 0   # To create the variable to store the total number
    
    for y in Newlist: # for every number (y) in the list of numbers
        total += y  # To add 'y' to the total

    return total   # To return the total

ExList = range(3, 6)  # To put any number for total
print(total(ExList))  # To print the total


  
