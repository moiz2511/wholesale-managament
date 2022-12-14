# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailPaymentOfPurchaseOrder.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_allPaymetsOfPurchaseOrders(object):
    def setupUi(self, allPaymetsOfPurchaseOrders):
        allPaymetsOfPurchaseOrders.setObjectName("allPaymetsOfPurchaseOrders")
        allPaymetsOfPurchaseOrders.resize(799, 505)
        allPaymetsOfPurchaseOrders.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(allPaymetsOfPurchaseOrders)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 21))
        self.label.setObjectName("label")
        self.periodCombo = QtWidgets.QComboBox(self.frame)
        self.periodCombo.setGeometry(QtCore.QRect(50, 10, 101, 22))
        self.periodCombo.setObjectName("periodCombo")
        self.periodCombo.addItem("")
        self.periodCombo.addItem("")
        self.periodCombo.addItem("")
        self.periodCombo.addItem("")
        self.periodCombo.addItem("")
        self.periodCombo.addItem("")
        self.periodCombo.addItem("")
        self.periodCombo.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 47, 21))
        self.label_2.setObjectName("label_2")
        self.startDateEdit = QtWidgets.QDateEdit(self.frame)
        self.startDateEdit.setEnabled(False)
        self.startDateEdit.setGeometry(QtCore.QRect(200, 10, 110, 22))
        self.startDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setObjectName("startDateEdit")
        self.supplierCombo = QtWidgets.QComboBox(self.frame)
        self.supplierCombo.setGeometry(QtCore.QRect(550, 10, 231, 22))
        self.supplierCombo.setObjectName("supplierCombo")
        self.supplierCombo.addItem("")
        self.supplierCombo.addItem("")
        self.supplierCombo.addItem("")
        self.supplierCombo.addItem("")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 40, 801, 401))
        self.treeWidget.setStyleSheet("border:0px;")
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 10, 21, 21))
        self.label_3.setObjectName("label_3")
        self.endDateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.endDateEdit_2.setEnabled(False)
        self.endDateEdit_2.setGeometry(QtCore.QRect(380, 10, 110, 22))
        self.endDateEdit_2.setObjectName("endDateEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 10, 47, 21))
        self.label_4.setObjectName("label_4")
        allPaymetsOfPurchaseOrders.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(allPaymetsOfPurchaseOrders)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        self.menuPayment = QtWidgets.QMenu(self.menubar)
        self.menuPayment.setObjectName("menuPayment")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        allPaymetsOfPurchaseOrders.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(allPaymetsOfPurchaseOrders)
        self.toolBar.setStyleSheet("background-color: rgb(251, 251, 251);")
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        allPaymetsOfPurchaseOrders.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        self.actionNew.setObjectName("actionNew")
        self.actionDelete = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        self.actionDelete.setObjectName("actionDelete")
        self.actionEdit = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        self.actionEdit.setObjectName("actionEdit")
        self.actionFind = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        self.actionFind.setObjectName("actionFind")
        self.actionFind_Next = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        self.actionFind_Next.setObjectName("actionFind_Next")
        self.actionClose = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        self.actionClose.setObjectName("actionClose")
        self.actionHelp_Contents = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        self.actionHelp_Contents.setObjectName("actionHelp_Contents")
        self.actionContact_Developers = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        self.actionContact_Developers.setObjectName("actionContact_Developers")
        self.actionNew_2 = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/plus-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_2.setIcon(icon)
        self.actionNew_2.setObjectName("actionNew_2")
        self.actionDelete_2 = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_2.setIcon(icon1)
        self.actionDelete_2.setObjectName("actionDelete_2")
        self.actionEdit_2 = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_2.setIcon(icon2)
        self.actionEdit_2.setObjectName("actionEdit_2")
        self.actionHelp = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/question-balloon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon3)
        self.actionHelp.setObjectName("actionHelp")
        self.actionPreview = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/document-search-result.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreview.setIcon(icon4)
        self.actionPreview.setObjectName("actionPreview")
        self.actionPrint = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon5)
        self.actionPrint.setObjectName("actionPrint")
        self.actionSave = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/document-pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        self.actionSave.setObjectName("actionSave")
        self.actionEmail = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/mail--arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEmail.setIcon(icon7)
        self.actionEmail.setObjectName("actionEmail")
        self.actionPayment = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/document-import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPayment.setIcon(icon8)
        self.actionPayment.setObjectName("actionPayment")
        self.actionPayment_2 = QtWidgets.QAction(allPaymetsOfPurchaseOrders)
        self.actionPayment_2.setObjectName("actionPayment_2")
        self.menuPayment.addAction(self.actionNew)
        self.menuPayment.addAction(self.actionDelete)
        self.menuPayment.addAction(self.actionEdit)
        self.menuPayment.addSeparator()
        self.menuPayment.addAction(self.actionPayment_2)
        self.menuPayment.addSeparator()
        self.menuPayment.addAction(self.actionFind_Next)
        self.menuPayment.addAction(self.actionFind)
        self.menuPayment.addSeparator()
        self.menuPayment.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionHelp_Contents)
        self.menuHelp.addAction(self.actionContact_Developers)
        self.menubar.addAction(self.menuPayment.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew_2)
        self.toolBar.addAction(self.actionDelete_2)
        self.toolBar.addAction(self.actionEdit_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPayment)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)

        self.retranslateUi(allPaymetsOfPurchaseOrders)
        QtCore.QMetaObject.connectSlotsByName(allPaymetsOfPurchaseOrders)

    def retranslateUi(self, allPaymetsOfPurchaseOrders):
        _translate = QtCore.QCoreApplication.translate
        allPaymetsOfPurchaseOrders.setWindowTitle(_translate("allPaymetsOfPurchaseOrders", "Payments Of Purchase Orders"))
        self.label.setText(_translate("allPaymetsOfPurchaseOrders", "Period:"))
        self.periodCombo.setItemText(0, _translate("allPaymetsOfPurchaseOrders", "All"))
        self.periodCombo.setItemText(1, _translate("allPaymetsOfPurchaseOrders", "Custom"))
        self.periodCombo.setItemText(2, _translate("allPaymetsOfPurchaseOrders", "Today"))
        self.periodCombo.setItemText(3, _translate("allPaymetsOfPurchaseOrders", "Yesterday"))
        self.periodCombo.setItemText(4, _translate("allPaymetsOfPurchaseOrders", "This Week"))
        self.periodCombo.setItemText(5, _translate("allPaymetsOfPurchaseOrders", "Last Week"))
        self.periodCombo.setItemText(6, _translate("allPaymetsOfPurchaseOrders", "This Month"))
        self.periodCombo.setItemText(7, _translate("allPaymetsOfPurchaseOrders", "Last Month"))
        self.label_2.setText(_translate("allPaymetsOfPurchaseOrders", "Start:"))
        self.supplierCombo.setItemText(0, _translate("allPaymetsOfPurchaseOrders", "All"))
        self.supplierCombo.setItemText(1, _translate("allPaymetsOfPurchaseOrders", "Ashfaq Chemicals"))
        self.supplierCombo.setItemText(2, _translate("allPaymetsOfPurchaseOrders", "Highlight Seed"))
        self.supplierCombo.setItemText(3, _translate("allPaymetsOfPurchaseOrders", "Highligh Seed Research Farm Arifwala Distt Pakpattan"))
        self.treeWidget.headerItem().setText(0, _translate("allPaymetsOfPurchaseOrders", "Date"))
        self.treeWidget.headerItem().setText(1, _translate("allPaymetsOfPurchaseOrders", "Due Date"))
        self.treeWidget.headerItem().setText(2, _translate("allPaymetsOfPurchaseOrders", "Payment IDs"))
        self.treeWidget.headerItem().setText(3, _translate("allPaymetsOfPurchaseOrders", "Purchase  Order ID"))
        self.treeWidget.headerItem().setText(4, _translate("allPaymetsOfPurchaseOrders", "Supplier"))
        self.treeWidget.headerItem().setText(5, _translate("allPaymetsOfPurchaseOrders", "Amount"))
        self.treeWidget.headerItem().setText(6, _translate("allPaymetsOfPurchaseOrders", "Due"))
        self.treeWidget.headerItem().setText(7, _translate("allPaymetsOfPurchaseOrders", "Status"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("allPaymetsOfPurchaseOrders", "2021-10-10"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("allPaymetsOfPurchaseOrders", "2022-1-1"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("allPaymetsOfPurchaseOrders", "3"))
        self.treeWidget.topLevelItem(0).setText(3, _translate("allPaymetsOfPurchaseOrders", "10009"))
        self.treeWidget.topLevelItem(0).setText(4, _translate("allPaymetsOfPurchaseOrders", "Highlight Seeds"))
        self.treeWidget.topLevelItem(0).setText(5, _translate("allPaymetsOfPurchaseOrders", "Rs 200,000"))
        self.treeWidget.topLevelItem(0).setText(7, _translate("allPaymetsOfPurchaseOrders", "Paid"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("allPaymetsOfPurchaseOrders", "2021-11-11"))
        self.treeWidget.topLevelItem(0).child(0).setText(2, _translate("allPaymetsOfPurchaseOrders", "5"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("allPaymetsOfPurchaseOrders", "End:"))
        self.label_4.setText(_translate("allPaymetsOfPurchaseOrders", "Supplier:"))
        self.menuPayment.setTitle(_translate("allPaymetsOfPurchaseOrders", "Payment"))
        self.menuHelp.setTitle(_translate("allPaymetsOfPurchaseOrders", "Help"))
        self.toolBar.setWindowTitle(_translate("allPaymetsOfPurchaseOrders", "toolBar"))
        self.actionNew.setText(_translate("allPaymetsOfPurchaseOrders", "New"))
        self.actionDelete.setText(_translate("allPaymetsOfPurchaseOrders", "Delete"))
        self.actionEdit.setText(_translate("allPaymetsOfPurchaseOrders", "Edit"))
        self.actionFind.setText(_translate("allPaymetsOfPurchaseOrders", "Find"))
        self.actionFind_Next.setText(_translate("allPaymetsOfPurchaseOrders", "Find Next"))
        self.actionClose.setText(_translate("allPaymetsOfPurchaseOrders", "Close"))
        self.actionHelp_Contents.setText(_translate("allPaymetsOfPurchaseOrders", "Help Contents"))
        self.actionContact_Developers.setText(_translate("allPaymetsOfPurchaseOrders", "Contact Developers"))
        self.actionNew_2.setText(_translate("allPaymetsOfPurchaseOrders", "New"))
        self.actionNew_2.setToolTip(_translate("allPaymetsOfPurchaseOrders", "New Payment"))
        self.actionDelete_2.setText(_translate("allPaymetsOfPurchaseOrders", "Delete"))
        self.actionDelete_2.setToolTip(_translate("allPaymetsOfPurchaseOrders", "Delete Selected Payment Record"))
        self.actionEdit_2.setText(_translate("allPaymetsOfPurchaseOrders", "Edit"))
        self.actionEdit_2.setToolTip(_translate("allPaymetsOfPurchaseOrders", "Edit Selected Payment"))
        self.actionHelp.setText(_translate("allPaymetsOfPurchaseOrders", "Help"))
        self.actionHelp.setToolTip(_translate("allPaymetsOfPurchaseOrders", "Hellp"))
        self.actionPreview.setText(_translate("allPaymetsOfPurchaseOrders", "Preview"))
        self.actionPreview.setToolTip(_translate("allPaymetsOfPurchaseOrders", "Preview"))
        self.actionPrint.setText(_translate("allPaymetsOfPurchaseOrders", "Print"))
        self.actionPrint.setToolTip(_translate("allPaymetsOfPurchaseOrders", "Print"))
        self.actionSave.setText(_translate("allPaymetsOfPurchaseOrders", "Save"))
        self.actionSave.setToolTip(_translate("allPaymetsOfPurchaseOrders", "Save as PDF"))
        self.actionEmail.setText(_translate("allPaymetsOfPurchaseOrders", "Email"))
        self.actionEmail.setToolTip(_translate("allPaymetsOfPurchaseOrders", "Email"))
        self.actionPayment.setText(_translate("allPaymetsOfPurchaseOrders", "Payment"))
        self.actionPayment.setToolTip(_translate("allPaymetsOfPurchaseOrders", "Payment regarding due"))
        self.actionPayment_2.setText(_translate("allPaymetsOfPurchaseOrders", "Payment"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    allPaymetsOfPurchaseOrders = QtWidgets.QMainWindow()
    ui = Ui_allPaymetsOfPurchaseOrders()
    ui.setupUi(allPaymetsOfPurchaseOrders)
    allPaymetsOfPurchaseOrders.show()
    sys.exit(app.exec_())
