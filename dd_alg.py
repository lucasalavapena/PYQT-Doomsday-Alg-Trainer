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


def workedDate(Date):
    # Initialised variableshttps://en.wikipedia.org/wiki/Doomsday_rule#The_%22odd_+_11%22_method
    # hardcoded days can use: anchorDay(year)
    anchorDays = {1800: 5,
        1900: 3,
        2000: 2,
        2100: 0}

    dayOfWeek = {0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"}

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

    dateStr = Date.strftime("%B %d, %Y")
    helpText = "1. The Date in question is {}.\n".format(dateStr)

    # Doomsday
    y = (Date.year) % 100
    a = math.floor(y/12)
    b = y % 12
    c = math.floor(b / 4)

    anchorDayKey = math.floor(Date.year/100) * 100
    anchorDay = anchorDays.get(anchorDayKey)
    helpText += "2. The anchor day is {} as the date is in the {}s. This can either be memorized or calculated using: 5 * (century % 2) % 7 + 2.\n \t In this case: 5 * ({} % 2) % 7 + 2 = {}\n".format(anchorDay,anchorDayKey,int(anchorDayKey/100),anchorDay)

    Doomsday = ((a+b+c) % 7 + anchorDay) % 7

    helpText += """3. Time to compute the Doomsday :)). First lets compute some steps (a,b,c) of the bigger computation as to not lose our mind. \n
    a. The last two digits of the year in question is {}, its floor when divided by 12 is: \n \t a = ⌊{}/12 ⌋ = {}.  \n
    b. The {} mod 12 is {}, so b = {}.\n
    c. c = ⌊{}/4 ⌋ = {}.\n
    This lets us compute the Doomsday:\n
    \t ((a+b+c) % 7 + anchorDay) \n
    Therefore in this case: \n
    \t Doomsday = (({}+{}+{}) % 7 + {}) % 7 = {} \n""".format(y,y,a,y,b,b,b,c,a,b,c,anchorDay,Doomsday)

    # print('Year: {} vs Doomsday: {}'.format(currentDate.year,Doomsday))

    helpText += """4. If we are in the first two months of the year and are in a
    leap year we need to use a different set of doomsday for that year so lets check that first."""
    if isLeapYear(Date.year) and Date.month < 3:
        closetDoomsday = DoomsdayNonLeap.get(Date.month)[0]
        DOW = ((Date.day-closetDoomsday) + Doomsday) % 7
        helpText +="The year {} is a leap year.\n".format(Date.year)
    else:
        closetDoomsday = DoomsdayNonLeap.get(Date.month)[0]
        DOW = ((Date.day-closetDoomsday) + Doomsday) % 7
        helpText +="The year {} is not a leap year.\n".format(Date.year)

    helpText += "5. Now we must find the closest Doomsday to the {}, that in this case would be {}.\n".format(dateStr,closetDoomsday)
    helpText += "6. Simply computing the differences we finally get that the day of the week is {} ie {}".format(DOW,dayOfWeek[DOW])

    # print('date: {} '.format(currentDate))
    # print('actual: {} vs mine: {}'.format((currentDate.weekday()+ 1 )% 7,DOW))
    # print(helpText)
    return helpText

def main():
     workedDate(datetime.datetime(1922, 3, 1, 0, 0, 0))

if __name__ == '__main__':
    main()
