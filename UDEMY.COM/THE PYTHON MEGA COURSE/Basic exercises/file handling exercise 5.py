# Coding Exercise 5
# Section 5, Lecture 47
# Here's a rather challenging exercise that integrates functions, loops, conditionals, and file handling.
#
# In exercise 4, you recursively printed out converted temperature in the command line. For this exercise, please consider the same list of Celsius values again as input:
#
# temperatures=[10,-20,-289,100]
#
# Try to make a script that converts Celsius to Fahrenheit and creates a text file and stores the converted values inside the text file. Your text file content should look like this:
#
# 50.0
# -4.0
# 212.0
#
# Please don't write any message in the text file when input is lower than -273.15.

def celsius_to_fahrenheit(temp_c):
    """Converts temp_c in Celcius to Fahrenheit"""
    if temp_c > -273.15:
        temp_f = temp_c * 9/5 + 32
        return temp_f

temperatures = [10,-20,-289,100]
file = open("temp_in_F.txt", "w")
for temp in temperatures:
    if temp > -273.15:
        file.write(str(celsius_to_fahrenheit(temp)) + "\n")
file.close()