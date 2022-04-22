#Author:-*-coding = utf-8 -*-
#@Time : 2022/4/19 22:16
#@Author : Shenzhi_Yang
#@File : QLineEdit.py
#@Software : PyCharm
'''
QLineEdit控件与1回显模式

EchoMode(回显模式)

4种回显模式
1.Normal
2.NoEcho(不回显)
3.Password
4.PasswordEchoOnEdit
'''

from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout = QFormLayout()
        normalLineEdit = QLineEdit()
        NoEchoLineEdit = QLineEdit()
        PasswordLineEdit = QLineEdit()
        PasswordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normal",normalLineEdit)
        formLayout.addRow("NoEcho", NoEchoLineEdit)
        formLayout.addRow("Password", PasswordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit", PasswordEchoOnEditLineEdit)

        #placeholdertext未输入前浅浅的提示

        normalLineEdit.setPlaceholderText("Normal")
        NoEchoLineEdit.setPlaceholderText("NoEcho")
        PasswordLineEdit.setPlaceholderText("Password")
        PasswordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        NoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        PasswordLineEdit.setEchoMode(QLineEdit.Password)
        PasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())



