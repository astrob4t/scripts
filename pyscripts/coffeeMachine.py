# Imports
import random
import time

# ASCII Art
print ("////////       //////////      //////////      //////////      //////////      //////////")
print ("//             //      //      //              //              //              //        ")
print ("//             //      //      //////          //////          /////////       //////////")
print ("//             //      //      //              //              //              //        ")
print ("////////       //////////      //              //              /////////       //////////")
print ('')
print ('')

# Ask what type of coffee you want
type = input ("What type of coffee are you making? ")

# Determine if you want coffee
coffee = 0
r = 1

while r <= 10:
  coffee += random.randint(0,10)
  print("Your coffee value as of this message is",coffee)
  time.sleep (0.225)
  r += 1

  # Tell the user if they get coffee
if coffee < 50:
    print('Yes, go get your', type)
    print(coffee)
else:
    print('The odds weren\'t in your favour, don\'t get your', type)
    print(coffee)