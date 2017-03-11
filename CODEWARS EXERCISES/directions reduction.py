from unit_testing import test

def dirReduc(arr):
    """ Return array with opposing directions reduced
    if south next to north - reduce
    if east next to west reduce
    after reduce - recheck """

    def is_opposite(item1, item2):
        if (item1 == "NORTH" and item2 == "SOUTH"):
            return True
        elif (item1 == "SOUTH" and item2 == "NORTH"):
            return True
        elif (item1 == "WEST" and item2 == "EAST"):
            return True
        elif (item1 == "EAST" and item2 == "WEST"):
            return True
        else:
            return False


    first_element = None
    second_element = None
    ix = 0
    while len(arr) > 1:
        if ix > len(arr) - 2:
            break

        first_element = arr[ix]
        second_element = arr[ix + 1]
        if is_opposite(first_element, second_element):
            arr = arr[0:ix] + arr[ix + 2:]
            ix = 0
        else:
            ix += 1
    return arr


test(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ["WEST"])