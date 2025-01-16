# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 136)
        MainWindow.setMinimumSize(QtCore.QSize(411, 136))
        MainWindow.setMaximumSize(QtCore.QSize(999, 136))
        MainWindow.setStyleSheet("background-color: #292b2c;\n"
"font-weight: bold;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BackupFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackupFolderButton.setMinimumSize(QtCore.QSize(220, 25))
        self.BackupFolderButton.setStyleSheet("QPushButton\n"
"{\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: #5bc0de;\n"
"    border-radius: 5px;\n"
"    color: #5bc0de;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #5bc0de;\n"
"    color: #292b2c;\n"
"}")
        self.BackupFolderButton.setDefault(False)
        self.BackupFolderButton.setFlat(False)
        self.BackupFolderButton.setObjectName("BackupFolderButton")
        self.verticalLayout.addWidget(self.BackupFolderButton)
        self.TargetFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.TargetFolderButton.setMinimumSize(QtCore.QSize(220, 25))
        self.TargetFolderButton.setStyleSheet("QPushButton\n"
"{\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: #5bc0de;\n"
"    border-radius: 5px;\n"
"    color: #5bc0de;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #5bc0de;\n"
"    color: #292b2c;\n"
"}")
        self.TargetFolderButton.setObjectName("TargetFolderButton")
        self.verticalLayout.addWidget(self.TargetFolderButton)
        self.BackupButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackupButton.setMinimumSize(QtCore.QSize(220, 25))
        self.BackupButton.setStyleSheet("QPushButton\n"
"{\n"
"    border-style: solid;\n"
"    border-width: 1.5px;\n"
"    border-color: #5bc0de;\n"
"    border-radius: 5px;\n"
"    color: #5bc0de;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #5bc0de;\n"
"    color: #292b2c;\n"
"}")
        self.BackupButton.setObjectName("BackupButton")
        self.verticalLayout.addWidget(self.BackupButton)
        self.ProcessLabel = QtWidgets.QLabel(self.centralwidget)
        self.ProcessLabel.setMinimumSize(QtCore.QSize(220, 25))
        self.ProcessLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.ProcessLabel.setStyleSheet("border: 1.5px solid #5cb85c;\n"
"border-radius: 5px;\n"
"color: #5cb85c;")
        self.ProcessLabel.setText("")
        self.ProcessLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProcessLabel.setObjectName("ProcessLabel")
        self.verticalLayout.addWidget(self.ProcessLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(120, 0))
        self.groupBox.setStyleSheet("QGroupBox\n"
"{\n"
"    border: 1.5px solid #5bc0de;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CommentLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.CommentLineEdit.setMinimumSize(QtCore.QSize(141, 25))
        self.CommentLineEdit.setStyleSheet("border: 1.5px solid #5bc0de;\n"
"border-radius: 5px;\n"
"color: #5bc0de;")
        self.CommentLineEdit.setInputMask("")
        self.CommentLineEdit.setText("")
        self.CommentLineEdit.setMaxLength(32)
        self.CommentLineEdit.setCursorPosition(0)
        self.CommentLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.CommentLineEdit.setObjectName("CommentLineEdit")
        self.verticalLayout_2.addWidget(self.CommentLineEdit)
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Backuper"))
        self.BackupFolderButton.setText(_translate("MainWindow", "Browse Backup Folder"))
        self.TargetFolderButton.setText(_translate("MainWindow", "Browse Target Folder"))
        self.BackupButton.setText(_translate("MainWindow", "Backup!"))
        self.CommentLineEdit.setPlaceholderText(_translate("MainWindow", "Type Comment Here"))
