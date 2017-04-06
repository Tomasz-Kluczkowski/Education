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


def from_list_to_tree(cargo_list):
    args = []
    try:
        for i in range(1, 3):
            args.append(Tree(cargo_list[i]))
    except IndexError:
        pass
    if cargo_list == []:
        cargo_list.append(None)

    root = Tree(cargo_list[0], *args)
    del cargo_list[0:3]
    bot_level = [root.left, root.right]
    while len(cargo_list) > 0:
        copy = bot_level[:]
        for t in copy:
            if cargo_list[0] is None:
                t.left = None
            else:
                t.left = Tree(cargo_list[0])

            if cargo_list[1] is None:
                t.right = None
            else:
                t.right = Tree(cargo_list[1])
            del cargo_list[0:2]
            bot_level.append(t.left)
            bot_level.append(t.right)
            del bot_level[0]
    return root


def from_tree_to_list(tree):
    # takes tree as an argument and returns a list of values corresponding to the cargos in each branch
    bot_level = [tree]
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


def tree_to_file(tree, filename):
    with open(filename, "a") as file:
        cargo_list = from_tree_to_list(tree)
        for item in cargo_list:
            file.write(str(item) + "\n")


def file_to_tree(file):
    with open(file, "r") as file:
        cargo_list = file.readlines()
        cargo_list = [item.rstrip("\n") for item in cargo_list]
        print(cargo_list)
    return from_list_to_tree(cargo_list)

# TESTS FO THIS MODULE:
# # [1, 2,3, 4,5,6,7, 8,9,10,11,12,13,14,15]
#
# cargo_list = [1, 2, None, 3, 4, 5,6,7,None,8,9,10,11,None,12]
# tree = from_list_to_tree(cargo_list)
# print_tree_indented(tree)
#
# recreate_cargo_list = from_tree_to_list(tree)
# print(recreate_cargo_list)
#
# tree_to_file(tree)
#
# file_tree = file_to_tree("tree.txt")
#
# print_tree_indented(file_tree)

# tree = from_list_to_tree(['can it bark', 'can it sting', 'dog', 'bird', 'moskito'])
#
# tree = Tree(1, Tree(2), Tree(3))
# cargo_list = from_tree_to_list(tree)
# print(cargo_list)
#
# new_tree = from_list_to_tree(cargo_list)
# print_tree_indented(new_tree)
