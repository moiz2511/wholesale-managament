# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewItem.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from newItem import  Ui_newItem
import mysql.connector
from editItem import Ui_editItem

import re

class Ui_viewItemWindow(object):
    
    def setupUi(self, viewItemWindow):
        self.found=[]
        viewItemWindow.setObjectName("viewItemWindow")
        viewItemWindow.resize(799, 600)
        self.centralwidget = QtWidgets.QWidget(viewItemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.frame.setStyleSheet("background-color: rgb(209, 202, 214);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(200, 10, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(165, 159, 159);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.findFunc())
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 801, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        
        viewItemWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(viewItemWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        self.menuItem = QtWidgets.QMenu(self.menubar)
        self.menuItem.setObjectName("menuItem")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        viewItemWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(viewItemWindow)
        self.toolBar.setObjectName("toolBar")
        viewItemWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAdd = QtWidgets.QAction(viewItemWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/plus-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd.setIcon(icon)
        self.actionAdd.setObjectName("actionAdd")
        self.actionAdd.triggered.connect(lambda:self.newItemFunc())
        self.actionDelete = QtWidgets.QAction(viewItemWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/cross-octagon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon1)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete.triggered.connect(lambda:self.deleteFuncTool())
        self.actionDelete.setEnabled(False)
        self.actionEdit = QtWidgets.QAction(viewItemWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon2)
        self.actionEdit.setObjectName("actionEdit")
        self.actionEdit.triggered.connect(lambda:self.editItemFuc())
        self.actionEdit.setEnabled(False)
        self.actionPrint = QtWidgets.QAction(viewItemWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon3)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint.setEnabled(False)
        self.actionAdd_new_Item = QtWidgets.QAction(viewItemWindow)
        self.actionAdd_new_Item.setObjectName("actionAdd_new_Item")
        self.actionDelete_this_Item = QtWidgets.QAction(viewItemWindow)
        self.actionDelete_this_Item.setObjectName("actionDelete_this_Item")
        self.actionDelete_this_Item.setEnabled(False)
        self.actionEdit_this_Item = QtWidgets.QAction(viewItemWindow)
        self.actionEdit_this_Item.setObjectName("actionEdit_this_Item")
        self.actionEdit_this_Item.setEnabled(False)
        self.actionFind_Item = QtWidgets.QAction(viewItemWindow)
        self.actionFind_Item.setObjectName("actionFind_Item")
        self.actionFind_Next_Item = QtWidgets.QAction(viewItemWindow)
        self.actionFind_Next_Item.setObjectName("actionFind_Next_Item")
        self.actionFind_Next_Item.triggered.connect(lambda:self.findNextFunc())
        self.actionFind_Next_Item.setEnabled(False)
        self.actionReport = QtWidgets.QAction(viewItemWindow)
        self.actionReport.setObjectName("actionReport")
        self.actionImport_Items_From_CSV = QtWidgets.QAction(viewItemWindow)
        self.actionImport_Items_From_CSV.setObjectName("actionImport_Items_From_CSV")
        self.actionClose = QtWidgets.QAction(viewItemWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionHelp_Contents = QtWidgets.QAction(viewItemWindow)
        self.actionHelp_Contents.setObjectName("actionHelp_Contents")
        self.actionContact_Software_Developer = QtWidgets.QAction(viewItemWindow)
        self.actionContact_Software_Developer.setObjectName("actionContact_Software_Developer")
        self.menuItem.addAction(self.actionAdd_new_Item)
        self.menuItem.addAction(self.actionDelete_this_Item)
        self.menuItem.addAction(self.actionEdit_this_Item)
        self.menuItem.addSeparator()
        self.menuItem.addAction(self.actionFind_Item)
        self.menuItem.addAction(self.actionFind_Next_Item)
        self.menuItem.addSeparator()
        self.menuItem.addAction(self.actionReport)
        self.menuItem.addAction(self.actionImport_Items_From_CSV)
        self.menuItem.addSeparator()
        self.menuItem.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionHelp_Contents)
        self.menuHelp.addAction(self.actionContact_Software_Developer)
        self.menubar.addAction(self.menuItem.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionAdd)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionEdit)
        self.toolBar.addAction(self.actionPrint)
        self.tableWidget.itemSelectionChanged.connect(self.print_row)
        

        self.retranslateUi(viewItemWindow)
        self.loadData()
        QtCore.QMetaObject.connectSlotsByName(viewItemWindow)
    
    def print_row(self):
        items = self.tableWidget.selectedItems()
        if(items):
            self.actionEdit.setEnabled(True)
            self.actionEdit_this_Item.setEnabled(True)
            self.actionDelete_this_Item.setEnabled(True)
            self.actionDelete.setEnabled(True)
            
        else:
            self.actionEdit.setEnabled(False)
            self.actionEdit_this_Item.setEnabled(False)
            self.actionDelete_this_Item.setEnabled(False)
            self.actionDelete.setEnabled(False)
    def newItemFunc(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_newItem()
        self.ui.setupUi(self.window,Ui_viewItemWindow,self)
        self.window.show()
    def editItemFuc(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_editItem()
        self.ui.setupUi(self.window,Ui_viewItemWindow,self)
        selectedId=self.tableWidget.item(self.tableWidget.currentRow(),0)
        self.ui.idInput.setText(selectedId.text())
        self.ui.loadData()
        self.window.show()
        
   
    def loadData(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE if not exists items (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), purchasePrice FLOAT,saleprice FLOAT,expirydate DATE )")
        
        mycursor.execute("SELECT * from items")
        row=0
        lenOfRow=0
        result=[]
        for x in mycursor:
            lenOfRow=lenOfRow+1
            result.append(x)
        self.tableWidget.setRowCount(lenOfRow)
        print('before')
        
        for x in result:
            print('between')
            print(x)
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(x[0])))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(x[1]))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(x[2]))
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(x[4])))
            self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(str(x[3])))
            
            row=row+1
        print('after')
        product=[{"Item":"fair and lovely","Description":"Cream","Selling Price":"450","Purchase Price":"250","Quantity":"56","last Sold":"21/21/21"},{"Item":"fair and lovely22","Description":"Cream","Selling Price":"450","Purchase Price":"250","Quantity":"56","last Sold":"21/21/21"}]
        #row=0
        #self.tableWidget.setRowCount(len(product))
        #for x in product:
            #self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(x["Item"]))
            #self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(x["Description"]))
            #row=row+1
        
    def deleteFuncTool(self):
        print(self.tableWidget.currentRow())
        selectedId=self.tableWidget.item(self.tableWidget.currentRow(),0)
        print(selectedId.text())
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        sql="DELETE FROM items WHERE id = %s"
        val=(int(selectedId.text()),)
        mycursor.execute(sql,val)
        mydb.commit()
        self.loadData()
    def findFunc(self):
        myText=self.lineEdit.text()
        self.found=self.tableWidget.findItems(myText,Qt.MatchContains)
        if self.found:
            founds=self.found[0]
            self.tableWidget.setCurrentItem(founds)
            self.found.pop(0)
            self.setEnaFunc()
    def findNextFunc(self):
        if self.found:
            self.tableWidget.setCurrentItem(self.found[0])
            self.found.pop(0)
            self.setEnaFunc()
    def setEnaFunc(self):
        if self.found:
            self.actionFind_Next_Item.setEnabled(True)
        else:
            self.actionFind_Next_Item.setEnabled(False)
        
    def retranslateUi(self, viewItemWindow):
        _translate = QtCore.QCoreApplication.translate
        viewItemWindow.setWindowTitle(_translate("viewItemWindow", "Items"))
        self.label.setText(_translate("viewItemWindow", "Find Item:"))
        self.pushButton.setText(_translate("viewItemWindow", "Find"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("viewItemWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("viewItemWindow", "Item"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("viewItemWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("viewItemWindow", "Selling Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("viewItemWindow", "Purchase Price"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("viewItemWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("viewItemWindow", "Last Sold"))
        
        
        self.menuItem.setTitle(_translate("viewItemWindow", "Item"))
        self.menuHelp.setTitle(_translate("viewItemWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("viewItemWindow", "toolBar"))
        self.actionAdd.setText(_translate("viewItemWindow", "Add"))
        self.actionAdd.setToolTip(_translate("viewItemWindow", "Add a new Item"))
        self.actionDelete.setText(_translate("viewItemWindow", "Delete"))
        self.actionDelete.setToolTip(_translate("viewItemWindow", "Delete a Item"))
        self.actionEdit.setText(_translate("viewItemWindow", "Edit"))
        self.actionEdit.setToolTip(_translate("viewItemWindow", "Edit an Item"))
        self.actionPrint.setText(_translate("viewItemWindow", "Print"))
        self.actionPrint.setToolTip(_translate("viewItemWindow", "Print Report"))
        self.actionAdd_new_Item.setText(_translate("viewItemWindow", "Add new Item"))
        self.actionDelete_this_Item.setText(_translate("viewItemWindow", "Delete this Item"))
        self.actionEdit_this_Item.setText(_translate("viewItemWindow", "Edit this Item"))
        self.actionFind_Item.setText(_translate("viewItemWindow", "Find Item"))
        self.actionFind_Next_Item.setText(_translate("viewItemWindow", "Find Next Item"))
        self.actionReport.setText(_translate("viewItemWindow", "Report"))
        self.actionImport_Items_From_CSV.setText(_translate("viewItemWindow", "Import Items from CSV"))
        self.actionClose.setText(_translate("viewItemWindow", "Close"))
        self.actionHelp_Contents.setText(_translate("viewItemWindow", "Help Contents"))
        self.actionContact_Software_Developer.setText(_translate("viewItemWindow", "Contact Software Developer"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewItemWindow = QtWidgets.QMainWindow()
    ui = Ui_viewItemWindow()
    ui.setupUi(viewItemWindow)
    viewItemWindow.show()
    sys.exit(app.exec_())
