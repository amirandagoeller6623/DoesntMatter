import datetime as dt
import requests
import math
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "238d18d07aa46535d9f3b6c35864dbb7"
CITY = input("Enter your city (capitalize first letter): ")
def kelvin_to_celcius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius,fahrenheit
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celcius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celcius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
theInput = 0
def sortingItOut(numberOfNums, equation):
    trigNum = 0
    numberOfMultipliers = 0
    num = 1
    pemdas = []
    for x in range((numberOfNums - 1)):
        if equation[num] == 4 or equation[num] == 5 or equation[num] == 6 or equation[num] == 7 or equation[num] == 8:
            pemdas.append(num)
        num = num + 2
    rtrtr = 0
    for x in range(len(pemdas)):
        if equation[pemdas[rtrtr]] == 4:
            putInEquation = equation[(pemdas[rtrtr] - 1)] / equation[(pemdas[rtrtr] + 1)]
            # add it to the list after removing equation[pemdas[rtrtr - and + 1]]
        if equation[pemdas[rtrtr]] == 5:
            putInEquation = equation[(pemdas[rtrtr] - 1)] * equation[(pemdas[rtrtr] + 1)]
            # add it to the list after removing equation[pemdas[rtrtr - and + 1]]
        if equation[pemdas[rtrtr]] == 6:
            putInEquation = equation[(pemdas[rtrtr] - 1)] * math.sin(equation[(pemdas[rtrtr] + 1)])
            # see other comments
        if equation[pemdas[rtrtr]] == 7:
            putInEquation = equation[(pemdas[rtrtr] - 1)] * math.cos(equation[(pemdas[rtrtr] + 1)])
        if equation[pemdas[rtrtr]] == 8:
            putInEquation = equation[(pemdas[rtrtr] - 1)] * math.tan(equation[(pemdas[rtrtr] + 1)])
        rtrtr = rtrtr + 1
    print(pemdas)

def checkNum():
    numberOfNums = int(input("How many different numbers are there in your equation? "))
    equation = []
    hjhjh = 0
    for x in range(numberOfNums):
        symbol = " "
        hjhjh = hjhjh + 1
        if hjhjh == 1:
            num = int(input("Enter the first number: "))
            equation.append(num)
            while symbol == " " or symbol == 1:
                symbol = int(input("enter your math operator, type 1 for all options: "))
                if symbol == 1:
                    print("2: plus")
                    print("3: minus")
                    print("4: divided by")
                    print("5: multiplied by")
                    print("6: timesSin (note this will put the number after the equation, in the sin function)")
                    print("7: timesCos (note this will put the number after the equation, in the cos function)")
                    print("8: timesTan (note this will put the number after the equation, in the tan function)")
            equation.append(symbol)
        elif hjhjh != numberOfNums:
            num = int(input("Enter the next number: "))
            equation.append(num)
            while symbol == " " or symbol == 1:
                symbol = int(input("enter your math symbol, type 1 for all options"))
                if symbol == 1:
                    print("plus")
                    print("minus")
                    print("divided by")
                    print("multiplied by")
                    print("timesSin (note this will put the number after the equation, in the sin function)")
                    print("timesCos (note this will put the number after the equation, in the cos function)")
                    print("timesTan (note this will put the number after the equation, in the tan function)")
            equation.append(symbol)
        elif hjhjh == numberOfNums:
            num = int(input("Enter the last number: "))
            equation.append(num)
    sortingItOut(numberOfNums, equation)

while theInput != 10:
    theInput = int(input("What would you like to know? type 1 for all options: "))
    if theInput == 1:
        print("2: Calculator on a budget")
        print("3: Weather")
        print("10: Done with program")
    if theInput == 3:
        print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit}°F")
        print(f"Temperature in {CITY} feels like: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
        print(f"Humidity in {CITY}: {humidity}%")
        print(f"Wind Speed in {CITY}: {wind_speed} m/s")
        print(f"General Weather in {CITY}: {description}")
        print(f"Sun rises in {CITY} at {sunrise_time} local time.")
        print(f"Sun sets in {CITY} at {sunset_time} local time.")
    if theInput == 2:
        checkNum()
print(" ")
print("Program Ended")