class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def print_tree_indented(self, level=0):
        """Prints tree indented so that branches are visible"""
        if self.left is not None:
            self.left.print_tree_indented(level + 1)
        print("  " * level + str(self.cargo))
        if self.right is not None:
            self.right.print_tree_indented(level + 1)

    def print_tree_preorder(self):
        """Prints tree in pre-order (pre-fix) """
        print(self.cargo, end=" ")
        if self.left is not None:
            self.left.print_tree_preorder()
        if self.right is not None:
            self.right.print_tree_preorder()

    def print_tree_postorder(self):
        """Prints tree in post-order (post-fix) """
        if self.left is not None:
            self.left.print_tree_postorder()
        if self.right is not None:
            self.right.print_tree_postorder()
        print(self.cargo, end=" ")

    def print_tree_inorder(self):
        """Prints tree in in-order (in-fix) """
        if self.left is not None:
            self.left.print_tree_inorder()
        print(self.cargo, end=" ")
        if self.right is not None:
            self.right.print_tree_inorder()


tree = Tree(1, Tree(2), Tree(3))

tree.print_tree_indented()
tree.print_tree_preorder()
print()
tree.print_tree_postorder()
print()
tree.print_tree_inorder()