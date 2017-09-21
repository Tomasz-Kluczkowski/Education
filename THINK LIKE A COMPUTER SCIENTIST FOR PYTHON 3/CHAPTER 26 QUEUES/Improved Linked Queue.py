import datetime
t1 = datetime.datetime.now()

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        if self.cargo == None:
            return ""
        return str(self.cargo)

    def print_backward(self):
        first_node = self
        if self.next is not None: #if not last item which does not have next defined
            tail = self.next      #move to the next item, print nothing
            tail.print_backward() #call to print tail recursively until we reach
        print(self.cargo, end=" ") #print item with no next defined
        if self is not first_node:
            print(",", end=" ")

class Queue:

    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            #if list is empty the new node is head and last
            self.head = self.last = node
        else:
            # find the last node in the list
            last = self.last
            # append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

qu = Queue()
for cargo in range(1,100000):
    qu.insert(cargo)

while not qu.is_empty():
    print(qu.remove())

t2 = datetime.datetime.now()
print(t2-t1)