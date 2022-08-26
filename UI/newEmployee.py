# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newEmployee.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newEmployee(object):
    def setupUi(self, newEmployee):
        newEmployee.setObjectName("newEmployee")
        newEmployee.resize(744, 324)
        self.centralwidget = QtWidgets.QWidget(newEmployee)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 20, 681, 241))
        self.frame.setMaximumSize(QtCore.QSize(681, 241))
        self.frame.setStyleSheet("\n"
"border: 1px solid rgb(186, 186, 186);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setStyleSheet("border:0px;\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 40, 641, 181))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, -1, 641, 188))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 8, 5, 5)
        self.formLayout.setHorizontalSpacing(32)
        self.formLayout.setVerticalSpacing(18)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("border:0px")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("border:0px;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setStyleSheet("border:0px;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setStyleSheet("border:0px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setStyleSheet("border:0px;")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.idInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.idInput.setObjectName("idInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idInput)
        self.nameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nameInput.setObjectName("nameInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameInput)
        self.addressInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.addressInput.setObjectName("addressInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.addressInput)
        self.salaryInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.salaryInput.setObjectName("salaryInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.salaryInput)
        self.jobTypecomboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.jobTypecomboBox.setObjectName("jobTypecomboBox")
        self.jobTypecomboBox.addItem("")
        self.jobTypecomboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.jobTypecomboBox)
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(480, 270, 75, 23))
        self.saveBtn.setObjectName("saveBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(560, 270, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.helpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.helpBtn.setGeometry(QtCore.QRect(640, 270, 75, 23))
        self.helpBtn.setObjectName("helpBtn")
        newEmployee.setCentralWidget(self.centralwidget)

        self.retranslateUi(newEmployee)
        QtCore.QMetaObject.connectSlotsByName(newEmployee)

    def retranslateUi(self, newEmployee):
        _translate = QtCore.QCoreApplication.translate
        newEmployee.setWindowTitle(_translate("newEmployee", "Add New Employee"))
        self.label.setText(_translate("newEmployee", "New Employee"))
        self.label_2.setText(_translate("newEmployee", "ID:"))
        self.label_3.setText(_translate("newEmployee", "Job Type:"))
        self.label_4.setText(_translate("newEmployee", "Salary:"))
        self.label_5.setText(_translate("newEmployee", "Address:"))
        self.label_6.setText(_translate("newEmployee", "Name:"))
        self.nameInput.setPlaceholderText(_translate("newEmployee", "eg. Amjad"))
        self.addressInput.setPlaceholderText(_translate("newEmployee", "[Enter Full Address Here]"))
        self.salaryInput.setPlaceholderText(_translate("newEmployee", "eg. RS 18000"))
        self.jobTypecomboBox.setItemText(0, _translate("newEmployee", "Employee"))
        self.jobTypecomboBox.setItemText(1, _translate("newEmployee", "Saleman"))
        self.saveBtn.setText(_translate("newEmployee", "Save"))
        self.cancelBtn.setText(_translate("newEmployee", "Cancel"))
        self.helpBtn.setText(_translate("newEmployee", "Help"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newEmployee = QtWidgets.QMainWindow()
    ui = Ui_newEmployee()
    ui.setupUi(newEmployee)
    newEmployee.show()
    sys.exit(app.exec_())
