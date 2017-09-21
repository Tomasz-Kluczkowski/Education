"""calculate determinant of a matrix m x n.
1. Find the solution for the simplest 2 x 2 matrix
    [m00, m01]
    [m10, m11]

2. matrix qill be given by list of rows (nested) ie. [[a, b, c], [d, e, f], [g, h, j]]
"""

def calc_det(m):
    """calculates determinant of the matrix m"""
    det = m[0][0] * m [1][1] - (m[0][1] * m[1][0])
    return det

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
    test(calc_det([[2, 1],[3, 4]]), 5)



test_suite()        # Here is the call to run the tests


