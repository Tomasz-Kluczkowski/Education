from unit_testing import test


class Matrix:
    """Use this class for creating and operating on matrices"""

    def __init__(self, rows=1, cols=1, fill=False, matrix=None):
        # TODO set arguments as matrix=None, rows=1, cols=1, fill=False.
        #  Then if matrix is given all the rest of the arguments can be empty
        #  and rows/cols can be obtained from the list given as matrix.
        """Create a Matrix class object of size rows x cols.
        If parameter matrix is given as a list use that for the array values.
        Alternatively if fill is True fill the array with zeroes."""

        self.rows = rows
        self.cols = cols
        if matrix == None:
            self.matrix = []
        elif isinstance(matrix, list):
            self.matrix = matrix

        if fill == True:
            self.matrix = [[0 for col in range(self.cols)] for row in range(self.rows)]

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, value):
        self.matrix[index] = value

    def append(self, item):
        return self.matrix.append(item)

    def __len__(self):
        return len(self.matrix)

    def max(self):

        return max(max(item) if isinstance(item, list) else item for item in self.matrix)

    def __str__(self):
        length_of_max_value = len(str(self.max()))
        matrix_str = ""
        for row in range(self.rows):
            for col in range(self.cols):
                matrix_str += "{0:<{width}} ".format(self.matrix[row][col], width=length_of_max_value)
            matrix_str += "\n"
        return matrix_str

    def rng_matrix_fill(self, low_boundary, upp_boundary):
        '''Fill existing Matrix object with random numbers from low_boundary to upp_boundary-1'''
        import  random
        rng = random.Random()
        self.matrix = [[rng.randrange(low_boundary, upp_boundary)
                      for col in range(self.cols)] for row in range(self.rows)]

    def det_2x2(self):
        """calculates determinant of the 2x2 matrix m"""
        determinant = self[0][0] * self[1][1] - (self[0][1] * self[1][0])
        return determinant

    def det(self):
        """calculate determinant of the matrix m """
        if self.rows != self.cols:
            print("Unable to calculate determinant. Rows != Cols")
            return None

        determinant = 0

        if len(self) == 1:  # solution for the trivial example of matrix 1x1
            determinant = self[0][0]
        elif len(self) == 2:  # solution for matrix 2x2
            determinant = self.det_2x2()
        elif len(self) > 2:  # recursive solution (laplace's expansion) for any matrix of size above 2
            for col in range(len(self)):
                determinant += ((-1) ** (2 + col)) * self[0][col] * self.sub_matrix(col).det()
        return determinant

    def sub_matrix(self, col):
        """creates a submatrix (minor) of m for the calculation of the determinant
        by removing top row 0 and column col"""
        sub_m = Matrix()
        sub_m.matrix = [self[row][0:col] + self[row][col + 1:] for row in range(1, len(self))]
        return sub_m





##def test_suite():
##    """ Run the suite of tests for code in this module (this file).
##    """
##    test(calc_det([[2, 1],[3, 4]]), 5)
##    test(calc_det_n_dim([[1, 2, 3], [2, 3 , 1], [3, 2 , 1]]), -12)
##    test(calc_det_n_dim([[5, 1, 3, 2], [4, 3, 2, 1], [2, 4, 5, 4], [2, 5, 2, 4]]), 143)
##
##test_suite()        # Here is the call to run the tests
##print(calc_det_n_dim(m_generator(10, 1, 11)))

m1 = Matrix(2,2,True)
print(m1.matrix)
print(m1)

print(m1[0][0])
m1[0][0] = 2
print(m1)

print("Determinant of m1 is = {0}".format(m1.det()))

m1 = Matrix(3,3)
m1.rng_matrix_fill(0,150)
print(m1)
print(m1.det())

print(m1.matrix)
print(type(m1.matrix))
print(m1.max())

m2 = Matrix(3,3,False,[[1,2,3],[3,6,8],[6,9,10]])
print(m2)