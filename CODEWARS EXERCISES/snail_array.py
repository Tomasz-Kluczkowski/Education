def snail(array):

    if array[0] == []:
        return []
    output = []
    row = 0
    max_row = len(array)
    col = 0
    max_col = len(array)

    while len(output) < len(array) ** 2:
        # move forward
        for i in range(col, max_col):
            output.append(array[row][i])
        row += 1
        if len(output) == len(array) ** 2:
            return output
        # move down
        for i in range(row, max_row):
            output.append(array[i][max_col - 1])
        max_col -= 1
        if len(output) == len(array) ** 2:
            return output
        # move left
        for i in range(max_col-1, col - 1, -1):
            output.append(array[max_row - 1][i])
        max_row -= 1
        if len(output) == len(array) ** 2:
            return output
        # move up
        for i in range(max_row - 1, row - 1, -1):
            output.append(array[i][col])
        col += 1
        if len(output) == len(array) ** 2:
            return output

    return output

matrix = [[]]
lista = snail(matrix)
print(lista)