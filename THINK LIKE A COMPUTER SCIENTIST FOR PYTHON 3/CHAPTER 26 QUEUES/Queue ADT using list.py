import datetime
t1 = datetime.datetime.now()

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        first = self.items[0]
        del self.items[0]
        return first

qu = Queue()
for i in range(1,100000):
    qu.insert(i)

while not qu.is_empty():
    print(qu.remove())

t2 = datetime.datetime.now()
print(t2-t1)