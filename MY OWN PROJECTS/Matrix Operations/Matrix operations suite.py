from unit_testing import test

class Matrix:
    """ Generates square matrix of given size.
    Provides methods to operate on matrices """

    def __init__(self, rows, cols, fill=False):
        """If fill parameter is True then fill matrix with zeros"""

        self.rows = rows
        self.cols = cols

        self.matrix = []

        if fill == True:
            for row in range(self.rows):
                self.matrix.append([])
                for col in range(cols):
                    self.matrix[row].append(0)

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, value):
        self.matrix[index] = value

    def __len__(self):
        return len(self.matrix)

    def __str__(self):
        matrix_str = ""
        for row in range(self.rows):
            for col in range(self.cols):
                matrix_str += "{0} ".format(self.matrix[row][col])
            matrix_str += "\n"
        return matrix_str



    # def m_generator(self, low_boundary, upp_boundary):
    #     '''Generates a square matrix of size filled with random numbers from low_boundary to upp_boundary'''
    #     import  random
    #     rng = random.Random()       # create object to invoke random methods on
    #
    #     for row in range(self.size):
    #
    #         Matrix.array.append([])            # add row to the matrix
    #
    #         for col in range(self.size):
    #
    #             Matrix.array[row].append(rng.randrange(low_boundary, upp_boundary))    #add elements to the row being iterated
    #
    #     return Matrix.array


    def calc_det_2x2(self):
        """calculates determinant of the 2x2 matrix m"""

        det = self[0][0] * self[1][1] - (self[0][1] * self[1][0])

        return det


    def sub_matrix(self, col):
        """creates a submatrix (minor) of m for the calculation of the determinant
        by removing top row 0 and column col"""

        sub_m = []

        for i in range(1,len(self)):    # swap rows

            row = self[i][0:col]+self[i][col+1:]
            sub_m.append(row)

        return sub_m


    def det(self):
        """calculate determinant of the matrix m """

        determinant = 0

        if len(self) == 1:             # solution for the trivial example of matrix 1x1

            determinant = self[0][0]

        elif len(self) == 2:           # solution for matrix 2x2

            determinant = calc_det_2x2(self)

        elif len(self) > 2:            # recursive solution (laplace's expansion) for any matrix of size above 2

            for col in range(len(self)):

                determinant += ((-1) **  (2 + col)) * self[0][col] * det(sub_matrix(self, col))

        return determinant





# macierz1 = Matrix(3)
# macierz2 = Matrix(3)
#
# macierz1.m_generator(1, 10)


##def test_suite():
##    """ Run the suite of tests for code in this module (this file).
##    """
##    test(calc_det([[2, 1],[3, 4]]), 5)
##    test(calc_det_n_dim([[1, 2, 3], [2, 3 , 1], [3, 2 , 1]]), -12)
##    test(calc_det_n_dim([[5, 1, 3, 2], [4, 3, 2, 1], [2, 4, 5, 4], [2, 5, 2, 4]]), 143)
##
##test_suite()        # Here is the call to run the tests
##print(calc_det_n_dim(m_generator(10, 1, 11)))

m1 = Matrix(3,3, True)
print(m1.matrix)
print(m1)

print(m1[0][1])
m1[0][1] = 2
print(m1)

print(m1.det())