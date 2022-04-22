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
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtGui
import xunuo


def read_txt():
    if ui.read_flag == 0:
        data = np.loadtxt("D:/学习资料/毕业设计/徐诺/桥梁测量数据.txt")
        ui.weizhi = data[:,0].tolist()
        ui.yingbian = data[:,1].tolist()
        ui.timer.timeout.connect(update)
    # _weizhi = ui.weizhi[(ui.read_flag - 1) * 100:ui.read_flag * 100]
    # print(_weizhi)
    # print(len(_weizhi))
    else:
        # ui.timer.timeout.connect(update)
        ui.timer.start(1000)



def huatu(ui_x,ui_y):
    ui.graph_huatu.clear()
    ui.graph_huatu.addPlot(title="bridge detect", x=ui_x, y=ui_y)


def jiance():
    weizhi = int(ui.lineEdit_weihzi.text())
    print(weizhi)
    print(ui.yingbian[weizhi - 1])
    print(type(ui.yingbian[weizhi - 1]))
    ui.lineEdit_yingbian.setText(str(ui.yingbian[weizhi - 1]))

def update():
    ui.read_flag += 1
    ui._weizhi = []
    ui._yingbian = []
    ui._weizhi = ui.weizhi[(ui.read_flag-1)*100:ui.read_flag*100]
    ui._yingbian = ui.yingbian[(ui.read_flag - 1) * 100:ui.read_flag * 100]
    huatu(ui._weizhi, ui._yingbian)

def stop_read():
    ui.timer.stop()



def click_button():
    ui.button_kaishi.clicked.connect(read_txt)
    #ui.button_kaishi.clicked.connect(huatu)
    ui.button_chaxun.clicked.connect(jiance)
    ui.button_zanting.clicked.connect(stop_read)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = xunuo.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    click_button()
    #huatu()
    sys.exit(app.exec_())
