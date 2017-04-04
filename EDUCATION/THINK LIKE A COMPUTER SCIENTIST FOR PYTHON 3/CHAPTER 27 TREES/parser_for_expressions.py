class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    # def print_tree(self):
    #     if self is None: return
    #     print(self.cargo, end=" ")
    #     print_tree(self.left)
    #     print_tree(self.right)

#preorder (prefix) root before children
def print_tree_preorder(tree):
    if tree is None: return
    print(tree.cargo, end = " ")
    print_tree_preorder(tree.left)
    print_tree_preorder(tree.right)

#postorder print - postfix
def print_tree_postorder(tree):
    if tree is None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end = " ")

#inorder print - infix (natural math notation)
def print_tree_inorder(tree):
    if tree is None: return
    print_tree_inorder(tree.left)
    print(tree.cargo, end = " ")
    print_tree_inorder(tree.right)

def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

# parser for calculator

# tokenize expression below
def create_token_list(expr):
    import re
    expr_list = re.split("([^0-9])", expr)
    expr_list.append("end")

    token_list = []
    for token in expr_list:
        if token not in ["", " "]:
            try:
                token = int(token)
            except ValueError:
                pass
            token_list.append(token)
    return token_list

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, "("):
        x = get_sum(token_list)
        if not get_token(token_list, ")"):
            raise ValueError("Missing close parenthesis")
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None)

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_product(token_list)
        return Tree("*", a, b)
    return a

def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return Tree("+", a, b)
    return a



token_list = [9,11,"end"]
x = get_number(token_list)
print_tree_postorder(x)
print(token_list)

token_list = [9, "*", 11, "end"]
tree = get_product(token_list)
print_tree_postorder(tree)
print()

token_list = [2, "*", 3, "*", 5, "*", 7, "end"]
tree = get_product(token_list)
print_tree_postorder(tree)
print()

token_list = create_token_list("9 * 11 + 5 * 7")
print(token_list)
tree = get_sum(token_list)
print_tree_postorder(tree)
print()

token_list = create_token_list("9 * (11 + 5 * 7")
print(token_list)
tree = get_sum(token_list)
print_tree_postorder(tree)




#
# tree = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))
# print_tree_preorder(tree)
# print()
# print_tree_postorder(tree)
# print()
# print_tree_indented(tree)
#
# expression = "(3 + 7) * 9"
# expr_list = create_token_list(expression)
# print(expr_list)
#
# # def total(tree):
# #     if tree is None: return 0
# #     return total(tree.left) + total(tree.right) + tree.cargo