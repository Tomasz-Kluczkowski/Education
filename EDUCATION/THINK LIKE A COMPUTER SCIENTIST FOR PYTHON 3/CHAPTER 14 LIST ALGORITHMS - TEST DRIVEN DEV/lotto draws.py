from unit_testing import test


my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]


def lotto_draw():
    """ Returns a draw of 6 numbers from 1 to 49 """

    import random
    rng = random.Random()
    draw = []

    for i in range(1,7):
        number = 0
        while number not in draw:
            number = rng.randrange(1,50)
            draw.append(number)

    return draw


def lotto_match(draw, ticket):
    """ Compares ticket to the draw, returns number of matching numbers """
    matches = 0
    for item in ticket:
        if item in draw:
            matches += 1
    return matches


def lotto_matches(draw, tickets):
    """ Checks how many matches are for each item in the list: tickets.
    Returns a list with number of matches for each ticket. """
    matches = []
    for item in tickets:
        number = lotto_match(draw, item)
        matches.append(number)
    return matches


def primes_in(ticket):
    """ Returns how many numers are prime in the ticket """
    number_of_primes = 0

    for item in ticket:
        divides_no_remainder = 0
        for i in range(1, item+1):
            if item % i == 0:
                divides_no_remainder += 1
        if divides_no_remainder == 2:
            number_of_primes += 1

    return number_of_primes


def prime_misses(ticket):
    """ Returns a list of unused primes in the list of tickets """
    list_of_primes = []
    for i in range(1,50):
        if primes_in([i]) == 1:
            list_of_primes.append(i)

    for sub_item in ticket:
        for elem in sub_item:
            if elem in list_of_primes:
                list_of_primes.remove(elem)

    return list_of_primes


"""
f.Write a function that repeatedly makes a new draw, and compares the draw to the four tickets.
i.Count how many draws are needed until one of the computer scientist’s tickets has at least 3 correct picks. Try the experiment twenty times, and average out the number of draws needed.
ii.How many draws are needed, on average, before she gets at least 4 picks correct?
iii.How many draws are needed, on average, before she gets at least 5 correct? (Hint: this might take a while. It would be nice if you could print some dots, like a progress bar, to show when each of the 20 experiments has completed.)

Notice that we have difficulty constructing test cases here, because our random numbers are not deterministic. Automated testing only really works if you already know what the answer should be!
"""

def auto_draw(tries, correct_picks):
    """ Repeatedly makes a new draw and compares to my_tickets
    Return average num_of_draws when my_tickets has 3 correct picks
    Will try 20 times and calculate the average  """
    sum_num_of_draws = 0
    for i in range(1, tries + 1):
        draw = []
        num_of_draws = 0
        while max(lotto_matches(draw, my_tickets)) < correct_picks:
            draw = lotto_draw()
            num_of_draws += 1
            if num_of_draws % 20 == 0:
                print(".", end = "")
            if num_of_draws % 1000 == 0:
                print("1000 draws checked")
        sum_num_of_draws += num_of_draws
    return (sum_num_of_draws / tries)


print(lotto_draw())


test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]), 3)
test(lotto_matches([42,4,7,11,1,13], my_tickets), [1,2,3,1])
test(primes_in([42, 4, 7, 11, 1, 13]), 3)
test(prime_misses(my_tickets), [3, 29, 47])
print(prime_misses(my_tickets))
print(auto_draw(20, 3))
