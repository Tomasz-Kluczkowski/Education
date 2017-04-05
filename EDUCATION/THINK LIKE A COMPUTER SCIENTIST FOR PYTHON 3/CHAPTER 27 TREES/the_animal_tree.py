import record_tree_to_file

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animal():
    #start with already gained knowledge from previous questions
    try:
        root = record_tree_to_file.file_to_tree("animal_data.txt")
    except FileNotFoundError:
        root = Tree("bird")
#loop until user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # walk the tree
        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        #make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        #get new information
        prompt = "What is the animal's name? "
        animal = input(prompt)
        prompt = "What question would distinguish a {0} from a {1} ? "
        question = input(prompt.format(animal, guess))

        #add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)
    # store gained knowledge for future use
    record_tree_to_file.tree_to_file(tree, "animal_data.txt")

animal()