class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def print_tree_indented(self, level=0):
        if self == None: return
        if self.right == None: return
        self.left.print_tree_indented(level + 1)
        print("  " * level + str(self.cargo))
        if self.right == None: return
        self.right.print_tree_indented(level + 1)

tree = Tree(1, Tree(2), Tree(3))
tree.print_tree_indented()