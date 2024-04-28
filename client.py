import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
import requests


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('qtex1.ui', self)
        self.btn.clicked.connect(self.login)

    def login(self):
        log = self.le1.text()
        pas = self.le2.text()
        query = 'http://127.0.0.1:5000/login'
        data = {'login': log, 'password': pas}
        answer = requests.get(query, params=data).json()
        self.lbl_status.setText(answer['answer'])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
