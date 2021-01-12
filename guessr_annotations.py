# invoking the import machinery using import statements
# you can import native or inherited modules
# random creates random numbers

import random

# math brings in built in math functions

import math

# Taking Inputs from the User
# lower and upper create the bounds for random module
# int is a class that designates inputs as integers
# input means that we are taking input from the User
# "enter ... bound ..." displays what the user sees

lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))

# Okey Doke! Now for the computer math!
# program is choosing a number based on inputs and 
# program gives user number of tries 
# these tries are log function base 2 of the lower subtracted from the upper plus one
# print displays message to user
# \n "example" \n starts and ends a new line of text
# \t is a tab space separator for print
# x defines what the user is inputing as a random integer 
# these integers will define the lower and upper bounds for the machine's math

x = random.randint(lower, upper)
print("\n\tYou've only", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")

# user initial guesses is set at nil

count = 0

# while creates a loop
# this loop is how many attempts the user has to guess the machine's random interger
# the integer's bounds were created in the previous code



while count < math.log(upper - lower + 1,2):
    
    # this adds one to the count of the user's attempts
    # += is addition

    count += 1

    # guess establishes a new variable for the machine to recognize
    # guess is defined as an integer
    # this integer is input by the user
    # the user sees the message Guess a number...

    guess = int(input("Guess a number:-"))
    
    # Start of If Statement for Machine

    # if the variable guess is the same as randint
    # the computer will print the message Congratulations and call the count of user inputs
    # == is to check for equality

    if x == guess:
        print("Congratulations you did it in ", count, "try")

# break statement will terminate loop and resume function
# the counst will increase as the loop terminates and function resumes

        break

        # Start If else Statement
        # first elif describes what machine will display when the loop terminates if the user input is too small

    elif x > guess:

        # print displays the string 

        print("You Guessed Too Small")

    # second elif describes what machine will display when the loop terminates if the user input is too high

    elif x < guess:
        print("You Guessed Too High")

# if the user does not guess randint == exactly before "guess" arrives at integer created from math.log
# the following two line message will display

if count >= math.log(upper - lower + 1, 2):

    # %d prints a value
    #  %x defines the value as x which was random.randint 
    # random.randint is the number the machine chose for the user to guess

    print("\nThe number is %d"%x) 
    print("\tBetter Luck Next Time!")   