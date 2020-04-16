# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\download.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from nwebrequest import GetTitleAndLink, GetIMGsURL, MakeDirectory, MakePDF, GetFileName, chdir, DownloadWebtoon

from subprocess import Popen


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1259, 875)
        self.downloadURL = QtWidgets.QLineEdit(Dialog)
        self.downloadURL.setGeometry(QtCore.QRect(30, 40, 991, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.downloadURL.setFont(font)
        self.downloadURL.setObjectName("downloadURL")
        self.episodeSearchBtn = QtWidgets.QPushButton(Dialog)
        self.episodeSearchBtn.setGeometry(QtCore.QRect(1040, 40, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.episodeSearchBtn.setFont(font)
        self.episodeSearchBtn.setObjectName("episodeSearchBtn")
        self.downloadList = QtWidgets.QListWidget(Dialog)
        self.downloadList.setGeometry(QtCore.QRect(30, 180, 531, 661))
        self.downloadList.setObjectName("downloadList")
        self.downloadStatus = QtWidgets.QProgressBar(Dialog)
        self.downloadStatus.setGeometry(QtCore.QRect(740, 814, 481, 23))
        self.downloadStatus.setProperty("value", 0)
        self.downloadStatus.setObjectName("downloadStatus")
        self.downloadLog = QtWidgets.QTextEdit(Dialog)
        self.downloadLog.setGeometry(QtCore.QRect(740, 180, 471, 611))
        self.downloadLog.setObjectName("downloadLog")
        self.viewLogLabel = QtWidgets.QLabel(Dialog)
        self.viewLogLabel.setGeometry(QtCore.QRect(740, 140, 171, 31))
        self.viewLogLabel.setObjectName("viewLogLabel")
        self.viewListLabel = QtWidgets.QLabel(Dialog)
        self.viewListLabel.setGeometry(QtCore.QRect(30, 140, 131, 31))
        self.viewListLabel.setObjectName("viewListLabel")
        self.downloadBtn = QtWidgets.QPushButton(Dialog)
        self.downloadBtn.setGeometry(QtCore.QRect(580, 470, 141, 51))
        self.downloadBtn.setObjectName("downloadBtn")
        self.checkAllBox = QtWidgets.QCheckBox(Dialog)
        self.checkAllBox.setGeometry(QtCore.QRect(480, 150, 96, 19))
        self.checkAllBox.setObjectName("checkAllBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.episodeSearchBtn.clicked.connect(self.SetListWidgetItem)
        self.downloadBtn.clicked.connect(self.WebtoonDownload)
        self.checkAllBox.stateChanged.connect(self.CheckAllList)
        



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Naver Webtoon Download"))
        self.episodeSearchBtn.setText(_translate("Dialog", "웹툰 회차 검색"))
        self.viewLogLabel.setText(_translate("Dialog", "다운로드 로그"))
        self.viewListLabel.setText(_translate("Dialog", "웹툰 회차 수"))
        self.downloadBtn.setText(_translate("Dialog", "웹툰 다운로드"))
        self.checkAllBox.setText(_translate("Dialog", "전체선택"))



    def SetListWidgetItem(self):
        url = self.downloadURL.text()
        epiList = GetTitleAndLink(url)

        self.downloadList.clear()
        for epi in enumerate(epiList):
            item = QtWidgets.QListWidgetItem()
            item.setText(epi[1][0])
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.downloadList.addItem(item)


    
    def GetCheckedList(self):
        checkItemsIndex = []
        
        for index in range(self.downloadList.count()):
            if self.downloadList.item(index).checkState() == QtCore.Qt.Checked:
                checkItemsIndex.append(index)

        return checkItemsIndex



    def CheckAllList(self):
        for index in range(self.downloadList.count()):
            if self.checkAllBox.isChecked():
                self.downloadList.item(index).setCheckState(QtCore.Qt.Checked)
                
            else:
                self.downloadList.item(index).setCheckState(QtCore.Qt.Unchecked)


    def WebtoonDownload(self):
        self.downloadURL.setDisabled(True)
        self.downloadBtn.setDisabled(True)
        self.checkAllBox.setDisabled(True)
        self.downloadList.setDisabled(True)
        self.downloadLog.setDisabled(True)

        epiIndex = self.GetCheckedList()
        nwLink = self.downloadURL.text()


        wtInfo = GetTitleAndLink(nwLink)
        for i in enumerate(epiIndex):
            MakeDirectory('./naver_download_temp/')
            wtTitle = wtInfo[i[0]][0]
            wtLink = wtInfo[i[0]][1]

            imgsURL = GetIMGsURL(wtLink)
            fname = GetFileName(wtTitle) + '.pdf'

            imgList = DownloadWebtoon(filename=wtTitle, imgURLs=imgsURL)

            chdir('../')

            MakePDF(imgList, fname, './naver_download_temp/')

            self.downloadStatus.setProperty("value", (i[0]+1)*100 / len(epiIndex) )

            self.downloadLog.insertPlainText(f'\n"./{fname}" 으로 저장\n')



        Popen(['explorer.exe', '.'])
             
        self.downloadURL.setDisabled(False)
        self.downloadBtn.setDisabled(False)
        self.checkAllBox.setDisabled(False)
        self.downloadList.setDisabled(False)
        self.downloadLog.setDisabled(False)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())

