# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'discountWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_discountWindow(object):
    def setupUi(self, discountWindow,first,firstSelf):
        discountWindow.setObjectName("discountWindow")
        discountWindow.resize(371, 203)
        self.centralwidget = QtWidgets.QWidget(discountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.flat = QtWidgets.QRadioButton(self.centralwidget)
        self.flat.setGeometry(QtCore.QRect(30, 10, 221, 21))
        self.flat.setObjectName("flat")
        self.flat.clicked.connect(lambda:self.checkFunc())
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 91, 16))
        self.label.setObjectName("label")
        self.percen = QtWidgets.QRadioButton(self.centralwidget)
        self.percen.setGeometry(QtCore.QRect(30, 70, 261, 21))
        self.percen.setObjectName("percen")
        self.percen.clicked.connect(lambda:self.checkFunc())
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 111, 16))
        self.label_2.setObjectName("label_2")
        self.flatInput = QtWidgets.QLineEdit(self.centralwidget)
        self.flatInput.setGeometry(QtCore.QRect(270, 40, 71, 20))
        self.flatInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.flatInput.setObjectName("flatInput")
        self.flatInput.setValidator(QtGui.QDoubleValidator(0.0,100.0,3))
        self.percenInput = QtWidgets.QLineEdit(self.centralwidget)
        self.percenInput.setGeometry(QtCore.QRect(270, 100, 71, 20))
        self.percenInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.percenInput.setObjectName("percenInput")
        stu_id_regx = QtCore.QRegExp('^([1-9]?\d|100)$')
        stu_id_validator = QtGui.QRegExpValidator(stu_id_regx, self.percenInput)
        self.percenInput.setValidator(stu_id_validator)
        self.applyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.applyBtn.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.applyBtn.setObjectName("applyBtn")
        self.applyBtn.clicked.connect(lambda:sendFunc(self))
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(200, 150, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.cancelBtn.clicked.connect(lambda:discountWindow.close())
        self.helpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.helpBtn.setGeometry(QtCore.QRect(280, 150, 75, 23))
        self.helpBtn.setObjectName("helpBtn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 130, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        discountWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(discountWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 21))
        self.menubar.setObjectName("menubar")
        discountWindow.setMenuBar(self.menubar)
        self.flatInput.setEnabled(False)
        self.percenInput.setEnabled(False)

        self.retranslateUi(discountWindow)
        QtCore.QMetaObject.connectSlotsByName(discountWindow)
        def sendFunc(self):
        
            if(self.percen.isChecked()):
                if(self.percenInput.text()):
                    myText=self.percenInput.text()
                    first.applyDiscount(firstSelf,myText,1)
                    discountWindow.close()
                else:
                    self.label_2.setStyleSheet('color:red')
                    self.label.setStyleSheet('color:black')
            if(self.flat.isChecked()):
                if(self.flatInput.text()):
                    myText=self.flatInput.text()
                    first.applyDiscount(firstSelf,myText,2)
                    discountWindow.close()
                else:
                    self.label.setStyleSheet('color:red')
                    self.label_2.setStyleSheet('color:black')
    def checkFunc(self):
        if(self.flat.isChecked()):
            self.flatInput.setEnabled(True)
            self.percenInput.setEnabled(False)
        if(self.percen.isChecked()):
            self.flatInput.setEnabled(False)
            self.percenInput.setEnabled(True)
    
        
            
            

    def retranslateUi(self, discountWindow):
        _translate = QtCore.QCoreApplication.translate
        discountWindow.setWindowTitle(_translate("discountWindow", "Apply Discount"))
        self.flat.setText(_translate("discountWindow", "Fixed Flat Discount to the Whole Invoice"))
        self.label.setText(_translate("discountWindow", "Discount Amount:"))
        self.percen.setText(_translate("discountWindow", "Fixed Percentage Discount to the Whole Invoice"))
        self.label_2.setText(_translate("discountWindow", "Discount Percentage:"))
        self.applyBtn.setText(_translate("discountWindow", "Apply"))
        self.cancelBtn.setText(_translate("discountWindow", "Cancel"))
        self.helpBtn.setText(_translate("discountWindow", "Help"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    discountWindow = QtWidgets.QMainWindow()
    ui = Ui_discountWindow()
    ui.setupUi(discountWindow)
    discountWindow.show()
    sys.exit(app.exec_())
