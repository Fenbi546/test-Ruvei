# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit)

from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def initUI(self):
        self.workh_text = QLabel(text_workheart)
        self.index_text = QLabel(text_index)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = QtAlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = QtAlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(text_finalwin)
        self.resize(win_height, win_width)
        self.move(win_x, win_y)
