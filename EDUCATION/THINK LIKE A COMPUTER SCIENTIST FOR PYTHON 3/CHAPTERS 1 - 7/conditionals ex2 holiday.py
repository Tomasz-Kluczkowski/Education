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
"""You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving
on day number 3 (a Wednesday). You return home after 137 sleeps. Write a general
version of the program which asks for the starting day number, and the length of your
stay, and it will tell you the name of day of the week you will return on."""

''' days are numbered from 0 to 6.
0 - sunday
1 - monday
2 - tuesday
3 - wednesday
4 - thursday
5 - friday
6 - saturday
'''

'''the best approach would be to create a list of days and slice it according to what number we get as an imput, but we have not covered this in the book yet so we are going to use chained conditionals if elif else
'''

def day_of_the_week(day):

	'''returns day of the week from start_day after number of sleeps
    use modulus operator to get the remaining amount after total number of days is divided by 7 '''

	if day%7 == 0:
		day = "Sunday"
		return day

	elif day%7== 1:
		day = "Monday"
		return day

	elif day%7 == 2:
		day = "Tuesday"
		return day

	elif day%7 == 3:
		day = "Wednesday"
		return day

	elif day%7 == 4:
		day = "Thursday"
		return day

	elif day%7 == 5:
		day = "Friday"
		return day

	else:
		day = "Saturday"
		return day

start_day = int(input("Please enter the day number: "))
sleeps = int(input("Please enter the number of sleeps: "))

last_day = day_of_the_week(start_day + sleeps)


print("You will leave on:", last_day)