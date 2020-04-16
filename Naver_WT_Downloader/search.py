# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from nwebrequest import WebToonInfo, ImageDownload, MakeDirectory, chdir



class ImgWidget(QtWidgets.QLabel):
    def __init__(self, imgURL, filename, parent=None):
        self.imgURL = imgURL
        self.filename = filename

        ImageDownload(self.filename, self.imgURL)
        
        super(ImgWidget, self).__init__(parent)
        pic = QtGui.QPixmap(filename)
        self.setPixmap(pic)



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1240, 878)
        self.wtSearchBox = QtWidgets.QLineEdit(Dialog)
        self.wtSearchBox.setGeometry(QtCore.QRect(30, 40, 981, 51))
        self.wtSearchBox.setObjectName("wtSearchBox")
        self.wtList = QtWidgets.QTableWidget(Dialog)
        self.wtList.setGeometry(QtCore.QRect(30, 130, 1181, 711))
        self.wtList.setObjectName("wtList")
        self.wtList.setColumnCount(0)
        self.wtList.setRowCount(0)
        self.wtSearchBtn = QtWidgets.QPushButton(Dialog)
        self.wtSearchBtn.setGeometry(QtCore.QRect(1060, 40, 151, 51))
        self.wtSearchBtn.setObjectName("wtSearchBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.wtSearchBtn.clicked.connect(self.SetTableWidgetData)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Naver Webtoon Search"))
        self.wtSearchBtn.setText(_translate("Dialog", "웹툰 검색"))



    def SetTableWidgetData(self):
        
        searchKword = self.wtSearchBox.text()

        if searchKword.replace(' ', '') != '':
            data = WebToonInfo(searchKword)

            self.wtList.setColumnCount(7)
            self.wtList.setRowCount(len(data))

            horizonHeader = self.wtList.horizontalHeader()
            horizonHeader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            verticalHeader = self.wtList.verticalHeader()
            verticalHeader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)


            self.wtList.setHorizontalHeaderLabels(["썸네일", '제목', "웹툰 주소", "글/그림", "장르", "노출회수", "최종업데이트"])

            MakeDirectory('./naver_wt_search_temp/')
            
            for dataIdx, dataList in enumerate(data):
                for i, d in enumerate(dataList):
                    if i == 0:
                        self.wtList.setCellWidget(dataIdx, i, ImgWidget(imgURL=d, filename=f'./{dataIdx}_{i}.jpg'))
                    else:
                        self.wtList.setItem(dataIdx, i, QtWidgets.QTableWidgetItem(d))

            chdir('../')
            self.wtList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) 

        else:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())