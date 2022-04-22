#Author:-*-coding = utf-8 -*-
#@Time : 2022/4/21 14:29
#@Author : Shenzhi_Yang
#@File : xunuoGUI.py
#@Software : PyCharm
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
from PyQt5 import QtCore, QtWidgets,QtGui

class xunuoGUI(QWidget):
    def __init__(self):
        super(xunuoGUI,self).__init__()
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, -90, 931, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/ASUS/Desktop/qiaoliang.png"))
        self.label.setObjectName("label")

        self.initUI()
        self.weizhi = []
        self.yingbian = []

    def initUI(self):
        self.resize(500,500)
        self.setWindowTitle('桥梁形变检测')
        #整体布局
        VLayout1 = QVBoxLayout()#最大的整个界面为垂直布局

        #第一层四个按钮为水平布局
        self.Hlayout = QHBoxLayout()
        self.button_canshu = QPushButton()
        #self.button_canshu.move(0, 0)
        self.button_canshu.setText('参数设置')
        self.button_canshu.setCheckable(True)

        self.button_lishi = QPushButton()
        #self.button_lishi.move(0, 100)
        self.button_lishi.setText('历史查询')
        self.button_lishi.setCheckable(True)


        self.button_kaishi = QPushButton()
        #self.button_kaishi.move(0, 200)
        self.button_kaishi.setText('开始测量')
        self.button_kaishi.setCheckable(True)
        self.button_kaishi.clicked.connect(self.read_txt)
        self.button_kaishi.clicked.connect(self.plot_txt)

        self.button_zanting = QPushButton()
        #self.button_zanting.move(0, 300)
        self.button_zanting.setText('暂停')
        self.button_zanting.setCheckable(True)


        self.Hlayout.addWidget(self.button_canshu)
        self.Hlayout.addWidget(self.button_lishi)
        self.Hlayout.addWidget(self.button_kaishi)
        self.Hlayout.addWidget(self.button_zanting)


        #self.Hlayout.setGeometry(0,0,500,100)

        #桥梁图 未完成
        self.pic_bridge = QLabel('pic_bridge')
        #self.pic_bridge.resize(400,100)
        #self.pic_bridge.move(0,100)
        # self.pic_bridge.setPixmap(QtGui.QPixmap("C:/Users/ASUS/Desktop/qiaoliang.png"))


        #画图控件
        #self.figure, self.ax = plt.subplots(1, 1)
        #self.figure = Figure(figsize = (50,50), dpi = 100)
        self.figure,self.ax = plt.subplots(1, 1)
        self.canvas = FigureCanvas(self.figure)
        #self.canvas.move(0,200)

        #位置 应变 检测 水平布局
        self.hlayout = QHBoxLayout()
        self.label_weizhi = QLabel('位置')
        #self.label_weizhi.move(0,300)
        self.label_weizhi.setStyleSheet('color: white')

        self.lineEdit1 = QLineEdit(self)
        #self.lineEdit1.move(100,300)

        self.label_yingbian = QLabel('应变')
        #self.label_yingbian.move(200,300)
        self.label_yingbian.setStyleSheet('color:white')

        self.lineEdit2 = QLineEdit(self)
        #self.lineEdit2.move(300,300)

        self.button_jiance = QPushButton('检测')
        #self.button_jiance.move(400,300)
        self.button_jiance.clicked.connect(self.jiance)

        self.hlayout.addWidget(self.label_weizhi)
        self.hlayout.addWidget(self.lineEdit1)
        self.hlayout.addWidget(self.label_yingbian)
        self.hlayout.addWidget(self.lineEdit2)
        self.hlayout.addWidget(self.button_jiance)

        #self.hlayout.setGeometry(0,300,500,100)


        #组合起来
        VLayout1.addLayout(self.Hlayout)
        #VLayout1.addStretch(2)
        VLayout1.addWidget(self.pic_bridge)
        VLayout1.addWidget(self.canvas)
        VLayout1.addLayout(self.hlayout)

        self.setLayout(VLayout1)

    def read_txt(self):
        data = np.loadtxt("D:/学习资料/毕业设计/徐诺/1.txt")
        self.weizhi = data[0].tolist()
        self.yingbian = data[1].tolist()
        #print(self.weizhi[3])
        #print(self.yingbian)

    def plot_txt(self):
        x = self.weizhi
        y = self.yingbian
        self.ax.plot(x,y)
        self.canvas.draw()

    def jiance(self):
        weizhi = int(self.lineEdit1.text())
        print(weizhi)
        print(type(self.yingbian[weizhi-1]))
        self.lineEdit2.setText(str(self.yingbian[weizhi-1]))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = xunuoGUI()
    main.show()
    sys.exit(app.exec_())