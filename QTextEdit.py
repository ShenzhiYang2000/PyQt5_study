#Author:-*-coding = utf-8 -*-
#@Time : 2022/4/20 13:06
#@Author : Shenzhi_Yang
#@File : QTextEdit.py
#@Software : PyCharm
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
import os
import matplotlib.pyplot as plt
import pandas as pd

class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit控件演示')

        self.resize(300,280)

        self.textEdit = QTextEdit()
        #self.lineEdit = QLineEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonHTML = QPushButton('显示HTML')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)

    def onClick_ButtonText(self):
        #self.textEdit.setPlainText('Hello World!')
        f = open("D:/学习资料/毕业设计/徐诺/1.txt")
        X,Y = [],[]




    def onClick_ButtonHTML(self):
        self.textEdit.setHtml('<font color = "blue" size="5">Hello World</font>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())
