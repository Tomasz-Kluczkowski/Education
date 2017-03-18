
# In the following 6 digit number:
# 283910
#
# 91 is the greatest sequence of 2 digits.
#
# Complete the solution so that it returns the largest five digit number found within the number given
# .. The number will be passed in as a string of only digits. It should return a five digit integer.
#  The number passed may be as large as 1000 digits.
from unit_testing import test

def solution(digits):
    """Return the largest 5 digit number in a string of digits
    :type digits: str
    """

    # check the largest possible number starting from all numbers beginning at 9
    largest = 0
    check_num = 9
    ix = 0
    while check_num > 0:
        while ix != -1:
            ix = digits.find(str(check_num), ix)
            if ix != -1:
                sub = int(digits[ix:ix+5])
                # decrementing function for inner loop
                ix += 1
                if sub > largest:
                    largest = sub

    # here we have to check if early termination is possible
            else:
                if largest > 0 and len(str(largest)) == 5:
                    return largest

    # decrementing function for main loop
        check_num = check_num - 1
    if largest > 0 and len(str(largest)) == 5:
        return largest

test(solution('1234567898765'), 98765)