# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GenratePass.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#BackEnd.
from PyQt5.QtGui import QIntValidator
#BackEnd.
import random
import string
    
   


class Ui_MainWindow(object):
#BackEnd! .showing AlertBox When user enter Nothing.
    def alertBox(self,title,message):
           Window=QtWidgets.QMessageBox()
           Window.setWindowTitle(title)
           Window.setText(message)
           Window.setStandardButtons(QtWidgets.QMessageBox.Ok)
           Window.exec_()
#@Backend! .Generate Random Password.
    def RandomPassGen(self):
        if self.Genrate_Pass.text() =="":
                self.alertBox("Error!","Please Enter Your Password Limit.")
        else:
             number=int(self.Genrate_Pass.text())
             password=""
             for n in range(number):
                     Limit=random.randint(1,99)
                     password=password +string.printable[Limit]
        self.Genrate_Pass.clear()
        return self.output_Pass.setText(password)
                     
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 480)
        MainWindow.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 461, 61))
        self.label.setStyleSheet("color:yellow;\n"
"font-family:calibri;\n"
"font-weight:bold;\n"
"font-size:28px;")
        self.label.setObjectName("label")
        self.Pass_Limit = QtWidgets.QLabel(self.centralwidget)
        self.Pass_Limit.setGeometry(QtCore.QRect(70, 100, 261, 41))
        self.Pass_Limit.setStyleSheet("color:yellow;\n"
"font-family:calibri;\n"
"font-weight:bold;\n"
"font-size:20px;")
        self.Pass_Limit.setObjectName("Pass_Limit")
        self.Genrate_Pass = QtWidgets.QLineEdit(self.centralwidget)
        
        self.Genrate_Pass.setGeometry(QtCore.QRect(80, 150, 421, 41))
        self.Genrate_Pass.setStyleSheet("font-weight:bold;\n"
"padding:8px;\n"
"border:2px solid yellow;\n"
"color:yellow;\n"
"font-size:18px;\n"
"border-radius:8px;\n"
"\n"
"")
        self.Genrate_Pass.setObjectName("Genrate_Pass")
        #BackEnd.Seting Validater.
        self.Genrate_Pass.setValidator(QIntValidator(1,99))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #BackEnd!. Button connected.
        self.pushButton.clicked.connect(self.RandomPassGen)
        self.pushButton.setGeometry(QtCore.QRect(80, 230, 421, 41))
        self.pushButton.setStyleSheet("background-color:yellow;\n"
"font-family:calibri;\n"
"font-weight:bold;\n"
"font-size:18px;\n"
"border-radius:8px;\n"
"border:2px solid white;")
        self.pushButton.setObjectName("pushButton")
        self.output_Pass = QtWidgets.QLineEdit(self.centralwidget)
        self.output_Pass.setGeometry(QtCore.QRect(80, 310, 421, 41))
        self.output_Pass.setStyleSheet("font-weight:bold;\n"
"padding:8px;\n"
"border:2px solid yellow;\n"
"color:yellow;\n"
"font-size:18px;\n"
"border-radius:8px;\n"
"\n"
"")
        self.output_Pass.setObjectName("output_Pass")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Strong Password Generator"))
        self.label.setText(_translate("MainWindow", " Strong Random Password Generator"))
        self.Pass_Limit.setText(_translate("MainWindow", " Ente Your Password Limit"))
        self.pushButton.setText(_translate("MainWindow", "Generate Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
