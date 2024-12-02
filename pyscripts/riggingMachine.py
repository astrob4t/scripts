import random
import time
from art import *

# Set global vars
b1 = 0
b2 = 0
b3 = 0
game = 0

def decision(g1, g2, g3):

    print ('These three values must equal 100% total, if needed weigh it like 33, 33, 34.')
    b1 = float(input('Game one chance(percent)'))
    b2 = float(input('Game two chance(percent)'))
    b3 = float(input('Game three chance(percent)'))
    print ('Deciding between', g1, ',', g2, ',', g3)

    # Determine what game you want
    totalBalance = b1 + b2 + b3
    if totalBalance != 100:
        print('You entered values that total at', totalBalance, 'the script will end now')
    else:
        game = random.uniform(0, 100)

    if game < b1:
        print ('Get', g1)
    elif game < b1+b2:
        print ('Get', g2)
    elif game <= 100:
        print ('Get', g3)
    
# Get the games the user wants
print ('Enter one game per entry')
decision(
    input('What games do you need to decide from(entry 1)? '),
    input('What games do you need to decide from(entry 2)? '),
    input('What games do you need to decide from(entry 3)? ')
)
