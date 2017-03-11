#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kilthar
#
# Created:     24-01-2017
# Copyright:   (c) Kilthar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""Write a function which is given an exam mark, and it returns a string â€” the grade for
that mark â€” according to this scheme:
Mark Grade
>= 75 First
[70-75) Upper Second
[60-70) Second
[50-60) Third
[45-50) F1 Supp
[40-45) F2
< 40 F3
The square and round brackets denote closed and open intervals. A closed interval includes
the number, and open interval excludes it. So 39.99999 gets grade F3, but 40 gets
grade F2. Assume
xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]
Test your function by printing the mark and the grade for all the elements in this list.

"""
def exam_mark(score):

    "returns a grade according to the score"
    if score >= 75:
        grade = "First"
        return grade

    elif score >= 70 and score < 75:
        grade = "Upper Second"
        return grade

    elif score >= 60 and score < 70:
        grade = "Second"
        return grade

    elif score >= 50 and score < 60:
        grade = "Third"
        return grade

    elif score >= 45 and score < 50:
        grade = "F1 Supp"
        return grade

    elif score >= 40 and score < 45:
        grade = "F2"
        return grade

    else:
        grade = "F3"
        return grade

marks = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in marks:
    grade = exam_mark(i)
    print("Congratulations! For scoring", i, "% in the exam you get the", grade, "grade")







xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]