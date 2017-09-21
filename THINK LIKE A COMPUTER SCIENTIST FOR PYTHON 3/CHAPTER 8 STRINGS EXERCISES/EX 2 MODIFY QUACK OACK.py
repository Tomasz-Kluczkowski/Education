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
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O":
        letter += "U"
    elif letter == "Q":
        letter += "U"
    print(letter + suffix)

