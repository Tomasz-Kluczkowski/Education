class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()
        print("]")

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        if self.cargo == None:
            return ""
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")

linklist = LinkedList()
node1 = Node(1)
node1.print_backward()
linklist.print_backward()

# def print_list(node):
#     while node is not None:
#         print(node, end=" ")
#         node = node.next
#     print()
#
# def remove_second(list):
#     if list is None: return
#     if list.next is None: return
#     second = list.next
#     first = list
#     # this makes the first node refer to the third as the
#     # second one refers to the third and now is assigned as next for the first
#     first.next = second.next
#     #separates second node from the rest (removes its link)
#     second.next = None
#     return second
#
#

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
#
# #
# node1.next = node2
# node2.next = node3
# # print_list(node1)
# node1.print_backward()
#
# removed = remove_second(node1)
# print_list(removed)
#
# print_list(node1)

