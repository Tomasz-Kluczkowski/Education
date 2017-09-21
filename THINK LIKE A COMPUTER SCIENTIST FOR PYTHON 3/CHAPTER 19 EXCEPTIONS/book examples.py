# filename = input("Enter a file name: ")
# try:
#     f = open(filename, "r")
# except:
#     print("There is no file named", filename)

# def exists(filename):
#     try:
#         f = open(filename)
#         f.close()
#         return True
#     except:
#         return False

# def get_age():
#     age = int(input("Please enter your age: "))
#     if age < 0:
#         #create a new instance of an exception
#         my_error = ValueError("{0} is not a valid age".format(age))
#         raise my_error
#     return age

# def recursion_depth(number):
#     print("Recursion depth number", number)
#     try:
#         recursion_depth(number + 1)
#     except:
#         print("\nI cannot go any deeper into this wormhole.")

import turtle
import time

def show_poly():
    try:
        win = turtle.Screen()
        tess = turtle.Turtle()

        n = int(input("How many sides do you want in your polygon?"))
        angle = 360 / n
        for i in range(n):
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)
    finally:
        win.bye()

show_poly()
show_poly()
show_poly()


