# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(900, 600)
        mainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        mainWindow.setMaximumSize(QtCore.QSize(1200, 800))

        # 创建主窗口的中心部件
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        mainWindow.setCentralWidget(self.centralwidget)

        # 创建一个主布局管理器
        self.mainLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        # 左侧布局
        self.leftWidget = QtWidgets.QWidget()
        self.leftLayout = QtWidgets.QVBoxLayout(self.leftWidget)

        # 左侧的上半部分布局
        self.topWidget = QtWidgets.QWidget()
        self.topLayout = QtWidgets.QVBoxLayout(self.topWidget)

        # 左侧的QLabel
        self.label = QtWidgets.QLabel(self.topWidget)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QtCore.QSize(100, 50))  # 设置最小大小
        self.topLayout.addWidget(self.label)

        # 左侧的QComboBox
        self.comboBox = QtWidgets.QComboBox(self.topWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setMinimumSize(QtCore.QSize(200, 50))  # 设置最小大小
        self.comboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)  # 设置大小策略
        self.topLayout.addWidget(self.comboBox)

        # 左侧的按钮布局
        self.buttonLayout = QtWidgets.QGridLayout()  # 使用网格布局管理按钮
        self.push1 = QtWidgets.QPushButton(self.topWidget)
        self.push1.setObjectName("push1")
        self.push1.setMinimumSize(QtCore.QSize(100, 50))  # 设置最小大小
        self.buttonLayout.addWidget(self.push1, 0, 0)  # 第0行第0列

        self.push2 = QtWidgets.QPushButton(self.topWidget)
        self.push2.setObjectName("push2")
        self.push2.setMinimumSize(QtCore.QSize(100, 50))  # 设置最小大小
        self.buttonLayout.addWidget(self.push2, 0, 1)  # 第0行第1列

        self.push3 = QtWidgets.QPushButton(self.topWidget)
        self.push3.setObjectName("push3")
        self.push3.setMinimumSize(QtCore.QSize(100, 50))  # 设置最小大小
        self.buttonLayout.addWidget(self.push3, 1, 0)  # 第1行第0列

        self.push6 = QtWidgets.QPushButton(self.topWidget)
        self.push6.setObjectName("push6")
        self.push6.setMinimumSize(QtCore.QSize(100, 50))  # 设置最小大小
        self.buttonLayout.addWidget(self.push6, 2, 0)  # 第2行第0列

        self.push4 = QtWidgets.QPushButton(self.topWidget)
        self.push4.setObjectName("push4")
        self.push4.setMinimumSize(QtCore.QSize(100, 50))  # 设置最小大小
        self.buttonLayout.addWidget(self.push4, 1, 1)  # 第1行第1列

        self.topLayout.addLayout(self.buttonLayout)

        # 将上半部分布局添加到左侧布局
        self.leftLayout.addWidget(self.topWidget)

        # 左侧的QTextEdit
        self.textEdit = QtWidgets.QTextEdit(self.leftWidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setMinimumSize(QtCore.QSize(200, 300))  # 设置最小大小
        self.leftLayout.addWidget(self.textEdit)


        # 将左侧布局添加到主布局
        self.mainLayout.addWidget(self.leftWidget)
        # 设置左侧布局的拉伸比例为2
        self.mainLayout.setStretch(0, 2)

        # 右侧布局
        self.rightWidget = QtWidgets.QWidget()
        self.rightLayout = QtWidgets.QVBoxLayout(self.rightWidget)

        # 右侧的QGraphicsView
        self.graphicsView = QtWidgets.QGraphicsView(self.rightWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setMinimumSize(QtCore.QSize(300, 300))  # 设置最小大小
        self.rightLayout.addWidget(self.graphicsView)

        # 将右侧布局添加到主布局
        self.mainLayout.addWidget(self.rightWidget)
        # 设置右侧布局的拉伸比例为3
        self.mainLayout.setStretch(1, 3)

        # 设置状态栏
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "AI路灯"))
        self.label.setText(_translate("mainWindow", "选择推理源:"))
        self.comboBox.setItemText(0, _translate("mainWindow", "笔记本摄像头"))
        self.comboBox.setItemText(1, _translate("mainWindow", "ZED摄像头"))
        self.comboBox.setItemText(2, _translate("mainWindow", "本地图片"))
        self.comboBox.setItemText(3, _translate("mainWindow", "本地视频"))
        self.push1.setText(_translate("mainWindow", "加载本地视频"))
        self.push2.setText(_translate("mainWindow", "启动摄像头"))
        self.push3.setText(_translate("mainWindow", "启动识别"))
        self.push6.setText(_translate("mainWindow", "暂停视频"))
        self.push4.setText(_translate("mainWindow", "播放视频"))
        self.textEdit.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">显示日志</span></p></body></html>"))
        # 设置字体大小
        self.setFontSize(mainWindow)

    def setFontSize(self, mainWindow):
        # 设置主窗口标题的字体大小
        font = QtGui.QFont()
        font.setPointSize(14)  # 设置字体大小为14
        mainWindow.setFont(font)

        # 设置QLabel的字体大小
        font = QtGui.QFont()
        font.setPointSize(12)  # 设置字体大小为12
        self.label.setFont(font)

        # 设置QComboBox的字体大小
        font = QtGui.QFont()
        font.setPointSize(12)  # 设置字体大小为12
        self.comboBox.setFont(font)

        # 设置按钮的字体大小
        font = QtGui.QFont()
        font.setPointSize(12)  # 设置字体大小为12
        self.push1.setFont(font)
        self.push2.setFont(font)
        self.push3.setFont(font)
        self.push6.setFont(font)
        self.push4.setFont(font)

        # 设置QTextEdit的字体大小
        font = QtGui.QFont()
        font.setPointSize(12)  # 设置字体大小为12
        self.textEdit.setFont(font)