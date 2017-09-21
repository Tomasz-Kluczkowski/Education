import random
import string

letter_input_1 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
letter_input_2 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
letter_input_3 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")


def generator():
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxz"
    letter = string.ascii_lowercase
    if letter_input_1 == "v":
        letter_1 = random.choice(vowels)
    elif letter_input_1 == "c":
        letter_1 = random.choice(consonants)
    elif letter_input_1 == "l":
        letter_1 = random.choice(letter)
    else:
        letter_1 = letter_input_1 
    
    if letter_input_2 == "v":
        letter_2 = random.choice(vowels)
    elif letter_input_2 == "c":
        letter_2 = random.choice(consonants)
    elif letter_input_2 == "l":
        letter_2 = random.choice(letter)
    else:
        letter_2 = letter_input_2 
        
    if letter_input_3 == "v":
        letter_3 = random.choice(vowels)
    elif letter_input_3 == "c":
        letter_3 = random.choice(consonants)
    elif letter_input_3 == "l":
        letter_3 = random.choice(letter)
    else:
        letter_3 = letter_input_3

    name = letter_1 + letter_2 + letter_3
    return name
for i in range(20):
    print(generator())