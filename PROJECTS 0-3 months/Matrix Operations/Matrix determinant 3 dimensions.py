"""calculate determinant of a matrix m x n.
1. Find the solution for the simplest 2 x 2 matrix
    [m00, m01]
    [m10, m11]

2. matrix will be given by list of rows (nested) ie. [[a, b, c], [d, e, f], [g, h, j]]
3. find a way to calculate determinant of a 3 x 3 matrix
"""

def calc_det(m):
    """calculates determinant of the 2x2 matrix m"""

    det = m[0][0] * m[1][1] - (m[0][1] * m[1][0])
    return det

def sub_matrix(m, col):
    """creates a submatrix of m for the calculation of the determinant by removing row 0 and column col"""

    sub_m = []

    for i in range(1,3):    # swap rows

            row = m[i][0:col]+m[i][col+1:]
            sub_m.append(row)







    return sub_m


def calc_det_3_dim(m):
    """calculate determinant of the matrix m 3 x 3"""

    det = 0
    for i in range(3):


        det += ((-1) **  (2 + i)) * m[0][i] * calc_det(sub_matrix(m, i))

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
    # test(calc_det([[2, 1],[3, 4]]), 5)
    test(calc_det_3_dim(m), -12)

m = [[1 ,2, 3], [2, 3 , 1], [3, 2 ,1]]

test_suite()        # Here is the call to run the tests



print(calc_det_3_dim(m))
