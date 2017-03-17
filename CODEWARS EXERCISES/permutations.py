def permutations(string):

    import itertools

    list_1 = []
    word = ""
    iter_1 = itertools.permutations(string)
    for item in iter_1:
        word = ""
        for letter in item:
            word += letter
        if word in list_1:
            continue
        list_1.append(word)
    return  list_1

print(permutations("abcdefgh"))