# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Appointmentview.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

# to load css file
import cs


class AppointmentViewsss(object):

    def ShowAppointments(self):
        db = sqlite3.connect("Hospital.db")
        result = db.execute("select * from PatientAppointment")
        # Set the row count to be zero in order to show all the info that matches with email
        self.tableWidget.setRowCount(0)
        for RowNum, RowData in enumerate(result):
            self.tableWidget.insertRow(RowNum)
            for columnNum, columnData in enumerate(RowData):
                self.tableWidget.setItem(RowNum, columnNum, QtWidgets.QTableWidgetItem(str(columnData)))

        db.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 531)
        MainWindow.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 200, 781, 251))
        self.tableWidget.setStyleSheet("background-color: rgb(238, 240, 244);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #### to actiate show appointments
        self.pushButton.clicked.connect(self.ShowAppointments)

        self.pushButton.setGeometry(QtCore.QRect(640, 150, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(89, 128, 255);")
        self.pushButton.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 162, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 100, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 50, 131, 51))
        self.label_8.setStyleSheet("image: url(:/background/images.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ap. Status"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Patient Full  Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Patient Age"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Patient Number"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Patient  Gender"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Medical Condition"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", " Day of Appointment"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Time of Appointment"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Email"))
        self.pushButton.setText(_translate("MainWindow", "View All Appointments   "))
        self.label.setText(_translate("MainWindow", "Appointments "))
        self.label_3.setText(_translate("MainWindow", "Welcome to New Horizon Hospital"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AppointmentViewsss()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
