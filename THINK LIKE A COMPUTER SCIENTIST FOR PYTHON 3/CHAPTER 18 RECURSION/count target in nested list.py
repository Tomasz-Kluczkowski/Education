from unit_testing import test


def count(target, nested_list):
    """ Return number of occurences of target in nested_list """
    occurences = 0

    for item in nested_list:
        if type(item) == type([]):
            occurences += count(target, item)

        else:
            if item == target:
                occurences += 1
    return occurences

test(count(2, []), 0)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]), 4)
test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]), 2)
test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]), 0)
test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]), 6)
test(count("a", [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]), 4)
