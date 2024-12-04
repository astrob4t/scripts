# Imports
import random
import time

# ASCII art on code start
print ('        /////////       //////////        //////////        //////////      /////////       /////////       ')
print ('       //              //      //        //                //              //              //               ')
print ('      //              //      //        ///////           ///////         ////////        /////////         ')
print ('     //              //      //        //                //              //              //                 ')
print ('    ////////        //////////        //                //              ////////        /////////           ')

# Global Vars
type = 0
percent = 0

def coffeeAddiction(type, percent):
    
    genPercent = random.randint(0, 100)
    
    # Print Stuff
    if percent >= genPercent:
        print ('Go get your', type)
        
        if type == 'Espresso':
            print ('   .-~~-.   ')
            print (' ,|`-__-\'|  ')
            print (' ||      |  ')
            print (' `|      |  ')
            print ('   `-__-\'   ')
            
        else:
            print (' c[_] ')
        
        print (percent, '>', genPercent)
    
    else:
        print ('No coffee for you, deal with the headache.')
        print (percent, '<', genPercent)


# COFFEEEEEEEEEEEEEEEEE
coffeeAddiction(
    input('What type of coffee do you want? '),
    round (float (input ('What percent chance do you want for it to tell you to get it? ')), 2)
)
