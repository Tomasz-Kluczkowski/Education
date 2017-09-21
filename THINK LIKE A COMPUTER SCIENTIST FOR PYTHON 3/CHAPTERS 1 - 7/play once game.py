#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      T Kluczlowski
#
# Created:     01/02/2017
# Copyright:   (c) T Kluczlowski 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def play_once(human_plays_first):
    """
        Must play one round of the game. If the parameter is True,
        the human gets to play first. When the round ends, the return value of
    the function is one of: -1 (human wins), 0 (game drawn), 1 (computer wins).
    """
    # this is all dummy scaffolding code right now
    import random
    rng = random.Random()
    #pick a random result between -1 and 1.
    result = rng.randrange(-1,2)

    print("Human plays first={0}, winner={1} ".format(human_plays_first, result))
    return result




""" set scores and other start values to zero"""

human_score = 0
computer_score = 0
draws = 0
game_start = True # to start the first round of the game with choice of the first player


while True:
    """ first we check if the player wants to play first for the first game only"""

    if game_start: # checks for first round of game

        player_test = input("Do you want to play first? (type yes or no)")
        human_first = player_test == "yes" # assign first player status for swapping later on

        result = play_once(human_first) # if human player choice is yes then play_once(True) is called
                                        # if not then computer plays first

    if game_start == False: # for the following rounds players swap places
                            # depending on the human choice in the first round
                            # only question now if human wants to keep playing to be able
                            # to terminate the game
        human_first = not human_first # player take turns from second round on
        result = play_once(human_first)



    if result == -1:
        human_score += 1
        print("You win!")

    if result == -0:
        print("Game drawn!")
        human_score += 1
        computer_score += 1
        draws += 1

    if result == 1:
        print("I win!")
        computer_score += 1

    percentage_human_wins = round(100 * human_score/(human_score + computer_score),1)

    print("Results:\n\n", "Human =", human_score, "(", percentage_human_wins, "%)", "Computer =", computer_score, "Draws =", draws)

    game_start = False # here we change the first game status

    player_test = input("Do you want to play again? (type yes or no)")
    if player_test == "yes":
        continue

    if player_test == "no":
        print("Goodbye")
        break










