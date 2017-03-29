def celsius_to_fahrenheit(temp_c):
    """Converts temp_c in Celcius to Fahrenheit"""
    if temp_c < -273.15:
        return "The lowest possible temperatuer for physical matter is -273.15C"
    else:
        temp_f = temp_c * 9/5 + 32
        return temp_f

# temp_c = float(input("Please enter temperature in Celcius: "))
temperatures=[10,-20,-289,100]
for temperature in temperatures:
    print(celsius_to_fahrenheit(temperature))
