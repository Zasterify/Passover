def parrot():
    """
    This function takes a word and a number from the user, 
    it then prints the word as many times as the number given. 
    """
    userInput = input("Enter a word here: ")  # Takes a user input for the word
    repeatNumber = int(
        input("Enter a number here: ")
    )  # Takes a user input for the number, converts to an integer
    print((userInput + " ") * repeatNumber)  # Print the word as many times as needed


parrot()  # Calls the function to run
