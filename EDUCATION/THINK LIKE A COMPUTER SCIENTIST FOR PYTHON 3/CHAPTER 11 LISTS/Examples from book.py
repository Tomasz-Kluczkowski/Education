students = [("John", ["CompSci", "Physics"]), ("Vusi", ["Maths", "CompSci", "Stats"]),
("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

# count how many students take CompSci

counter = 0
for (name, subjects) in students:
    if "CompSci" in subjects:
        counter += 1

print("The number of students taking CompSci is", counter)


xs = [1, 2, 3, 4, 5]

for i in range(len(xs)):
    xs[i] = xs[i]**2

xs = [1, 2, 3, 4, 5]

for (i, val) in enumerate(xs):
    xs[i] = val**2


for (i, v) in enumerate(["banana", "apple", "pear", "leamon"]):
    print(i, v)


def double_stuff(a_list):
    """ overwrite each element of the list and double its value"""
    for (idx, val) in enumerate(a_list):
        a_list[idx] = 2 * val

things = [2, 5, 8]
double_stuff(things)
print(things)


mylist = []
mylist.append(5)


things = [2, 5, 8]
def double_stuff_pure(a_list):
    """return a new list with double elements from the original list"""
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)

    return new_list


def f(n):
    """Find the first positive integer between 101 and lass than n that is
    divisible by 21 """
    for i in range(101, n):
        if (i % 21 == 0):
            return i

print(f(110))
print(f(100000000000000000000000))