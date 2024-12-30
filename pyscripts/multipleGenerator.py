import random
import time

# Functions
def multOf(multiple,amount,start):
    print ("Generating", amount, "of", multiple, "starting on", start)
    
    # Vars
    i = 0
    
    while i < amount:
        current = multiple * i + start
        print (current)
        i += 1

# Get user reaquests
multOf(
    float (input ("What number do you want multiples of? ")),
    float (input ("What amount of multiples do you want? ")),
    float (input ("What number do you want to start on? "))
)    