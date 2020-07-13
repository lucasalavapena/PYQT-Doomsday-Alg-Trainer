from dd_alg import *
import datetime
import csv
import os



class gameStat():
    def __init__(self,startTime,dateAsked,FeedbackStatus):
        self.startTime_ = startTime
        self.timeTaken_ = -1
        self.dateAsked_ = dateAsked
        self.weekdayGuessed_ = -1
        self.correctGuess_ = False
        self.FeedbackStatus_ = FeedbackStatus

    def setstartTime(self,startTime):
        self.startTime_ = startTime

    def getstartTime(self):
        return self.startTime_

    def settimeTakenTime(self,time):
        self.timeTaken_ = time

    def gettimeTakenTime(self):
        return self.timeTaken_

    def setweekdayGuessed(self,guess):
        self.weekdayGuessed_ = guess

    # def updateStatus(self,endTime):
    #     self.endTime_ = endTime
    #     dayOfWeek = (self.dateAsked_.weekday()+ 1 ) % 7
    #     if (dayOfWeek == self.weekdayGuessed_):
    #          self.correctGuess_ = True

    def setguessedCorrectly(self,bool):
        self.correctGuess_ = bool

    def writeToCSV(self):
        #
        csvFilename = "Stats.csv"
        row = [self.startTime_, self.dateAsked_, self.weekdayGuessed_,self.correctGuess_,round(self.timeTaken_,3),self.FeedbackStatus_]

        if (os.path.isfile(csvFilename)):
            with open(csvFilename, 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
        else:
            csvData = [["Start Time","Date Asked","Weekday Guessed [0-6]","Guessed Correctly [T/F]","Time [s]","Feedback Status"],row]
            with open(csvFilename, 'w') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(csvData)
        csvFile.close()

def computeAverageofX(times,X):
    sortedList = sorted(times, key=float)
    numRemoveAdd = math.ceil(len(times)/20)
    #Removing best times
    sortedList = sortedList[numRemoveAdd:-(numRemoveAdd+1)]
    print(sortedList)
    return(sum(sortedList)/len(sortedList))
def getLastXtimes(X):
    return X

def main():
     # test = gameStat(1,datetime.datetime(1800, 1, 1, 0, 0, 0),True)
     #
     # test.writeToCSV()
     times = [15.56,13.91,16,44,19.10,15.87,17.20,17.09,14.46,15.91,15.04,14.90,15.48]
     print(computeAverageofX(times,12))
if __name__ == '__main__':
    main()
