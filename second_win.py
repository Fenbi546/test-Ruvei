# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit)

from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connect()
        self.show()
        def next_click(self):
            self.tw = TestWin()
            self.hide()

        def connect(self):
            self.btn_next.clicked.connect(self.next.click)

        def set_appear(self):
            self.setWindowTitle('')
            self.resise(win_width, win_height)
            self.move(win_x, win_y)

        def initUI(self):
            self.btn_next = QPushButton(text_sendresults, self)
            self.btn_test1 = QPushButton(text_starttest1, self)
            self.btn_test2 = QPushButton(text_starttest2, self)
            self.btn_test3 = QPushButton(text_starttest3, self)

            self.text_name  = QLabel(text_name)
            self.text_age = QLabel(text_age)
            self.text_test1 = QLabel(text_test1)
            self.txt_test2 = QLabel(text_test2)
            self.txt_test3 = QLabel(text_test3)
            self.txt_timer = QLabel(text_timer)

            self.line_name = QLineEdit(text_hintname)
            self.line_age = QLineEdit(text_hinttage)
            self.line_test1 = QLineEdit(text_hinttest1)
            self.line_test2 = QLineEdit(text_hinttest2)
            self.line_test3 = QLineEdit(text_hinttest3)
            
            self.l_line = QVBoxLayout()
            self.r_line = QVBoxLayout()
            self.h_line = QHBoxLayout()
            self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
            self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.line_age, alignment = Qt.Alignleft)
            self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.line_test2, alignment = Qt.Alignleft)
            self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
            self.h_line.addLayout(self.l_line)
            self.h_line.addLayout(self.r_line)
            self.setLayout(self.h_line)

            def next_clicked():
                self.hide()
                self.fw = FinalWin()

            def connects(self):
                self.btn_next.clicked.connect(self.next_click)

            def set_appear(self):
                self.setWindowTitle(txt_title)
                self.resize(win_width, win_height)
                self.move(win_x, win_y)