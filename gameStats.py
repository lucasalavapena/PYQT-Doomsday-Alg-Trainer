import doomsdayalg
import datetime


class gameStat():
    def __init__(self, startTime, dateAsked):
        self.startTime_ = startTime
        self.endTime_ = -1
        self.dateAsked_ = dateAsked
        self.weekdayGuessed_ = -1
        self.correctGuess_ = False

    def setstartTime(self, startTime):
        self.startTime_ = startTime

    def getstartTime(self):
        return self.startTime_

    def setendTime(self, endTime):
        self.endTime_ = endTime

    def getendTime(self):
        return self.startTime_

    def updateStatus(self,endTime):
        self.endTime_ = endTime
        dayOfWeek = (self.dateAsked_.weekday()+ 1 ) % 7
        if (dayOfWeek == self.weekdayGuessed_):
             self.correctGuess_ = True

    def guessedCorrectly(self):
        return self.correctGuess_

    
test = gameStat(1,datetime.datetime(1800, 1, 1, 0, 0, 0))

print(test.getstartTime())

print(test.guessedCorrectly())
