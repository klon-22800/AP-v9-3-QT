import sys

import libs.task_1
import libs.task_2
import libs.task_3

from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QPushButton, QToolTip,
                             QVBoxLayout, QGridLayout, QScrollArea, QDialog, QLineEdit, QFileDialog, QMessageBox)
from PyQt5.QtGui import (QFont, QIcon, QPixmap)

from libs.task_5 import Iterator


class MessageBox:
    def __init__(self, parent: QWidget, text: str) -> None:
        """constructor of MessageBox
        Args:
            parent (_type_): QWidget 
            text (str): text to show
        """
        message_box = QMessageBox(parent)
        message_box.setText(text)
        ok_button = message_box.addButton(QMessageBox.Ok)
        ok_button.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 100px;")
        message_box.setStyleSheet('color: white')
        message_box.exec_()


class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs) -> None:
        """Constructor of ScrollLabel
        """
        QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        text = QWidget(self)
        self.setWidget(text)
        lay = QVBoxLayout(text)
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)
        self.label.setFont(QFont("SansSerif", 15))

    def setText(self, text: str) -> None:
        """The function set text to ScrollLabel object

        Args:
            text (str): text to set
        """
        self.label.setText(text)


class Window(QWidget):

    def __init__(self) -> None:
        """Constructor of main Window
        """
        super().__init__()
        self.initUI()
        self.setStyleSheet(
            "background:#061E33; color: #C3D0DB; font-weight:bold; border-radius: 5px;")

    def initUI(self) -> None:
        """The function create an UI object of main Window
        """
        self.mode = 2

        self.setWindowTitle('Dataset maker')
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowIcon(QIcon('home.png'))

        self.button_create_csv = QPushButton('Create CSV-Dataset', self)
        self.button_create_csv.adjustSize()
        self.button_create_csv.setFont(QFont('Arial', 15))
        self.button_create_csv.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;")
        self.button_create_csv.clicked.connect(self.choice_1)

        self.button_dataset = QPushButton('Create Dataset2', self)
        self.button_dataset.adjustSize()
        self.button_dataset.setFont(QFont('Arial', 15))
        self.button_dataset.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;")
        self.button_dataset.clicked.connect(self.choice_2)

        self.button_dataset2 = QPushButton('Create Dataset-Random', self)
        self.button_dataset2.adjustSize()
        self.button_dataset2.setFont(QFont('Arial', 15))
        self.button_dataset2.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;")
        self.button_dataset2.clicked.connect(self.choice_3)

        self.logo = QPixmap("logo.png").scaled(300, 90)
        self.logo_label = QLabel()
        self.logo_label.setPixmap(self.logo)

        self.button_class_1 = QPushButton('1', self)
        self.button_class_1.setFont(QFont("Arial", 15))
        self.button_class_1.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_class_1.clicked.connect(self.next_1)

        self.button_class_2 = QPushButton('2', self)
        self.button_class_2.setFont(QFont("Arial", 15))
        self.button_class_2.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_class_2.clicked.connect(self.next_2)

        self.button_class_3 = QPushButton('3', self)
        self.button_class_3.setFont(QFont("Arial", 15))
        self.button_class_3.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_class_3.clicked.connect(self.next_3)

        self.button_class_4 = QPushButton('4', self)
        self.button_class_4.setFont(QFont("Arial", 15))
        self.button_class_4.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_class_4.clicked.connect(self.next_4)

        self.button_class_5 = QPushButton('5', self)
        self.button_class_5.setFont(QFont("Arial", 15))
        self.button_class_5.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 150px; min-height: 70px;")
        self.button_class_5.clicked.connect(self.next_5)

        self.review = ScrollLabel(self)
        self.review.setStyleSheet("background:#d9d4e7; color: #3C5A75; ")

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(self.button_create_csv, 0, 0)
        layout.addWidget(self.button_dataset, 1, 0, 1, 1)
        layout.addWidget(self.button_dataset2, 2, 0)
        layout.addWidget(self.review, 0, 1, 3, 5)
        layout.addWidget(self.logo_label, 3, 0, 1, 1)

        layout.addWidget(self.button_class_1, 3, 1)
        layout.addWidget(self.button_class_2, 3, 2)
        layout.addWidget(self.button_class_3, 3, 3)
        layout.addWidget(self.button_class_4, 3, 4)
        layout.addWidget(self.button_class_5, 3, 5)

        self.show()

    def choice_1(self) -> None:
        """The function show dialog window to make csv of initial dataset
        """
        dialog = QDialog(self)
        dialog.setWindowTitle('Create file CSV')
        dialog.setFixedSize(500, 200)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #C3D0DB; min-height:30%')
        self.folderpath = ''
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setTextMargins(10, 10, 10, 10)
        self.path_line_edit.setStyleSheet(
            "background:#d9d4e7; border-radius: 5px; color: #0e172c; min-height:30%")

        browse_button = QPushButton("Browse source directory", dialog)
        browse_button.setFont(QFont("Sanserif", 10))
        browse_button.clicked.connect(self.select_folder)
        browse_button.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-height:30%")
        browse_button.adjustSize()

        create_button = QPushButton("Сreate CSV", dialog)
        create_button.setFont(QFont("Sanserif", 10))
        create_button.setStyleSheet(
            "background:#3C5A75; border-radius: 5px;min-height:30%")
        create_button.clicked.connect(self.create_csv)
        create_button.adjustSize()

        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(browse_button)
        layout.addWidget(create_button)
        dialog.setLayout(layout)

        dialog.exec_()

    def double_choice(self) -> None:
        """The function show window to make copies of dataset
        """
        dialog = QDialog(self)
        dialog.setWindowTitle('Create file CSV')
        dialog.setFixedSize(500, 300)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #C3D0DB; min-height:30%')
        self.old_folderpath = ''
        self.new_folderpath = ''

        self.old_path_line_edit = QLineEdit(dialog)
        self.old_path_line_edit.setEnabled(False)
        self.old_path_line_edit.setTextMargins(10, 10, 10, 10)
        self.old_path_line_edit.setStyleSheet(
            "background:#d9d4e7; border-radius: 5px; color: #0e172c;")

        self.new_path_line_edit = QLineEdit(dialog)
        self.new_path_line_edit.setEnabled(False)
        self.new_path_line_edit.setTextMargins(10, 10, 10, 10)
        self.new_path_line_edit.setStyleSheet(
            "background:#d9d4e7; border-radius: 5px; color: #0e172c;")

        browse_button = QPushButton("Browse source directory", dialog)
        browse_button.setFont(QFont("Sanserif", 10))
        browse_button.clicked.connect(self.select_old_folder)
        browse_button.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-height:30%")
        browse_button.adjustSize()

        browse_button_2 = QPushButton("Browse destination directory ", dialog)
        browse_button_2.setFont(QFont("Sanserif", 10))
        browse_button_2.clicked.connect(self.select_new_folder)
        browse_button_2.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-height:30%")
        browse_button_2.adjustSize()

        create_button = QPushButton("Make new dataset", dialog)
        create_button.setFont(QFont("Sanserif", 10))
        create_button.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-height:30%")
        if self.mode == 2:
            create_button.clicked.connect(self.create_dataset_2)
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

    def choice_2(self) -> None:
        """
        The function changes the mode in which the dialog box will launch
        """
        self.mode = 2
        self.double_choice()

    def choice_3(self) -> None:
        """
        The function changes the mode in which the dialog box will launch
        """
        self.mode = 3
        self.double_choice()

    def select_folder(self) -> None:
        """
        The function gets the path to the source dataset and creates iterators for each class
        """
        self.folderpath = (QFileDialog.getExistingDirectory(
            self, 'Select Folder')).replace('/', '\\')
        self.iter1 = libs.task_5.Iterator(self.folderpath, '1')
        self.iter2 = libs.task_5.Iterator(self.folderpath, '2')
        self.iter3 = libs.task_5.Iterator(self.folderpath, '3')
        self.iter4 = libs.task_5.Iterator(self.folderpath, '4')
        self.iter5 = libs.task_5.Iterator(self.folderpath, '5')

        self.path_line_edit.setText(self.folderpath)

    def select_old_folder(self) -> None:
        """
        The function gets the path to the dataset to transform
        """
        self.old_folderpath = (QFileDialog.getExistingDirectory(
            self, 'Select Folder')).replace('/', '\\')
        self.old_path_line_edit.setText(self.old_folderpath)

    def select_new_folder(self) -> None:
        """
        The function gets the path to the directory for creating a new dataset
        """
        self.new_folderpath = (QFileDialog.getExistingDirectory(
            self, 'Select Folder')).replace('/', '\\')
        self.new_path_line_edit.setText(self.new_folderpath)

    def create_csv(self) -> None:
        """
        The function creates a csv annotation for the source dataset
        """
        path = self.folderpath.split('\\')[-1]
        libs.task_1.make_csv(path)

    def create_dataset_2(self) -> None:
        """
        The function creates a csv annotation for a copy of the dataset
        """
        old_path = self.old_folderpath.split('\\')[-1]
        new_path = self.new_folderpath.split('\\')[-1]
        print(old_path, new_path)
        libs.task_2.main(old_path, new_path)

    def create_dataset_random(self) -> None:
        """
        The function creates a csv annotation for a copy of the dataset with random names
        """
        old_path = self.old_folderpath.split('\\')[-1]
        new_path = self.new_folderpath.split('\\')[-1]
        print(old_path, new_path)
        libs.task_3.main(old_path, new_path)

    def next_1(self) -> None:
        """ The function gets the file text from the iterator for class 1"""
        try:
            with open(next(self.iter1), 'r', encoding='utf-8') as file:
                self.review.setText(''.join(file.readlines()))
        except StopIteration:
            MessageBox(self, 'Class 1 is end')
            self.iter1 = libs.task_5.Iterator(self.folderpath, '1')

    def next_2(self) -> None:
        """ The function gets the file text from the iterator for class 2"""
        try:
            with open(next(self.iter1), 'r', encoding='utf-8') as file:
                self.review.setText(''.join(file.readlines()))
        except StopIteration:
            MessageBox(self, 'Class 2 is end')
            self.iter1 = libs.task_5.Iterator(self.folderpath, '2')

    def next_3(self) -> None:
        """ The function gets the file text from the iterator for class 3"""
        try:
            with open(next(self.iter1), 'r', encoding='utf-8') as file:
                self.review.setText(''.join(file.readlines()))
        except StopIteration:
            MessageBox(self, 'Class 3 is end')
            self.iter1 = libs.task_5.Iterator(self.folderpath, '3')

    def next_4(self) -> None:
        """ The function gets the file text from the iterator for class 4"""
        try:
            with open(next(self.iter1), 'r', encoding='utf-8') as file:
                self.review.setText(''.join(file.readlines()))
        except StopIteration:
            MessageBox(self, 'Class 4 is end')
            self.iter1 = libs.task_5.Iterator(self.folderpath, '4')

    def next_5(self) -> None:
        """ The function gets the file text from the iterator for class 5"""
        try:
            with open(next(self.iter1), 'r', encoding='utf-8') as file:
                self.review.setText(''.join(file.readlines()))
        except StopIteration:
            MessageBox(self, 'Class 5 is end')
            self.iter1 = libs.task_5.Iterator(self.folderpath, '5')


def start() -> None:
    """The function makes a main Window and show it
    """
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
