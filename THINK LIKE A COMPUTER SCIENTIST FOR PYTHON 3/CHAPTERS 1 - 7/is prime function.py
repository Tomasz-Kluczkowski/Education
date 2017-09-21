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


def is_prime(n):
    """returns True if integer n is prime, False otherwise"""
    for i in range(1,n):
        if n%i == 0 and i < n and i > 1:
            return False
            break
    return True





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
    test(is_prime(1),True)
    test(is_prime(2),True)
    test(is_prime(3),True)
    test(is_prime(4),False)
    test(is_prime(11),True)
    test(is_prime(13),True)
    test(not is_prime(35), True)
    test(is_prime(22),False)



test_suite()        # Here is the call to run the tests
