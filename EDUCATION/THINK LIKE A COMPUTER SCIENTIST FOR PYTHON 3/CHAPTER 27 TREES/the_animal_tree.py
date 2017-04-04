import

def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animal():
    #start with a singleton
    root = Tree("bird")