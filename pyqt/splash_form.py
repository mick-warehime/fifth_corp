# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Mick/Documents/Projects/fifth_corp/src/view/splash.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashForm(object):
    def setupUi(self, SplashForm):
        SplashForm.setObjectName("SplashForm")
        SplashForm.resize(640, 480)
        self.verticalLayoutWidget = QtWidgets.QWidget(SplashForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 240, 331, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.newgame_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.newgame_button.setObjectName("newgame_button")
        self.verticalLayout.addWidget(self.newgame_button)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(SplashForm)
        self.label.setGeometry(QtCore.QRect(200, 40, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(SplashForm)
        QtCore.QMetaObject.connectSlotsByName(SplashForm)

    def retranslateUi(self, SplashForm):
        _translate = QtCore.QCoreApplication.translate
        SplashForm.setWindowTitle(_translate("SplashForm", "Form"))
        self.newgame_button.setText(_translate("SplashForm", "New Game"))
        self.pushButton_3.setText(_translate("SplashForm", "Settings"))
        self.pushButton.setText(_translate("SplashForm", "Quit"))
        self.label.setText(_translate("SplashForm", "5th Corp"))
