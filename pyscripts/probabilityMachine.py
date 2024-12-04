import random
import time
from art import *

tprint ('Probability', font='random')
tprint (' Machine' , font='random')

percent = float (input ('What percent do you want to have to win (if over 100 will be defaulted to 2)'))

if percent > 100:
    percent = 2
    
rolled = (random.uniform(0, 100))


if rolled > percent:
    tprint('You Lost :(')
    print ('one *lonely* coffee for you')
    time.sleep (0.75)
    aprint ('coffee', number = 1, space = 0)
    print (rolled, '>', percent)
else:
    tprint ('You Won')
    print ('have some coffee')
    time.sleep(0.75)
    aprint("coffee", number=3, space=5) 