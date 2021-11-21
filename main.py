#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Main file
"""
import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(500, 500)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
