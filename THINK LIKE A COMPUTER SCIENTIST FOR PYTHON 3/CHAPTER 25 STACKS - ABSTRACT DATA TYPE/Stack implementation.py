class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

s = Stack()

s.push("(")
s.push(3)
s.push("+")
s.push(4)
s.push(")")
s.push("*")
s.push(5)

def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    for token in token_list:
        if token == "" or token == " ":
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "-":
            op_1 = stack.pop()
            op_2 = stack.pop()
            substraction = op_2 - op_1
            stack.push(substraction)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        elif token == "/":
            op_1 = stack.pop()
            op_2 = stack.pop()
            division = op_2 / op_1
            stack.push(division)
        else:
            stack.push(int(token))
    return stack.pop()
