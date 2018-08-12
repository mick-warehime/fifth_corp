# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Mick/Documents/Projects/fifth_corp/src/view/decision.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DecisionForm(object):
    def setupUi(self, DecisionForm):  # type ignore
        DecisionForm.setObjectName("DecisionForm")
        DecisionForm.resize(640, 480)
        self.verticalLayoutWidget = QtWidgets.QWidget(DecisionForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 240, 331, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fight_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.fight_button.setObjectName("fight_button")
        self.verticalLayout.addWidget(self.fight_button)
        self.back_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)
        self.label = QtWidgets.QLabel(DecisionForm)
        self.label.setGeometry(QtCore.QRect(150, 40, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(DecisionForm)
        QtCore.QMetaObject.connectSlotsByName(DecisionForm)

    def retranslateUi(self, DecisionForm):  # type ignore

        _translate = QtCore.QCoreApplication.translate
        DecisionForm.setWindowTitle(_translate("DecisionForm", "Form"))
        self.fight_button.setText(_translate("DecisionForm", "Fight"))
        self.back_button.setText(_translate("DecisionForm", "Back"))
        self.label.setText(_translate("DecisionForm", "Decision Time"))
