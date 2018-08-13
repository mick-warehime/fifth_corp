# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../pyqt/combat.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CombatForm(object):
    def setupUi(self, CombatForm):
        CombatForm.setObjectName("CombatForm")
        CombatForm.resize(640, 480)
        self.label = QtWidgets.QLabel(CombatForm)
        self.label.setGeometry(QtCore.QRect(210, 200, 60, 16))
        self.label.setObjectName("label")

        self.retranslateUi(CombatForm)
        QtCore.QMetaObject.connectSlotsByName(CombatForm)

    def retranslateUi(self, CombatForm):
        _translate = QtCore.QCoreApplication.translate
        CombatForm.setWindowTitle(_translate("CombatForm", "Form"))
        self.label.setText(_translate("CombatForm", "Combat!"))
