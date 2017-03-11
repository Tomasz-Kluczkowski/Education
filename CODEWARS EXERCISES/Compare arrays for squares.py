import test

def comp(array1, array2):
    """ Return true if elements of the second array are squares of the first """
    array1.sort()
    array2.sort()
    if (array1 or array2) == None:
        return False
    if len(array1) != len(array2):
        return False
    if (array1 or array2) == []:
        return False
    for ix in range(len(array1)):
        if array1[ix] ** 2 == array2[ix]:
            pass
        else:
            return False
    return True

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
#test.assert_equals(comp(a1, a2), True)
print(comp(a1,a2))