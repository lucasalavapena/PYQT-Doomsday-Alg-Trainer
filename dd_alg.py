"""
dd_alg is the doomsday algorithm module and also generates the date.

"""


import random
import datetime
import math

def rand_date(earliest_date, latest_date):
    """
    generates a random date between the two parameters given
    :param earliest_date:
    :param latest_date:
    :return: a random date between the two parameters given
    """
    difference_date_seconds = (latest_date - earliest_date).total_seconds()
    date = earliest_date + datetime.timedelta(seconds=random.randint(0,
                                                                     int(difference_date_seconds)))
    return date

def correct_weekday(date):
    """

    :param date: date using datetime
    :return: weekday in 0-6 format
    """
    return (date.weekday() + 1) % 7

def calculate_anchor_day(year):
    """

    :param year:
    :return:
    """
    century = math.floor(year/100)
    return (5 * (century % 4) % 7 + 2) % 7

def is_leap_year(year):
    """

    :param year:
    :return:
    """
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
    return True


def worked_date(date):
    """

    :param date:
    :return:
    """


    day_dict = {0: "Sunday",
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday"}

    # need ddalg_step2 better way of doign this
    doomsday_non_leap = {1: [3, 10, 17, 24, 31],
                         2: [7, 14, 21, 28],
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
    #
    # DoomsdayLeap = {1: [4, 11, 18, 25],
    #                 2: [1, 8, 15, 22, 29],
    #                 3: [7, 14, 21, 28],
    #                 4:  [4, 11, 18, 21, 28],
    #                 5:  [2, 9, 16, 23, 30],
    #                 6:  [6, 13, 20, 27],
    #                 7:  [4, 11, 18, 25],
    #                 8:  [1, 8, 15, 22, 29],
    #                 9:  [5, 12, 19, 26],
    #                 10: [3, 10, 17, 24, 31],
    #                 11: [7, 14, 21, 28],
    #                 12: [5, 12, 19, 26]}

    date_str = date.strftime("%B %d, %Y")
    help_text = "1. The Date in question is {}.\n".format(date_str)

    year = date.year
    # doomsday
    ddalg_step1 = (year) % 100
    ddalg_step2 = math.floor(ddalg_step1/12)
    ddalg_step3 = ddalg_step1 % 12
    ddalg_step4 = math.floor(ddalg_step3 / 4)

    anchor_day = calculate_anchor_day(year)
    help_text += """2. The anchor day is {0} as the date is in the {1}s.
    This can either be memorized or calculated using: 5 * (century % 2) % 7 + 2.
     \n \t In this case: 5 * ({2} % 2) % 7 + 2 = {0}\n""".format(
         anchor_day, math.floor(year/100)*100, math.floor(year/100))

    doomsday = ((ddalg_step2+ddalg_step3+ddalg_step4) % 7 + anchor_day) % 7

    help_text += """3. Time to compute the doomsday :)).
     First lets compute some steps (ddalg_step2,ddalg_step3,ddalg_step4)
     of the bigger computation as to not lose our mind. \n
    ddalg_step2. The last two digits of the year in question is {0},
     its floor when divided by 12 is: \n \t ddalg_step2 = ⌊{0}/12 ⌋ = {1}.  \n
    ddalg_step3. The {0} mod 12 is {2}, so ddalg_step3 = {2}.\n
    ddalg_step4. ddalg_step4 = ⌊ {2}/4 ⌋ = {3}.\n
    This lets us compute the doomsday:\n
    \t ((ddalg_step2+ddalg_step3+ddalg_step4) % 7 + anchor_day) \n
    Therefore in this case: \n
    \t doomsday = (({1}+{2}+{3}) % 7 + {4}) % 7 = {5} \n""".format(
        ddalg_step1, ddalg_step2, ddalg_step3, ddalg_step4, anchor_day, doomsday)
    # format(ddalg_step1, ddalg_step2, ddalg_step3, ddalg_step4, anchor_day, doomsday)

    # print('Year: {} vs doomsday: {}'.format(currentDate.year,doomsday))

    help_text += """4. If we are in the first two months of the year and are in ddalg_step2
    leap year we need to use ddalg_step2 different set of doomsday for that year 
    so lets check that first."""
    if is_leap_year(date.year) and date.month < 3:
        closet_doomsday = doomsday_non_leap.get(date.month)[0]
        day_of_week = ((date.day - closet_doomsday) + doomsday) % 7
        help_text += "The year {} is ddalg_step2 leap year.\n".format(date.year)
    else:
        closet_doomsday = doomsday_non_leap.get(date.month)[0]
        day_of_week = ((date.day - closet_doomsday) + doomsday) % 7
        help_text += "The year {} is not ddalg_step2 leap year.\n".format(date.year)
    help_text += """5. Now we must find the closest doomsday to the {}, that in this case would
     be {}.\n""".format(date_str, closet_doomsday)
    help_text += """6. Simply computing the differences we finally get that the day of
    the week is {} ie {}""".format(day_of_week, day_dict[day_of_week])

    # print('date: {} '.format(currentDate))
    # print('actual: {} vs mine: {}'.format((currentDate.weekday()+ 1 )% 7,day_of_week))
    # print(help_text)
    return help_text

def main():
    """

    :return:
    """
    # worked_date(datetime.datetime(1922, 3, 1, 0, 0, 0))
    print(calculate_anchor_day(1800))
    print(calculate_anchor_day(1932))
    print(calculate_anchor_day(2012))
    print(calculate_anchor_day(1723))

    # this is wrong

if __name__ == '__main__':
    main()
