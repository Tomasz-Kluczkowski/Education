import sys

def test(actual, expected):
    """ Compare the actual to the expected value,
        and print a suitable message.
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
                .format(linenum, expected, actual))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(add_vectors([1, 1], [1, 1]), [2, 2])
    test(add_vectors([1, 2], [1, 4]), [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]), [2, 6, 4])
    test(scalar_mult(5, [1,2]), [5, 10])
    test(scalar_mult(3, [1, 0, -1]), [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]), [21, 0, 35, 77, 14])
    test(dot_product([1, 1], [1, 1]), 2)
    test(dot_product([1, 2], [1, 4]), 9)
    test(dot_product([1, 2, 1], [1, 4, 3]), 12)
    test(cross_product([1, 4, -3], [-2, 3, 2]), [17, 4, 11])
    test(replace("Mississippi", "i", "I"), "MIssIssIppI")

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am"), "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a"), "I lave spam! Spam is my favarite faad. Spam, spam, yum!")



# ex 5 sum of vectors
def add_vectors(u, v):
    """sums vectors u and v and returns the sum as a result"""
    sum = []
    for i in range(len(u)):

        sum.append(u[i]+v[i])

    return sum


# ex 6 multiply vector by a scalar
def scalar_mult(s, v):
    """multiply vector v by a scalar s and return the result"""
    new_vector = []
    for i in range(len(v)):
        new_vector.append(s * v[i])

    return new_vector


# ex 7 calculate the dot product of vectors u, v
def dot_product(u, v):
    """calculate dot product of vectors u and v and return the result"""
    dot_product = 0
    for i in range(len(v)):
        dot_product += u[i] * v[i]

    return dot_product


# ex 8 calculate the cross product of vectors u and v
def cross_product(u, v):
    """calculates the cross product of 3 dimensional vectors u and v"""
    cross_product = []

   # < a2 b3 - a3 b2, -(a1 b3 - a3 b1) , a1 b2 - a2 b1 >

    cross_product.append(u[1] * v[2] - u[2] * v[1])
    cross_product.append(-(u[0] * v[2] - u[2] * v[0]))
    cross_product.append(u[0] * v[1] - u[1] * v[0])

    return cross_product


def replace(s, old, new):
    """replaces all occurences of old with new in a string s which gets returned"""
    if old not in s:
        return s

    s = s.split()

    for i in range(len(s)):
        #cuts out the old and puts new in its place for each element in the list s

        item = str(s[i])
        ix = 0
        while item.find(old) != -1:

            ix = item.find(old)
            item = item[0:ix] + new + item[ix + len(old):]

        s[i] = item

    s = " ".join(s)
    return s

test_suite()        # Here is the call to run the tests


