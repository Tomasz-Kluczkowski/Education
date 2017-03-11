#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      T Kluczlowski
#
# Created:     04/02/2017
# Copyright:   (c) T Kluczlowski 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("i\ti**2\ti**5\ti**10\ti**20")
for i in range(1,11):
    print(i, "\t", i**2, "\t", i**3, "\t", i**5, "\t", i**10, "\t", i**20)

layout = "{0:>4} {1:>6} {2:>6} {3:>8} {4:>13} {5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1,11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))
