#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kilthar
#
# Created:     27-01-2017
# Copyright:   (c) Kilthar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys


def sum_of_sqares(xs):
    """count sum of squares of numbers in a list xs"""
    sum = 0
    for i in xs:
        sum +=  i**2

    return sum



def num_digits(n):

    count = 0

    if n == 0:
        return 1

    while n != 0:
        count += 1
        n = abs(n)
        n = n // 10
    return count


def num_even_digits(n):
    """counts even digits in a number"""
    count = 0
    if n == 0:
        return 1

    while n > 0:
        digit = abs(n) % 10
        if digit % 2 == 0:
            count += 1
        n = abs(n) // 10

    return count






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
    test(num_digits(120),3)
    test(num_digits(120),3)
    test(num_digits(0),1)
    test(num_digits(-12345),5)
    test(num_even_digits(123456),3)
    test(num_even_digits(2468),4)
    test(num_even_digits(1357),0)
    test(num_even_digits(0), 1)
    test(sum_of_sqares([2,3,4]),29)
    test(sum_of_sqares([]),0)
    test(sum_of_sqares([2,-3,4]),29)

test_suite()        # Here is the call to run the tests
