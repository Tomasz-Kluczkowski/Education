"""
2. Guess the Number

The Goal: Similar to the first project, this project also uses the random module in Python. The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input information.) If the userâ€™s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. Youâ€™ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.

1. roll a random number from a specified range
2. display the range to the user
3. wait for the user to enter the number (guess)
4. count guesses and display
5. diplay if guess was too low or too high
6. if user guesses correctly display win screen
7. ask if user wants to play again
"""

import random

rng = random.Random()


def difficulty_selection():
    """ Alllows user to select difficultty level """
    error = ""
    while True:

        difficulty = input(error + "Please select difficulty level:\n{0:<12} | {1:^12} | {2:>12}".format("1 - easy "," 2 - medium ", " 3 - hard"))
        # error handling
        if difficulty not in ["1", "2", "3"]:     # eliminate incorrect inputs by asking for the correct one continously
            error = "Incorrect selection, please try again\n"
            continue
        elif int(difficulty) == 1:
            max_range = 10
        elif int(difficulty) == 2:
            max_range = 100
        else:
            max_range = 1000
        break
    return max_range

# main game section
max_range = difficulty_selection()
random_no = rng.randrange(1, max_range+1)
info = ""
no_of_tries = 0

while True:
    if next == "n":     # this is to quit program on user selection below
        break
    no_of_tries += 1
    guess = input(info + "Try to guess number between 1 and {0}".format(max_range))
    if int(guess) < random_no:
        info += "Your guess {0} was too low\n".format(guess)
    elif int(guess) > random_no:
        info += "Your guess {0} was too high\n".format(guess)
    else:
        while True:

            next = input("""Great guess !!!\n\u263A\u263A\u263A\u263A\u263A\nThe number is: {0}\nYou guessed after {1} tries.\nDo you want to play again? (y/n)""".format(random_no, no_of_tries))
            if next not in ["y", "n"]:  # incorrect selection returns us to the choice again
                continue
            elif next =="n":            # quit loop and program
                break
            else:               # set up variables for next game
                info = ""       # clean input window
                no_of_tries = 0 # reset tries counter
                break










