# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 433)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 30, 141, 51))
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 92, 241, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 150, 241, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 210, 241, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 270, 241, 41))
        self.pushButton_4.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 339, 241, 41))
        self.lineEdit.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "InputDialog"))
        self.pushButton.setText(_translate("Form", "ВВОД СТРОКИ"))
        self.pushButton_2.setText(_translate("Form", "ВВОД ЦЕЛОГО ЧИСЛА"))
        self.pushButton_3.setText(_translate("Form", "ВВОД ВЕЩ. ЧИСЛА"))
        self.pushButton_4.setText(_translate("Form", "ВЫБОР ПУНКТА ИЗ СПИСКА"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())