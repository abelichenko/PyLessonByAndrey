import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Хімчистка')
        self.setWindowIcon(QIcon('exchanging.png'))
        self.ui.input_pib.setPlaceholderText('ПІБ:')
        self.ui.input_product.setPlaceholderText('Виріб:')
        self.ui.input_servise.setPlaceholderText('Вид послуги:')
        self.ui.input_time.setPlaceholderText('Дата прийому:')
        self.ui.input_cost.setPlaceholderText('Вартість послуги:')
        self.ui.pushButton.clicked.connect(self.write_check)

    def write_check(self):
        input_pib = self.ui.input_pib.text()
        input_product = self.ui.input_product.text()
        input_service = self.ui.input_servise.text()
        input_time = self.ui.input_time.text()
        input_cost = self.ui.input_cost.text()
        self.ui.label_3.setText( "\nФіскальний чек\n" + "ФОП \"Dry Cleaning\"" + "\n\n----------------------------\n" + "Замовник: "+str(input_pib) + "\n----------------------------\n" + "Опис виробу: " + str(input_product) + "\n----------------------------\n" + "Вид послуги: " + str(input_service) + "\n-----------------------------\n" + "Дата прийому: " + str(input_time) + "\n----------------------------" + "\n\n----------------------------\n" + "Сумма: " + str(input_cost) + "грн." + "\n----------------------------\n")


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
 
sys.exit(app.exec())


