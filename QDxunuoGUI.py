# Author:-*-coding = utf-8 -*-
# @Time : 2022/4/22 13:05
# @Author : Shenzhi_Yang
# @File : QDxunuoGUI.py
# @Software : PyCharm
# 导入matplotlib模块并使用Qt5Agg
import matplotlib
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')
# 使用 matplotlib中的FigureCanvas (在使用 Qt5 Backends中 FigureCanvas继承自QtWidgets.QWidget)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtGui
import xunuo


def read_txt():
    data = np.loadtxt("D:/学习资料/毕业设计/徐诺/1.txt")
    ui.weizhi = data[0].tolist()
    ui.yingbian = data[1].tolist()
    # print(self.weizhi[3])
    # print(self.yingbian)


def huatu():
    ui.graph_huatu.clear()
    ui.graph_huatu.addPlot(title="bridge detect", x=ui.weizhi, y=ui.yingbian)


def jiance():
    weizhi = int(ui.lineEdit_weihzi.text())
    print(weizhi)
    print(ui.yingbian[weizhi - 1])
    print(type(ui.yingbian[weizhi - 1]))
    ui.lineEdit_yingbian.setText(str(ui.yingbian[weizhi - 1]))


def click_button():
    ui.button_kaishi.clicked.connect(read_txt)
    ui.button_kaishi.clicked.connect(huatu)
    ui.button_chaxun.clicked.connect(jiance)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = xunuo.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    click_button()
    huatu()
    sys.exit(app.exec_())
