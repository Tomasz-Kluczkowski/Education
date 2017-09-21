import random

def make_random_ints(num, lower_bound, upper_bound):

    rng = random.Random()
    result = []
    for i in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
    return result

xs = list(range(1, 13))
rng = random.Random()
rng.shuffle(xs)
result = xs[:5]


def make_random_ints_no_dups(num, lower_bound, upper_bound):
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result