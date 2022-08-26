# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewInvoicesAll.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_allInvoicesView(object):
    def setupUi(self, allInvoicesView):
        allInvoicesView.setObjectName("allInvoicesView")
        allInvoicesView.setEnabled(True)
        allInvoicesView.resize(800, 527)
        self.centralwidget = QtWidgets.QWidget(allInvoicesView)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.frame.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 20))
        self.label.setObjectName("label")
        self.periodComboBox = QtWidgets.QComboBox(self.frame)
        self.periodComboBox.setGeometry(QtCore.QRect(60, 10, 101, 22))
        self.periodComboBox.setObjectName("periodComboBox")
        self.periodComboBox.addItem("")
        self.periodComboBox.addItem("")
        self.periodComboBox.addItem("")
        self.periodComboBox.addItem("")
        self.periodComboBox.addItem("")
        self.periodComboBox.addItem("")
        self.periodComboBox.addItem("")
        self.periodComboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 47, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(390, 10, 47, 20))
        self.label_3.setObjectName("label_3")
        self.startDateEdit = QtWidgets.QDateEdit(self.frame)
        self.startDateEdit.setGeometry(QtCore.QRect(240, 10, 110, 22))
        self.startDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.startDateEdit.setObjectName("startDateEdit")
        self.endDateEdit_2 = QtWidgets.QDateEdit(self.frame)
        self.endDateEdit_2.setGeometry(QtCore.QRect(430, 10, 110, 22))
        self.endDateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 31), QtCore.QTime(0, 0, 0)))
        self.endDateEdit_2.setObjectName("endDateEdit_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(590, 10, 31, 20))
        self.label_7.setObjectName("label_7")
        self.findInput = QtWidgets.QLineEdit(self.frame)
        self.findInput.setGeometry(QtCore.QRect(630, 10, 113, 20))
        self.findInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.findInput.setObjectName("findInput")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 40, 801, 421))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        allInvoicesView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(allInvoicesView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuInvoices = QtWidgets.QMenu(self.menubar)
        self.menuInvoices.setObjectName("menuInvoices")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        allInvoicesView.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(allInvoicesView)
        self.toolBar.setStyleSheet("QToolButton { padding-right: 20px; }\n"
"")
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        allInvoicesView.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Invoice = QtWidgets.QAction(allInvoicesView)
        self.actionNew_Invoice.setObjectName("actionNew_Invoice")
        self.actionCopy_Invoice = QtWidgets.QAction(allInvoicesView)
        self.actionCopy_Invoice.setObjectName("actionCopy_Invoice")
        self.actionDelete_Invoice = QtWidgets.QAction(allInvoicesView)
        self.actionDelete_Invoice.setObjectName("actionDelete_Invoice")
        self.actionFind = QtWidgets.QAction(allInvoicesView)
        self.actionFind.setObjectName("actionFind")
        self.actionFind_Next_f3 = QtWidgets.QAction(allInvoicesView)
        self.actionFind_Next_f3.setObjectName("actionFind_Next_f3")
        self.actionPrint_Invoice = QtWidgets.QAction(allInvoicesView)
        self.actionPrint_Invoice.setObjectName("actionPrint_Invoice")
        self.actionPrint_Preview = QtWidgets.QAction(allInvoicesView)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.actionCloose = QtWidgets.QAction(allInvoicesView)
        self.actionCloose.setObjectName("actionCloose")
        self.actionHelp_Contents = QtWidgets.QAction(allInvoicesView)
        self.actionHelp_Contents.setObjectName("actionHelp_Contents")
        self.actionContact_Developer = QtWidgets.QAction(allInvoicesView)
        self.actionContact_Developer.setObjectName("actionContact_Developer")
        self.actionNewInvoiceTool = QtWidgets.QAction(allInvoicesView)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/plus-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewInvoiceTool.setIcon(icon)
        self.actionNewInvoiceTool.setObjectName("actionNewInvoiceTool")
        self.actionCopytool = QtWidgets.QAction(allInvoicesView)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/document-copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopytool.setIcon(icon1)
        self.actionCopytool.setObjectName("actionCopytool")
        self.actionDeleteTool = QtWidgets.QAction(allInvoicesView)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteTool.setIcon(icon2)
        self.actionDeleteTool.setObjectName("actionDeleteTool")
        self.actionEditTool = QtWidgets.QAction(allInvoicesView)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditTool.setIcon(icon3)
        self.actionEditTool.setObjectName("actionEditTool")
        self.actionPreviewTool = QtWidgets.QAction(allInvoicesView)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/document-search-result.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreviewTool.setIcon(icon4)
        self.actionPreviewTool.setObjectName("actionPreviewTool")
        self.actionPrintTool = QtWidgets.QAction(allInvoicesView)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/printer-empty.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrintTool.setIcon(icon5)
        self.actionPrintTool.setObjectName("actionPrintTool")
        self.actionEmailTool = QtWidgets.QAction(allInvoicesView)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/mail-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEmailTool.setIcon(icon6)
        self.actionEmailTool.setObjectName("actionEmailTool")
        self.actionSave = QtWidgets.QAction(allInvoicesView)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/document-pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon7)
        self.actionSave.setObjectName("actionSave")
        self.actionPayment = QtWidgets.QAction(allInvoicesView)
        self.actionPayment.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPayment.setIcon(icon8)
        self.actionPayment.setObjectName("actionPayment")
        self.actionReturn = QtWidgets.QAction(allInvoicesView)
        self.actionReturn.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/document-invoice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReturn.setIcon(icon9)
        self.actionReturn.setObjectName("actionReturn")
        self.menuInvoices.addAction(self.actionNew_Invoice)
        self.menuInvoices.addAction(self.actionCopy_Invoice)
        self.menuInvoices.addAction(self.actionDelete_Invoice)
        self.menuInvoices.addSeparator()
        self.menuInvoices.addAction(self.actionFind)
        self.menuInvoices.addAction(self.actionFind_Next_f3)
        self.menuInvoices.addSeparator()
        self.menuInvoices.addAction(self.actionPrint_Invoice)
        self.menuInvoices.addAction(self.actionPrint_Preview)
        self.menuInvoices.addSeparator()
        self.menuInvoices.addAction(self.actionCloose)
        self.menuHelp.addAction(self.actionHelp_Contents)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionContact_Developer)
        self.menubar.addAction(self.menuInvoices.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNewInvoiceTool)
        self.toolBar.addAction(self.actionCopytool)
        self.toolBar.addAction(self.actionDeleteTool)
        self.toolBar.addAction(self.actionEditTool)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreviewTool)
        self.toolBar.addAction(self.actionPrintTool)
        self.toolBar.addAction(self.actionEmailTool)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPayment)
        self.toolBar.addAction(self.actionReturn)

        self.retranslateUi(allInvoicesView)
        QtCore.QMetaObject.connectSlotsByName(allInvoicesView)

    def retranslateUi(self, allInvoicesView):
        _translate = QtCore.QCoreApplication.translate
        allInvoicesView.setWindowTitle(_translate("allInvoicesView", "Invoices"))
        self.label.setText(_translate("allInvoicesView", "Period:"))
        self.periodComboBox.setItemText(0, _translate("allInvoicesView", "All"))
        self.periodComboBox.setItemText(1, _translate("allInvoicesView", "Custom"))
        self.periodComboBox.setItemText(2, _translate("allInvoicesView", "Today"))
        self.periodComboBox.setItemText(3, _translate("allInvoicesView", "Yesterday"))
        self.periodComboBox.setItemText(4, _translate("allInvoicesView", "This Week"))
        self.periodComboBox.setItemText(5, _translate("allInvoicesView", "Last Week"))
        self.periodComboBox.setItemText(6, _translate("allInvoicesView", "This Month"))
        self.periodComboBox.setItemText(7, _translate("allInvoicesView", "Last Month"))
        self.label_2.setText(_translate("allInvoicesView", "Start:"))
        self.label_3.setText(_translate("allInvoicesView", "End:"))
        self.label_7.setText(_translate("allInvoicesView", "Find:"))
        self.findInput.setToolTip(_translate("allInvoicesView", "Search by Invoice Number OR Customer Name OR Saleperson"))
        self.treeWidget.headerItem().setText(0, _translate("allInvoicesView", "Date"))
        self.treeWidget.headerItem().setText(1, _translate("allInvoicesView", "Invoice"))
        self.treeWidget.headerItem().setText(2, _translate("allInvoicesView", "Order"))
        self.treeWidget.headerItem().setText(3, _translate("allInvoicesView", "Customer"))
        self.treeWidget.headerItem().setText(4, _translate("allInvoicesView", "Saleperson"))
        self.treeWidget.headerItem().setText(5, _translate("allInvoicesView", "Amount"))
        self.treeWidget.headerItem().setText(6, _translate("allInvoicesView", "Due"))
        self.treeWidget.headerItem().setText(7, _translate("allInvoicesView", "Status"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("allInvoicesView", "1/31/2021"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("allInvoicesView", "10009"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("allInvoicesView", "0001"))
        self.treeWidget.topLevelItem(0).setText(3, _translate("allInvoicesView", "ali"))
        self.treeWidget.topLevelItem(0).setText(4, _translate("allInvoicesView", "hamza"))
        self.treeWidget.topLevelItem(0).setText(5, _translate("allInvoicesView", "Rs 1000"))
        self.treeWidget.topLevelItem(0).setText(6, _translate("allInvoicesView", "Rs 100"))
        self.treeWidget.topLevelItem(0).setText(7, _translate("allInvoicesView", "Partially Paid"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menuInvoices.setTitle(_translate("allInvoicesView", "Invoices"))
        self.menuHelp.setTitle(_translate("allInvoicesView", "Help"))
        self.toolBar.setWindowTitle(_translate("allInvoicesView", "toolBar"))
        self.actionNew_Invoice.setText(_translate("allInvoicesView", "New Invoice"))
        self.actionCopy_Invoice.setText(_translate("allInvoicesView", "Copy Invoice"))
        self.actionDelete_Invoice.setText(_translate("allInvoicesView", "Delete Invoice"))
        self.actionFind.setText(_translate("allInvoicesView", "Find                Ctrl+F"))
        self.actionFind_Next_f3.setText(_translate("allInvoicesView", "Find Next           F3"))
        self.actionPrint_Invoice.setText(_translate("allInvoicesView", "Print Invoice"))
        self.actionPrint_Preview.setText(_translate("allInvoicesView", "Print Preview"))
        self.actionCloose.setText(_translate("allInvoicesView", "Close"))
        self.actionHelp_Contents.setText(_translate("allInvoicesView", "Help Contents"))
        self.actionContact_Developer.setText(_translate("allInvoicesView", "Contact Developer"))
        self.actionNewInvoiceTool.setText(_translate("allInvoicesView", "New"))
        self.actionNewInvoiceTool.setToolTip(_translate("allInvoicesView", "New Invoice"))
        self.actionCopytool.setText(_translate("allInvoicesView", "Copy"))
        self.actionCopytool.setToolTip(_translate("allInvoicesView", "Copy Selected Invoice for New Invoice"))
        self.actionDeleteTool.setText(_translate("allInvoicesView", "Delete"))
        self.actionDeleteTool.setToolTip(_translate("allInvoicesView", "Delete Selected Invoice"))
        self.actionEditTool.setText(_translate("allInvoicesView", "Edit"))
        self.actionEditTool.setToolTip(_translate("allInvoicesView", "Edit Selected Invoice"))
        self.actionPreviewTool.setText(_translate("allInvoicesView", "Preview"))
        self.actionPreviewTool.setToolTip(_translate("allInvoicesView", "Preview Selected Invoice"))
        self.actionPrintTool.setText(_translate("allInvoicesView", "Print"))
        self.actionPrintTool.setToolTip(_translate("allInvoicesView", "Print Selected Invoice"))
        self.actionPrintTool.setShortcut(_translate("allInvoicesView", "Ctrl+P"))
        self.actionEmailTool.setText(_translate("allInvoicesView", "Email"))
        self.actionEmailTool.setToolTip(_translate("allInvoicesView", "Email Selected Invoice"))
        self.actionSave.setText(_translate("allInvoicesView", "Save"))
        self.actionSave.setToolTip(_translate("allInvoicesView", "Save Selected Invoice as PDF"))
        self.actionPayment.setText(_translate("allInvoicesView", "Payment"))
        self.actionPayment.setToolTip(_translate("allInvoicesView", "Apply a Payment for Selected Invoice"))
        self.actionReturn.setText(_translate("allInvoicesView", "Return"))
        self.actionReturn.setToolTip(_translate("allInvoicesView", "Return for Seleced Invoice"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    allInvoicesView = QtWidgets.QMainWindow()
    ui = Ui_allInvoicesView()
    ui.setupUi(allInvoicesView)
    allInvoicesView.show()
    sys.exit(app.exec_())
