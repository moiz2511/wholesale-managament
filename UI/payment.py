# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payment.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_paymentWindow(object):
    def setupUi(self, paymentWindow):
        paymentWindow.setObjectName("paymentWindow")
        paymentWindow.resize(640, 504)
        self.centralwidget = QtWidgets.QWidget(paymentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 601, 201))
        self.frame.setStyleSheet("border: 1px solid rgb(215, 215, 215);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label.setStyleSheet("border: 0px solid rgb(215, 215, 215);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label_2.setStyleSheet("border: 0px solid rgb(215, 215, 215);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.label_3.setStyleSheet("border: 0px solid rgb(215, 215, 215);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 111, 16))
        self.label_4.setStyleSheet("border: 0px solid rgb(215, 215, 215);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label_5.setStyleSheet("border: 0px solid rgb(215, 215, 215);\n"
"")
        self.label_5.setObjectName("label_5")
        self.dateInput = QtWidgets.QDateEdit(self.frame)
        self.dateInput.setGeometry(QtCore.QRect(310, 10, 261, 22))
        self.dateInput.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateInput.setCalendarPopup(True)
        self.dateInput.setObjectName("dateInput")
        self.customerInput = QtWidgets.QComboBox(self.frame)
        self.customerInput.setGeometry(QtCore.QRect(310, 40, 191, 22))
        self.customerInput.setObjectName("customerInput")
        self.customerInput.addItem("")
        self.customerInput.addItem("")
        self.customerInput.addItem("")
        self.amountInput = QtWidgets.QLineEdit(self.frame)
        self.amountInput.setEnabled(True)
        self.amountInput.setGeometry(QtCore.QRect(310, 76, 261, 20))
        self.amountInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.amountInput.setText("")
        self.amountInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.amountInput.setPlaceholderText("")
        self.amountInput.setObjectName("amountInput")
        self.methodCombo = QtWidgets.QComboBox(self.frame)
        self.methodCombo.setGeometry(QtCore.QRect(310, 106, 261, 20))
        self.methodCombo.setObjectName("methodCombo")
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")
        self.refInput = QtWidgets.QLineEdit(self.frame)
        self.refInput.setEnabled(False)
        self.refInput.setGeometry(QtCore.QRect(310, 140, 261, 20))
        self.refInput.setObjectName("refInput")
        self.validationLabel = QtWidgets.QLabel(self.frame)
        self.validationLabel.setGeometry(QtCore.QRect(180, 80, 121, 16))
        self.validationLabel.setStyleSheet("color:rgb(255, 0, 0);\n"
"border: 0px solid rgb(215, 215, 215);")
        self.validationLabel.setObjectName("validationLabel")
        self.customerToolBtn = QtWidgets.QToolButton(self.frame)
        self.customerToolBtn.setGeometry(QtCore.QRect(510, 40, 25, 19))
        self.customerToolBtn.setStyleSheet("border:0px;")
        self.customerToolBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons8-customer-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.customerToolBtn.setIcon(icon)
        self.customerToolBtn.setAutoRaise(False)
        self.customerToolBtn.setObjectName("customerToolBtn")
        self.editCustomerToolBtn = QtWidgets.QToolButton(self.frame)
        self.editCustomerToolBtn.setGeometry(QtCore.QRect(540, 40, 25, 19))
        self.editCustomerToolBtn.setStyleSheet("border:0px;")
        self.editCustomerToolBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/MOIZ/Downloads/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editCustomerToolBtn.setIcon(icon1)
        self.editCustomerToolBtn.setAutoRaise(False)
        self.editCustomerToolBtn.setObjectName("editCustomerToolBtn")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 260, 601, 201))
        self.frame_2.setStyleSheet("\n"
"border: 1px solid rgb(215, 215, 215);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label_7.setStyleSheet("border: 0px solid rgb(215, 215, 215);")
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 581, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
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
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 4, item)
        self.recordBtn = QtWidgets.QPushButton(self.centralwidget)
        self.recordBtn.setGeometry(QtCore.QRect(370, 470, 75, 23))
        self.recordBtn.setObjectName("recordBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(460, 470, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.helpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.helpBtn.setGeometry(QtCore.QRect(550, 470, 75, 23))
        self.helpBtn.setObjectName("helpBtn")
        self.previewBtn = QtWidgets.QPushButton(self.centralwidget)
        self.previewBtn.setGeometry(QtCore.QRect(280, 470, 75, 23))
        self.previewBtn.setObjectName("previewBtn")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 240, 47, 13))
        self.label_9.setObjectName("label_9")
        paymentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(paymentWindow)
        QtCore.QMetaObject.connectSlotsByName(paymentWindow)

    def retranslateUi(self, paymentWindow):
        _translate = QtCore.QCoreApplication.translate
        paymentWindow.setWindowTitle(_translate("paymentWindow", "Apply a Payment"))
        self.label.setText(_translate("paymentWindow", "Date:"))
        self.label_2.setText(_translate("paymentWindow", "Customer:"))
        self.label_3.setText(_translate("paymentWindow", "Amount:"))
        self.label_4.setText(_translate("paymentWindow", "Reference Number:"))
        self.label_5.setText(_translate("paymentWindow", "Method:"))
        self.customerInput.setItemText(0, _translate("paymentWindow", "Ali Hmaza SHop"))
        self.customerInput.setItemText(1, _translate("paymentWindow", "Chaudhary Saab"))
        self.customerInput.setItemText(2, _translate("paymentWindow", "Badshaho"))
        self.methodCombo.setItemText(0, _translate("paymentWindow", "Cash"))
        self.methodCombo.setItemText(1, _translate("paymentWindow", "Check"))
        self.methodCombo.setItemText(2, _translate("paymentWindow", "Bank Deposit"))
        self.methodCombo.setItemText(3, _translate("paymentWindow", "Credit Card"))
        self.validationLabel.setText(_translate("paymentWindow", "Enter Valid Amount"))
        self.label_7.setText(_translate("paymentWindow", "Unapplied amount remaining:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("paymentWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("paymentWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("paymentWindow", "Invoice #"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("paymentWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("paymentWindow", "Date Due"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("paymentWindow", "Total"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("paymentWindow", "Due"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("paymentWindow", "Applied"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("paymentWindow", "10001"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("paymentWindow", "12/121/2"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("paymentWindow", "12/12/12"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("paymentWindow", "1000"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("paymentWindow", "1000"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("paymentWindow", "1002"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("paymentWindow", "12/121/21"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("paymentWindow", "12/12/12"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("paymentWindow", "1000"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("paymentWindow", "1000"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.recordBtn.setText(_translate("paymentWindow", "Record"))
        self.cancelBtn.setText(_translate("paymentWindow", "Cancel"))
        self.helpBtn.setText(_translate("paymentWindow", "Help"))
        self.previewBtn.setText(_translate("paymentWindow", "Preview"))
        self.label_8.setText(_translate("paymentWindow", "Customer Payment"))
        self.label_9.setText(_translate("paymentWindow", "Invoices"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    paymentWindow = QtWidgets.QMainWindow()
    ui = Ui_paymentWindow()
    ui.setupUi(paymentWindow)
    paymentWindow.show()
    sys.exit(app.exec_())
