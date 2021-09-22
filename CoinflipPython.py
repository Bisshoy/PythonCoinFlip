import random 

key = input("Press ENTER to flip a coin! Input anything else to quit! ")

while (len(key) == 0): 
    num = random.randint(0, 1)
    if num == 1:
        print("HEADS!") 
        key = input("Press ENTER to flip again! Input anything else to quit! ")
    else:
        print("TAILS!") 
        key = input("Press ENTER to flip again! Input anything else to quit! ")

if len(key) != 0:
    print("Goodbye!") 

