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

def count_letters(string,letter):
    """ count how many time letter is in the string"""

    count = 0

    for char in string:
        if char == letter:
            count += 1

    return count


print(count_letters("totalitaryzm","t"))

print(count_letters("lalala","l"))







def test_suite():
    """ Run the suite of tests for code in this module (this file)."""
    test(absolute_value(17), 17)


"""
test_suite()        # Here is the call to run the tests
"""