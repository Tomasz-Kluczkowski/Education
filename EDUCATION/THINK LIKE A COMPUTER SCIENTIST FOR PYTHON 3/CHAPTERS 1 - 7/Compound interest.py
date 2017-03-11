#-------------------------------------------------------------------------------
# Name:        First program ever
# Purpose:
#
# Author:      Kilthar
#
# Created:     17-01-2017
# Copyright:   (c) Kilthar 2017
# Licence:     <your licence>
#------------------------------------------------------------------------------
'''The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
formula for compound interest
Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the money will be# compounded for. Calculate and print the final amount after t years.'''


P = 10
n = 12
r = 0.08
t = int(input("please enter number of years"))
A = P*(1+r/n)**(n*t)
print("Total amount after", t,"years =", A)

