""" Usage: call function test(actual, expected) that checks if argument actual
(function with a parameter to test) matches the expected result of tested functions utput. """


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

'''
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17), 17)



test_suite()        # Here is the call to run the tests
'''