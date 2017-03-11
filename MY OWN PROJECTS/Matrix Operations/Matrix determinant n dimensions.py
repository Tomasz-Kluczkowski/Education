"""calculate determinant of a matrix m of size n. - done
1. Find the solution for the simplest 2 x 2 matrix - done
    [m00, m01]
    [m10, m11]

2. matrix will be given by list of rows (nested) ie. [[a, b, c], [d, e, f], [g, h, j]]
3. find a way to calculate determinant of a 3 x 3 matrix - done
4. add error handling:
    a) empty matrix (size 0)
    b) non square matrix
    c) one of the rows contains too small / too large number of items
5. add random filling of the matrix, user enters matrix size and number range to fill the items with
"""
import sys


def m_generator(size, low_boundary, upp_boundary):
    '''generates a square matrix of size filled with random numbers from low_boundary to upp_boundary'''
    import  random
    rng = random.Random()       # create object to invoke random methods on

    m = []                      # create empty matrix

    for row in range(size):

        m.append([])            # add row to the matrix

        for col in range(size):

            m[row].append(rng.randrange(low_boundary, upp_boundary))    #add elements to the row being iterated

    return m


def calc_det(m):
    """calculates determinant of the 2x2 matrix m"""

    det = m[0][0] * m[1][1] - (m[0][1] * m[1][0])

    return det


def sub_matrix(m, col):
    """creates a submatrix (minor) of m for the calculation of the determinant by removing top row 0 and column col"""

    sub_m = []

    for i in range(1,len(m)):    # swap rows

            row = m[i][0:col]+m[i][col+1:]
            sub_m.append(row)

    return sub_m


def calc_det_n_dim(m):
    """calculate determinant of the matrix m """

    det = 0

    if len(m) == 1:             # solution for the trivial example of matrix 1x1

        det = m[0][0]

    elif len(m) == 2:           # solution for matrix 2x2

        det = calc_det(m)

    elif len(m) > 2:            # recursive solution (laplace's expansion) for any matrix of size above 2

        for col in range(len(m)):

            det += ((-1) **  (2 + col)) * m[0][col] * calc_det_n_dim(sub_matrix(m, col))

    return det


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
    test(calc_det_n_dim([[1, 2, 3], [2, 3 , 1], [3, 2 , 1]]), -12)
    test(calc_det_n_dim([[5, 1, 3, 2], [4, 3, 2, 1], [2, 4, 5, 4], [2, 5, 2, 4]]), 143)

test_suite()        # Here is the call to run the tests
print(calc_det_n_dim(m_generator(10, 1, 11)))