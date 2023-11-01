from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.setFixedSize(470,350)

        self.comboBox_mode = QtWidgets.QComboBox(Dialog)
        self.comboBox_mode.setGeometry(QtCore.QRect(240, 20, 201, 21))
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItems(['1','2','3'])

        self.comboBox_class = QtWidgets.QComboBox(Dialog)
        self.comboBox_class.setGeometry(QtCore.QRect(30, 160, 160, 30))
        self.comboBox_class.setObjectName("comboBox_class")
        self.comboBox_class.addItems(['1','2','3','4','5'])

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 70, 141, 51))
        self.pushButton.setObjectName("pushButton")

        self.nextNote = QtWidgets.QPushButton(Dialog)
        self.nextNote.setGeometry(QtCore.QRect(270, 160, 171, 30))
        self.nextNote.setObjectName("nextNote")

        self.pushButton_file = QtWidgets.QPushButton(Dialog)
        self.pushButton_file.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_file.setObjectName("pushButton_file")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 220, 411, 101))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.nextNote.setText(_translate("Dialog", "next note"))
        self.pushButton_file.setText(_translate("Dialog", "Choose folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
