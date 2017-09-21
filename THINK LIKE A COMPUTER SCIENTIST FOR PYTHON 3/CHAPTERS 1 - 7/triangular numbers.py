#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      T Kluczlowski
#
# Created:     31/01/2017
# Copyright:   (c) T Kluczlowski 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def print_triangular_numbers(n):
    """prints out the first n triangular numbers"""

    for i in range(n+1):
        x = i*(i+1)/2
        print(i, "\t", int(x))


print_triangular_numbers(5)