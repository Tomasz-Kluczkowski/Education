from unit_testing import test


def flatten(nested_list):
    """ Returns a simple list with all elements of the nested_list """
    new_list = []
    for item in nested_list:
        if type(item) == type([]):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)

    return new_list



test(flatten([2,9,[2,1,13,2],8,[2,6]]), [2,9,2,1,13,2,8,2,6])
test(flatten([[9,[7,1,13,2],8],[7,6]]), [9,7,1,13,2,8,7,6])
test(flatten([[9,[7,1,13,2],8],[2,6]]), [9,7,1,13,2,8,2,6])
test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]),
              ["this","a","thing","a","is","a","easy"])
test(flatten([]), [])