''' days are numbered from 0 to 6. 
0 - sunday
1 - monday
2 - tuesday
3 - wednesday
4 - thursday
5 - friday
6 - saturday
write a function which when given the day number returns the day name (a string)
'''

'''the best approach would be to create a list of days and slice it according to what number we get as an imput, but we have not covered this in the book yet so we are going to use chained conditionals if elif else
'''

def day_of_the_week(day):
	
	'''returns day of the week for a given number'''
	
	if day == 0:
		day = "Sunday"
		return day
		
	elif day == 1:
		day = "Monday"
		return day

	elif day == 2:
		day = "Tuesday"
		return day
		
	elif day == 3:
		day = "Wednesday"
		return day
		
	elif day == 4:
		day = "Thursday"
		return day
		
	elif day == 5:
		day = "Friday"
		return day
		
	else:
		day = "Saturday"
		return day
		
day_number = int(input("Please enter the day number: "))

day = day_of_the_week(day_number)

print("Today is:", day)

