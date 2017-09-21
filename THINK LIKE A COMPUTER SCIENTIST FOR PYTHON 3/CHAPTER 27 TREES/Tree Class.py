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
    operations = ["+", "-", "*", "/"]
    if tree is None: return
    try:
        if type(tree.left.cargo) is int or tree.left.cargo in operations:
            print("(", end="")
        # elif tree.left.cargo in operations:
        #     print("(", end="")
    except AttributeError:
        pass
    print_tree_inorder(tree.left)
    print(tree.cargo, end = "")
    print_tree_inorder(tree.right)
    try:
        if type(tree.right.cargo) is int or tree.right.cargo in operations:
            print(")", end="")
        # elif tree.right.cargo in operations:
        #     print(")", end="")
    except AttributeError:
        pass

def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

# parser for calculator
def create_token_list(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    token_list.append("end")
    token_list = [token for token in token_list if token not in ["", " "]]
    return token_list

tree = Tree("+", Tree("+", Tree(1), Tree(2)), Tree("*", Tree(1), Tree(2)))
print_tree_preorder(tree)
print()
print_tree_inorder(tree)
print()
print_tree_postorder(tree)
print()
print_tree_indented(tree)

expression = "(3 + 7) * 9"
expr_list = create_token_list(expression)
print(expr_list)

# def total(tree):
#     if tree is None: return 0
#     return total(tree.left) + total(tree.right) + tree.cargo