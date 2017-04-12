class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def print_tree_indented(self, level=0):
        """Prints tree indented so that branches are visible since we print from top to bottom we have to print right
        branch first to visualise left branch properly. """
        if self.right is not None:
            self.right.print_tree_indented(level + 1)
        print("  " * level + str(self.cargo))
        if self.left is not None:
            self.left.print_tree_indented(level + 1)

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

    # TODO: implement class method from tree to list
    def from_tree_to_list(self):
        """ Takes tree as an argument and returns a list of values corresponding to the cargos in each branch """
        bot_level = [self]
        cargo_list = []
        while len(bot_level) > 0:
            copy = bot_level[:]
            for t in copy:
                if isinstance(t, Tree):
                    cargo_list.append(t.cargo)
                    bot_level.append(t.left)
                    bot_level.append(t.right)
                    del bot_level[0]
                else:
                    cargo_list.append(None)
                    del bot_level[0]
        return cargo_list


    @classmethod
    def from_list_to_tree(cls, cargo_list):
    """Takes a list as argument and returns Tree object"""
        args = []
        try:
            for i in range(1, 3):
                args.append(Tree(cargo_list[i]))
        except IndexError:
            pass
        # if we get empty list generate Tree with None value
        if not cargo_list:
            cargo_list.append(None)

        root = Tree(cargo_list[0], *args)
        del cargo_list[0:3]
        bot_level = [root.left, root.right]
        while len(cargo_list) > 0:
            copy = bot_level[:]
            for t in copy:
                try:
                    if cargo_list[0] == "None":
                        t.left = None
                    else:
                        t.left = Tree(cargo_list[0])
                        bot_level.append(t.left)
                except IndexError:
                    t.left = None
                try:
                    if cargo_list[1] == "None":
                        t.right = None
                    else:

                        t.right = Tree(cargo_list[1])
                        bot_level.append(t.right)
                except IndexError:
                    t.right = None
                del cargo_list[0:2]
                del bot_level[0]
        return cls(root.cargo, root.left, root.right)


# tree = Tree(1, Tree(2), Tree(3))
#
# tree.print_tree_indented()
# tree.print_tree_preorder()
# print()
# tree.print_tree_postorder()
# print()
# tree.print_tree_inorder()

cargo_list = [1, 2, 3, 4]
list_tree = Tree.from_list_to_tree(cargo_list)
list_tree.print_tree_indented()