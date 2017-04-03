import random
import datetime



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

class PriorityQueueLinked:
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        # if queue is empty, insert as first item,
        # head and last is the inserted node
        if self.head == None:
            self.head = node
            self.last = node
            self.length += 1
        # find where to fit the following cargo in the priority order
        else:
            # when there is only one node in the queue
            # initial setting for comparison
            # we need to keep track of the node before the one we are currently comparing to
            curr_node = self.head
            previous_node = None
            while curr_node is not None:
                # if greater or equal than current_node move to its place
                if cargo >= curr_node.cargo:
                    # insert new node before current_node
                    # if previous_node is None we have only 1 item in the queue
                    # insert it at head
                    if previous_node == None:
                        copy = self.head
                        self.head = node
                        self.head.next = copy
                        # self.last = copy
                        self.length += 1
                        break
                    else:
                        # link new node to the previous
                        previous_node.next = node
                        # link new node to the current one
                        node.next = curr_node
                        self.length += 1
                        break
                # when cargo smaller than current head
                else:
                    # move 1 item further down the link
                    # in both previous and current nodes
                    previous_node = curr_node
                    curr_node = curr_node.next
                    # if already at the end of the link
                    if curr_node is None:
                        self.last.next = node
                        self.last = node
                        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo


t0 = datetime.datetime.now()

rng = random.Random()
pr_qu_linked = PriorityQueueLinked()
for i in range(1,10000):
    pr_qu_linked.insert(rng.randrange(1,1001))
pr_qu_linked.insert(5)
pr_qu_linked.insert(5)
pr_qu_linked.insert(5)
pr_qu_linked.insert(5)
pr_qu_linked.insert(50)
pr_qu_linked.insert(1)

t1 = datetime.datetime.now()

while not pr_qu_linked.is_empty():

    print(pr_qu_linked.remove())

t2 = datetime.datetime.now()

print("insertion time: ", t1-t0)
print("removal time: ", t2-t1)