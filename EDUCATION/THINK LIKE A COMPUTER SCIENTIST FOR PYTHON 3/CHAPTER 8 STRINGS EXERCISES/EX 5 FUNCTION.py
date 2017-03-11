#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      T Kluczlowski
#
# Created:     05/02/2017
# Copyright:   (c) T Kluczlowski 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""remove punctuation, break string into words, count words with letter "e".
layout: Your text contains 243 words, of which 109 (44.8%) contain an "e"
"""
import string # call string module to aid in punctuation removal

def analyze_text(text,letter):
    """removes punctuation, breaks the string into words, finds how many letters (letter) is in the text"""
    copy = ""   # create a new empty string
    for char in text:
        if char not in string.punctuation:  #if char is not in punctuation set
            copy += char                    # add it to the copy string
    copy = copy.split()                     # split the text into words
    amount_words = len(copy)                #count total number of words
    word_w_letter = 0                       # set counter for number of words containing letter given as the function parameter

    for word in copy:                       # count number of words containing letter given as the function parameter
        if letter in word:
            word_w_letter += 1

    layout = "Your text contains {0} words, of which {1} ({2:.2%}) contain an {3}".format(amount_words,word_w_letter,word_w_letter/amount_words,letter)

    print(layout)

    #print(copy, "words =", amount_words, "words with letter", letter, "=", word_w_letter)

text = """
Uwaga: Uprzejmie informujemy, iż Wydział Konsularny dodaje nowe miejca na spotkania paszportowe (na platformie e-konsulat) w dni robocze:

w poniedziałki w godzinach 10.00-10.30 oraz 20.00-20.30

od wtorku do piątku w godzinach 8.30-9.00 oraz 20.00-20.30



Brak dostępności terminów w danym dniu oznacza wykorzystanie wszystkich dostępnych miejsc, w związku z czym prosimy o podjęcie próby umówienia spotkania w kolejnym dniu roboczym rano.
"""

analyze_text(text,"e")