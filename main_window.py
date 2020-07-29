import math
import datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow
from dd_alg import rand_date, correct_weekday, worked_date
from gamestats import GameStats

class MainWindow(QMainWindow):
    """
    Main Window Class
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_settings()
        self.init_ui()
        self.time = 0
        self.timer = QTimer()
        self.timer.setInterval(2 ** 6)
        self.timer.timeout.connect(self.update_timer)
        print(1)
    # def button_clicked(self):
    #     self.label.setText('you pressed the button')
    #     self.update()

    def init_ui(self):
        self.setWindowTitle('Doomsday Trainer')
        self.label = QtWidgets.QLabel(self)

        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('You know what to do :))')
        self.label.move(150, 150)
        self.label.adjustSize()
        self.date_asked = QtWidgets.QLabel(self)
        self.date_asked.setAlignment(Qt.AlignCenter)
        if self.feedback:
            self.feedback_text = QtWidgets.QLabel(self)
            self.feedback_text.setAlignment(Qt.AlignCenter)
            self.feedback_text.move(250, 250)

    def init_settings(self):
        self.doing_test = False
        self.feedback = True
        self.action_key = QtCore.Qt.Key_Space

        self.mon_key = QtCore.Qt.Key_0
        self.tue_key = QtCore.Qt.Key_1
        self.wed_key = QtCore.Qt.Key_2
        self.thu_key = QtCore.Qt.Key_3
        self.fri_key = QtCore.Qt.Key_4
        self.sat_key = QtCore.Qt.Key_5
        self.sun_key = QtCore.Qt.Key_6
        self.key_day = {self.mon_key: 0,
                        self.tue_key: 1,
                        self.wed_key: 2,
                        self.thu_key: 3,
                        self.fri_key: 4,
                        self.sat_key: 5,
                        self.sun_key: 6}

        self.earliest_date = datetime.datetime(1800, 1, 1, 0, 0, 0)
        self.latest_date = datetime.datetime.now()

    def update_display(self):
        self.label.setText("{:02d}:{:.3f}".format(math.floor(self.time / 60),
                                                  round(self.time % 60, 3)))
        self.label.adjustSize()

    def update(self):
        self.label.adjustSize()

    def update_timer(self):
        self.time += 2 ** 6 / 1000
        self.update_display()

    def startTimer(self):
        if self.time != 0:
            self.time = 0
        self.label.setStyleSheet('color: black')
        self.generated_date = rand_date(self.earliest_date, self.latest_date)
        self.correct_answer = correct_weekday(self.generated_date)
        self.date_asked.setText(self.generated_date.strftime("%B %d, %Y"))
        self.date_asked.move(50, 50)
        self.date_asked.setFont(QFont('Arial', 30))
        self.date_asked.adjustSize()

        self.game_stats = GameStats(QDateTime.currentDateTime().toPyDateTime(),
                                    self.generated_date, self.feedback)
        self.doing_test = True
        self.timer.start()

    def stop_timer(self):
        self.timer.stop()
        self.game_stats.set_time_taken(self.time)
        self.doing_test = False

    # def changeLabelColor(self,Label,color):
    #     palette = QPalette()
    #     palette.setColor(self.label.foregroundRole(), color)
    #     self.Label.setPalette(palette)

    def correctly_answered(self):
        print("yeeeeet")
        self.stop_timer()
        # self.changeLabelColor(self.label,QtGui.QColor(25,255,25))
        self.label.setStyleSheet('color: green')

    def incorrectly_answered(self):
        """
        display
        :return:
        """
        print("ooof.")
        self.stop_timer()
        self.label.setStyleSheet('color: red')

        if self.feedback:
            self.feedback_text.setText(worked_date(self.generated_date))
            self.feedback_text.adjustSize()

    def keyPressEvent(self, event):
        if self.doing_test:
            if event.key() in self.key_day:
                if self.key_day[event.key()] == self.correct_answer:
                    self.correctly_answered()
                    self.game_stats.set_guess_correctly(True)
                else:
                    self.incorrectly_answered()
                    self.game_stats.set_guess_correctly(False)

                self.game_stats.set_weekday_guessed(self.key_day[event.key()])
                self.game_stats.write_to_csv()
            # if e.key() == self.actionKey2:
            #     print("bye")
            #     self.stop_timer()

        if self.doing_test == False:
            if event.key() == self.action_key:
                self.startTimer()

        if event.key() == QtCore.Qt.Key_Q and self.doing_test:
            self.close()

    def timer(self, event):
        if event.type() == QtCore.QEvent.KeyPress and event.key() == self.action_key:
            print("Hi")