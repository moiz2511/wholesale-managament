# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editSupplier.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_editClient(object):
    def setupUi(self, editSupplier,first,firstSelf):
        editSupplier.setObjectName("editSupplier")
        editSupplier.resize(559, 370)
        self.centralwidget = QtWidgets.QWidget(editSupplier)
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
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(300, 320, 75, 23))
        self.saveBtn.setObjectName("saveBtn")
        self.saveBtn.clicked.connect(lambda:okFunc(self))
        self.cancelInput = QtWidgets.QPushButton(self.centralwidget)
        self.cancelInput.setGeometry(QtCore.QRect(380, 320, 75, 23))
        self.cancelInput.setObjectName("cancelInput")
        self.cancelInput.clicked.connect(lambda:editSupplier.close())
        self.helpInput = QtWidgets.QPushButton(self.centralwidget)
        self.helpInput.setGeometry(QtCore.QRect(460, 320, 75, 23))
        self.helpInput.setObjectName("helpInput")
        editSupplier.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(editSupplier)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 21))
        self.menubar.setObjectName("menubar")
        editSupplier.setMenuBar(self.menubar)

        self.retranslateUi(editSupplier)
        QtCore.QMetaObject.connectSlotsByName(editSupplier)
        def okFunc(self):
            if(self.nameInput.text()==''):
                self.label.setStyleSheet("color: rgb(243, 0, 0);")
            else:
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="mysql1122",
                database="accountingsoftware"
                )
                mycursor = mydb.cursor()
                
                sql="UPDATE clients SET name=%s, contactperson=%s, address=%s, phone=%s, contact=%s,email=%s WHERE id=%s"
                val=(self.nameInput.text(),self.contactPersonInput.text(),self.addressInput.toPlainText(),self.phoneInput.text(),self.altPhoneInput.text(),self.emailInput.text(),int(self.lineEdit.text()),)
                mycursor.execute(sql,val)
                mydb.commit()
                first.loadData(firstSelf)
                editSupplier.close()
        
    def loadData(self):
        myId=self.lineEdit
        val=(int(myId.text()),)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        sql="SELECT * FROM clients WHERE id = %s"
        
        mycursor.execute(sql,val)
        result=mycursor.fetchall()
        listItem=[]
        for x in result:
            for y in x:
                listItem.append(y)
        print(listItem)
        self.nameInput.setText(listItem[1])
        self.contactPersonInput.setText(listItem[2])
        self.addressInput.setText(listItem[3])
        self.phoneInput.setText(listItem[4])
        self.altPhoneInput.setText(listItem[5])
        self.emailInput.setText(listItem[6])

    def retranslateUi(self, editSupplier):
        _translate = QtCore.QCoreApplication.translate
        editSupplier.setWindowTitle(_translate("editSupplier", "Edit Client"))
        self.label.setText(_translate("editSupplier", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Client:</span></p></body></html>"))
        self.label_2.setText(_translate("editSupplier", "Name"))
        self.label_4.setText(_translate("editSupplier", "Contact Person"))
        self.label_3.setText(_translate("editSupplier", "Address"))
        self.label_5.setText(_translate("editSupplier", "Phone Number"))
        self.label_6.setText(_translate("editSupplier", "Alternative Contact"))
        self.label_7.setText(_translate("editSupplier", "Email"))
        self.contactPersonInput.setPlaceholderText(_translate("editSupplier", "eg. Ali Saab"))
        self.nameInput.setPlaceholderText(_translate("editSupplier", "eg. Ali Brothers"))
        self.phoneInput.setPlaceholderText(_translate("editSupplier", "eg. 03123456789"))
        self.altPhoneInput.setPlaceholderText(_translate("editSupplier", "eg. 042345678"))
        self.emailInput.setPlaceholderText(_translate("editSupplier", "eg. ali@gmail.com"))
        self.addressInput.setPlaceholderText(_translate("editSupplier", "[Enter Full Address Here]"))
        self.label_8.setText(_translate("editSupplier", "ID"))
        self.lineEdit.setToolTip(_translate("editSupplier", "ID auto Generated"))
        self.saveBtn.setText(_translate("editSupplier", "Save"))
        self.cancelInput.setText(_translate("editSupplier", "Cancel"))
        self.helpInput.setText(_translate("editSupplier", "Help"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editSupplier = QtWidgets.QMainWindow()
    ui = Ui_editSupplier()
    ui.setupUi(editSupplier)
    editSupplier.show()
    sys.exit(app.exec_())
