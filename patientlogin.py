# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patientlogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui,  QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import cs


class Patientlog(object):

    def ViewRegssInfo(self):
        db= sqlite3.connect("Hospital.db")
        # Getting email address used at patient point of registration
        r = db.execute("select Email from SaveEmails")
        list = []  # appending email to list
        for RowNum, RowData in enumerate(r):
            for ColumnNum, ColumnData in enumerate(RowData):
                list.append(ColumnData)
        result = db.execute("select * from PatientInfo where Email=" + "'" + list[0] + "'")
       # result = db.execute("select * from PatientEmail ")
        self.tableWidget.setRowCount(0)
        # Using two for loops to insert the data into tableWidget
        for RowNum, RowDATA in enumerate(result):
            self.tableWidget.insertRow(RowNum)
            for ColumnNum, ColumnData in enumerate(RowDATA):
                self.tableWidget.setItem(RowNum, ColumnNum, QtWidgets.QTableWidgetItem(str(ColumnData)))
        for RowNum, RowDATA in enumerate(result):
            self.tableWidget.insertRow(RowNum)
            for ColumnNum, ColumnData in enumerate(RowDATA):
                self.tableWidget.setItem(RowNum, ColumnNum, QtWidgets.QTableWidgetItem(str(ColumnData)))
        db.close()
        print("view info")

    # to make appintments
    def MakeAppointment(self):
        ## table for appointment
        AppStatus= ""
        FullName = self.FullNameLE.text()
        Age = self.AgeLE.text()
        Phone = self.PhoneLE.text()
        Gender = self.GenderCMB.currentText()
        MedicalCondition = self.MedConLE.text()
        Email= self.EmailLE.text()
        Day = self.PreDayCMB.currentText()
        Time= self.timeEdit.text()
        ### database for appointment
        db= sqlite3.connect("Hospital.db")
        db.execute("create table if not exists PatientAppointment (AppStatus text,Fullname text, Age int, Phone int, Gender text, MedicalCondition text,time text , Day text,Email text )")
        db.execute("insert into PatientAppointment values(?,?,?,?,?,?,?,?,?)",(AppStatus, FullName, Age,Phone,Gender,MedicalCondition,Time,Day,Email))
        db.commit()
        message=QMessageBox()
        message.setWindowTitle("Succesful")
        message.setInformativeText("You have succesfully booked an appointment")
        message.exec_()
        print("make appointment")

    ## update appointment
    def UpdateAppointment(self):
        FullName = self.FullNameLE.text()
        Age = self.AgeLE.text()
        Phone = self.PhoneLE.text()
        Gender = self.GenderCMB.currentText()
        MedicalCondition = self.MedConLE.text()
        Email = self.EmailLE.text()
        Day = self.PreDayCMB.currentText()
        Time = self.timeEdit.text()
        db = sqlite3.connect("Hospital.db")

        ### update appointment database
        db.execute("update PatientAppointment set Fullname=?, Age=?, Phone=?, Gender=?, MedicalCondition=?, Email=?, Day=?, Time=? where FullName="+"'"+FullName+"'",
                   (FullName,Age, Phone, Gender,MedicalCondition,Email,Day,Time))
        db.commit()
        message = QMessageBox()
        message.setWindowTitle("Succesful")
        message.setInformativeText("You have succesfully updated your appointment")
        message.exec_()

        #show appointment

    def ShowAppointments(self):
        db = sqlite3.connect("Hospital.db")
        # Getting the only email address that the patient entered when he/she logged in to check if there is data that matches with this email
        r = db.execute("select Email from SaveEmails")
        list = []  # Using for loop to go over SaveEmails table and append that email into a list
        # Going through the Emails by changing the data type, RowNum is the number of rows, RowData is the column data
        for RowNum, RowData in enumerate(r):
            for columnNum, columnData in enumerate(RowData):
                list.append(columnData)
        # Getting all the info of an appointment that matches with the email address in list[]
        result = db.execute("select * from PatientAppointment where Email= " + "'" + list[0] + "'")
        # Set the row count to be zero in order to show all the info that matches with email
        self.tableWidget_2.setRowCount(0)
        for RowNum, RowData in enumerate(result):
            self.tableWidget_2.insertRow(RowNum)
            for columnNum, columnData in enumerate(RowData):
                self.tableWidget_2.setItem(RowNum, columnNum, QtWidgets.QTableWidgetItem(str(columnData)))

        db.close()

        # Function to delete an appointment based on FullName

    def DeleteAppointment(self):
        # Get the full name from lineEdit and delete data if it matches that fullname
        FullName = self.FullNameLE.text()
        db = sqlite3.connect("Hospital.db")
        db.execute("delete from PatientAppointment where FullName= " + "'" + FullName + "'")
        db.commit()
        message1 = QMessageBox()
        message1.setWindowTitle("Successfull")
        message1.setInformativeText("You have successfully deleted your appointment")
        message1.exec_()
        # Showing the Appointments of patient after deleting one
        result = db.execute("select * from PatientAppointment where FullName= " + "'" + FullName + "'")
        self.tableWidget_2.setRowCount(0)
        # Using two for loops to insert the data of Appointments if there is any into tableWidget
        for RowNum, RowDATA in enumerate(result):
            self.tableWidget_2.insertRow(RowNum)
            for ColumnNum, ColumnData in enumerate(RowDATA):
                self.tableWidget_2.setItem(RowNum, ColumnNum,QtWidgets.QTableWidgetItem(str(ColumnData)))
        # Clearing the fields after deleting
        db.close()
        self.FullNameLE.clear()
        self.AgeLE.clear()
        self.PhoneLE.clear()
        self.GenderCMB.setCurrentText("")
        self.MedConLE.clear()
        self.EmailLE.clear()
        self.PreDayCMB.setCurrentText("")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 733)
        MainWindow.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 519, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 599, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 519, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 559, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 639, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 559, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.PreDayCMB = QtWidgets.QComboBox(self.centralwidget)
        self.PreDayCMB.setGeometry(QtCore.QRect(430, 599, 141, 31))
        self.PreDayCMB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PreDayCMB.setObjectName("PreDayCMB")
        self.PreDayCMB.addItem("")
        self.PreDayCMB.setItemText(0, "")
        self.PreDayCMB.addItem("")
        self.PreDayCMB.addItem("")
        self.PreDayCMB.addItem("")
        self.PreDayCMB.addItem("")
        self.PreDayCMB.addItem("")
        self.PreDayCMB.addItem("")
        self.PreDayCMB.addItem("")
        self.GenderCMB = QtWidgets.QComboBox(self.centralwidget)
        self.GenderCMB.setGeometry(QtCore.QRect(100, 639, 101, 31))
        self.GenderCMB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GenderCMB.setObjectName("GenderCMB")
        self.GenderCMB.addItem("")
        self.GenderCMB.setItemText(0, "")
        self.GenderCMB.addItem("")
        self.GenderCMB.addItem("")
        self.GenderCMB.addItem("")
        self.PhoneLE = QtWidgets.QLineEdit(self.centralwidget)
        self.PhoneLE.setGeometry(QtCore.QRect(100, 599, 141, 31))
        self.PhoneLE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PhoneLE.setObjectName("PhoneLE")
        self.EmailLE = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailLE.setGeometry(QtCore.QRect(430, 559, 141, 31))
        self.EmailLE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EmailLE.setObjectName("EmailLE")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 599, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.UpdateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateBtn.setGeometry(QtCore.QRect(120, 680, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.UpdateBtn.setFont(font)
        self.UpdateBtn.setStyleSheet("background-color: rgb(138, 173, 255);")
        self.UpdateBtn.setObjectName("UpdateBtn")
        # to activate appointment data
        self.UpdateBtn.clicked.connect(self.UpdateAppointment)

        self.FullNameLE = QtWidgets.QLineEdit(self.centralwidget)
        self.FullNameLE.setGeometry(QtCore.QRect(100, 519, 141, 31))
        self.FullNameLE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FullNameLE.setObjectName("FullNameLE")
        self.AgeLE = QtWidgets.QLineEdit(self.centralwidget)
        self.AgeLE.setGeometry(QtCore.QRect(100, 559, 141, 31))
        self.AgeLE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AgeLE.setObjectName("AgeLE")
        self.MedConLE = QtWidgets.QLineEdit(self.centralwidget)
        self.MedConLE.setGeometry(QtCore.QRect(430, 519, 141, 31))
        self.MedConLE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MedConLE.setObjectName("MedConLE")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 110, 791, 151))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(238, 240, 244);")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.LogoutBTN = QtWidgets.QPushButton(self.centralwidget)
        self.LogoutBTN.setGeometry(QtCore.QRect(0, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.LogoutBTN.setFont(font)
        self.LogoutBTN.setStyleSheet("background-color: rgb(138, 173, 255);")
        self.LogoutBTN.setObjectName("LogoutBTN")
        self.ShowAppBTN = QtWidgets.QPushButton(self.centralwidget)
        ## activate show appointment
        self.ShowAppBTN.clicked.connect(self.ShowAppointments)


        self.ShowAppBTN.setGeometry(QtCore.QRect(640, 490, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.ShowAppBTN.setFont(font)
        self.ShowAppBTN.setStyleSheet("background-color: rgb(138, 173, 255);")
        self.ShowAppBTN.setObjectName("ShowAppBTN")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 330, 791, 161))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("background-color: rgb(238, 240, 244);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 80, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.ShowInfoBTN = QtWidgets.QPushButton(self.centralwidget)
        self.ShowInfoBTN.setGeometry(QtCore.QRect(640, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.ShowInfoBTN.setFont(font)
        self.ShowInfoBTN.setStyleSheet("background-color: rgb(138, 173, 255);")
        self.ShowInfoBTN.setObjectName("ShowInfoBTN")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        ## activate show infromation button
        self.ShowInfoBTN.clicked.connect(self.ViewRegssInfo)


        self.label_12.setGeometry(QtCore.QRect(10, 290, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 639, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(430, 640, 141, 31))
        self.timeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit.setObjectName("timeEdit")
        self.DelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DelBtn.setGeometry(QtCore.QRect(250, 680, 91, 31))
        #### activate delete button
        self.DelBtn.clicked.connect(self.DeleteAppointment)





        font = QtGui.QFont()
        font.setFamily("Courier")
        self.DelBtn.setFont(font)
        self.DelBtn.setStyleSheet("background-color: rgb(138, 173, 255);")
        self.DelBtn.setObjectName("DelBtn")
        self.MakeAppBTN = QtWidgets.QPushButton(self.centralwidget)
        self.MakeAppBTN.setGeometry(QtCore.QRect(390, 680, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.MakeAppBTN.setFont(font)
        self.MakeAppBTN.setStyleSheet("background-color: rgb(138, 173, 255);")
        self.MakeAppBTN.setObjectName("MakeAppBTN")
        #### to activate appointment
        self.MakeAppBTN.clicked.connect(self.MakeAppointment)

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(320, 20, 131, 51))
        self.label_13.setStyleSheet("image: url(:/background/images.png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Full Name:"))
        self.label_5.setText(_translate("MainWindow", "Phone"))
        self.label_8.setText(_translate("MainWindow", "Medical Condition"))
        self.label_3.setText(_translate("MainWindow", "Age"))
        self.label_7.setText(_translate("MainWindow", "Gender"))
        self.label_9.setText(_translate("MainWindow", "Email"))
        self.PreDayCMB.setItemText(1, _translate("MainWindow", "Sunday"))
        self.PreDayCMB.setItemText(2, _translate("MainWindow", "Monday"))
        self.PreDayCMB.setItemText(3, _translate("MainWindow", "Tueday"))
        self.PreDayCMB.setItemText(4, _translate("MainWindow", "Wednesday"))
        self.PreDayCMB.setItemText(5, _translate("MainWindow", "Thursday"))
        self.PreDayCMB.setItemText(6, _translate("MainWindow", "Friday"))
        self.PreDayCMB.setItemText(7, _translate("MainWindow", "Saturday"))
        self.GenderCMB.setItemText(1, _translate("MainWindow", "Male"))
        self.GenderCMB.setItemText(2, _translate("MainWindow", "Female"))
        self.GenderCMB.setItemText(3, _translate("MainWindow", "Other"))
        self.label_6.setText(_translate("MainWindow", "Prefered Day"))
        self.UpdateBtn.setText(_translate("MainWindow", "Update"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Full Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Birth Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Marital Status"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Illness"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Email"))
        self.LogoutBTN.setText(_translate("MainWindow", "Logout "))
        self.ShowAppBTN.setText(_translate("MainWindow", "Show Appointments"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "App Status"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Patient Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Patient Age"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Patient Phone"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Patient Gender"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Medical Condition"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Scheduled Day of Appointment"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Time of Appointment"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Email"))
        self.label_11.setText(_translate("MainWindow", "Your Information"))
        self.ShowInfoBTN.setText(_translate("MainWindow", "Show Information"))
        self.label_12.setText(_translate("MainWindow", "Your Appointment"))
        self.label_10.setText(_translate("MainWindow", "Prefered Time"))
        self.DelBtn.setText(_translate("MainWindow", "Delete"))
        self.MakeAppBTN.setText(_translate("MainWindow", "Make Appointments"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Patientlog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
