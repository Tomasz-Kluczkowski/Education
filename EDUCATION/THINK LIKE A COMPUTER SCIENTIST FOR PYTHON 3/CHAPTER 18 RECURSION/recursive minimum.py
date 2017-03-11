from unit_testing import test

def recursive_min(nested_list):
    """ Returns the smallest value in a nested list """
    minimum = None
    first_run = True

    for item in nested_list:

        if type(item) == type([]):
            val = recursive_min(item)

        else:
            val = item


        if first_run or val < minimum:
            minimum = val
            first_run = False
    return minimum


test(recursive_min([2, 9, [1, 13], 8, 6]), 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]), 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]), -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]), -13)




