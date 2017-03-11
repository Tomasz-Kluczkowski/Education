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

"""
Now do the opposite: write the function c2f which converts Celcius to
Fahrenheit:
"""


def c2f(t):
    """convert Celcius to Fahrenheit"""

    return round(t * 9/5 + 32)


"""
Write the function f2c(t) designed to return the integer value of the nearest
degree Celsius for given temperature in Fahrenheit.
(hint: you may want to make use of the built-in function, round.
Try printing round.__doc__ in a Python shell or looking up help for the round
function, and experimenting with it until you are
comfortable with how it works.)
"""


def f2c(t):
    """convert farhenhait to celcius"""

    return round((t - 32) * 5/9)


"""
Write is_multiple to satisfy these unit tests:
test(is_multiple(12, 3), True)
test(is_multiple(12, 4), True)
test(is_multiple(12, 5), False)
test(is_multiple(12, 6), True)
test(is_multiple(12, 7), False)
"""

def is_multiple(x,y):
    """returns True if x can be multiplied by an integer to make 12 else
    returns False. The factor and number are reversed with function is_factor"""

    return is_factor(y,x)



"""
Write a function is_factor(f, n) that passes these tests:
An important role of unit tests is that they can also act as unambiguous
 “specifications” of what is expected. These test cases answer the question
 Do we treat 1 and 15 as factors of 15?
"""

def is_factor(f, n):
    """returns True if f is a factor of n otherwise returns False"""

    return n%f == 0

"""
Now write the function is_odd(n) that returns True when n is odd and False
otherwise. Include unit tests for this function too.
"""

def is_odd(n):
    """returns True when n is odd and False otherwise"""

    return not(is_even(n))

"""
Write a function called is_even(n) that takes an integer as an argument and returns True
if the argument is an even number and False if it is odd.
Add your own tests to the test suite.
"""

def is_even(n):
    """ takes an integer as an argument and returns True if the argument is an
    even number and False if it is odd"""
    return n%2 == 0


"""
Then use a call to slope in a new function named intercept(x1, y1, x2, y2) that
returns the y-intercept of the line through the points (x1, y1) and (x2, y2)"""

def intercept(x1,y1,x2,y2):
    """returns the y-intercept of the line through the points (x1, y1) and
     (x2, y2)"""

    return y1 - slope(x1,y1,x2,y2)*x1

"""
Write a function slope(x1, y1, x2, y2) that returns the slope of the line through the points (x1, y1) and (x2, y2). Be sure your implementation of slope can pass the following tests:
"""

def slope(x1,y1,x2,y2):
    """returns the slope of the line through the points (x1, y1) and (x2, y2)"""

    return (y2 - y1)/(x2-x1)



"""
Write a function called hypotenuse that returns the length of the hypotenuse of
 a right triangle given the lengths of the two legs as parameters:
"""


def hypotenuse(x,y):
    """returns the length of the hypotenuse of
 a right triangle given the lengths of the two legs as parameters"""

    return (x**2+y**2)**0.5


"""
Write a compare function that returns 1 if a > b, 0 if a == b, and -1 if a < b
"""


def compare(a,b):
    """returns 1 if a > b, 0 if a == b, and -1 if a < b"""

    if a > b:
        return 1

    elif a == b:
        return 0

    return -1

"""
Write three functions that are the Ã¢â‚¬Å“inversesÃ¢â‚¬Â of to_secs:
hours_in returns the whole integer number of hours represented by a total number
 of seconds.
minutes_in returns the whole integer number of left over minutes in a total
 number of seconds, once the hours have been taken out.
seconds_in returns the left over seconds represented by a total numbe
r of seconds.
You may assume that the total number of seconds passed to these functions is
an integer. Here are some test cases:

test(hours_in(9010), 2)
test(minutes_in(9010), 30)
test(seconds_in(9010), 10)
"""


def hours_in(seconds):
    """returns whole integer amount of hours in amount of seconds given"""

    return seconds//3600


def minutes_in(seconds):
    """returns the whole integer number of left over minutes in a total
 number of seconds, once the hours have been taken out."""

    return seconds//60-hours_in(seconds)*60


def seconds_in(seconds):
    """returns the left over seconds represented by a total numbe
r of seconds."""

    return seconds-hours_in(seconds)*3600-minutes_in(seconds)*60


"""
Write a function to_secs that converts hours, minutes and seconds to a total
number of seconds. Here are some tests that should pass:
Extend to_secs so that it can cope with real values as inputs. It should always
return an integer number of seconds (truncated towards zero):
"""


def to_secs(hours, minutes, seconds):
    """returns the whole integer number of left over minutes in a total
 number of seconds, once the hours have been taken out."""

    return int(hours*3600+minutes*60+seconds)


"""
Write a function days_in_month which takes the name of a month, and returns
the number of days in the month. Ignore leap years:
test(days_in_month("February"), 28)
test(days_in_month("December"), 31)
If the function is given invalid arguments, it should return None.
"""


def days_in_month(month_name):
    """given month_name returns number of days in that month"""

    if month_name == "January": #easiest solution would be to use a dictionary
        return 31

    elif month_name == "February":
        return 28

    elif month_name == "March":
        return 31

    elif month_name == "April":
        return 30

    elif month_name == "May":
        return 31

    elif month_name == "June":
        return 30

    elif month_name == "July":
        return 31

    elif month_name == "August":
        return 31

    elif month_name == "September":
        return 30

    elif month_name == "October":
        return 31

    elif month_name == "November":
        return 30

    elif month_name == "December":
        return 31

"""
Write a function that helps answer questions like Ã¢â‚¬ËœÃ¢â‚¬Å“Today is Wednesday.
I leave on holiday in 19 days time. What day will that be?Ã¢â‚¬ÂÃ¢â‚¬â„¢
So the function must take a day name and a delta argument Ã¢â‚¬â€ the number of days
 to add Ã¢â‚¬â€ and should return the resulting day name:
Hint: use the first two functions written above to help you write this one.
Can your day_add function already work with negative deltas? For example,
-1 would be yesterday, or -7 would be a week ago:
"""


def day_add(start_day, delta):
    """calculates what day will be from day_name after delta number of days"""

    return day_name((day_num(start_day)+delta)%7)



"""Write the inverse function day_num which is given a day name, and returns its
number.
Once again, if this function is given an invalid argument, it should return None"""


def day_num(day_name):
    """returns day number for a given day name"""

    if day_name == "Sunday":
        return 0

    elif day_name == "Monday":
        return 1

    elif day_name == "Tuesday":
        return 2

    elif day_name == "Wednesday":
        return 3

    elif day_name == "Thursday":
        return 4

    elif day_name == "Friday":
        return 5

    elif day_name == "Saturday":
        return 6

"""Write a function day_name that converts an integer number 0 to 6 into the name
 of a day. Assume day 0 is Ã¢â‚¬Å“SundayÃ¢â‚¬Â. Once again, return None if the arguments
to the function are not valid. Here are some tests that should pass:"""


def day_name(day_number):
    """returns day name for a given day number"""

    if day_number == 0:
        return "Sunday"

    elif day_number == 1:
        return "Monday"

    elif day_number == 2:
        return "Tuesday"

    elif day_number == 3:
        return "Wednesday"

    elif day_number == 4:
        return "Thursday"

    elif day_number == 5:
        return "Friday"

    elif day_number == 6:
        return "Saturday"




"""The four compass points can be abbreviated by single-letter strings as
ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œNÃƒÂ¢Ã¢â€šÂ¬Ã‚Â, ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œEÃƒÂ¢Ã¢â€šÂ¬Ã‚Â, ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSÃƒÂ¢Ã¢â€šÂ¬Ã‚Â, and ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œWÃƒÂ¢Ã¢â€šÂ¬Ã‚Â. Write a function turn_clockwise that takes
 one of these four compass points as its parameter, and returns the next compass
 point in the clockwise direction. Here are some tests that should pass:
test(turn_clockwise("N"), "E")
test(turn_clockwise("W"), "N")
You might ask ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œWhat if the argument to the function is some other value?ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â For
 all other cases, the function should return the value None:
test(turn_clockwise(42), None)
test(turn_clockwise("rubbish"), None)"""


def turn_clockwise(direction):
    """gives next compass point after the specified direction"""

    """since no operations on lists were introduced this version is a crude
    implementation with conditionals. The way it should be done is by reading
    the index of the argument in the list and finding the next one with
    special case when the index is the last one and the next one will be the
    first one in the list"""

    if direction == "N":    #how to force capitals only in input?
        return "E"

    elif direction == "E":
        return "S"

    elif direction == "S":
        return "W"

    elif direction == "W":
        return "N"


def absolute_value(x):   # good version
    """ Compute the absolute value of n """
    if x < 0:
        return -x
    return x


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











def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17), 17)
    test(absolute_value(-17), 17)
    test(absolute_value(0), 0)
    test(absolute_value(3.14), 3.14)
    test(absolute_value(-3.14), 3.14)
    test(turn_clockwise("N"),("E"))
    test(turn_clockwise("E"),("S"))
    test(turn_clockwise("42"),(None))
    test(turn_clockwise("rubbish"),(None))
    test(day_name(3), "Wednesday")
    test(day_name(6), "Saturday")
    test(day_name(0), "Sunday")
    test(day_name(42), None)
    test(day_num("Friday"), 5)
    test(day_num("Sunday"), 0)
    test(day_num(day_name(3)), 3)
    test(day_name(day_num("Thursday")), "Thursday")
    test(day_num("Halloween"), None)
    test(day_add("Monday", 4),  "Friday")
    test(day_add("Tuesday", 0), "Tuesday")
    test(day_add("Tuesday", 14), "Tuesday")
    test(day_add("Sunday", 100), "Tuesday")
    test(day_add("Sunday", -1), "Saturday")
    test(day_add("Sunday", -7), "Sunday")
    test(day_add("Tuesday", -100), "Sunday")
    test(days_in_month("February"), 28)
    test(days_in_month("December"), 31)
    test(to_secs(2, 30, 10), 9010)
    test(to_secs(2, 0, 0), 7200)
    test(to_secs(0, 2, 0), 120)
    test(to_secs(0, 0, 42), 42)
    test(to_secs(0, -10, 10), -590)
    test(to_secs(2.5, 0, 10.71), 9010)
    test(to_secs(2.433,0,0), 8758)
    test(hours_in(9010), 2)
    test(minutes_in(9010), 30)
    test(seconds_in(9010), 10)
    test(3 % 4, 0) #fail incorrect expected value
    test(3 % 4, 3) #pass
    test(3 / 4, 0) #fail  - incorrect expected value- should be 0.75
    test(3 // 4, 0) #pass
    test(3+4  *  2, 14) #fail should be 11
    test(4-2+2, 0) #fail should be 4
    test(len("hello, world!"), 13) #pass
    test(compare(5, 4), 1)
    test(compare(7, 7), 0)
    test(compare(2, 3), -1)
    test(compare(42, 1), 1)
    test(hypotenuse(3, 4), 5.0)
    test(hypotenuse(12, 5), 13.0)
    test(hypotenuse(24, 7), 25.0)
    test(hypotenuse(9, 12), 15.0)
    test(slope(5, 3, 4, 2), 1.0)
    test(slope(1, 2, 3, 2), 0.0)
    test(slope(1, 2, 3, 3), 0.5)
    test(slope(2, 4, 1, 2), 2.0)
    test(intercept(1, 6, 3, 12), 3.0)
    test(intercept(6, 1, 1, 6), 7.0)
    test(intercept(4, 6, 12, 8), 5.0)
    test(is_even(2), True)
    test(is_even(153), False)
    test(is_even(0), True)
    test(is_odd(3), True)
    test(is_odd(144), False)
    test(is_odd(0), False)
    test(is_factor(3, 12), True)
    test(is_factor(5, 12), False)
    test(is_factor(7, 14), True)
    test(is_factor(7, 15), False)
    test(is_factor(1, 15), True)
    test(is_factor(15, 15), True)
    test(is_factor(25, 15), False)
    test(is_multiple(12, 3), True)
    test(is_multiple(12, 4), True)
    test(is_multiple(12, 5), False)
    test(is_multiple(12, 6), True)
    test(is_multiple(12, 7), False)
    test(f2c(212), 100)     # Boiling point of water
    test(f2c(32), 0)        # Freezing point of water
    test(f2c(-40), -40)     # Wow, what an interesting case!
    test(f2c(36), 2)
    test(f2c(37), 3)
    test(f2c(38), 3)
    test(f2c(39), 4)
    test(c2f(0), 32)
    test(c2f(100), 212)
    test(c2f(-40), -40)
    test(c2f(12), 54)
    test(c2f(18), 64)
    test(c2f(-48), -54)


test_suite()        # Here is the call to run the tests
