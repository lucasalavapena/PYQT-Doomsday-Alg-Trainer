#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer, Qt, QDateTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow

from game_stats import *


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.initSettings()
        self.initUI()

        self.time = 0
        self.timer = QTimer()
        self.timer.setInterval(2 ** 6)
        self.timer.timeout.connect(self.updateTimer)

    # def button_clicked(self):
    #     self.label.setText('you pressed the button')
    #     self.update()

    def initUI(self):
        self.setWindowTitle('Doomsday Trainer')
        self.label = QtWidgets.QLabel(self)

        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('You know what to do :))')
        self.label.move(150, 150)
        self.label.adjustSize()
        self.dateAsked = QtWidgets.QLabel(self)
        self.dateAsked.setAlignment(Qt.AlignCenter)
        if (self.feedback):
            self.feedbackText = QtWidgets.QLabel(self)
            self.feedbackText.setAlignment(Qt.AlignCenter)
            self.feedbackText.move(250, 250)

    def initSettings(self):
        self.doingTest = False
        self.feedback = True
        self.actionKey = QtCore.Qt.Key_Space

        self.MonKey = QtCore.Qt.Key_0
        self.TueKey = QtCore.Qt.Key_1
        self.WedKey = QtCore.Qt.Key_2
        self.ThuKey = QtCore.Qt.Key_3
        self.FriKey = QtCore.Qt.Key_4
        self.SatKey = QtCore.Qt.Key_5
        self.SunKey = QtCore.Qt.Key_6
        self.KeyDay = {self.MonKey: 0,
                       self.TueKey: 1,
                       self.WedKey: 2,
                       self.ThuKey: 3,
                       self.FriKey: 4,
                       self.SatKey: 5,
                       self.SunKey: 6}

        self.earliestDate = datetime.datetime(1800, 1, 1, 0, 0, 0)
        self.LatestDate = datetime.datetime.now()

    def updateDisplay(self):
        self.label.setText("{:02d}:{:.3f}".format(math.floor(self.time / 60), round(self.time % 60, 3)))
        self.label.adjustSize()

    def update(self):
        self.label.adjustSize()

    def updateTimer(self):
        self.time += 2 ** 6 / 1000
        self.updateDisplay()

    def startTimer(self):
        if (self.time != 0):
            self.time = 0
        self.label.setStyleSheet('color: black')
        self.date2BAsked = rand_date(self.earliestDate, self.LatestDate)
        self.correctAnswer = correct_weekday(self.date2BAsked)
        self.dateAsked.setText(self.date2BAsked.strftime("%B %d, %Y"))
        self.dateAsked.move(50, 50)
        self.dateAsked.setFont(QFont('Arial', 30))
        self.dateAsked.adjustSize()

        self.gameStats = gameStat(QDateTime.currentDateTime().toPyDateTime(), self.date2BAsked, self.feedback)
        self.doingTest = True
        self.timer.start()

    def stopTimer(self):
        self.timer.stop()
        self.gameStats.settimeTakenTime(self.time)
        self.doingTest = False

    # def changeLabelColor(self,Label,color):
    #     palette = QPalette()
    #     palette.setColor(self.label.foregroundRole(), color)
    #     self.Label.setPalette(palette)

    def correctlyAnswered(self):
        print("yeeeeet")
        self.stopTimer()
        # self.changeLabelColor(self.label,QtGui.QColor(25,255,25))
        self.label.setStyleSheet('color: green')

    def incorrectlyAnswered(self):
        print("ooof.")
        self.stopTimer()
        self.label.setStyleSheet('color: red')

        if (self.feedback):
            self.feedbackText.setText(worked_date(self.date2BAsked))
            self.feedbackText.adjustSize()

    def keyPressEvent(self, e):

        if self.doingTest == True:
            # if e.key() == QtCore.Qt.Key_0 or QtCore.Qt.Key_1 or QtCore.Qt.Key_2 or QtCore.Qt.Key_3 or QtCore.Qt.Key_4 or QtCore.Qt.Key_5 or QtCore.Qt.Key_6:
            if e.key() in self.KeyDay:

                if self.KeyDay[e.key()] == self.correctAnswer:
                    self.correctlyAnswered()
                    self.gameStats.setguessedCorrectly(True)
                else:
                    self.incorrectlyAnswered()
                    self.gameStats.setguessedCorrectly(False)

                self.gameStats.setweekdayGuessed(self.KeyDay[e.key()])
                self.gameStats.writeToCSV()
            # if e.key() == self.actionKey2:
            #     print("bye")
            #     self.stopTimer()

        if self.doingTest == False:
            if e.key() == self.actionKey:
                print("hi")
                self.startTimer()

        if e.key() == QtCore.Qt.Key_Q and self.doingTest == False:
            self.close()

    def timer(self, e):
        if e.type() == QtCore.QEvent.KeyPress and e.key() == self.actionKey:
            print("Hi")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.resize(500, 500)
    win.show()
    sys.exit(app.exec_())


window()
