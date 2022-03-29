# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(270, 142)
        Form.setStyleSheet("font: 9pt \"Microsoft YaHei UI\";")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.labelRegion = QtWidgets.QLabel(Form)
        self.labelRegion.setStyleSheet("")
        self.labelRegion.setFrameShape(QtWidgets.QFrame.Box)
        self.labelRegion.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelRegion.setObjectName("labelRegion")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelRegion)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEditContent = QtWidgets.QTextEdit(Form)
        self.textEditContent.setAutoFillBackground(True)
        self.textEditContent.setObjectName("textEditContent")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEditContent)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "位置"))
        self.labelRegion.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "文本"))
