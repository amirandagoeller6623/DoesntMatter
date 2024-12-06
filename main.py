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
twoURL = "https://v6.exchangerate-api.com/v6/b887674c3d49e19270ab641c"
rate_original = "USD"
def hangman():
    words = list("dominant",litigation,module,shorts,couple,nervous,polite,dilemma,percent,silver,survivor,shiver,
moving,
control,
series,
develop,
ministry,
limited,
accompany,
variable,
interrupt,
perform,
eyebrow,
release,
extraterrestrial,
length,
trance,
uniform,
photography,
sulphur,
restrict,
tactic,
strike,
willpower,
import,
demonstrate,
normal,
embryo,greeting,pasture,company,assume,latest,initiative,competence,reality,opposition,exemption,rescue,session")
def get_exchange_rates(og_rate, to_rate):
    url = f"{twoURL}/latest/{og_rate}"
    response = requests.get(url)
    if response.status_code == 200:
        rate_data = response.json()
        thingy = rate_data['conversion_rates'][to_rate]
        print(thingy)
    else:
        print(f"failed to retrieve data {response.status_code}")
def exchange():
    ask = input("what is the original currency you want to exchange from (three letter abbreviation)?")
    second = input("What is the currency you want to exchange to (three letter abbreviation)?")
    get_exchange_rates(ask, second)
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
            equation.pop(pemdas[rtrtr] - 1)
            equation.pop(pemdas[rtrtr] - 1)
            equation.pop(pemdas[rtrtr] - 1)
            equation.insert(pemdas[rtrtr] - 1, putInEquation)
            pemdas.pop(rtrtr)
            hjhjh = 0
            for y in range(len(pemdas)): # 5,9,,, rjrjr = 3,,,, 5,3,9,,,,3,9
                rjrjr = pemdas[hjhjh] - 2
                pemdas.insert((hjhjh + 1), rjrjr)
                pemdas.pop(hjhjh)
                hjhjh += 1
        elif equation[pemdas[rtrtr]] == 5:
            putInEquation = equation[(pemdas[rtrtr] - 1)] * equation[(pemdas[rtrtr] + 1)]
            # add it to the list after removing equation[pemdas[rtrtr - and + 1]
            equation.pop(pemdas[rtrtr] - 1)
            equation.pop(pemdas[rtrtr] - 1)
            equation.pop(pemdas[rtrtr] - 1)
            equation.insert(pemdas[rtrtr] - 1, putInEquation)
            pemdas.pop(rtrtr)
            hjhjh = 0
            for y in range(len(pemdas)):  # 5,9,,, rjrjr = 3,,,, 5,3,9,,,,3,9
                rjrjr = pemdas[hjhjh] - 2
                pemdas.insert((hjhjh + 1), rjrjr)
                pemdas.pop(hjhjh)
                hjhjh += 1
        elif equation[pemdas[rtrtr]] == 6:
            putInEquation = equation[(pemdas[rtrtr] - 1)] * math.sin(math.radians(equation[(pemdas[rtrtr] + 1)]))
            # see other comments
            equation.pop(pemdas[rtrtr] - 1)
            equation.pop(pemdas[rtrtr] - 1)
            equation.pop(pemdas[rtrtr] - 1)
            equation.insert(pemdas[rtrtr] - 1, putInEquation)
            pemdas.pop(rtrtr)
            hjhjh = 0
            for y in range(len(pemdas)):  # 5,9,,, rjrjr = 3,,,, 5,3,9,,,,3,9
                rjrjr = pemdas[hjhjh] - 2
                pemdas.insert((hjhjh + 1), rjrjr)
                pemdas.pop(hjhjh)
                hjhjh += 1
        elif equation[pemdas[rtrtr]] == 7:
            putInEquation = equation[(pemdas[rtrtr] - 1)] * math.cos(math.radians(equation[(pemdas[rtrtr] + 1)]))
            equation.pop(pemdas[rtrtr] - 1)
            equation.pop(pemdas[rtrtr] - 1)
            equation.pop(pemdas[rtrtr] - 1)
            equation.insert(pemdas[rtrtr] - 1, putInEquation)
            pemdas.pop(rtrtr)
            hjhjh = 0
            for y in range(len(pemdas)):  # 5,9,,, rjrjr = 3,,,, 5,3,9,,,,3,9
                rjrjr = pemdas[hjhjh] - 2
                pemdas.insert((hjhjh + 1), rjrjr)
                pemdas.pop(hjhjh)
                hjhjh += 1
        elif equation[pemdas[rtrtr]] == 8:
            putInEquation = equation[(pemdas[rtrtr] - 1)] * math.tan(math.radians(equation[(pemdas[rtrtr] + 1)]))
            equation.pop(pemdas[rtrtr] - 1)
            equation.pop(pemdas[rtrtr] - 1)
            equation.pop(pemdas[rtrtr] - 1)
            equation.insert(pemdas[rtrtr] - 1, putInEquation)
            pemdas.pop(rtrtr)
            hjhjh = 0
            for y in range(len(pemdas)):  # 5,9,,, rjrjr = 3,,,, 5,3,9,,,,3,9
                rjrjr = pemdas[hjhjh] - 2
                pemdas.insert((hjhjh + 1), rjrjr)
                pemdas.pop(hjhjh)
                hjhjh += 1
        print(equation)
    looplevel = len(equation) // 2
    checker = 1
    for i in range(looplevel):
        # Herrrreeeeeeeeeeeeee
        if equation[checker] == 2:
            putInEquation = equation[checker - 1] + equation[checker + 1]
            equation.pop(checker - 1)
            equation.pop(checker - 1)
            equation.pop(checker - 1)
            equation.insert(checker - 1, putInEquation)
        elif equation[checker] == 3:
            putInEquation = equation[checker - 1] - equation[checker + 1]
            equation.pop(checker - 1)
            equation.pop(checker - 1)
            equation.pop(checker - 1)
            equation.insert(checker - 1, putInEquation)
    print(equation)


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
        elif hjhjh == numberOfNums:
            num = int(input("Enter the last number: "))
            equation.append(num)
    sortingItOut(numberOfNums, equation)

while theInput != 10:
    theInput = int(input("What would you like to know? type 1 for all options: "))
    if theInput == 1:
        print("2: Calculator on a budget")
        print("3: Weather")
        print("4: Currency exchange rates")
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
    if theInput == 4:
        exchange()
print(" ")
print("Program Ended")