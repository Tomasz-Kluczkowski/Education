import random
import string

def generator():
    letter_1 = random.choice(string.ascii_lowercase)
    letter_2 = random.choice(string.ascii_lowercase)
    letter_3 = random.choice(string.ascii_lowercase)
    name = letter_1 + letter_2 + letter_3
    return name

print(generator())