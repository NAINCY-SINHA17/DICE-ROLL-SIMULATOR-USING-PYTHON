# DICE ROLL SIMULATOR...

import random
x = 'n'

while x == 'n':
    number = random.randint(1,6)
    
    if number == 1:
          print("- - - - - ")
          print("|        |")
          print("|   0    |")
          print("|        |")
          print("- - - - - ")
          print("You got one")


    if number == 2:
        print("- - - - - ")
        print("|   0    |")
        print("|     0  |")
        print("|        |") 
        print("- - - - - ")
        print("You got Two")

    if number == 3:
       print("- - - - - ")
       print("|   0    |")
       print("|    0   |")
       print("|     0  |")
       print("- - - - - ")
       print("You got Three")


    if number == 4:
       print("- - - - - ")
       print("| 0  0   |")
       print("|        |")
       print("| 0  0   |")
       print("- - - - - ")
       print("You got Four ")


    if number == 5:
        print("- - - - -  ")
        print("|  0   0  |")
        print("|    0    |")
        print("|  0   0  |")
        print("- - - - -  ")
        print("You got Five")


    if number == 6:
          print("- - - - - ")
          print("|   0 0  |")
          print("|   0 0  |")
          print("|   0 0  |")
          print("- - - - - ") 
          print("You got Six")

    x = input ("Press n to play again and  E for exit: ") 
print("Thanks for playing!")
     
