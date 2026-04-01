### Import Stuff ###
from turtle import *

### Vars ###
tsteps = 0 # Counter for spiral reset

### The actual script ###
for steps in range(15000): # A loop, once steps becomes above number defined in range, loop ends, automatically defines steps as zero and adds one to steps each loop.

    if tsteps == 37: # Reset spiral after tsteps equals defined number, default is 37 because cool stuff happens
            home()
            tsteps = 0
    speed(10)
    forward(steps)
    right(30)
    tsteps += 1 # Adds one to tsteps so spiral actually resets on time   