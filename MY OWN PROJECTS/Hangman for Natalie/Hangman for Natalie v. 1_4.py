"""
Create a hangman game displaying in turtle module the graphics for the user since I dont know anything better at the moment.

- Can think of a difficulty level (how many syllables the word has) so that a 5 year old can still play the game with fun... DONE
- Word gets randomly selected from some list DONE
- it would be interesting to see if we can put the words into an external file which gets modified every time user adds a new word, the idea being that I can choose a word for Natalie and it gets added to the list so that it grows in size eventually - using vocabulary files from internet for this DONE
- User sees a representation of the word as a number of underscores or other sign for a placeholder for a letter in the word we are trying to guess DONE
- gather input from user (single letters alowed only and exclude those that were guessed already) DONE
- correct guess displays letter instead of the underscore DONE
- incorrect draws a part of the hangman until the whole thing is drawn and game is lost DONE
- ask for replay DONE
- if LOSS display the word anyway and then ask for replay DONE
- disallow to enter the wrong letter more than once DONE

"""

import random, turtle, string


def draw_word(guess, x_pos):
    """ Prints current guess on the trutle screen starting at position (X_pos, -200)  """
    for char in guess:
        tur_1.write(char, move=False, align="left", font=("Courier", 64, "normal"))
        tur_1.forward(74)
    tur_1.goto(x_pos,-200)


def draw_hint(letter, num_of_guesses):
    """ Prints used letter on the turtle screen. Num_of_guesses = 1 - print text message also """
    if num_of_guesses == 1:
        tur_3.goto(-600,-300)
        tur_3.write("You have used letter(s): " + letter + " ", True, align = "left", font = ("Courier", 12, "normal"))
    else:
        tur_3.write(letter + " ", True, align = "left", font = ("Courier", 12, "normal"))


def amend_guess(letter, word, guess):
    """ Finds all positions of guessed letter in word, displays them on the screen and amends current guess  """
    ix = 0
    while word.find(letter, ix) != -1:
        ix = word.find(letter, ix)
        guess = guess[:ix] + letter + guess[ix+1:]
        ix += 1
    draw_word(guess, x_pos)
    return guess


def draw_gallows():
    mr_gallows.hideturtle()
    mr_gallows.penup()
    mr_gallows.goto(150,-50)
    mr_gallows.pendown()
    mr_gallows.forward(300)
    mr_gallows.penup()
    mr_gallows.backward(150)
    mr_gallows.pendown()
    mr_gallows.left(90)
    mr_gallows.forward(300)
    mr_gallows.left(90)
    mr_gallows.forward(100)
    mr_gallows.left(90)
    mr_gallows.forward(50)


def draw_hangman(hangman_state):
    """ Draws the hangman in parts depending on current value of hangman_state """
    hangman.speed(0)
    hangman.color("pink")
    hangman.hideturtle()
    # head
    if hangman_state == 1:
        hangman.pensize(3)
        hangman.penup()
        hangman.goto(200, 200)
        hangman.pendown()
        hangman.circle(-30)
    # eyes
    elif hangman_state == 2:
        hangman.pensize(1)
        hangman.penup()
        hangman.right(90)
        hangman.forward(30)
        hangman.left(90)
        hangman.backward(15)
        hangman.pendown()
        hangman.circle(5)
        hangman.penup()
        hangman.forward(30)
        hangman.pendown()
        hangman.circle(5)
    # nose
    elif hangman_state == 3:
        hangman.penup()
        hangman.goto(195,160)
        hangman.pendown()
        hangman.forward(10)
        hangman.left(120)
        hangman.forward(10)
        hangman.left(120)
        hangman.forward(10)
    # smile
    elif hangman_state == 4:
        hangman.setheading(-55)
        hangman.penup()
        hangman.goto(188,155)
        hangman.pendown()
        hangman.circle(15, 120)
    # neck
    elif hangman_state == 5:
        hangman.pensize(5)
        hangman.setheading(0)
        hangman.penup()
        hangman.goto(200, 140)
        hangman.pendown()
        hangman.right(90)
        hangman.forward(20)
    # arm 1
    elif hangman_state == 6:
        hangman.left(45)
        hangman.forward(70)
    # arm 2
    elif hangman_state == 7:
        hangman.penup()
        hangman.goto(200, 120)
        hangman.pendown()
        hangman.right(90)
        hangman.forward(70)
    # skirt
    elif hangman_state == 8:
        hangman.penup()
        hangman.goto(200, 120)
        hangman.pendown()
        hangman.goto(235, 25)
        hangman.setheading(180)
        hangman.forward(70)
        hangman.goto(200, 120)
    # leg 1
    elif hangman_state == 9:
        hangman.penup()
        hangman.goto(190, 25)
        hangman.pendown()
        hangman.setheading(270)
        hangman.forward(40)
        hangman.right(90)
        hangman.forward(20)
    # leg 2
    elif hangman_state == 10:
        hangman.penup()
        hangman.goto(210, 25)
        hangman.pendown()
        hangman.setheading(270)
        hangman.forward(40)
        hangman.left(90)
        hangman.forward(20)


def quit_prog():
    """ Quit turtle window after pressing Escape or if called by the program """
    wn.bye()


def terminate_game():
    """ Ask user a question if they would like to quit the game """
    answer = wn.textinput("Do you want to quit playing?", "Please enter y / n:\t\t\t\t\t")
    if (answer == None or answer not in ["y", "n"]):
        terminate_game()
    else:
        return answer


def win_loss(condition):
    """ If condition = 1 display Win, 0 - Loss on the screen and end game. """
    tur_2.penup()
    tur_2.goto(-600,0)
    if condition == 1:
        msg = "You Win !!!"
    else:
        msg = "You Lose !!!"
    tur_2.write(msg, move=False, align="left", font=("Times New Roman", 80, "normal"))
    draw_word(word, x_pos)


turtle.setup(1.0, 1.0, 0, 0)    # control the turtle grahics screen size and position
wn = turtle.Screen()
wn.title("Hangman for Natalie")

tur_1 = turtle.Turtle() # this turtle will draw letters
tur_1.speed(0)
tur_1.hideturtle()
tur_1.penup()

tur_2 = turtle.Turtle() # this turtle will draw win / loss screen
tur_2.speed(0)
tur_2.hideturtle()

tur_3 = turtle.Turtle() # this turtle will draw hint letters
tur_3.hideturtle()
tur_3.penup()
tur_3.speed(0)

mr_gallows = turtle.Turtle()    # this turtle will draw the gallows
mr_gallows.speed(0)
mr_gallows.pensize(5)
mr_gallows.color("brown")
draw_gallows()

hangman = turtle.Turtle()    # this turtle will draw the hangman
hangman.hideturtle()

play_again = 0
wn.onkey(quit_prog, "Escape")
wn.listen()

# continous game loop
while play_again != "n":

    used_letters = ""
    num_of_guesses = 0
    diff_lvl = 0
    hangman_state = 0
    user_quit = 0
    letter = ""
    word = ""
    guess = ""
    answer = ""
    while diff_lvl not in range(1,6):   # difficulty loop
        diff_lvl = wn.numinput("Difficulty level selection", "Please enter difficulty level 1 - 5:\t\t", 1, minval = 1, maxval = 5)
        if diff_lvl == None:
            answer = terminate_game()
        if answer == "y":
            quit_prog()
            play_again = "n"
            break
        elif answer =="n":
            continue

    while answer !="y": # answer loop
        vocab_file_handle = open("Grade " + str(int(diff_lvl)) + " vocabulary_filtered.txt", "r")
        word_list = vocab_file_handle.readlines()
        vocab_file_handle.close()

        rng = random.Random()
        word = word_list[rng.randrange(1,len(word_list))]
        word = word.replace("\n", "")
        word_lenght = len(word)
        guess = "_" * word_lenght   # initial display of the word as underscores

        # initial absolute x position of tur_1 to keep the word nicely in the middle of the screen
        x_pos = -(len(guess) * 74) / 2
        tur_1.goto(x_pos,-200)

        draw_word(guess, x_pos)

        # loop for guessing all the letters
        while guess != word:

            letter = wn.textinput("Guess the word !", "Please enter a letter that is in the word:")
            if letter == "quit":     # for debug  or quick escape
                user_quit = 1
                break
            if letter == None:
                continue
            if len(letter) == 1 and letter in string.ascii_lowercase and letter not in used_letters:
                used_letters += letter

                if letter in word:
                    guess = amend_guess(letter, word, guess)
                    num_of_guesses += 1
                    draw_hint(letter, num_of_guesses)
                    if guess == word:
                        win = 1
                else:
                    hangman_state += 1 # draw next element of the hangman
                    draw_hangman(hangman_state)
                    num_of_guesses += 1
                    draw_hint(letter, num_of_guesses)
                    if hangman_state == 10:
                        win = 0
                        break
            else:
                continue    # ask user to type a letter again
        if user_quit == 0:
            win_loss(win)         # call to display WIN / LOSS

        # continue game? loop
        while True:
            play_again = wn.textinput("Do you want to play again?", "Please enter y / n:\t\t\t\t\t")
            if play_again == None:
                continue
            elif play_again == "y":
                hangman.reset()
                hangman.hideturtle()
                tur_1.clear()
                tur_2.clear()
                tur_3.clear()
                break
            elif play_again == "n":
                answer = "y"    # terminates answer loop above
                quit_prog()
                break
