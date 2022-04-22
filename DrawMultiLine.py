#Author:-*-coding = utf-8 -*-
#@Time : 2022/4/20 16:21
#@Author : Shenzhi_Yang
#@File : DrawMultiLine.py
#@Software : PyCharm
import sys , math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine,self).__init__()
        self.resize(300,300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.begin(self)

        pen = QPen(Qt.Red,3,Qt.SolidLine)

        painter.setPen(pen)
        painter.drawLine(20,40,250,40)
        size = self.size()

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())