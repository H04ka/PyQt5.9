from PyQt5 import QtWidgets
import un

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = un.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Text)
        self.ui.pushButton_2.clicked.connect(self.Int)
        self.ui.pushButton_3.clicked.connect(self.Double)
        self.ui.pushButton_4.clicked.connect(self.Item)

    def Text(self):
        try:
            text, ok = QtWidgets.QInputDialog.getText(window, "Вывод строки", "Текст", echo=0)
            if ok:
                self.ui.lineEdit.setText(str(text))
        except ValueError:
             QtWidgets.QMessageBox.critical(window, 'Empty String Error', 'Строка пуста, введите значение', buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)
    def Int(self):
        try:
            c_chislo, ok = QtWidgets.QInputDialog.getInt(window, "Ввод целого числа", "число", min=0, max=10, step=1)
            if ok:
                self.ui.lineEdit.setText(str(c_chislo))
        except ValueError:
             QtWidgets.QMessageBox.critical(window, 'Empty String Error', 'Строка пуста, введите значение', buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)

    def Double(self):
        try:
             v_chislo, ok = QtWidgets.QInputDialog.getDouble(window, "Вывод вещественного числа", "число",value=0, min = -2147483647, max = 2147483647, decimals=3)
             if ok:
                  self.ui.lineEdit.setText(str(v_chislo))
        except ValueError:
             QtWidgets.QMessageBox.critical(window, 'Empty String Error', 'Строка пуста, введите значение', buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)
    def Item(self):
        try:
             item, ok = QtWidgets.QInputDialog.getItem(window, "САМЫЙ ВАЖНЫЙ ВЫБОР", "Выбрано", ["На танки сам сяду", "На танки друга посажу", "В танки батя играет"], current=0, editable=False)
             if ok:
                  self.ui.lineEdit.setText(str(item))
        except ValueError:
             QtWidgets.QMessageBox.critical(window, 'Empty String Error', 'Строка пуста, введите значение', buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
