import time
import random
from art import *

i = 0
decisions = int (input ('How many decisions do you need to make? \n'))

decide = random.randint(1, decisions)

# Trick the user into giving the script their options when it's already decided
while i < decide:
    i += 1
    print ('What do you want for decision', i)
    choseDecision = input ('')

# Finish the trick
while i < decisions:
    i += 1
    print ('What do you want for decision', i)
    chosenDecision = input ('')

# Tell the user the final decision
time.sleep(0.5)
tprint ('3', font='random')

time.sleep(0.5)
tprint ('2', font='random')

time.sleep(0.5)
tprint ('1', font='random')

time.sleep(1)
print ('The script has chosen', chosenDecision, 'as your final decision make.')
