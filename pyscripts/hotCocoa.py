import random
import time

def hotCocoa(chance):
    percent = random.randint(1, 100)
    if percent <= chance:
        print ("Get your cocoa.")
    else:
        print ("No cocoa, sorry")
    
hotCocoa(int (input ("What percent chance do you want to get cocoa? ")))