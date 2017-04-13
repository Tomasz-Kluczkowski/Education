"""Thank you for the subscription to OpenWeatherMap Free service!


Dear Customer,
Your account and API key are activated for operating with OpenWeatherMap Free weather services.
Endpoint for any API calls
api.openweathermap.org
Example of API call

api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=fa730d41d41ae83226a227a150d927ac

API documentation
http://openweathermap.org/api


Contact our Helpdesk info@openweathermap.org for any technical issues.


	Please, always use your API keys as &APPID=fa730d41d41ae83226a227a150d927ac in any queries.
We will refuse calls without API key or unauthorized API key. Read more http://openweathermap.org/appid#use
"""

"""
Background
If you would like to know the basics of what an API is, check out this post by iamapizza. http://www.reddit.com/r/explainlikeimfive/comments/qowts/eli5_what_is_api/c3z9kok
Goal
Create a program that pulls data from OpenWeatherMap.org that prints out information about the current weather,
such as the high, the low, and the amount of rain for wherever you live. Depending on how skilled you are, you can actually do some neat stuff with this project.
Subgoals
Print out data for the next 5-7 days so you have a 5 day/week long forecast.
Print the data to another file that you can open up and view at, instead of viewing the information in the command line.
If you know html, write a file that you can print information to so that your project is more interesting. Here is an example of the results from what I threw together.
Tips
APIs that are in Json are essentially lists and dictionaries. Remember that to reference something in a list,
you must refer to it by what number element it is in the list, and to reference a key in a dictionary, you must refer to it by it's name.
Don't like Celsius? Add &units=imperial to the end of the URL of the API to receive your data in Fahrenheit.

"""

import requests

def question():
    user_answer = ""
    while user_answer not in ["y", "yes", "n", "no"]:
        user_answer = input("Do you want to try again after enabling internet connection? ")
        if user_answer.lower() in ["y", "yes"]:
            return True
        elif user_answer.lower() in ["n", "no"]:
            return False
        else:
            # TODO: find how to clear screen here,
            # TODO: trying to use ANSI escape code but it does not work
            print("\x1B[2J")
            continue

response = {}
api_key = "fa730d41d41ae83226a227a150d927ac"
base_url = "http://api.openweathermap.org/data/2.5/weather?q={0},uk&units=metric&APPID="

# file_handle = open("weather_dict.txt", "w")
while not response:
    location = input("Please enter location: ")
    try:
        response = requests.get(base_url.format(location) + api_key)
    except requests.exceptions.ConnectionError:
        print("Unable to establish connection. Please connect to the internet")
        if question():
            continue
        else:
            break


    weather_dict = response.json()
    if weather_dict["cod"] == "404":
        print("Location not found. Please try again.\n")
        continue
    for (key, value) in weather_dict.items():
        print("{0} {1}".format(key, value))
# file_handle.writelines()