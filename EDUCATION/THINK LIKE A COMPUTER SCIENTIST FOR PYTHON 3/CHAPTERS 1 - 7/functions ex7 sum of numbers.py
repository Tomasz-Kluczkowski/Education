#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kilthar
#
# Created:     23-01-2017
# Copyright:   (c) Kilthar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""7. Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to
and including n. So sum_to(10) would be 1+2+3...+10 which would return the value
55."""

#sum = 0

def sum_to(n):

    """sums all integers up to and including n"""

    sum = 0     # have to define sum variable in the function itself before it is used in the for loop

    for i in range(n+1):

        sum = sum + i

    return sum


user_n = int(input("Please enter integer value up to which you want to calculate the sum"))

total = sum_to(user_n)

print("The sum of all integers up to and including ", user_n, "is", total)