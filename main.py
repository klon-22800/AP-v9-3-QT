import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication, QMainWindow, QPushButton)
from  PyQt5 import QtWidgets
from design import Ui_Dialog

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.pushButton_file = self.findChild(QPushButton, 'pushButton_file')
        self.label = self.findChild(QLabel, 'label')
        self.pushButton_file.clicked.connect(self.clicker)
        self.mode = '1'
        self.path = ""
    def update_mode(self):
        self.mode = self.findChild(QComboBox, 'comboBox_mode').currentText()

    def clicker(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath:
            self.path = folderpath
            self.label.setText(f'{self.path}')

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())