# Imports
import random

floatInput = float(input("Enter a number between 0 and 10M(can have up to two decimals): ")) # Get user input in form of float

# Make global var
randVal = 0
numbersGenerated = 0 # Counter for the amount of numbers generated

while randVal != floatInput:
    randVal = round(random.uniform(0, 10000000), 2)
    if randVal == floatInput:
        print("The number you typed: ", randVal)
    else:
        print(randVal, "is not", floatInput)
print("We generated", numbersGenerated, "numbers before we found the number you typed.") # Print the amount of numbers generated before the correct number was found
