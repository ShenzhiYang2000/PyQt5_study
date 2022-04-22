#Author:-*-coding = utf-8 -*-
#@Time : 2022/3/21 16:28
#@Author : Shenzhi_Yang
#@File : main.py
#@Software : PyCharm
import sys
import demo2

from PyQt5.QtWidgets import  QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = demo2.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())