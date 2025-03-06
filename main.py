import datetime as dt
import requests
import math
import random
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "238d18d07aa46535d9f3b6c35864dbb7"
CITY = input("Enter your city: ")
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
    words = list(['carbon', 'recognize', 'correspondence', 'farewell', 'necklace', 'diplomat', 'shareholder',
    'photograph', 'shoulder', 'sunrise', 'gravel', 'automatic', 'shower', 'beautiful', 'serious', 'ritual',
    'distributor', 'opponent', 'liberal', 'scrape', 'residence', 'faithful', 'condition', 'committee', 'realism',
    'career', 'willpower', 'penalty', 'bundle', 'jurisdiction', 'oppose', 'listen', 'mechanical', 'latest', 'favourite',
    'abortion', 'inhibition', 'provide', 'kitchen', 'summer', 'chance', 'aspect', 'ticket', 'convict', 'artificial',
    'material', 'drawing', 'dynamic', 'freight', 'specimen', 'percent', 'remunerate', 'hardware', 'offend', 'finished',
    'legislature', 'archive', 'listen', 'grudge', 'purpose', 'ancestor', 'temporary', 'temptation', 'assertive',
    'memory', 'appointment', 'series', 'affect', 'dilemma', 'baseball', 'advantage', 'equation', 'element', 'function',
    'declaration', 'tournament', 'whisper', 'provide', 'module', 'context', 'particle', 'superintendent', 'dependence',
    'process', 'mobile', 'prisoner', 'island', 'diamond', 'climate', 'infrastructure', 'threaten', 'buttocks',
    'welcome', 'experiment', 'implication', 'chapter', 'resignation', 'budget', 'courtship'])
    num = random.randint(0, 98)
    theWord = words[num]
    letters = list(theWord)
    ig = 0
    revealed = []
    conv = []
    won = 0
    count = 0
    for x in range(len(letters)):
        conv.append("_")
    print(conv)
    while won == 0 and ig != 8:
        revealed.clear()
        guess = input("What letter do you want to guess")
        e = 0
        if guess in letters:
            for x in range(len(letters)):
                if letters[e] == guess:
                    revealed.append(letters[e])
                    conv.insert(e, letters[e])
                    conv.pop(e + 1)
                    count += 1
                    if count == len(letters):
                        won = 1
                else:
                    revealed.append("_")
                e = e + 1
            print(conv)
        else:
            ig = ig + 1
            if ig == 1:
                print("___|___")
                print(" ")
            if ig == 2:
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("___|___")
                print(" ")
            if ig == 3:
                print("   ------")
                print("   |/")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("___|___")
                print(" ")
            if ig == 4:
                print("   ----------")
                print("   |/       |")
                print("   |       (_)")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("___|___")
                print(" ")
            if ig == 5:
                print("   ----------")
                print("   |/       |")
                print("   |       (_)")
                print("   |        |")
                print("   |        |")
                print("   |")
                print("   |")
                print("___|___")
                print(" ")
            if ig == 6:
                print("   ----------")
                print("   |/       |")
                print("   |       (_)")
                print("   |       \|/")
                print("   |        |")
                print("   |")
                print("   |")
                print("___|___")
                print(" ")
            if ig == 7:
                print("   ----------")
                print("   |/       |")
                print("   |       (_)")
                print("   |       \|/")
                print("   |        |")
                print("   |       / \ ")
                print("   |")
                print("___|___")
                print("YOU LOSE")
                print(" ")
                ig = 8
    if won == 1:
        print("You won!!!!!!!!!!!!!!!!!!!")
def dictionary():
    word = input("What word would you like to look up: ")
    urld = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    responses = requests.get(urld).json()
    i = 0
    for x in range(len(responses[0]['meanings'])):
        print(responses[0]['meanings'][x]['definitions'][0]['definition'])
        i = i + 1
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
def battleship():
    rows, cols = (11, 11)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for x in range(10):
        arr[x + 1][0] = x + 1
    arr[0][1] = "a"
    arr[0][2] = "b"
    arr[0][3] = "c"
    arr[0][4] = "d"
    arr[0][5] = "e"
    arr[0][6] = "f"
    arr[0][7] = "g"
    arr[0][8] = "h"
    arr[0][9] = "i"
    arr[0][10] = "j"
    printboard(arr)
    placed = 5
    valid = 0
    first = 1
    while placed != 1:
        valid = 0
        while valid == 0:
            letter = input("Where do you want to place your " + str(placed) + " long boat letter coordinate? (the top left part of the ship will be at your coordinate) ")
            number = int(input("Where is the number coordinate "))
            orientation = input("vertical or horizontal? (type 'v' or 'h') ")
            valid = correct(letter, number, orientation, placed)
        if letter == "a":
            arr[number][1] = 3
            if orientation == "h":
                for x in range(placed - 1):
                    arr[number][1 + x + 1] = 3
            if orientation == "v":
                for p in range(placed - 1):
                    arr[number + p + 1][1] = 3
        if letter == "b":
            arr[number][2] = 3
            if orientation == "h":
                for x in range(placed - 1):
                    arr[number][2 + x + 1] = 3
            if orientation == "v":
                for p in range(placed - 1):
                    arr[number + p + 1][2] = 3
        if letter == "c":
            arr[number][3] = 3
            if orientation == "h":
                for x in range(placed - 1):
                    arr[number][3 + x + 1] = 3
            if orientation == "v":
                for p in range(placed - 1):
                    arr[number + p + 1][3] = 3
        if letter == "d":
            arr[number][4] = 3
            if orientation == "h":
                for x in range(placed - 1):
                    arr[number][4 + x + 1] = 3
            if orientation == "v":
                for p in range(placed - 1):
                    arr[number + p + 1][4] = 3
        if letter == "e":
            arr[number][5] = 3
            if orientation == "h":
                for x in range(placed - 1):
                    arr[number][5 + x + 1] = 3
            if orientation == "v":
                for p in range(placed - 1):
                    arr[number + p + 1][5] = 3
        if letter == "f":
            arr[number][6] = 3
            if orientation == "h":
                for x in range(placed - 1):
                    arr[number][6 + x + 1] = 3
            if orientation == "v":
                for p in range(placed - 1):
                    arr[number + p + 1][6] = 3
        if letter == "g":
            arr[number][7] = 3
            if orientation == "h":
                for x in range(placed - 1):
                    arr[number][7 + x + 1] = 3
            if orientation == "v":
                for p in range(placed - 1):
                    arr[number + p + 1][7] = 3
        if letter == "h":
            arr[number][8] = 3
            if orientation == "h":
                for x in range(placed - 1):
                    arr[number][8 + x + 1] = 3
            if orientation == "v":
                for p in range(placed - 1):
                    arr[number + p + 1][8] = 3
        if letter == "i":
            arr[number][9] = 3
            if orientation == "h":
                for x in range(placed - 1):
                    arr[number][9 + x + 1] = 3
            if orientation == "v":
                for p in range(placed - 1):
                    arr[number + p + 1][9] = 3
        if letter == "j":
            arr[number][10] = 3
            if orientation == "h":
                for x in range(placed - 1):
                    arr[number][10 + x + 1] = 3
            if orientation == "v":
                for p in range(placed - 1):
                    arr[number + p + 1][10] = 3
        if placed != 3 or first != 1:
            placed = placed - 1
        else:
            first = 2
        printboard(arr)

def enemy():
    rows, cols = (11, 11)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for x in range(10):
        arr[x + 1][0] = x + 1
    arr[0][1] = "a"
    arr[0][2] = "b"
    arr[0][3] = "c"
    arr[0][4] = "d"
    arr[0][5] = "e"
    arr[0][6] = "f"
    arr[0][7] = "g"
    arr[0][8] = "h"
    arr[0][9] = "i"
    arr[0][10] = "j"
    arr[2][3] = 3
    arr[2][4] = 3
    arr[2][5] = 3
    arr[2][6] = 3
    arr[2][7] = 3
    arr[8][9] = 3
    arr[9][9] = 3
    arr[10][9] = 3
    arr[11][9] = 3
    arr[3][11] = 3
    arr[4][11] = 3
    arr[5][11] = 3
    arr[4][5] = 3
    arr[4][6] = 3
    arr[4][7] = 3
    arr[7][7] = 3
    arr[7][8] = 3
    row,col = (11, 11)
    pri = [[0 for i in range(col)] for j in range(row)]
    for x in range(10):
        pri[x + 1][0] = x + 1
    pri[0][1] = "a"
    pri[0][2] = "b"
    pri[0][3] = "c"
    pri[0][4] = "d"
    pri[0][5] = "e"
    pri[0][6] = "f"
    pri[0][7] = "g"
    pri[0][8] = "h"
    pri[0][9] = "i"
    pri[0][10] = "j"
    printboard(pri)
    letter = input("What letter coordinate do you guess: ")
    num = int(input("What number coordinate do you guess: "))
    d = 0
    if letter == "a":
        d = 1 + 1
    if letter == "b":
        d = 2 + 1
    if letter == "c":
        d = 3 + 1
    if letter == "d":
        d = 4 + 1
    if letter == "e":
        d = 5 + 1
    if letter == "f":
        d = 6 + 1
    if letter == "g":
        d = 7 + 1
    if letter == "h":
        d = 8 + 1
    if letter == "i":
        d = 9 + 1
    if letter == "j":
        d = 10 + 1
    if arr[num][d] == 3:
        pri[num][d] = 9
        print("Hit (9's are hits)")
    else:
        pri[num][d] = 6
        print("Missed (6's are misses)")
    five = 0
    four = 0
    three = 0
    three2 = 0
    two = 0
    if pri[2][3] == 9 and pri[2][4] == 9 and pri[2][4] == 9 and pri[2][5] == 9 and pri[2][6] == 9:
        print("5 long ship is sunk")
        five = 1
    if pri[8][9] == 9 and pri[8][9] == 9 and pri[9][9] == 9 and pri[10][9] == 9 and pri[11][9] == 9:
        print("4 long ship is sunk")
        four = 1
    if pri[3][11] == 9 and pri[4][11] == 9 and pri[5][11]:
        print("one three ship is sunk")
        three = 1
    if pri[4][5] == 9 and pri[4][6] == 9 and pri[4][7]:
        print("one three ship is sunk")
        three2 = 1
    if pri[7][7] == 9 and pri[7][8] == 9:
        print("2 long ship is sunk")
        two = 1
    if five == 1 and four == 1 and three == 1 and three2 == 1 and two == 1:
        print("You Won!")
        return 1
    printboard(pri)
def printboard(arr):
    print("3's represent your boats")
    print("[" + "   " + arr[0][1] + ", " + arr[0][2] + ", " + arr[0][3] + ", " + arr[0][4] + ", " + arr[0][5] + ", " +
          arr[0][6] + ", " + arr[0][7] + ", " + arr[0][8] + ", " + arr[0][9] + ", " + arr[0][10] + "]")
    print(arr[1])
    print(arr[2])
    print(arr[3])
    print(arr[4])
    print(arr[5])
    print(arr[6])
    print(arr[7])
    print(arr[8])
    print(arr[9])
    print(arr[10])
def correct(let, num, ore, len):
    if len == 5:
        if ore == "h":
            if let == "g" or let == "h" or let == "i" or let == "j":
                return 0
        if ore == "v":
            if num == 7 or num == 8 or num == 9 or num == 10:
                return 0
    if len == 4:
        if ore == "h":
            if let == "h" or let == "i" or let == "j":
                return 0
        if ore == "v":
            if num == 8 or num == 9 or num == 10:
                return 0
    if len == 3:
        if ore == "h":
            if let == "i" or let == "j":
                return 0
        if ore == "v":
            if num == 9 or num == 10:
                return 0
    if len == 2:
        if ore == "h":
            if let == "j":
                return 0
        if ore == "v":
            if num == 10:
                return 0
    return 1
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
        print("5: Hangman")
        print("6: Dictionary")
        print("7: Battleship")
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
    if theInput == 5:
        hangman()
    if theInput == 6:
        dictionary()
    if theInput == 7:
        battleship()
print(" ")
print("Program Ended")