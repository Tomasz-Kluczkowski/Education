from unit_testing import test
import copy
import draw_queens


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)   # absolute y distance
    dx = abs(x1 - x0)   # absolute x distance
    return dx == dy     # they clash if dx == dy, share diagonal


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes with any queen to its left """
    for i in range(c):   # check at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False    # no clashes - col c has a safe placement


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def main():
    import random
    rng = random.Random()   # Instantiate a generator
    solutions = []
    solutions_symetries = []

    bd = list(range(8))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 12:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd) and (bd not in solutions):
           bd_copy = copy.deepcopy(bd)
           solutions_symetries = solutions_family(bd_copy)
           for i in range(len(solutions_symetries)):
                solutions.append(solutions_symetries[i])
           print("Found solution {0} in {1} tries.".format(bd, tries))
           draw_queens.draw_board(bd)
           tries = 0
           num_found += 1


def mirror_y(board):
    """ Mirrors board setup in Y axis, returns mirrored board. """
    new_board = board[:]
    new_board.reverse()
    return new_board


def mirror_x(board):
    """ Mirrors board setup in X axis, returns mirrored board. """
    new_board = board[:]
    for (ix, item) in enumerate(board):
        new_board[ix] = (len(board) - 1) - item

    return new_board

def rotate_left_90(board):
    """ Return board rotate 90 degrees left. """
    new_board = board[:]
    for (col, item) in enumerate(board):
        new_board[item] = (len(board)-1) - col

    return new_board

def rotate_left_180(board):
    """ Return board rotated 180 degrees left. """
    new_board = board[:]
    for i in range(2):
        new_board = rotate_left_90(new_board)

    return new_board

def rotate_left_270(board):
    """ Return board rotated 180 degrees left. """
    new_board = board[:]
    for i in range(3):
        new_board = rotate_left_90(new_board)

    return new_board

def solutions_family(board):
    """ For given solution returns family of symmetries for that solution """
    new_board = board[:]
    solutions_family = []
    solutions_family.append(new_board)
    solutions_family.append(rotate_left_90(new_board))
    solutions_family.append(rotate_left_180(new_board))
    solutions_family.append(rotate_left_270(new_board))
    solutions_family.append(mirror_y(new_board))
    solutions_family.append(mirror_y(rotate_left_270(new_board)))
    solutions_family.append(mirror_x(new_board))
    solutions_family.append(mirror_y(rotate_left_90(new_board)))

    return solutions_family





test(not share_diagonal(5,2,2,0), True)
test(share_diagonal(5,2,3,0), True)
test(share_diagonal(5,2,4,3), True)
test(share_diagonal(5,2,4,1), True)

# Solutions cases that should not have any clashes
test(not col_clashes([6,4,2,0,5], 4), True)
test(not col_clashes([6,4,2,0,5,7,1,3], 7), True)

# More test cases that should mostly clash
test(col_clashes([0,1], 1), True)
test(col_clashes([5,6], 1), True)
test(col_clashes([6,5], 1), True)
test(col_clashes([0,6,4,3], 3), True)
test(col_clashes([5,0,7], 2), True)
test(not col_clashes([2,0,1,3], 1), True)
test(col_clashes([2,0,1,3], 2), True)

# mirror in the y axis
test(mirror_y([0,2,4,6,3,5,1,7]), [7,1,5,3,6,4,2,0])
test(mirror_y([0,1,2,3,4,5,6,7]), [7,6,5,4,3,2,1,0])

test(mirror_x([0,2,4,6,3,5,1,7]), [7,5,3,1,4,2,6,0])
test(mirror_x([2,5,1,4,7,0,6,3]), [5,2,6,3,0,7,1,4])

test(rotate_left_90([2,5,1,4,7,0,6,3]), [2,5,7,0,4,6,1,3])
test(rotate_left_90([0,7,5,2,3,6,4,1]), [7,0,4,3,1,5,2,6])

test(rotate_left_180([2,5,1,4,7,0,6,3]), [4,1,7,0,3,6,2,5])
test(rotate_left_180([0,7,5,2,3,6,4,1]), [6,3,1,4,5,2,0,7])

test(rotate_left_270([2,5,1,4,7,0,6,3]), [4,6,1,3,7,0,2,5])
test(rotate_left_270([0,7,5,2,3,6,4,1]), [1,5,2,6,4,3,7,0])


board = [0,4,7,5,2,6,1,3]
print(mirror_x(board))
print(mirror_y(board))
print(rotate_left_90(board))
print(rotate_left_180(board))
print(rotate_left_270(board))

board = [0,4,7,5,2,6,1,3]
print(solutions_family(board))

main()