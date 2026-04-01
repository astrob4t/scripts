from turtle import *

tsteps = 0

for steps in range(15000):
    if tsteps == 37:
            home()
            tsteps = 0
    speed(10)
    forward(steps)
    right(30)
    tsteps += 1    