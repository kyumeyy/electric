# -*- coding: UTF-8 -*-

#导入PyQt5组件
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QFormLayout,\
QVBoxLayout,QHBoxLayout,QTextEdit,QLineEdit,QListView,QMessageBox,QComboBox, \
QScrollArea,QMainWindow,QTableWidget,QTableWidgetItem,QMainWindow,QAction,qApp, \
QInputDialog,QFileDialog
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QFont,QPixmap,QPalette
from PyQt5.QtCore import Qt

#from pylab import*    #交互性能好

#三维绘图
import matplotlib.animation as animation

from matplotlib import pyplot as plt

import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

#导入系统组件
import sys

#导入自定义组件
#from mycommand import *
#from editor import *

#导入其它组件
import re          #导入正则
import os

#查询对象和命令
#PyQt5.QtWidgets.QTableWidget.selectRow

# <<<<<<<<<<定义主窗口类
class mywindow(QMainWindow):

    # <<<<<<<<<<类的初始化方法
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口')
        self.setGeometry(50, 50, 1800, 900)
        self.addui()

    # >>>>>>>>>>

    # <<<<<<<<<<创建GUI方法
    def addui(self):
        mylayout=QVBoxLayout()
        button1=QPushButton('绘图')
        button1.clicked.connect(self.drawlineanimation)
        button2=QPushButton('立方体')
        button2.clicked.connect(self.cube)
        mylayout.addWidget(button1)
        mylayout.addWidget(button2)
        mywidget=QWidget()
        mywidget.setLayout(mylayout)
        self.setCentralWidget(mywidget)

    def drawlineanimation(self):
        fig=plt.figure()
        ax=plt.axes()
        x=[]
        y=[]
        line,=ax.plot([],[],'gray')
        def initline():
            ax.set_xlim(1,50)
            ax.set_ylim(1,50)
            return line,
        def updateline(i):
            x.append(i)
            y.append(i+np.sin(i))
            line.set_data(x,y)
            return line,
        ani=animation.FuncAnimation(fig,updateline,frames=np.linspace(0, 50, 128),init_func=initline,interval=50,blit=True)
        plt.show()
    #绘制立方体
    def cube(self):
        fig=plt.figure()
        ax=plt.axes(projection='3d')
        xd=range(30)
        yd=range(30)
        zd=range(30)
        ax.scatter3D(xd,yd,zd, cmap='Blues')  #绘制散点图    没有这个散点图坐标轴会缩放到一个尺寸
        a=5
        b=6
        c=30
        #画xy面
        x,y=np.mgrid[0:a:5j,0:b:5j]
        z=np.zeros((5,5),)
        ax.plot_surface(x,y,z,color='r',rstride=1,cstride=1)
        z=z+c
        ax.plot_surface(x,y,z,color='r',rstride=1,cstride=1)
        #画xz面
        x,z=np.mgrid[0:a:5j,0:c:5j]
        y=np.zeros((5,5),)
        ax.plot_surface(x,y,z,color='r',rstride=1,cstride=1)
        y=y+b
        ax.plot_surface(x,y,z,color='r',rstride=1,cstride=1)
        #画yz面
        y,z=np.mgrid[0:b:5j,0:c:5j]
        x=np.zeros((5,5),)
        ax.plot_surface(x,y,z,color='r',rstride=1,cstride=1)
        x=x+a
        ax.plot_surface(x,y,z,color='r',rstride=1,cstride=1)
        plt.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    mywin=mywindow()
    mywin.show()
    sys.exit(app.exec_())
