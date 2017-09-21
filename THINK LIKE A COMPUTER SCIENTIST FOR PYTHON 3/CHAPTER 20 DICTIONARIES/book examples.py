# eng2sp = {}
# eng2sp["one"] = "uno"
# eng2sp["two"] = "dos"
# print(eng2sp)

eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
print(eng2sp["two"])

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)
del inventory["pears"]
print(inventory)
inventory["pears"] = 0
print(inventory)
inventory["bananas"] += 200
print(inventory)
print(len(inventory))

for k in eng2sp.keys():
    print("Got key", k, "which maps to value", eng2sp[k])

ks = list(eng2sp.keys())
print(ks)

for k in eng2sp:
    print("Got key", k)

print(list(eng2sp.values()))
print(list(eng2sp.items()))

for (k, v) in eng2sp.items():
    print("Got", k, "that maps to ", v)

print("one" in eng2sp)
print("tres" in eng2sp) # in tests only for keys and not values


alreadyknown = {0 : 0, 1: 1}

def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]

print(fib(100))

letter_counts = {}
for letter in "Mississippi":
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
print(letter_counts)
letter_items = list(letter_counts.items())
letter_items.sort()
print(letter_items)