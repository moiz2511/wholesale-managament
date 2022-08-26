# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allSuppliers.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from newClient import Ui_newCustomer
import mysql.connector
from PyQt5.QtCore import Qt
from editClient import Ui_editClient

class Ui_viewClients(object):
    def setupUi(self, viewSuppliers):
        self.found=[]
        self.vari=0
        viewSuppliers.setObjectName("viewSuppliers")
        viewSuppliers.resize(800, 600)
        viewSuppliers.setProperty("marginLeft", 12)
        self.centralwidget = QtWidgets.QWidget(viewSuppliers)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 801, 41))
        self.frame.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.findInput = QtWidgets.QLineEdit(self.frame)
        self.findInput.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.findInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.findInput.setObjectName("findInput")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(190, 10, 51, 20))
        self.pushButton.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.findFunc())
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(250, 10, 71, 20))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.pushButton_2.clicked.connect(lambda:self.findNextFunc())
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(370, 10, 131, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(lambda:self.selChanged())
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 40, 801, 491))
        self.treeWidget.setObjectName("treeWidget")
        #item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        #item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        
        viewSuppliers.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(viewSuppliers)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuCustomer = QtWidgets.QMenu(self.menubar)
        self.menuCustomer.setObjectName("menuCustomer")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        viewSuppliers.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(viewSuppliers)
        self.toolBar.setStyleSheet("QToolButton { padding-right: 20px; }")
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setProperty("margin", 24)
        self.toolBar.setObjectName("toolBar")
        viewSuppliers.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAdd_new_Customer = QtWidgets.QAction(viewSuppliers)
        self.actionAdd_new_Customer.setObjectName("actionAdd_new_Customer")
        self.actionDelete_Customer = QtWidgets.QAction(viewSuppliers)
        self.actionDelete_Customer.setObjectName("actionDelete_Customer")
        self.actionEdit_Customer_Details = QtWidgets.QAction(viewSuppliers)
        self.actionEdit_Customer_Details.setObjectName("actionEdit_Customer_Details")
        self.actionEmail_Customer = QtWidgets.QAction(viewSuppliers)
        self.actionEmail_Customer.setObjectName("actionEmail_Customer")
        self.actionTelephone_Customer = QtWidgets.QAction(viewSuppliers)
        self.actionTelephone_Customer.setObjectName("actionTelephone_Customer")
        self.actionClose = QtWidgets.QAction(viewSuppliers)
        self.actionClose.setObjectName("actionClose")
        self.actionPrint = QtWidgets.QAction(viewSuppliers)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint_Preview = QtWidgets.QAction(viewSuppliers)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.actionSend_to_email = QtWidgets.QAction(viewSuppliers)
        self.actionSend_to_email.setObjectName("actionSend_to_email")
        self.actionSave_as_PDF = QtWidgets.QAction(viewSuppliers)
        self.actionSave_as_PDF.setObjectName("actionSave_as_PDF")
        self.actionSave_as_CSV = QtWidgets.QAction(viewSuppliers)
        self.actionSave_as_CSV.setObjectName("actionSave_as_CSV")
        self.actionHelp_Contents = QtWidgets.QAction(viewSuppliers)
        self.actionHelp_Contents.setObjectName("actionHelp_Contents")
        self.actionAccounting_Software_Home_Page = QtWidgets.QAction(viewSuppliers)
        self.actionAccounting_Software_Home_Page.setObjectName("actionAccounting_Software_Home_Page")
        self.actiontoolBarAddNewCustomer = QtWidgets.QAction(viewSuppliers)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/plus-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiontoolBarAddNewCustomer.setIcon(icon)
        self.actiontoolBarAddNewCustomer.setObjectName("actiontoolBarAddNewCustomer")
        self.actiontoolBarAddNewCustomer.triggered.connect(lambda:self.newCustomerFunc())
        self.actionDeleteToolBar = QtWidgets.QAction(viewSuppliers)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteToolBar.setIcon(icon1)
        self.actionDeleteToolBar.setObjectName("actionDeleteToolBar")
        self.actionDeleteToolBar.triggered.connect(lambda:self.deleteFunc())
        self.actionEditToolBar = QtWidgets.QAction(viewSuppliers)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditToolBar.setIcon(icon2)
        self.actionEditToolBar.setObjectName("actionEditToolBar")
        self.actionEditToolBar.triggered.connect(lambda:self.editFunc())
        self.actionInvoice = QtWidgets.QAction(viewSuppliers)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/receipt--plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvoice.setIcon(icon3)
        self.actionInvoice.setObjectName("actionInvoice")
        self.actionPayment = QtWidgets.QAction(viewSuppliers)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/receipt-import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPayment.setIcon(icon4)
        self.actionPayment.setObjectName("actionPayment")
        self.actionStatement = QtWidgets.QAction(viewSuppliers)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStatement.setIcon(icon5)
        self.actionStatement.setObjectName("actionStatement")
        self.actionSave = QtWidgets.QAction(viewSuppliers)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/memory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        self.actionSave.setObjectName("actionSave")
        self.menuCustomer.addAction(self.actionAdd_new_Customer)
        self.menuCustomer.addAction(self.actionDelete_Customer)
        self.menuCustomer.addAction(self.actionEdit_Customer_Details)
        self.menuCustomer.addSeparator()
        self.menuCustomer.addAction(self.actionEmail_Customer)
        self.menuCustomer.addAction(self.actionTelephone_Customer)
        self.menuCustomer.addSeparator()
        self.menuCustomer.addAction(self.actionClose)
        self.menuReport.addAction(self.actionPrint)
        self.menuReport.addAction(self.actionPrint_Preview)
        self.menuReport.addAction(self.actionSend_to_email)
        self.menuReport.addAction(self.actionSave_as_PDF)
        self.menuReport.addAction(self.actionSave_as_CSV)
        self.menuHelp.addAction(self.actionHelp_Contents)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAccounting_Software_Home_Page)
        self.menubar.addAction(self.menuCustomer.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actiontoolBarAddNewCustomer)
        self.toolBar.addAction(self.actionDeleteToolBar)
        self.toolBar.addAction(self.actionEditToolBar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionInvoice)
        self.toolBar.addAction(self.actionPayment)
        self.toolBar.addAction(self.actionStatement)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.actionEditToolBar.setEnabled(False)
        self.actionEdit_Customer_Details.setEnabled(False)
        self.actionDeleteToolBar.setEnabled(False)
        self.actionDelete_Customer.setEnabled(False)
        self.loadData()
        self.treeWidget.itemSelectionChanged.connect(lambda:self.enaFunc())
        self.pushButton_2.setEnabled(False)

        self.retranslateUi(viewSuppliers)
        QtCore.QMetaObject.connectSlotsByName(viewSuppliers)
    def findFunc(self):
        myText=self.findInput.text()
        self.found=self.treeWidget.findItems(myText,Qt.MatchContains,1)
        if self.found:
            print(self.found[0].text(1))
            self.treeWidget.setCurrentItem(self.found[0])
            self.found.pop(0)
            self.setEnaFunc()
        
        
    def findNextFunc(self):
        if self.found:
            self.treeWidget.setCurrentItem(self.found[0])
            self.found.pop(0)
            self.setEnaFunc()
    def setEnaFunc(self):
        if self.found:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
    def deleteFunc(self):
        sel=self.treeWidget.selectedItems()
        for x in sel:
            myId=int(x.text(0))
            
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        print('m')
        sql="DELETE FROM clients WHERE id = %s"
        val=(myId,)
        mycursor.execute(sql,val)
        mydb.commit()
        self.loadData()
    def enaFunc(self):
        if self.treeWidget.selectedItems():
            self.actionEditToolBar.setEnabled(True)
            self.actionEdit_Customer_Details.setEnabled(True)
            self.actionDeleteToolBar.setEnabled(True)
            self.actionDelete_Customer.setEnabled(True)
        else:
            self.actionEditToolBar.setEnabled(False)
            self.actionEdit_Customer_Details.setEnabled(False)
            self.actionDeleteToolBar.setEnabled(False)
            self.actionDelete_Customer.setEnabled(False)
    def selChanged(self):
        print(self.comboBox.currentText())
    def editFunc(self):
        sel=self.treeWidget.selectedItems()
        for x in sel:
            myId=x.text(0)
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_editClient()
        self.ui.setupUi(self.window,Ui_viewClients,self)
        self.ui.lineEdit.setText(myId)
        self.ui.loadData()
        self.window.show()
        


    def newCustomerFunc(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_newCustomer()
        self.ui.setupUi(self.window,Ui_viewClients,self)
        self.window.show()
    def lastInserFunc(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE if not exists suppliers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), contactperson VARCHAR(255), address VARCHAR(255),phone VARCHAR(255),contact VARCHAR(255),email VARCHAR(255) )")
        mycursor.execute("SELECT * FROM suppliers")
        result=mycursor.fetchall()
        item_0=QtWidgets.QTreeWidgetItem(self.treeWidget)
        y=[]
        for x in result:
           y=x 
        
        self.treeWidget.topLevelItem(self.vari).setText(0,str(y[0]))
        self.treeWidget.topLevelItem(self.vari).setText(1,y[1])
        self.treeWidget.topLevelItem(self.vari).setText(2,"RS 15000")
        self.treeWidget.topLevelItem(self.vari).setText(3,"01-01-2021")
        self.treeWidget.topLevelItem(self.vari).setText(4,y[4])
        self.vari=self.vari+1
    def loadData(self):
        self.treeWidget.clear()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1122",
        database="accountingsoftware"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE if not exists suppliers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), contactperson VARCHAR(255), address VARCHAR(255),phone VARCHAR(255),contact VARCHAR(255),email VARCHAR(255) )")
        mycursor.execute("SELECT * FROM clients")
        result=mycursor.fetchall()
        i=0
        for x in result:
            
            item_0=QtWidgets.QTreeWidgetItem(self.treeWidget)
            
        
        for x in result:
            self.treeWidget.topLevelItem(i).setText(0,str(x[0]))
            self.treeWidget.topLevelItem(i).setText(1,x[1])
            self.treeWidget.topLevelItem(i).setText(2,"RS 15000")
            self.treeWidget.topLevelItem(i).setText(3,"01-01-2021")
            self.treeWidget.topLevelItem(i).setText(5,x[4])
            i=i+1
            self.vari=i
        #self.treeWidget.setSortingEnabled(True)
        #__sortingEnabled = self.treeWidget.isSortingEnabled()
        #self.treeWidget.setSortingEnabled(__sortingEnabled)
    def retranslateUi(self, viewSuppliers):
        _translate = QtCore.QCoreApplication.translate
        viewSuppliers.setWindowTitle(_translate("viewSuppliers", "All Clients"))
        self.findInput.setPlaceholderText(_translate("viewSuppliers", "Find a Client"))
        self.pushButton.setText(_translate("viewSuppliers", "Find"))
        self.pushButton_2.setText(_translate("viewSuppliers", "Find Next"))
        self.comboBox.setItemText(0, _translate("viewSuppliers", "All Customers"))
        self.comboBox.setItemText(1, _translate("viewSuppliers", "Pending Balances"))
        self.comboBox.setItemText(2, _translate("viewSuppliers", "Over Due Date"))
        self.treeWidget.headerItem().setText(0, _translate("viewSuppliers", "ID"))
        self.treeWidget.headerItem().setText(1, _translate("viewSuppliers", "Customers"))
        self.treeWidget.headerItem().setText(2, _translate("viewSuppliers", "Balance"))
        self.treeWidget.headerItem().setText(3, _translate("viewSuppliers", "Due Date"))
        self.treeWidget.headerItem().setText(4, _translate("viewSuppliers", "Last Invoice"))
        self.treeWidget.headerItem().setText(5, _translate("viewSuppliers", "Phone Number"))
        
        
        #self.treeWidget.topLevelItem(0).setText(0, _translate("viewSuppliers", "1"))
        #self.treeWidget.topLevelItem(0).setText(1, _translate("viewSuppliers", "Ali Traders"))
        #self.treeWidget.topLevelItem(0).setText(2, _translate("viewSuppliers", "RS 15000"))
        #self.treeWidget.topLevelItem(0).setText(3, _translate("viewSuppliers", "01-01-2021"))
        #self.treeWidget.topLevelItem(0).setText(4, _translate("viewSuppliers", "030078232932"))
        #self.treeWidget.topLevelItem(1).setText(0, _translate("viewSuppliers", "2"))
        #self.treeWidget.topLevelItem(1).setText(1, _translate("viewSuppliers", "Iqbal  Shop"))
        #self.treeWidget.topLevelItem(1).setText(2, _translate("viewSuppliers", "RS 1300"))
        #self.treeWidget.topLevelItem(1).setText(3, _translate("viewSuppliers", "01-01-2021"))
        #self.treeWidget.topLevelItem(1).setText(4, _translate("viewSuppliers", "030103011131"))
        
        self.menuCustomer.setTitle(_translate("viewSuppliers", "Supplier"))
        self.menuReport.setTitle(_translate("viewSuppliers", "Report"))
        self.menuHelp.setTitle(_translate("viewSuppliers", "Help"))
        self.toolBar.setWindowTitle(_translate("viewSuppliers", "toolBar"))
        self.actionAdd_new_Customer.setText(_translate("viewSuppliers", "New"))
        self.actionDelete_Customer.setText(_translate("viewSuppliers", "Delete "))
        self.actionEdit_Customer_Details.setText(_translate("viewSuppliers", "Edit"))
        self.actionEmail_Customer.setText(_translate("viewSuppliers", "Email"))
        self.actionTelephone_Customer.setText(_translate("viewSuppliers", "Call"))
        self.actionClose.setText(_translate("viewSuppliers", "Close"))
        self.actionPrint.setText(_translate("viewSuppliers", "Print"))
        self.actionPrint_Preview.setText(_translate("viewSuppliers", "Print Preview"))
        self.actionSend_to_email.setText(_translate("viewSuppliers", "Send to email"))
        self.actionSave_as_PDF.setText(_translate("viewSuppliers", "Save as PDF"))
        self.actionSave_as_CSV.setText(_translate("viewSuppliers", "Save as CSV"))
        self.actionHelp_Contents.setText(_translate("viewSuppliers", "Help Contents"))
        self.actionAccounting_Software_Home_Page.setText(_translate("viewSuppliers", "Accounting Software Home Page"))
        self.actiontoolBarAddNewCustomer.setText(_translate("viewSuppliers", "Add"))
        self.actiontoolBarAddNewCustomer.setToolTip(_translate("viewSuppliers", "Add New Customer"))
        self.actionDeleteToolBar.setText(_translate("viewSuppliers", "Delete"))
        self.actionDeleteToolBar.setToolTip(_translate("viewSuppliers", "Delete a Customer"))
        self.actionEditToolBar.setText(_translate("viewSuppliers", "Edit"))
        self.actionEditToolBar.setToolTip(_translate("viewSuppliers", "Edit existing Customer"))
        self.actionInvoice.setText(_translate("viewSuppliers", "Invoice"))
        self.actionInvoice.setToolTip(_translate("viewSuppliers", "New Invoice for Selected Customer"))
        self.actionPayment.setText(_translate("viewSuppliers", "Payment"))
        self.actionPayment.setToolTip(_translate("viewSuppliers", "Receive Payment for Selected Customer"))
        self.actionStatement.setText(_translate("viewSuppliers", "Statement"))
        self.actionStatement.setToolTip(_translate("viewSuppliers", "Statement of Selected Customer"))
        self.actionSave.setText(_translate("viewSuppliers", "Save"))
        self.actionSave.setToolTip(_translate("viewSuppliers", "Save the Record of all Customers"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewSuppliers = QtWidgets.QMainWindow()
    ui = Ui_viewClients()
    ui.setupUi(viewSuppliers)
    viewSuppliers.show()
    sys.exit(app.exec_())
