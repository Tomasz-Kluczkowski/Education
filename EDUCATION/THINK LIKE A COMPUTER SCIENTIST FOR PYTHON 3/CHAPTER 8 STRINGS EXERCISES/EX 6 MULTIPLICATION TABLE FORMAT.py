#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      T Kluczlowski
#
# Created:     05/02/2017
# Copyright:   (c) T Kluczlowski 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
""" PRINT OUT MULTIPLICATION TABLE UP TO 12 X 12 """

def multiplication_table(n):
    """prints out multiplication table n x n"""
    layout = ""
    for i in range(0,n):
        layout += "{"+str(i)+":<4}"






    for row in range(1,n+1):
        list1 = []
        list1.extend(range(1,n+1))
        list1 = [i*row for i in list1]
        #print(layout.format(row,row*2,row*3,row*4,row*5,row*6,row*7,row*8,row*9,row*10,row*11,row*12))
        print(layout.format(*(list1)))

multiplication_table(25)