import sys

import libs.task_1
import libs.task_2
import libs.task_3

from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication, QMainWindow, QPushButton, QToolTip, QVBoxLayout, QGridLayout, QScrollArea, QDialog, QLineEdit, QFileDialog)
from  PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QIcon
from libs.design import Ui_Dialog

class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        text = QWidget(self)
        self.setWidget(text)
        lay = QVBoxLayout(text)
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)
        self.label.setFont(QFont("SansSerif", 15))

    def setText(self, text):
        self.label.setText(text)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet(
            "background:#061E33; color: #C3D0DB; font-weight:bold; border-radius: 5px;")

    def initUI(self):

        self.setWindowTitle('Dataset maker')
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowIcon(QIcon('home.png'))

        self.button = QPushButton('Create CSV-Dataset', self)
        self.button.adjustSize()
        self.button.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;")

        self.button_dataset = QPushButton('Create Dataset2', self)
        self.button_dataset.adjustSize()
        self.button_dataset.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;")

        self.button_dataset2 = QPushButton('Create Dataset-Random', self)
        self.button_dataset2.adjustSize()
        self.button_dataset2.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;")

        self.button_rating1 = QPushButton('1', self)
        self.button_rating1.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        
        self.button_rating2 = QPushButton('2', self)
        self.button_rating2.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        
        self.button_rating3 = QPushButton('3', self)
        self.button_rating3.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        
        self.button_rating4 = QPushButton('4', self)
        self.button_rating4.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        
        self.button_rating5 = QPushButton('5', self)
        self.button_rating5.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")

        self.review = ScrollLabel(self)
        self.review.setStyleSheet("background:#d9d4e7; color: #3C5A75; ")

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(self.button, 0, 0, )
        layout.addWidget(self.button_dataset, 1, 0, 1, 1)
        layout.addWidget(self.button_dataset2, 2, 0)
        layout.addWidget(self.review, 0, 1, 3, 5)

        layout.addWidget(self.button_rating1, 3, 1)
        layout.addWidget(self.button_rating2, 3, 2)
        layout.addWidget(self.button_rating3, 3, 3)
        layout.addWidget(self.button_rating4, 3, 4)
        layout.addWidget(self.button_rating5, 3, 5)

        self.show()            

        
def start():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()