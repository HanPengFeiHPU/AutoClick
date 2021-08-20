# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
# class ComboxDemo(QWidget):
#     def __init__(self,parent=None):
#         super(ComboxDemo,self).__init__(parent)
#         self.setWindowTitle("倒计时")
#         self.resize(300,90)
#         layout = QVBoxLayout()
#         self.lb1 = QLabel("")
#
#         self.cb = QComboBox()
#         self.cb.addItem("C")
#         self.cb.addItem("D")
#         self.cb.addItems(["E","F"])
#         self.cb.currentIndexChanged.connect(self.selectionchange)
#         layout.addWidget(self.cb)
#         layout.addWidget(self.lb1)
#         self.setLayout(layout)

#     def selectionchange(self,i):
#         self.lb1.setText(self.cb.currentText())
#         print("Items in the list are:")
#         for count in range(self.cb.count()):
#             print("item"+str(count)+"="+self.cb.itemText(count))
#             print("Current index",i,"selection changed",self.cb.currentText())
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     comboxDemo = ComboxDemo()
#     comboxDemo.show()
#     sys.exit(app.exit())
# !/usr/bin/python3
# -*- coding: utf-8 -*-


# import sys
#
# # 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
# from PyQt5.QtWidgets import QApplication, QWidget
#
# if __name__ == '__main__':
#     # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
#     app = QApplication(sys.argv)
#     # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
#     w = QWidget()
#     # resize()方法调整窗口的大小。这离是250px宽150px高
#     w.resize(250, 150)
#     # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
#     w.move(300, 300)
#     # 设置窗口的标题
#     w.setWindowTitle('Simple')
#     # 显示在屏幕上
#     w.show()
#
#     # 系统exit()方法确保应用程序干净的退出
#     # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication,QComboBox)
from PyQt5.QtGui import QFont
import datetime

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.tag_date = datetime.datetime.strptime('2021-05-29', '%Y-%m-%d')
        self.now_date = datetime.datetime.strptime(str(datetime.datetime.now()).split(' ')[0], '%Y-%m-%d')
        self.delta = str(self.tag_date - self.now_date).split(' ')[0]
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        review = QLabel('Days')

        titleEdit = QComboBox()
        titleEdit.addItems(["软考"])
        titleEdit.currentIndexChanged.connect(self.selectionchange)

        reviewEdit = QTextEdit()
        reviewEdit.setText(self.delta)
        reviewEdit.setFont(QFont("",40,QFont.Bold))
        reviewEdit.setDisabled(True)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(150, 150, 100, 150)
        self.setWindowTitle('倒计时')
        self.show()
    def selectionchange(self,i):
        print("Items in the list are:",i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())