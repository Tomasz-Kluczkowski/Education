class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level + 1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level + 1)