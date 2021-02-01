# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import EmployeeReg
import Viewemployee
import patientreg
import Viewpatient
import Appointmentview
import cs


class AdminView(object):

# function to display staff registration portal
    def staffReg(self):
        self.window = QtWidgets.QMainWindow()
        self.OpenEmp = EmployeeReg.EmployeeRegister()
        self.OpenEmp.setupUi(self.window)
        self.window.show()

# function to display staff registration details
    def ViewStaffInfo(self):
        self.window = QtWidgets.QMainWindow()
        self.OpenViewEmp = Viewemployee.ViewEmployees()
        self.OpenViewEmp.setupUi(self.window)
        self.window.show()

# function to register patientes details
    def PatientReg(self):
        self.window = QtWidgets.QMainWindow()
        self.OpenPat = patientreg.PatientRegster()
        self.OpenPat.setupUi(self.window)
        self.window.show()

# function to view patients information
    def PatientView(self):
        self.window = QtWidgets.QMainWindow()
        self.OpenPat = Viewpatient.ViewPatientssInfo()
        self.OpenPat.setupUi(self.window)
        self.window.show()
# function to view patients information
    def Appointments(self):
        self.window = QtWidgets.QMainWindow()
        self.OpenApp = Appointmentview.AppointmentViewsss()
        self.OpenApp.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PatRegBTN = QtWidgets.QPushButton(self.centralwidget)
        self.PatRegBTN.setGeometry(QtCore.QRect(80, 270, 181, 61))
        ## to activate patient registeration portal
        self.PatRegBTN.clicked.connect(self.PatientReg)
        print("logout")

        font = QtGui.QFont()
        font.setFamily("Courier")
        self.PatRegBTN.setFont(font)
        self.PatRegBTN.setObjectName("PatRegBTN")
        self.PatInfoBTN = QtWidgets.QPushButton(self.centralwidget)
        self.PatInfoBTN.setGeometry(QtCore.QRect(310, 270, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.PatInfoBTN.setFont(font)
        self.PatInfoBTN.setStyleSheet("background-color: rgb(138, 173, 255);")
        self.PatInfoBTN.setObjectName("PatInfoBTN")
        # to activate patient info
        self.PatInfoBTN.clicked.connect(self.PatientView)


        self.StaffInfoBTN = QtWidgets.QPushButton(self.centralwidget)
        self.StaffInfoBTN.setGeometry(QtCore.QRect(90, 380, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.StaffInfoBTN.setFont(font)
        self.StaffInfoBTN.setStyleSheet("background-color: rgb(138, 173, 255);")
        self.StaffInfoBTN.setObjectName("StaffInfoBTN")
        #### to activate staff info button
        self.StaffInfoBTN.clicked.connect(self.ViewStaffInfo)


        self.AppointmentBTN = QtWidgets.QPushButton(self.centralwidget)
        self.AppointmentBTN.setGeometry(QtCore.QRect(530, 270, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.AppointmentBTN.setFont(font)
        self.AppointmentBTN.setObjectName("AppointmentBTN")
        ## to activate appointment views
        self.AppointmentBTN.clicked.connect(self.Appointments)

        self.LogoutBTN = QtWidgets.QPushButton(self.centralwidget)
        self.LogoutBTN.setGeometry(QtCore.QRect(530, 380, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.LogoutBTN.setFont(font)
        ## logout buton activate
        self.LogoutBTN.clicked.connect(QtWidgets.qApp.quit)
        
        self.LogoutBTN.setStyleSheet("background-color: rgb(138, 173, 255);")
        self.LogoutBTN.setObjectName("LogoutBTN")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -20, 811, 621))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/background/H.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 140, 131, 51))
        self.label_2.setStyleSheet("image: url(:/background/images.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 200, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.StaffRegBTN = QtWidgets.QPushButton(self.centralwidget)
        self.StaffRegBTN.setGeometry(QtCore.QRect(310, 380, 181, 61))
        # activate staff registration
        self.StaffRegBTN.clicked.connect(self.staffReg)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.StaffRegBTN.setFont(font)
        self.StaffRegBTN.setObjectName("PatRegBTN_2")
        self.label.raise_()
        self.PatRegBTN.raise_()
        self.PatInfoBTN.raise_()
        self.StaffInfoBTN.raise_()
        self.AppointmentBTN.raise_()
        self.LogoutBTN.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.StaffRegBTN.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PatRegBTN.setText(_translate("MainWindow", "Patient Registration"))
        self.PatInfoBTN.setText(_translate("MainWindow", "Patients Information"))
        self.StaffInfoBTN.setText(_translate("MainWindow", "Staff Information"))
        self.AppointmentBTN.setText(_translate("MainWindow", "Appointments"))
        self.LogoutBTN.setText(_translate("MainWindow", "Logout"))
        self.label_3.setText(_translate("MainWindow", "Welcome to New Horizon Hospital"))
        self.StaffRegBTN.setText(_translate("MainWindow", "Staff Registration"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AdminView()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())