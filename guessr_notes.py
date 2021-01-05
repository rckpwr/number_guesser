# invoking the import machinery

import random
import math

# Taking Inputs

lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))

# program is choosing a number based on inputs and 
# program gives user number of tries 

x = random.randint(lower, upper)
print("\n\tYou've only", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")

count = 0

while count < math.log(upper - lower + 1,2):
    count += 1

    guess = int(input("Guess a number:-"))
    
    if x == guess:
        print("Congratulations you did it in ", count, "try")

# break statement will terminate loop and resume function

        break
    elif x > guess:
        print("You Guessed Too Small")
    elif x < guess:
        print("You Guessed Too High")

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d"%x) 
    print("\tBetter Luck Next Time!")   