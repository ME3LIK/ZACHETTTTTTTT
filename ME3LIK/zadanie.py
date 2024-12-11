from PyQt5 import QtWidgets, QtGui, QtCore
import form


class Mywindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = form.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open)
        self.ui.pushButton_4.clicked.connect(self.tri)
        self.ui.pushButton_5.clicked.connect(self.rkr)
        self.ui.checkBox.clicked.connect(self.dva)
        self.ui.checkBox_2.clicked.connect(self.dva)
        self.ui.checkBox_3.clicked.connect(self.dva)
        self.ui.comboBox.currentIndexChanged.connect(self.last)
        

    
    def dva(self):
        if self.ui.checkBox.isChecked():
            self.ui.label_2.clear()
            self.ui.label_2.setText("5")
        if self.ui.checkBox_2.isChecked():
            self.ui.label_2.clear()
            self.ui.label_2.setText("15")
        if self.ui.checkBox_3.isChecked():
            self.ui.label_2.clear()
            self.ui.label_2.setText("50")
        if self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked():
            self.ui.label_2.clear()
            self.ui.label_2.setText("20")
        if self.ui.checkBox.isChecked() and self.ui.checkBox_3.isChecked():
            self.ui.label_2.clear()
            self.ui.label_2.setText("55")
        if self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked():
            self.ui.label_2.clear()
            self.ui.label_2.setText("65")
        if self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked():
            self.ui.label_2.clear()
            self.ui.label_2.setText("70")
    def tri(self):
        a = float(self.ui.lineEdit_2.text())
        b = float(self.ui.lineEdit_3.text())
        if self.ui.radioButton.isChecked():
            self.ui.label_3.setText(a+b)
        if self.ui.radioButton_2.isChecked():
            self.ui.label_3.setText(a-b)
        if self.ui.radioButton_3.isChecked():
            self.ui.label_3.setText(a*b)
        if self.ui.radioButton_4.isChecked():
            self.ui.label_3.setText(a/b)

    def rkr(self):
        QtWidgets.QMessageBox.information(window, "О программе", "Блисковка Ярослав Александрович ИП-24-26Б"
                                          ,buttons=QtWidgets.QMessageBox.Ok
                                          ,defaultButton=QtWidgets.QMessageBox.NoButton)
    
    def open(self):
        a = float(self.ui.lineEdit.text())
        window.ui.label_5.setText(str(a))

    def last(self):
        country = self.comboBox_countries.currentText()
        if country == "Россия":
            self.label_country_flag.setPixmap(QtGui.QPixmap("flag_russia.png"))
        elif country == "Англия":
            self.label_country_flag.setPixmap(QtGui.QPixmap("flag_uk.png"))
        elif country == "США":
            self.label_country_flag.setPixmap(QtGui.QPixmap("flag_usa.png"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())



