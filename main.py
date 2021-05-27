 # This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader


class mainwindow(QWidget):
    def __init__(self):
        super(mainwindow, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()

        self.a = ''
        self.b = ''
        self.op = ''
        self.op2 = ''

        self.ui.sum.clicked.connect(self.sum)
        self.ui.sub.clicked.connect(self.sub)
        self.ui.mul.clicked.connect(self.mul)
        self.ui.div.clicked.connect(self.div)
        self.ui.equal.clicked.connect(self.equal)

        self.ui.clear.clicked.connect(self.clear)
        self.ui.btn_dot.clicked.connect(self.dot)
        self.ui.negative.clicked.connect(self.negative)
        self.ui.percent.clicked.connect(self.percent)


        self.ui.btn_1.clicked.connect(partial(self.num, '1'))
        self.ui.btn_2.clicked.connect(partial(self.num, '2'))
        self.ui.btn_3.clicked.connect(partial(self.num, '3'))
        self.ui.btn_4.clicked.connect(partial(self.num, '4'))
        self.ui.btn_5.clicked.connect(partial(self.num, '5'))
        self.ui.btn_6.clicked.connect(partial(self.num, '6'))
        self.ui.btn_7.clicked.connect(partial(self.num, '7'))
        self.ui.btn_8.clicked.connect(partial(self.num, '8'))
        self.ui.btn_9.clicked.connect(partial(self.num, '9'))
        self.ui.btn_0.clicked.connect(partial(self.num, '0'))

    def num(self, x):
        self.ui.tb1.setText(self.ui.tb1.text() + x)



    def equal(self):

        if self.op2 != '%':
            self.b = self.ui.tb1.text()

        if isinstance(self.a, str):
            if '.' in self.a:
                self.a = float(self.a)
            else:
                self.a = int(self.a)

        if isinstance(self.b, str):
            if '.' in self.b:
                self.b = float(self.b)
            else:
                self.b = int(self.b)
        # if '.' in self.b and isinstance(self.b, str):
        #     self.b = float(self.b)
        # else:
        #     self.b = int(self.b)

        if self.op == '+':
            if self.op2 == '%':
                self.a, self.b = int(self.a),int(self.b)
                res = (self.a) + (self.b / 100)*(self.a)
                self.op2 = ''
            else:
                res = (self.a) + (self.b)

        elif self.op == '-':
            if self.op2 == '%':
                self.a, self.b = int(self.a),int(self.b)
                res = (self.a) - (self.b / 100)*(self.a)
                self.op2 = ''
            else:
                res = (self.a) - (self.b)
        elif self.op == '*':
            res = (self.a) * (self.b)
        elif self.op == '/':
            if self.b != '0':
                res = (self.a) / (self.b)
            else:
                self.ui.tb1.clear()
                self.ui.tb1.setText('IMPOSSIBLE!')

        # res = self.a
        if res is not None:
            if type(res) is float:
                res = format(res, '.7f')

        self.ui.tb1.setText(str(res).rstrip('0'))

    def sum(self):
        self.op = '+'
        self.a = self.ui.tb1.text()
        self.ui.tb1.clear()

    def sub(self):
        self.op = '-'
        self.a = self.ui.tb1.text()
        self.ui.tb1.clear()

    def mul(self):
        self.op = '*'
        self.a = self.ui.tb1.text()
        self.ui.tb1.clear()

    def div(self):
        self.op = '/'
        self.a = self.ui.tb1.text()
        self.ui.tb1.clear()

    def clear(self):
        self.ui.tb1.setText('')
        self.a = ''
        self.b = ''

    def dot(self):
        if '.' not in self.ui.tb1.text():
            self.ui.tb1.setText(self.ui.tb1.text() + '.')

    def negative(self):
        if '-' in self.ui.tb1.text():
            self.ui.tb1.setText(self.ui.tb1.text().lstrip('-'))
        else:
            self.ui.tb1.setText('-' + self.ui.tb1.text())

    def percent(self):
        self.op2 = '%'
        self.b = self.ui.tb1.text()
        self.ui.tb1.clear()



if __name__ == "__main__":
    app = QApplication([])
    window = mainwindow()
    sys.exit(app.exec())
