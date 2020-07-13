#Day of the week

import random
import datetime
import math

def randDate(earliestDate,LatestDate):
    differenceDateSeconds = (LatestDate-earliestDate).total_seconds()
    Date = earliestDate + datetime.timedelta(seconds=random.randint(0,int(differenceDateSeconds)))
    return Date

def correctWeekday(Date):
    return (Date.weekday()+ 1 )% 7

def play():
    # Initialised variables
    correctGuess = 0
    Guesses = 0

    earliestDate = datetime.datetime(1800, 1, 1, 0, 0, 0)
    LatestDate = datetime.datetime.now()
    try:
      while True:

        currentDate = randDate(earliestDate,LatestDate)
        actualDOW = currentDate.weekday()

        inputGuess = input('Date {}: What day of the week was {} on?\n'.format(Guesses, currentDate.strftime("%B %d, %Y")))
        if (int(inputGuess) == actualDOW):
          correctGuess += 1
          Guesses += 1
        else:
          Guesses += 1
    except KeyboardInterrupt:
      print('\nCorrectly Guessed:{} Guessed:{} .'.format(correctGuess, Guesses))
      print('\nDone.')

def anchorDay(year):
    century = math.floor(year/100)
    return 5 * (century % 2) % 7 + 2

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True


def workedDate():
    # Initialised variableshttps://en.wikipedia.org/wiki/Doomsday_rule#The_%22odd_+_11%22_method

    # hardcoded days can use: anchorDay(year)
    anchorDays = {1800: 5,
        1900: 3,
        2000: 2,
        2100: 0}

    # need a better way of doign this
    DoomsdayNonLeap = {1: [3,10,17,24,31],
        2: [7,14,21,28],
        3: [7, 14, 21, 28],
        4:  [4, 11, 18, 21, 28],
        5:  [2, 9, 16, 23, 30],
        6:  [6, 13, 20, 27],
        7:  [4, 11, 18, 25],
        8:  [1, 8, 15, 22, 29],
        9:  [5, 12, 19, 26],
        10: [3, 10, 17, 24, 31],
        11: [7, 14, 21, 28],
        12: [5, 12, 19, 26]}

    DoomsdayLeap = {1: [4,11,18,25],
        2: [1,8,15,22,29],
        3: [7, 14, 21, 28],
        4:  [4, 11, 18, 21, 28],
        5:  [2, 9, 16, 23, 30],
        6:  [6, 13, 20, 27],
        7:  [4, 11, 18, 25],
        8:  [1, 8, 15, 22, 29],
        9:  [5, 12, 19, 26],
        10: [3, 10, 17, 24, 31],
        11: [7, 14, 21, 28],
        12: [5, 12, 19, 26]}

    earliestDate = datetime.datetime(1800, 1, 1, 0, 0, 0)
    LatestDate = datetime.datetime.now()
    # currentDate = earliestDate + datetime.timedelta(seconds=random.randint(0,int(differenceDateSeconds)))
    currentDate = randDate(earliestDate,LatestDate)
    # currentDate = datetime.datetime(2004, 1, 5, 0, 0, 0)

    # Doomsday
    y = (currentDate.year) % 100
    a = math.floor(y/12)
    b = y % 12
    c = math.floor(b / 4)

    anchorDayKey = math.floor(currentDate.year/100) * 100
    anchorDay = anchorDays.get(anchorDayKey)

    print(anchorDay)
    Doomsday = ((a+b+c) % 7 + anchorDay) % 7

    # print('Year: {} vs Doomsday: {}'.format(currentDate.year,Doomsday))

    if isLeapYear(currentDate.year):
        DOW = ((currentDate.day-DoomsdayLeap.get(currentDate.month)[0]) + Doomsday) % 7
    else:
        DOW = ((currentDate.day-DoomsdayNonLeap.get(currentDate.month)[0]) + Doomsday) % 7

    print('date: {} '.format(currentDate))
    print('actual: {} vs mine: {}'.format((currentDate.weekday()+ 1 )% 7,DOW))

    # actualDOW = currentDate.weekday()


    # print('Mine: {} vs Actual {}'.format(DOW,actualDOW))

def main():
     #play()
     workedDate()
     # if isLeapYear(1660):
     #     print("Leap year")
if __name__ == '__main__':
    main()
