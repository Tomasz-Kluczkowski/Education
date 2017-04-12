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


        # TODO: convert method below to classmethod for generating trees from lists
        #add None to the tree if missing elements in the list

    @classmethod
    def from_list_to_tree(cls, cargo_list):
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
                if cargo_list[0] == "None":
                    t.left = None
                else:
                    t.left = Tree(cargo_list[0])
                    bot_level.append(t.left)

                if cargo_list[1] == "None":
                    t.right = None
                else:
                    t.right = Tree(cargo_list[1])
                    bot_level.append(t.right)
                del cargo_list[0:2]
                del bot_level[0]
        return cls(root.cargo, root.left, root.right)


tree = Tree(1, Tree(2), Tree(3))

tree.print_tree_indented()
tree.print_tree_preorder()
print()
tree.print_tree_postorder()
print()
tree.print_tree_inorder()

cargo_list = [1, 2, 3, 4, 5, 6, 7]
list_tree = Tree.from_list_to_tree(cargo_list)
list_tree.print_tree_indented()