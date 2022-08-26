# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newSupplier.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_newCustomer(object):
    def setupUi(self, newSupplier,first,firstSelf):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE if not exists clients (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), contactperson VARCHAR(255), address VARCHAR(255),phone VARCHAR(255),contact VARCHAR(255),email VARCHAR(255) )")
        mycursor.execute("SELECT id FROM clients")
        result=mycursor.fetchall()
        idToAssign=1
        if result:
            for x in result:
                idToAssign=x[0]+1
        
        
        newSupplier.setObjectName("newSupplier")
        newSupplier.resize(559, 370)
        self.centralwidget = QtWidgets.QWidget(newSupplier)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 40, 521, 271))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 521, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setHorizontalSpacing(17)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.contactPersonInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.contactPersonInput.setObjectName("contactPersonInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.contactPersonInput)
        self.nameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nameInput.setObjectName("nameInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameInput)
        self.phoneInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.phoneInput.setObjectName("phoneInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.phoneInput)
        self.altPhoneInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.altPhoneInput.setObjectName("altPhoneInput")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.altPhoneInput)
        self.emailInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.emailInput.setObjectName("emailInput")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.emailInput)
        self.addressInput = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.addressInput.setObjectName("addressInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.addressInput)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(str(idToAssign))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(300, 320, 75, 23))
        self.saveBtn.setObjectName("saveBtn")
        self.saveBtn.clicked.connect(lambda:saveFunc(self))
        self.cancelInput = QtWidgets.QPushButton(self.centralwidget)
        self.cancelInput.setGeometry(QtCore.QRect(380, 320, 75, 23))
        self.cancelInput.setObjectName("cancelInput")
        self.helpInput = QtWidgets.QPushButton(self.centralwidget)
        self.helpInput.setGeometry(QtCore.QRect(460, 320, 75, 23))
        self.helpInput.setObjectName("helpInput")
        newSupplier.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(newSupplier)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 21))
        self.menubar.setObjectName("menubar")
        newSupplier.setMenuBar(self.menubar)

        self.retranslateUi(newSupplier)
        QtCore.QMetaObject.connectSlotsByName(newSupplier)
        def saveFunc(self):
            if(self.nameInput.text()==''):
                self.label.setStyleSheet('color: rgb(243, 0, 0);')
            else:
                sql="INSERT into clients (name,contactperson,address,phone,contact,email) VALUES(%s,%s,%s,%s,%s,%s) "
                val=(self.nameInput.text(),self.contactPersonInput.text(),self.addressInput.toPlainText(),self.phoneInput.text(),self.altPhoneInput.text(),self.emailInput.text(),)
                mycursor.execute(sql,val)
                mydb.commit()
                first.loadData(firstSelf)
                newSupplier.close()
    def retranslateUi(self, newSupplier):
        _translate = QtCore.QCoreApplication.translate
        newSupplier.setWindowTitle(_translate("newSupplier", "Add New Client"))
        self.label.setText(_translate("newSupplier", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Client:</span></p></body></html>"))
        self.label_2.setText(_translate("newSupplier", "Name"))
        self.label_4.setText(_translate("newSupplier", "Contact Person"))
        self.label_3.setText(_translate("newSupplier", "Address"))
        self.label_5.setText(_translate("newSupplier", "Phone Number"))
        self.label_6.setText(_translate("newSupplier", "Alternative Contact"))
        self.label_7.setText(_translate("newSupplier", "Email"))
        self.contactPersonInput.setPlaceholderText(_translate("newSupplier", "eg. Ali Saab"))
        self.nameInput.setPlaceholderText(_translate("newSupplier", "eg. Ali Brothers"))
        self.phoneInput.setPlaceholderText(_translate("newSupplier", "eg. 03123456789"))
        self.altPhoneInput.setPlaceholderText(_translate("newSupplier", "eg. 042345678"))
        self.emailInput.setPlaceholderText(_translate("newSupplier", "eg. ali@gmail.com"))
        self.addressInput.setPlaceholderText(_translate("newSupplier", "[Enter Full Address Here]"))
        self.label_8.setText(_translate("newSupplier", "ID"))
        self.lineEdit.setToolTip(_translate("newSupplier", "ID auto Generated"))
        self.saveBtn.setText(_translate("newSupplier", "Save"))
        self.cancelInput.setText(_translate("newSupplier", "Cancel"))
        self.helpInput.setText(_translate("newSupplier", "Help"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newSupplier = QtWidgets.QMainWindow()
    ui = Ui_newCustomer()
    ui.setupUi(newSupplier)
    newSupplier.show()
    sys.exit(app.exec_())
