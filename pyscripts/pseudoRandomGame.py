import random
import time

# Make global variables
determine = 0
do = 0
output = 0

print ('     ////////      ////////////      //              //')
print ('    //   //       //        //      //              //')
print ('   ///////       //        //      //              //')
print ('  //   \\       //        //      //              //')
print (' //     \\     ////////////      ////////        //////// ')

# Crear la función.
def roll(times, length, output):

    # Vars being fixed
    determine = 0
    do = 0
    timesdone = 0

    while timesdone < times:

        determine = 0
        do = 0 
        
        while do < 5:
            determine += random.randint(1, 4)
            do += 1
            if output in ['y', 'yes']:
                print ('After', do, 'roll, the product of all rolls is now', determine)

        if determine <= 14 & determine >= 12:
          print ('You have gotten', determine, 'one of the three losing scores.')
        elif determine == 20:
          print ('You got the highest possible score, nice job')
        else:
          print ('You won with a score of', determine, '.')
          
        timesdone += 1
        time.sleep (length)

roll(int (input ('How many times do you want to roll? ')), float (input ('How many seconds do you want to wait between rolls(in seconds w/ decimals)? ')), input ('Do you want intense output [y/n]'))
