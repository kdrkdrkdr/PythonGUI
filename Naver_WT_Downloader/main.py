# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import search
import download

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 171)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 311, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.searchBtn.setObjectName("searchBtn")
        self.verticalLayout.addWidget(self.searchBtn)
        self.downloadBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.downloadBtn.setObjectName("downloadBtn")
        self.verticalLayout.addWidget(self.downloadBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.searchBtn.clicked.connect(self.openSearchWindow)
        self.downloadBtn.clicked.connect(self.openDownloadWindow)


    def openSearchWindow(self):
        self.sWin = QtWidgets.QDialog()
        self.sUi = search.Ui_Dialog()
        self.sUi.setupUi(self.sWin)
        self.sWin.show()


    
    def openDownloadWindow(self):
        self.dWin = QtWidgets.QDialog()
        self.dUi = download.Ui_Dialog()
        self.dUi.setupUi(self.dWin)
        self.dWin.show()
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchBtn.setText(_translate("MainWindow", "네이버 웹툰 검색하기"))
        self.downloadBtn.setText(_translate("MainWindow", "네이버 웹툰 다운로드"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
