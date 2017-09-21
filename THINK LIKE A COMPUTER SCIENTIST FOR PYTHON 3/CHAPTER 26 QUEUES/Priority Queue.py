import datetime
import random


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item
# q = PriorityQueue()
# for num in ["a", "f", "z", "b"]:
#     q.insert(num)
#
# while not q.is_empty():
#     print(q.remove())

# class Golfer:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def __str__(self):
#         return "{0:16}: {1}".format(self.name, self.score)
#
#     def __gt__(self, other):
#         return self.score < other.score # less is more in Golf game

# tiger = Golfer("Tiger Woods", 61)
# phil = Golfer("Phil Mickelson", 72)
# hal = Golfer("Hal Sutton", 69)
#
# pq = PriorityQueue()
# for g in [tiger, phil, hal]:
#     pq.insert(g)
#
# while not pq.is_empty():
#     print(pq.remove())


pq = PriorityQueue()
rng = random.Random()

t0 = datetime.datetime.now()

for i in range(1,10000):
    pq.insert(rng.randrange(1,1001))
pq.insert(5)
pq.insert(5)
pq.insert(5)
pq.insert(5)
pq.insert(50)
pq.insert(1)

t1 = datetime.datetime.now()

while not pq.is_empty():

    print(pq.remove())

t2 = datetime.datetime.now()

print("insertion time: ", t1-t0)
print("removal time: ", t2-t1)