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
        self.mode = 2

        self.setWindowTitle('Dataset maker')
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowIcon(QIcon('home.png'))

        self.button_create_csv = QPushButton('Create CSV-Dataset', self)
        self.button_create_csv.adjustSize()
        self.button_create_csv.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;")
        self.button_create_csv.clicked.connect(self.choice_1)

        self.button_dataset = QPushButton('Create Dataset2', self)
        self.button_dataset.adjustSize()
        self.button_dataset.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;")
        self.button_dataset.clicked.connect(self.choice_2)

        self.button_dataset2 = QPushButton('Create Dataset-Random', self)
        self.button_dataset2.adjustSize()
        self.button_dataset2.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;")
        self.button_dataset2.clicked.connect(self.choice_3)

        self.button_rating1 = QPushButton('1', self)
        self.button_rating1.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating1.clicked.connect(self.next_1)
        
        self.button_rating2 = QPushButton('2', self)
        self.button_rating2.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating2.clicked.connect(self.next_2)
        
        self.button_rating3 = QPushButton('3', self)
        self.button_rating3.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating3.clicked.connect(self.next_3)
        
        self.button_rating4 = QPushButton('4', self)
        self.button_rating4.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating4.clicked.connect(self.next_4)
        
        self.button_rating5 = QPushButton('5', self)
        self.button_rating5.setStyleSheet("background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_rating5.clicked.connect(self.next_5)

        self.review = ScrollLabel(self)
        self.review.setStyleSheet("background:#d9d4e7; color: #3C5A75; ")

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(self.button_create_csv, 0, 0, )
        layout.addWidget(self.button_dataset, 1, 0, 1, 1)
        layout.addWidget(self.button_dataset2, 2, 0)
        layout.addWidget(self.review, 0, 1, 3, 5)

        layout.addWidget(self.button_rating1, 3, 1)
        layout.addWidget(self.button_rating2, 3, 2)
        layout.addWidget(self.button_rating3, 3, 3)
        layout.addWidget(self.button_rating4, 3, 4)
        layout.addWidget(self.button_rating5, 3, 5)

        self.show()   

    def choice_1(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Create file CSV')
        dialog.setFixedSize(400, 200)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #C3D0DB')
        self.folderpath = ''
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setTextMargins(10,10,10,10)
        self.path_line_edit.setStyleSheet("background:#d9d4e7; border-radius: 5px; color: #0e172c;")

        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_folder)
        browse_button.setStyleSheet("background:#3C5A75; border-radius: 5px;")
        browse_button.adjustSize()

        create_button = QPushButton("Сreate CSV", dialog)
        create_button.setStyleSheet("background:#3C5A75; border-radius: 5px;")
        create_button.clicked.connect(self.create_csv)
        create_button.adjustSize()


        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(browse_button)
        layout.addWidget(create_button)
        dialog.setLayout(layout)

        dialog.exec_()

    def double_choice(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Create file CSV')
        dialog.setFixedSize(500, 300)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #C3D0DB')
        self.old_folderpath = ''
        self.new_folderpath = ''

        self.old_path_line_edit = QLineEdit(dialog)
        self.old_path_line_edit.setEnabled(False)
        self.old_path_line_edit.setTextMargins(10,10,10,10)
        self.old_path_line_edit.setStyleSheet("background:#d9d4e7; border-radius: 5px; color: #0e172c;")

        self.new_path_line_edit = QLineEdit(dialog)
        self.new_path_line_edit.setEnabled(False)
        self.new_path_line_edit.setTextMargins(10,10,10,10)
        self.new_path_line_edit.setStyleSheet("background:#d9d4e7; border-radius: 5px; color: #0e172c;")

        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_old_folder)
        browse_button.setStyleSheet("background:#3C5A75; border-radius: 5px;")
        browse_button.adjustSize()

        browse_button_2 = QPushButton("Browse2", dialog)
        browse_button_2.clicked.connect(self.select_new_folder)
        browse_button_2.setStyleSheet("background:#3C5A75; border-radius: 5px;")
        browse_button_2.adjustSize()

        create_button = QPushButton("Make new dataset", dialog)
        create_button.setStyleSheet("background:#3C5A75; border-radius: 5px;")
        if self.mode == 2:
            create_button.clicked.connect(self.create_dataset2)
        else:
            create_button.clicked.connect(self.create_dataset_random)
        create_button.adjustSize()


        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.old_path_line_edit)
        layout.addWidget(self.new_path_line_edit)
        layout.addWidget(browse_button)
        layout.addWidget(browse_button_2)
        layout.addWidget(create_button)
        dialog.setLayout(layout)

        dialog.exec_()


    def choice_2(self):
        self.mode = 2
        self.double_choice()

    def choice_3(self):
        self.mode = 3
        self.double_choice()

    
    def select_folder(self):
        self.folderpath = (QFileDialog.getExistingDirectory(self, 'Select Folder')).replace('/', '\\')
        self.path_line_edit.setText(self.folderpath)

    def select_old_folder(self):
        self.old_folderpath = (QFileDialog.getExistingDirectory(self, 'Select Folder')).replace('/', '\\')
        self.old_path_line_edit.setText(self.old_folderpath)

    def select_new_folder(self):
        self.new_folderpath = (QFileDialog.getExistingDirectory(self, 'Select Folder')).replace('/', '\\')
        self.new_path_line_edit.setText(self.new_folderpath)

    def create_csv(self):
        path = self.folderpath.split('\\')[-1]
        libs.task_1.make_csv(path)
            
    def create_dataset2(self):
        old_path = self.old_folderpath.split('\\')[-1]
        new_path = self.new_folderpath.split('\\')[-1]
        print(old_path, new_path)
        libs.task_2.main(old_path, new_path)

    def create_dataset_random(self):
        old_path = self.old_folderpath.split('\\')[-1]
        new_path = self.new_folderpath.split('\\')[-1]
        print(old_path, new_path)
        libs.task_3.main(old_path, new_path)

    def next_1(self):
        print(1)
    def next_2(self):
        print(1)
    def next_3(self):
        print(1)
    def next_4(self):
        print(1)
    def next_5(self):
        print(1)
                 

        
def start():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()