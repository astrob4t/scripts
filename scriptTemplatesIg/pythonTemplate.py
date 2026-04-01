### Import stuff ###
import random

### Variables ###
example = int(input("Give number for example. ")) # Highest number for random number
blankExample = 0 # Number to write random number to

### The Actual Script ###
blankExample = random.uniform(1, example) # Write random number to blankExample
print("A random number under " + str(example) + " is " + str(blankExample))