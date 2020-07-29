"""
sadsd
"""

import csv
import math
import os



class GameStats():
    """
    Class
    """

    def __init__(self, start_time, date_asked, feedback_status):
        """

        :param start_time:
        :param date_asked:
        :param feedback_status:
        """
        self.start_time = start_time
        self.time_taken = -1
        self.date_asked = date_asked
        self.weekday_guessed = -1
        self.correct_guess = False
        self.feedback_status = feedback_status

    def set_start_time(self, start_time):
        """
        setter for the start time
        :param start_time: timestamp of the starting time
        :return: none
        """
        self.start_time = start_time

    def get_start_time(self):
        """

        :return:
        """
        return self.start_time

    def set_time_taken(self, time):
        """
        setter for the time taken
        :param time: time taken
        :return:
        """
        self.time_taken = time

    def get_time_taken(self):
        """

        :return:
        """
        return self.time_taken

    def set_weekday_guessed(self, guess):
        """
        setter for the weekday guessed
        :param guess:
        :return:
        """
        self.weekday_guessed = guess

    def set_guess_correctly(self, bool):
        """
        setter for the guess
        :param bool:
        :return:
        """
        self.correct_guess = bool

    def write_to_csv(self):
        """

        :return:
        """

        csv_filename = "Stats.csv"
        row = [self.start_time, self.date_asked, self.weekday_guessed, self.correct_guess,
               round(self.time_taken, 3), self.feedback_status]

        if os.path.isfile(csv_filename):
            with open(csv_filename, 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(row)
        else:
            csv_data = [["Start Time", "Date Asked", "Weekday Guessed [0-6]",
                         "Guessed Correctly [T/F]", "Time [s]", "Feedback Status"], row]
            with open(csv_filename, 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(csv_data)
        csv_file.close()


def compute_ao_x(times, no_times):
    """

    :param times:
    :param no_times:
    :return:
    """
    x_times = times[-no_times:]
    sorted_list = sorted(x_times, key=float)
    discard_ids = math.ceil(len(x_times) / 20)

    # Removing best times and worst time
    sorted_list = sorted_list[discard_ids:-(discard_ids + 1)]

    print(sorted_list)
    return sum(sorted_list) / len(sorted_list)


def main():
    """

    :return:
    """
    # test = GameStats(1,datetime.datetime(1800, 1, 1, 0, 0, 0),True)
    #
    # test.write_to_csv()
    times = [15.56, 13.91, 16, 44, 19.10, 15.87, 17.20, 17.09, 14.46, 15.91, 15.04, 14.90, 15.48]
    print(compute_ao_x(times, 12))


if __name__ == '__main__':
    main()
