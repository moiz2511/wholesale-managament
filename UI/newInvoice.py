# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newInvoice.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from allClients  import Ui_viewAllClients
from discountWidow import Ui_discountWindow
import mysql.connector
from datetime import date
import re

class Ui_newInvoiceWindow(object):
    def setupUi(self, newInvoiceWindow):
        self.totalDisco=0.0
        self.discoPer='0%'
        self.cusId=0
        self.rowNum=1
        self.result=[]
        self.totalAmountOfAll=0.0
        self.total1=0.0
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE if not exists allinvoices (id INT AUTO_INCREMENT PRIMARY KEY, custId INT, name VARCHAR(255), address VARCHAR(255), contact VARCHAR(255),date Date, terms VARCHAR(255), noOfDays INT ,saleman VARCHAR(255), comments VARCHAR(255),private VARCHAR(255),total VARCHAR(255),status VARCHAR(255),saveAs VARCHAR(255),dtotal VARCHAR(255),dpercen VARCHAR(255) )")
        mycursor.execute('CREATE TABLE if not exists invoiceitem(id INT AUTO_INCREMENT PRIMARY KEY,invoiceId INT,itemId INT,qty INT,des VARCHAR(255),unitPrice FLOAT,discount VARCHAR(255),total FLOAT )')
        mycursor.execute("SELECT id FROM allinvoices")
        result=mycursor.fetchall()
        idToAssign=1
        if result:
            for x in result:
                idToAssign=x[0]+1
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
        
        for x in mycursor:
            lenOfRow=lenOfRow+1
            self.result.append(x)
        newInvoiceWindow.setObjectName("newInvoiceWindow")
        newInvoiceWindow.resize(785, 594)
        newInvoiceWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(newInvoiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 431, 181))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 31, 22))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 140, 42, 22))
        self.label_8.setObjectName("label_8")
        self.nameInput = QtWidgets.QLineEdit(self.frame)
        self.nameInput.setGeometry(QtCore.QRect(80, 10, 251, 20))
        self.nameInput.setObjectName("nameInput")
        self.billToInput = QtWidgets.QTextEdit(self.frame)
        self.billToInput.setGeometry(QtCore.QRect(80, 40, 331, 71))
        self.billToInput.setObjectName("billToInput")
        self.contactInput = QtWidgets.QLineEdit(self.frame)
        self.contactInput.setGeometry(QtCore.QRect(80, 140, 331, 20))
        self.contactInput.setObjectName("contactInput")
        self.showAllToolBtn = QtWidgets.QToolButton(self.frame)
        self.showAllToolBtn.setGeometry(QtCore.QRect(340, 10, 26, 25))
        self.showAllToolBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons8-customer-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showAllToolBtn.setIcon(icon)
        self.showAllToolBtn.setAutoRaise(True)
        self.showAllToolBtn.setObjectName("showAllToolBtn")
        self.showAllToolBtn.clicked.connect(lambda:self.showAllCustFunc())
        self.editToolBtn = QtWidgets.QToolButton(self.frame)
        self.editToolBtn.setEnabled(False)
        self.editToolBtn.setGeometry(QtCore.QRect(380, 11, 25, 20))
        self.editToolBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editToolBtn.setIcon(icon1)
        self.editToolBtn.setAutoRaise(True)
        self.editToolBtn.setObjectName("editToolBtn")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(470, 30, 291, 181))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.label_13.setObjectName("label_13")
        self.createFromInvoiceComboBOx = QtWidgets.QComboBox(self.frame_2)
        self.createFromInvoiceComboBOx.setGeometry(QtCore.QRect(100, 10, 141, 20))
        self.createFromInvoiceComboBOx.setObjectName("createFromInvoiceComboBOx")
        self.createFromInvoiceComboBOx.addItem("")
        self.createFromInvoiceComboBOx.addItem("")
        self.createFromInvoiceComboBOx.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit.setGeometry(QtCore.QRect(100, 40, 171, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName("dateEdit")
        self.tremsComboBox = QtWidgets.QComboBox(self.frame_2)
        self.tremsComboBox.setGeometry(QtCore.QRect(100, 70, 121, 22))
        self.tremsComboBox.setObjectName("tremsComboBox")
        self.tremsComboBox.addItem("")
        self.tremsComboBox.addItem("")
        self.tremsComboBox.currentIndexChanged.connect(lambda:self.selChanged())
        
        self.SalepersonComboBox = QtWidgets.QComboBox(self.frame_2)
        self.SalepersonComboBox.setGeometry(QtCore.QRect(100, 100, 171, 22))
        self.SalepersonComboBox.setObjectName("SalepersonComboBox")
        self.invoiceNumberInput = QtWidgets.QLineEdit(self.frame_2)
        self.invoiceNumberInput.setEnabled(False)
        self.invoiceNumberInput.setGeometry(QtCore.QRect(100, 130, 171, 20))
        self.invoiceNumberInput.setObjectName("invoiceNumberInput")
        self.invoiceNumberInput.setText(str(idToAssign))
        self.invoiceToolBtn = QtWidgets.QToolButton(self.frame_2)
        self.invoiceToolBtn.setGeometry(QtCore.QRect(250, 10, 25, 19))
        self.invoiceToolBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/receipt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.invoiceToolBtn.setIcon(icon2)
        self.invoiceToolBtn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.invoiceToolBtn.setAutoRaise(True)
        self.invoiceToolBtn.setObjectName("invoiceToolBtn")
        self.noOfDays = QtWidgets.QSpinBox(self.frame_2)
        self.noOfDays.setEnabled(False)
        self.noOfDays.setGeometry(QtCore.QRect(230, 70, 42, 22))
        self.noOfDays.setMaximum(365)
        self.noOfDays.setProperty("value", 30)
        self.noOfDays.setObjectName("noOfDays")
        
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 240, 751, 181))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.loadTable()
        
        self.addItemBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addItemBtn.setGeometry(QtCore.QRect(40, 430, 91, 23))
        self.addItemBtn.setObjectName("addItemBtn")
        self.addItemBtn.clicked.connect(lambda:self.addItemFunc())
        self.removeItemBtn = QtWidgets.QPushButton(self.centralwidget)
        self.removeItemBtn.setGeometry(QtCore.QRect(140, 430, 91, 23))
        self.removeItemBtn.setObjectName("removeItemBtn")
        self.removeItemBtn.clicked.connect(lambda:self.removeRowFunc())
        self.subTotalLabel = QtWidgets.QLabel(self.centralwidget)
        self.subTotalLabel.setGeometry(QtCore.QRect(480, 450, 47, 13))
        self.subTotalLabel.setObjectName("subTotalLabel")
        self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalLabel.setGeometry(QtCore.QRect(480, 470, 41, 20))
        self.totalLabel.setObjectName("totalLabel")
        self.subtotalShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.subtotalShowLabel.setGeometry(QtCore.QRect(680, 450, 101, 16))
        self.subtotalShowLabel.setObjectName("subtotalShowLabel")
        self.totalShowLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.totalShowLabel_2.setGeometry(QtCore.QRect(670, 470, 101, 16))
        self.totalShowLabel_2.setObjectName("totalShowLabel_2")
        self.commentsEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.commentsEdit.setGeometry(QtCore.QRect(20, 490, 191, 41))
        self.commentsEdit.setObjectName("commentsEdit")
        self.privateCommentsEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.privateCommentsEdit.setGeometry(QtCore.QRect(230, 490, 191, 41))
        self.privateCommentsEdit.setObjectName("privateCommentsEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 470, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 470, 101, 16))
        self.label_2.setObjectName("label_2")
        self.addDiscountBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addDiscountBtn.setGeometry(QtCore.QRect(240, 430, 91, 23))
        self.addDiscountBtn.setObjectName("addDiscountBtn")
        self.addDiscountBtn.clicked.connect(lambda:self.addDiscountFunc())
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 540, 741, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 47, 13))
        self.label_5.setObjectName("label_5")
        self.recordBtn = QtWidgets.QPushButton(self.centralwidget)
        self.recordBtn.setGeometry(QtCore.QRect(510, 560, 75, 23))
        self.recordBtn.setObjectName("recordBtn")
        self.recordBtn.clicked.connect(lambda:saveDataToDb(self))
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(600, 560, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.cancelBtn.clicked.connect(lambda:newInvoiceWindow.close())
        self.helpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.helpBtn.setGeometry(QtCore.QRect(690, 560, 75, 23))
        self.helpBtn.setObjectName("helpBtn")
        self.helpBtn.clicked.connect(lambda:self.test())
        
        newInvoiceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(newInvoiceWindow)
        QtCore.QMetaObject.connectSlotsByName(newInvoiceWindow)
        def saveDataToDb(self):
            print('save')
            if(self.nameInput.text() and self.rowNum>1):
                print('m')
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="mysql1122",
                database="accountingsoftware"
                )
                mycursor = mydb.cursor()
                sql='INSERT INTO allinvoices (custId,name,address,contact,date,terms,noOfDays,comments,private,total,status,saveAs,dtotal,dpercen) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                nam=''
                bil=''
                con=''
                noDays=-1
                stat='unpaid'
                savAs='record'
                if(self.noOfDays.isEnabled()):
                    noDays=self.noOfDays.value()
                if(self.nameInput.text()):
                    nam=self.nameInput.text()
                if(self.billToInput.toPlainText()):
                    bil=self.billToInput.toPlainText()
                if(self.contactInput.text()):
                    con=self.contactInput.text()
                val=(self.cusId,nam,bil,con,self.dateEdit.date().toPyDate(),self.tremsComboBox.currentText(),noDays,self.commentsEdit.toPlainText(),self.privateCommentsEdit.toPlainText(),self.totalShowLabel_2.text(),stat,savAs,str(self.totalDisco),self.discoPer)
                mycursor.execute(sql,val)
                mydb.commit()
                saveDetailItems(self)
            elif(self.rowNum==1):
                self.label_5.setStyleSheet('color:red')
            else:
                self.label_3.setStyleSheet('color:red')
        def saveDetailItems(self):
        
            for x in range(0,self.rowNum-1):
                print(self.tableWidget.cellWidget(x,0).value())
                print(self.tableWidget.cellWidget(x,1).currentText())
                print(self.tableWidget.item(x,2).text())
                print(self.tableWidget.item(x,3).text())
                print(self.tableWidget.item(x,4).text())
                print(self.tableWidget.item(x,5).text())
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="mysql1122",
                database="accountingsoftware"
                )
                mycursor = mydb.cursor()
                print(self.invoiceNumberInput.text)
                print(type(self.invoiceNumberInput.text))
                print(self.result[self.tableWidget.cellWidget(x,1).currentIndex()][0])
                print(type(self.result[self.tableWidget.cellWidget(x,1).currentIndex()][0]))
                
                                
                sql='INSERT INTO invoiceitem(invoiceId,itemId,qty,des,unitPrice,discount,total) VALUES(%s,%s,%s,%s,%s,%s,%s)'
                val=(int(self.invoiceNumberInput.text()),self.result[self.tableWidget.cellWidget(x,1).currentIndex()][0],self.tableWidget.cellWidget(x,0).value(),self.tableWidget.item(x,2).text(),float(self.tableWidget.item(x,3).text()),self.tableWidget.item(x,4).text(),float(self.tableWidget.item(x,5).text()))
                mycursor.execute(sql,val)
                mydb.commit()
                newInvoiceWindow.close()

    def test(self):
        myIndex=self.tableWidget.currentRow()
        #print(self.tableWidget.cellWidget(myIndex,1).currentText())
        print(self.totalAmountOfAll)
        print(self.tremsComboBox.currentText())
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql1122",
            database="accountingsoftware"
            )
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * from invoiceitem')
        for x in mycursor:
            print(x)
        print(self.cusId)
        
    def addDiscountFunc(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_discountWindow()
        self.ui.setupUi(self.window,Ui_newInvoiceWindow,self)
        self.window.show()
    def applyDiscount(self,disAmount,num):
        self.tableWidget.setRowCount(self.rowNum)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(self.rowNum, item)
        
        item = QtWidgets.QTableWidgetItem()
        item.setText('Discount')
        self.tableWidget.setItem(self.rowNum-1,1,item)
        item = QtWidgets.QTableWidgetItem()
        if(num==1):
            item = QtWidgets.QTableWidgetItem()
            item.setText(disAmount+'%')
            self.discoPer=disAmount+'%'
            self.tableWidget.setItem(self.rowNum-1,4,item)
            mul=float(disAmount)/100
            print(mul)
            print('check for')
            thisTotal=0.0
            for x in range(0,self.rowNum-1):
                thisTotal=float(self.tableWidget.item(x,5).text())+thisTotal
            # myDisc=self.totalAmountOfAll*mul
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(thisTotal*mul))
                self.totalDisco=thisTotal*mul
                self.tableWidget.setItem(self.rowNum-1,5,item)
                
                self.totalShowLabel_2.setText(str(thisTotal-thisTotal*mul))
            
        
        
    def loadTable(self):
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 751, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
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
        # item = QtWidgets.QTableWidgetItem()
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item.setForeground(brush)
        # self.tableWidget.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 5, item)
        # item = QtWidgets.QTableWidgetItem()
        # icon3 = QtGui.QIcon()
        # icon3.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/bin-metal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # item.setIcon(icon3)
        # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        # self.tableWidget.setItem(0, 6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 5, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        # self.tableWidget.setItem(1, 6, item)
    def addItemFunc(self):
        #self.totalAmountOfAll=self.totalAmountOfAll+self.total1
        self.tableWidget.setRowCount(self.rowNum)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(self.rowNum, item)
        self.recordBtn.setEnabled(False)
        #item = self.tableWidget.verticalHeaderItem(0)
        tableItem = QtWidgets.QLineEdit()
        #tableItem.setText( "Testing" )
        comList=[]
        
        
        
        
        
        #self.tableWidget.setRowCount(lenOfRow)
        
        
        for x in self.result:
            comList.append(x[1])
            print(x)
        #comList=['test1','test2','test3']
            
        
        self.myCombo=QtWidgets.QComboBox()
        self.myCombo.addItems(comList)
        self.myCombo.setEditable(False)
        #self.myCombo.setLineEdit(tableItem)
        self.myCombo.setInsertPolicy(0)
        self.myCombo.currentIndexChanged.connect(lambda:self.loadDataInToTable())
        self.tableWidget.setCellWidget(self.rowNum-1, 1, self.myCombo )
        mySpin=QtWidgets.QSpinBox()
        mySpin.setMinimum(1)
        mySpin.setMaximum(10000)
        mySpin.valueChanged.connect(lambda:self.itemPriceFunc())
        self.tableWidget.cellChanged.connect(lambda:self.valida())
        self.tableWidget.cellChanged.connect(lambda:self.itemPriceFunc())
        self.tableWidget.setCellWidget(self.rowNum-1, 0, mySpin )
        print('add')
        print(self.rowNum)
        
        self.rowNum=self.rowNum+1
    def valida(self):
        
        myIndex=self.tableWidget.currentRow()
        if(self.tableWidget.item(myIndex,3)):
            myPric=self.tableWidget.item(myIndex,3).text()
            if(myPric.isnumeric() or re.match(r'^-?\d+(?:\.\d+)$', myPric)):
                pass
            else:
                item = QtWidgets.QTableWidgetItem()
                item.setText('0')
                self.tableWidget.setItem(myIndex,3,item)
        if(self.tableWidget.item(myIndex,4)):
            myDisc=self.tableWidget.item(myIndex,4).text()
            myTotal='0'
            if(self.tableWidget.item(myIndex,5)):
                myTotal=self.tableWidget.item(myIndex,5).text()
            if(myDisc=='0' or myTotal=='0'):
                return
            myLen=len(myDisc)
            sub=myDisc[0:myLen-1]
            if('%'in myDisc):
                if(sub.isnumeric()):
                    print('yes')
                else:
                    item = QtWidgets.QTableWidgetItem()
                    item.setText('0')
                    self.tableWidget.setItem(myIndex,4,item)
            else:
                if(myDisc.isnumeric()):
                    print('second yes')
                else:
                    item = QtWidgets.QTableWidgetItem()
                    item.setText('0')
                    self.tableWidget.setItem(myIndex,4,item)
            #if(myDisc[myLen-1]=='%'):
                
        
            
    def loadDataInToTable(self):
        
        myIndex=self.tableWidget.currentRow()
        item = QtWidgets.QTableWidgetItem()
        myCur=self.tableWidget.cellWidget(myIndex,1).currentIndex()
        print('now')
        print(myCur)
        print(type(myCur))
        item.setText(self.result[myCur][2])
        self.tableWidget.setItem(myIndex,2,item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(str(self.result[myCur][4]))
        self.tableWidget.setItem(myIndex,3,item)
        item = QtWidgets.QTableWidgetItem()
        item.setText('0%')
        self.tableWidget.setItem(myIndex,4,item)
        self.recordBtn.setEnabled(True)
    def itemPriceFunc(self):

        myIndex=self.tableWidget.currentRow()
        myDisc=0
        myPric=0
        myQty=self.tableWidget.cellWidget(myIndex,0).text()
        
        if(self.tableWidget.item(myIndex,4)):
            myDisc=self.tableWidget.item(myIndex,4).text()
        if(self.tableWidget.item(myIndex,3).text()):
            myPric=self.tableWidget.item(myIndex,3).text()
      
        total=int(myQty)*float(myPric)
        if('%'in myDisc):
            myLen=len(myDisc)
            sub=myDisc[0:myLen-1]
            mul=float(sub)/100
            print(type(total))
            print(total)
            print(type(mul))
            print(type(myPric))
            print(type(myDisc))
            total=total-(total*mul)
            print(total)
            self.total1=total
            
        else:
            total=float(total)-float(myDisc)
            print(total)
            self.total1=total
        
        item = QtWidgets.QTableWidgetItem()
        item.setText(str(total))
        thisTotal=0.0
        for x in range(0,self.rowNum-1):
            if(self.tableWidget.item(x,5)):
                thisTotal=float(self.tableWidget.item(x,5).text())+thisTotal
                self.totalShowLabel_2.setText(str(thisTotal))
                self.subtotalShowLabel.setText(str(thisTotal))
        if(self.tableWidget.item(myIndex,5)):
            if(self.tableWidget.item(myIndex,5).text()==str(total)):
                return
            else:
                self.tableWidget.setItem(myIndex,5,item)
                self.totalAmountOfAll=self.totalAmountOfAll+self.total1
        else:
            self.tableWidget.setItem(myIndex,5,item)
            self.totalAmountOfAll=self.totalAmountOfAll+self.total1
      
    def removeRowFunc(self):
        self.tableWidget.removeRow(self.rowNum-2)
        self.rowNum=self.rowNum-1
        print('romove')
        print(self.rowNum)           
            
    def selChanged(self):
        if(self.tremsComboBox.currentText()=='Pay in Days'):
            self.noOfDays.setEnabled(True)
        else:
            self.noOfDays.setEnabled(False)
            
    def showAllCustFunc(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_viewAllClients()
        self.ui.setupUi(self.window,Ui_newInvoiceWindow,self)
        self.window.show()
    def loadDataa(self,myId,mySelf):
        print(myId)
        mySelf.cusId=myId
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        print('m')
        sql="SELECT * FROM clients WHERE id = %s"
        val=(myId,)
        mycursor.execute(sql,val)
        a=()
        for x in mycursor:
            a=x
        
        mySelf.nameInput.setText(a[1])
        mySelf.billToInput.setText(a[3])
        mySelf.contactInput.setText(a[4])

            
    
    def retranslateUi(self, newInvoiceWindow):
        _translate = QtCore.QCoreApplication.translate
        newInvoiceWindow.setWindowTitle(_translate("newInvoiceWindow", "New Invoice"))
        self.label_6.setText(_translate("newInvoiceWindow", "Name:"))
        self.label_7.setText(_translate("newInvoiceWindow", "Bill To:"))
        self.label_8.setText(_translate("newInvoiceWindow", "Contact:"))
        self.showAllToolBtn.setToolTip(_translate("newInvoiceWindow", "Open Customer Record"))
        self.editToolBtn.setToolTip(_translate("newInvoiceWindow", "Edit Customer Record"))
        self.label_9.setText(_translate("newInvoiceWindow", "Create From:"))
        self.label_10.setText(_translate("newInvoiceWindow", "Date:"))
        self.label_11.setText(_translate("newInvoiceWindow", "Terms:"))
        self.label_12.setText(_translate("newInvoiceWindow", "Saleperson:"))
        self.label_13.setText(_translate("newInvoiceWindow", "Invoice Number:"))
        self.createFromInvoiceComboBOx.setItemText(0, _translate("newInvoiceWindow", "[New Invoice]"))
        self.createFromInvoiceComboBOx.setItemText(1, _translate("newInvoiceWindow", "Existing Invoice"))
        self.createFromInvoiceComboBOx.setItemText(2, _translate("newInvoiceWindow", "Draft Invoice"))
        self.tremsComboBox.setItemText(0, _translate("newInvoiceWindow", "COD"))
        self.tremsComboBox.setItemText(1, _translate("newInvoiceWindow", "Pay in Days"))
        self.invoiceToolBtn.setToolTip(_translate("newInvoiceWindow", "Old Invoices"))
        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("newInvoiceWindow", "1"))
        # item = self.tableWidget.verticalHeaderItem(1)
        # item.setText(_translate("newInvoiceWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("newInvoiceWindow", "Qty"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("newInvoiceWindow", "Item"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("newInvoiceWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("newInvoiceWindow", "Unit Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("newInvoiceWindow", "Discount"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("newInvoiceWindow", "Total"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        # item = self.tableWidget.item(0, 0)
        # item.setText(_translate("newInvoiceWindow", "12"))
        
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.addItemBtn.setText(_translate("newInvoiceWindow", "Add Item"))
        self.removeItemBtn.setText(_translate("newInvoiceWindow", "Remove Item"))
        self.subTotalLabel.setText(_translate("newInvoiceWindow", "Subtotal:"))
        self.totalLabel.setText(_translate("newInvoiceWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Total:</span></p></body></html>"))
        self.subtotalShowLabel.setText(_translate("newInvoiceWindow", ""))
        self.totalShowLabel_2.setText(_translate("newInvoiceWindow", "<html><head/><body><p><span style=\" font-weight:600;\"></span></p></body></html>"))
        self.commentsEdit.setToolTip(_translate("newInvoiceWindow", "These notes are printed on the bottom of the invoice"))
        self.commentsEdit.setPlaceholderText(_translate("newInvoiceWindow", "[Enter Invoice Notes]"))
        self.privateCommentsEdit.setToolTip(_translate("newInvoiceWindow", "These are internal notes not printed on the invoice"))
        self.privateCommentsEdit.setPlaceholderText(_translate("newInvoiceWindow", "[Enter internal Notes]"))
        self.label.setText(_translate("newInvoiceWindow", "Comments"))
        self.label_2.setText(_translate("newInvoiceWindow", "Private Comments"))
        self.addDiscountBtn.setText(_translate("newInvoiceWindow", "Add Discount..."))
        self.label_3.setText(_translate("newInvoiceWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Billing</span></p></body></html>"))
        self.label_4.setText(_translate("newInvoiceWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Invoice</span></p><p><br/></p></body></html>"))
        self.label_5.setText(_translate("newInvoiceWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Sale</span></p></body></html>"))
        self.recordBtn.setText(_translate("newInvoiceWindow", "Record"))
        self.cancelBtn.setText(_translate("newInvoiceWindow", "Cancel"))
        self.helpBtn.setText(_translate("newInvoiceWindow", "Help"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newInvoiceWindow = QtWidgets.QMainWindow()
    ui = Ui_newInvoiceWindow()
    ui.setupUi(newInvoiceWindow)
    newInvoiceWindow.show()
    sys.exit(app.exec_())
