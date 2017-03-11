"""
1. Dice Rolling Simulator

The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.) The program will print what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.
"""

import random

rng = random.Random()

while True:
    result = rng.randrange(1,7)
    print("Result of a dice D6 roll is: {0}".format(result))
    choice = input("Would you like to make another roll (y / n) ?")
    if choice =="n":
        print("Good bye")
        break
