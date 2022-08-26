# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allPurchaseOrderView.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_allPurchaseOrderView(object):
    def setupUi(self, allPurchaseOrderView):
        allPurchaseOrderView.setObjectName("allPurchaseOrderView")
        allPurchaseOrderView.setEnabled(True)
        allPurchaseOrderView.resize(800, 527)
        self.centralwidget = QtWidgets.QWidget(allPurchaseOrderView)
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
        self.label_7.setGeometry(QtCore.QRect(570, 10, 51, 20))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(640, 10, 111, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 40, 801, 421))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        allPurchaseOrderView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(allPurchaseOrderView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuInvoices = QtWidgets.QMenu(self.menubar)
        self.menuInvoices.setObjectName("menuInvoices")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        allPurchaseOrderView.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(allPurchaseOrderView)
        self.toolBar.setStyleSheet("QToolButton { padding-right: 20px; }\n"
"")
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        allPurchaseOrderView.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Invoice = QtWidgets.QAction(allPurchaseOrderView)
        self.actionNew_Invoice.setObjectName("actionNew_Invoice")
        self.actionCopy_Invoice = QtWidgets.QAction(allPurchaseOrderView)
        self.actionCopy_Invoice.setObjectName("actionCopy_Invoice")
        self.actionDelete_Invoice = QtWidgets.QAction(allPurchaseOrderView)
        self.actionDelete_Invoice.setObjectName("actionDelete_Invoice")
        self.actionFind = QtWidgets.QAction(allPurchaseOrderView)
        self.actionFind.setObjectName("actionFind")
        self.actionFind_Next_f3 = QtWidgets.QAction(allPurchaseOrderView)
        self.actionFind_Next_f3.setObjectName("actionFind_Next_f3")
        self.actionPrint_Invoice = QtWidgets.QAction(allPurchaseOrderView)
        self.actionPrint_Invoice.setObjectName("actionPrint_Invoice")
        self.actionPrint_Preview = QtWidgets.QAction(allPurchaseOrderView)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.actionCloose = QtWidgets.QAction(allPurchaseOrderView)
        self.actionCloose.setObjectName("actionCloose")
        self.actionHelp_Contents = QtWidgets.QAction(allPurchaseOrderView)
        self.actionHelp_Contents.setObjectName("actionHelp_Contents")
        self.actionContact_Developer = QtWidgets.QAction(allPurchaseOrderView)
        self.actionContact_Developer.setObjectName("actionContact_Developer")
        self.actionNewInvoiceTool = QtWidgets.QAction(allPurchaseOrderView)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/plus-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewInvoiceTool.setIcon(icon)
        self.actionNewInvoiceTool.setObjectName("actionNewInvoiceTool")
        self.actionDeleteTool = QtWidgets.QAction(allPurchaseOrderView)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteTool.setIcon(icon1)
        self.actionDeleteTool.setObjectName("actionDeleteTool")
        self.actionEditTool = QtWidgets.QAction(allPurchaseOrderView)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditTool.setIcon(icon2)
        self.actionEditTool.setObjectName("actionEditTool")
        self.actionPreviewTool = QtWidgets.QAction(allPurchaseOrderView)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/document-search-result.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreviewTool.setIcon(icon3)
        self.actionPreviewTool.setObjectName("actionPreviewTool")
        self.actionPrintTool = QtWidgets.QAction(allPurchaseOrderView)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/printer-empty.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrintTool.setIcon(icon4)
        self.actionPrintTool.setObjectName("actionPrintTool")
        self.actionEmailTool = QtWidgets.QAction(allPurchaseOrderView)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/mail-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEmailTool.setIcon(icon5)
        self.actionEmailTool.setObjectName("actionEmailTool")
        self.actionSave = QtWidgets.QAction(allPurchaseOrderView)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/document-pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        self.actionSave.setObjectName("actionSave")
        self.actionPayment = QtWidgets.QAction(allPurchaseOrderView)
        self.actionPayment.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPayment.setIcon(icon7)
        self.actionPayment.setObjectName("actionPayment")
        self.actionReturn = QtWidgets.QAction(allPurchaseOrderView)
        self.actionReturn.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/document-invoice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReturn.setIcon(icon8)
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

        self.retranslateUi(allPurchaseOrderView)
        QtCore.QMetaObject.connectSlotsByName(allPurchaseOrderView)

    def retranslateUi(self, allPurchaseOrderView):
        _translate = QtCore.QCoreApplication.translate
        allPurchaseOrderView.setWindowTitle(_translate("allPurchaseOrderView", "Purcahse Orders"))
        self.label.setText(_translate("allPurchaseOrderView", "Period:"))
        self.periodComboBox.setItemText(0, _translate("allPurchaseOrderView", "All"))
        self.periodComboBox.setItemText(1, _translate("allPurchaseOrderView", "Custom"))
        self.periodComboBox.setItemText(2, _translate("allPurchaseOrderView", "Today"))
        self.periodComboBox.setItemText(3, _translate("allPurchaseOrderView", "Yesterday"))
        self.periodComboBox.setItemText(4, _translate("allPurchaseOrderView", "This Week"))
        self.periodComboBox.setItemText(5, _translate("allPurchaseOrderView", "Last Week"))
        self.periodComboBox.setItemText(6, _translate("allPurchaseOrderView", "This Month"))
        self.periodComboBox.setItemText(7, _translate("allPurchaseOrderView", "Last Month"))
        self.label_2.setText(_translate("allPurchaseOrderView", "Start:"))
        self.label_3.setText(_translate("allPurchaseOrderView", "End:"))
        self.label_7.setText(_translate("allPurchaseOrderView", "Supplier:"))
        self.comboBox.setItemText(0, _translate("allPurchaseOrderView", "All"))
        self.comboBox.setItemText(1, _translate("allPurchaseOrderView", "Ashfaq Chemicals"))
        self.treeWidget.headerItem().setText(0, _translate("allPurchaseOrderView", "Date"))
        self.treeWidget.headerItem().setText(1, _translate("allPurchaseOrderView", "Order"))
        self.treeWidget.headerItem().setText(2, _translate("allPurchaseOrderView", "Supplier"))
        self.treeWidget.headerItem().setText(3, _translate("allPurchaseOrderView", "Amount"))
        self.treeWidget.headerItem().setText(4, _translate("allPurchaseOrderView", "Paid"))
        self.treeWidget.headerItem().setText(5, _translate("allPurchaseOrderView", "Due"))
        self.treeWidget.headerItem().setText(6, _translate("allPurchaseOrderView", "Status"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("allPurchaseOrderView", "1/31/2021"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("allPurchaseOrderView", "0001"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("allPurchaseOrderView", "Ashfaq Chemicals"))
        self.treeWidget.topLevelItem(0).setText(3, _translate("allPurchaseOrderView", "Rs 1400000"))
        self.treeWidget.topLevelItem(0).setText(4, _translate("allPurchaseOrderView", "1000000"))
        self.treeWidget.topLevelItem(0).setText(5, _translate("allPurchaseOrderView", "400000"))
        self.treeWidget.topLevelItem(0).setText(6, _translate("allPurchaseOrderView", "partially paid"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menuInvoices.setTitle(_translate("allPurchaseOrderView", "Invoices"))
        self.menuHelp.setTitle(_translate("allPurchaseOrderView", "Help"))
        self.toolBar.setWindowTitle(_translate("allPurchaseOrderView", "toolBar"))
        self.actionNew_Invoice.setText(_translate("allPurchaseOrderView", "New Invoice"))
        self.actionCopy_Invoice.setText(_translate("allPurchaseOrderView", "Copy Invoice"))
        self.actionDelete_Invoice.setText(_translate("allPurchaseOrderView", "Delete Invoice"))
        self.actionFind.setText(_translate("allPurchaseOrderView", "Find                Ctrl+F"))
        self.actionFind_Next_f3.setText(_translate("allPurchaseOrderView", "Find Next           F3"))
        self.actionPrint_Invoice.setText(_translate("allPurchaseOrderView", "Print Invoice"))
        self.actionPrint_Preview.setText(_translate("allPurchaseOrderView", "Print Preview"))
        self.actionCloose.setText(_translate("allPurchaseOrderView", "Close"))
        self.actionHelp_Contents.setText(_translate("allPurchaseOrderView", "Help Contents"))
        self.actionContact_Developer.setText(_translate("allPurchaseOrderView", "Contact Developer"))
        self.actionNewInvoiceTool.setText(_translate("allPurchaseOrderView", "New"))
        self.actionNewInvoiceTool.setToolTip(_translate("allPurchaseOrderView", "New Purchase Order"))
        self.actionDeleteTool.setText(_translate("allPurchaseOrderView", "Delete"))
        self.actionDeleteTool.setToolTip(_translate("allPurchaseOrderView", "Delete Selected Purchase Order"))
        self.actionEditTool.setText(_translate("allPurchaseOrderView", "Edit"))
        self.actionEditTool.setToolTip(_translate("allPurchaseOrderView", "Edit Selected Purchase Order"))
        self.actionPreviewTool.setText(_translate("allPurchaseOrderView", "Preview"))
        self.actionPreviewTool.setToolTip(_translate("allPurchaseOrderView", "Preview Selected Purcahse Order"))
        self.actionPrintTool.setText(_translate("allPurchaseOrderView", "Print"))
        self.actionPrintTool.setToolTip(_translate("allPurchaseOrderView", "Print Selected Purchase Order"))
        self.actionPrintTool.setShortcut(_translate("allPurchaseOrderView", "Ctrl+P"))
        self.actionEmailTool.setText(_translate("allPurchaseOrderView", "Email"))
        self.actionEmailTool.setToolTip(_translate("allPurchaseOrderView", "Email Selected Purchase Order"))
        self.actionSave.setText(_translate("allPurchaseOrderView", "Save"))
        self.actionSave.setToolTip(_translate("allPurchaseOrderView", "Save Selected Purchase Order as PDF"))
        self.actionPayment.setText(_translate("allPurchaseOrderView", "Bill"))
        self.actionPayment.setToolTip(_translate("allPurchaseOrderView", "Pay a Bill For Selected Order"))
        self.actionReturn.setText(_translate("allPurchaseOrderView", "Return"))
        self.actionReturn.setToolTip(_translate("allPurchaseOrderView", "Return for Seleced Invoice"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    allPurchaseOrderView = QtWidgets.QMainWindow()
    ui = Ui_allPurchaseOrderView()
    ui.setupUi(allPurchaseOrderView)
    allPurchaseOrderView.show()
    sys.exit(app.exec_())