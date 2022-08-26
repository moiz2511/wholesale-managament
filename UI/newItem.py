# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newItem.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from datetime import date
import math





    
class Ui_newItem(object):
    
    def setupUi(self, newItem,firstWindow,sel):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE if not exists items (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), purchasePrice FLOAT,saleprice FLOAT,expirydate DATE )")
        mycursor.execute("SELECT * from items")
        for x in mycursor:
            print(x)
        mycursor.execute("SELECT id FROM items")
        idToAssign=0
        result=mycursor
        for x in result:
            idToAssign= x[0]+1
        
        newItem.setObjectName("newItem")
        newItem.resize(461, 303)
        self.centralwidget = QtWidgets.QWidget(newItem)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 421, 241))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 421, 215))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setHorizontalSpacing(35)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.nameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nameInput.setObjectName("nameInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameInput)
        self.purcahsePriceInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.purcahsePriceInput.setObjectName("purcahsePriceInput")
        self.purcahsePriceInput.setValidator(QtGui.QDoubleValidator(0.0,100.0,3))
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.purcahsePriceInput)
        self.salePriceInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.salePriceInput.setObjectName("salePriceInput")
        self.salePriceInput.setValidator(QtGui.QDoubleValidator(0.0,100.0,3))
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.salePriceInput)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.idInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.idInput.setPlaceholderText("")
        self.idInput.setObjectName("idInput")
        self.idInput.setText(str(idToAssign))
        self.idInput.setEnabled(False)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idInput)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.descInput = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.descInput.setObjectName("descInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.descInput)
        self.expiryDateTimeEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.expiryDateTimeEdit.setObjectName("expiryDateTimeEdit")
        self.expiryDateTimeEdit.setMinimumDate(date.today())
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.expiryDateTimeEdit)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(290, 260, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.clicked.connect(lambda:newItem.close())
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setGeometry(QtCore.QRect(370, 260, 75, 23))
        self.helpButton.setObjectName("helpButton")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(lambda:okFunc(self))
        newItem.setCentralWidget(self.centralwidget)
        
        
                                
                
        self.retranslateUi(newItem)
        QtCore.QMetaObject.connectSlotsByName(newItem)
        def okFunc(self):
            print('ok')
            print(self.expiryDateTimeEdit.date().toPyDate())
            print(self.nameInput.text())
            if(self.nameInput.text()==''):
                self.label.setStyleSheet('color: rgb(243, 0, 0);')
            else:
                
                sql="INSERT INTO items (name,description,purchasePrice,saleprice,expirydate) VALUES(%s,%s,%s,%s,%s)"
                val=(self.nameInput.text(),self.descInput.toPlainText(),float(self.purcahsePriceInput.text()),float(self.salePriceInput.text()),self.expiryDateTimeEdit.date().toPyDate())
                mycursor.execute(sql,val)
                mydb.commit()

                print(mycursor.rowcount, "record inserted.")
                print(mycursor.lastrowid)
                firstWindow.loadData(sel)
                newItem.close()

    def retranslateUi(self, newItem):
        _translate = QtCore.QCoreApplication.translate
        newItem.setWindowTitle(_translate("newItem", "Add New Item"))
        self.label.setText(_translate("newItem", "Name:"))
        self.label_2.setText(_translate("newItem", "Description:"))
        self.label_3.setText(_translate("newItem", "Purchase Price:"))
        self.label_4.setText(_translate("newItem", "Sale Price:"))
        self.nameInput.setPlaceholderText(_translate("newItem", "Item Name"))
        self.purcahsePriceInput.setPlaceholderText(_translate("newItem", "eg. RS 200"))
        self.salePriceInput.setPlaceholderText(_translate("newItem", "eg. RS 250"))
        self.label_5.setText(_translate("newItem", "Id:"))
        self.idInput.setToolTip(_translate("newItem", "<html><head/><body><p>ID Autogenerated</p></body></html>"))
        self.label_6.setText(_translate("newItem", "Expiry Date:"))
        self.descInput.setPlaceholderText(_translate("newItem", "[Enter Full Description Here]"))
        self.expiryDateTimeEdit.setToolTip(_translate("newItem", "<html><head/><body><p>For notification if stock still available 1 month prior to expiry</p></body></html>"))
        self.cancelButton.setText(_translate("newItem", "Cancel"))
        self.helpButton.setText(_translate("newItem", "Help"))
        self.okButton.setText(_translate("newItem", "Ok"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newItem = QtWidgets.QMainWindow()
    ui = Ui_newItem()
    ui.setupUi(newItem)
    newItem.show()
    sys.exit(app.exec_())
