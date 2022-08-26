# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editItem.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from datetime import date


class Ui_editItem(object):
    def setupUi(self, editItem,first,sel):
        
        editItem.setObjectName("editItem")
        editItem.resize(461, 303)
        self.centralwidget = QtWidgets.QWidget(editItem)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 421, 241))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 234))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setHorizontalSpacing(35)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.idInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.idInput.setPlaceholderText("")
        self.idInput.setObjectName("idInput")
        self.idInput.setEnabled(False)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idInput)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        #self.label.setStyleSheet("color: rgb(243, 0, 0);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nameInput.setObjectName("nameInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameInput)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.descInput = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.descInput.setObjectName("descInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.descInput)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.purcahsePriceInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.purcahsePriceInput.setObjectName("purcahsePriceInput")
        self.purcahsePriceInput.setValidator(QtGui.QDoubleValidator(0.0,100.0,3))
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.purcahsePriceInput)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.salePriceInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.salePriceInput.setObjectName("salePriceInput")
        self.salePriceInput.setValidator(QtGui.QDoubleValidator(0.0,100.0,3))
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.salePriceInput)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.expiryDateTimeEdit = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.expiryDateTimeEdit.setObjectName("expiryDateTimeEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.expiryDateTimeEdit)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(290, 260, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.clicked.connect(lambda:editItem.close())
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setGeometry(QtCore.QRect(370, 260, 75, 23))
        self.helpButton.setObjectName("helpButton")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(lambda:okFunc(self))
        
        
        editItem.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(editItem)
        QtCore.QMetaObject.connectSlotsByName(editItem)
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
                myId=self.idInput.text()
                myId=int(myId)
                sql="UPDATE items SET name=%s, description=%s, purchasePrice=%s, saleprice=%s, expirydate=%s WHERE id=%s"
                val=(self.nameInput.text(),self.descInput.toPlainText(),float(self.purcahsePriceInput.text()),float(self.salePriceInput.text()),self.expiryDateTimeEdit.date().toPyDate(),myId,)
                mycursor.execute(sql,val)
                mydb.commit()
                first.loadData(sel)
                editItem.close()
                
    def loadData(self):
        myId=self.idInput
        val=(int(myId.text()),)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        sql="SELECT * FROM items WHERE id = %s"
        
        mycursor.execute(sql,val)
        result=mycursor.fetchall()
        listItem=[]
        for x in result:
            for y in x:
                listItem.append(y)
        self.nameInput.setText(listItem[1])
        self.descInput.setPlainText(listItem[2])
        self.purcahsePriceInput.setText(str(listItem[3]))
        self.salePriceInput.setText(str(listItem[4]))
        self.expiryDateTimeEdit.setDate(listItem[5])
    def retranslateUi(self, editItem):
        _translate = QtCore.QCoreApplication.translate
        editItem.setWindowTitle(_translate("editItem", "Edit Item"))
        self.label_5.setText(_translate("editItem", "Id:"))
        self.idInput.setToolTip(_translate("editItem", "<html><head/><body><p>ID Autogenerated</p></body></html>"))
        self.label.setText(_translate("editItem", "Name:"))
        self.nameInput.setPlaceholderText(_translate("editItem", "Item Name"))
        self.label_2.setText(_translate("editItem", "Description:"))
        self.descInput.setPlaceholderText(_translate("editItem", "[Enter Full Description Here]"))
        self.label_3.setText(_translate("editItem", "Purchase Price:"))
        self.purcahsePriceInput.setPlaceholderText(_translate("editItem", "eg. RS 200"))
        self.label_4.setText(_translate("editItem", "Sale Price:"))
        self.salePriceInput.setPlaceholderText(_translate("editItem", "eg. RS 250"))
        self.label_6.setText(_translate("editItem", "Expiry Date:"))
        self.expiryDateTimeEdit.setToolTip(_translate("editItem", "<html><head/><body><p>For notification if stock still available 1 month prior to expiry</p></body></html>"))
        self.cancelButton.setText(_translate("editItem", "Cancel"))
        self.helpButton.setText(_translate("editItem", "Help"))
        self.okButton.setText(_translate("editItem", "Ok"))




if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    editItem = QtWidgets.QMainWindow()
    ui = Ui_editItem()
    ui.setupUi(editItem)
    editItem.show()
    sys.exit(app.exec_())
