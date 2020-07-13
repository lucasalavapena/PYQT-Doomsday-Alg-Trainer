#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from doomsdayalg import *





class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        self.initSettings()
        self.doingTest = False
        self.feedback = False

        self.time = 0
        self.timer = QTimer()
        self.timer.setInterval(2**6)
        self.timer.timeout.connect(self.updateTimer)

    # def button_clicked(self):
    #     self.label.setText('you pressed the button')
    #     self.update()




    def initUI(self):
        self.setWindowTitle('Doomsday Trainer')
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('You know what to do :))')
        self.label.move(80, 80)
        self.label.adjustSize()
        self.dateAsked = QtWidgets.QLabel(self)
        self.dateAsked.setAlignment(Qt.AlignCenter)


    def initSettings(self):
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
        self.label.setText("{:02d}:{:.3f}".format(math.floor(self.time/60),
                                                  round(self.time %60, 3)))
        self.label.adjustSize()

    def update(self):
        self.label.adjustSize()

    def updateTimer(self):
        self.time += 2**6/1000
        self.updateDisplay()

    def startTimer(self):
        if (self.time != 0):
            self.time = 0
        self.label.setStyleSheet('color: black')
        date2BAsked = randDate(self.earliestDate, self.LatestDate)
        self.correctAnswer = correctWeekday(date2BAsked)
        self.dateAsked.setText(date2BAsked.strftime("%d/%m/%Y"))
        self.dateAsked.move(40, 40)
        self.timer.start()
        self.doingTest = True

    def stopTimer(self):
        self.timer.stop()
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

        # tbd
        if (self.feedback):
            pass




    def keyPressEvent(self, e):

        if self.doingTest == True:
            # if e.key() == QtCore.Qt.Key_0 or QtCore.Qt.Key_1 or QtCore.Qt.Key_2 or QtCore.Qt.Key_3 or QtCore.Qt.Key_4 or QtCore.Qt.Key_5 or QtCore.Qt.Key_6:
            if e.key() in self.KeyDay:
                if self.KeyDay[e.key()] == self.correctAnswer:
                    self.correctlyAnswered()
                else:
                    self.incorrectlyAnswered()
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
