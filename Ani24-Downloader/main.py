# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QTimer)

from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)

from PySide2.QtWidgets import *

from functools import partial

from requests import get

from bs4 import BeautifulSoup

from urllib.parse import quote_plus, urlparse

from youtube_dl import YoutubeDL as DownloadFile

from threading import Semaphore, Thread

from re import sub

s = Semaphore(3)



class TimerMessageBox(QMessageBox):

    def __init__(self, timeout=3, contents="", parent=None):

        super(TimerMessageBox, self).__init__(parent)
        self.setWindowTitle('Ani24 애니 다운로더')
        self.time_to_wait = timeout
        self.setText(contents)
        self.setStandardButtons(QMessageBox.NoButton)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changeContent)
        self.timer.start()

    def changeContent(self):
        # self.setText(contents)
        self.time_to_wait -= 1
        if self.time_to_wait <= 0:
            self.close()

    def eclose(self):
    	self.close()

    def closeEvent(self, event):
    	self.timer.stop()
    	event.accept()



class Ui_MainWindow(object):
    def __init__(self):
        self.ani24URL = 'https://ani24do.com'
        self.yaani24URL = 'https://yaani24.net'

    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1130, 820)
        MainWindow.setMinimumSize(QSize(1130, 820))
        MainWindow.setMaximumSize(QSize(1130, 820))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 31, 1111, 761))
        self.searchTab = QWidget()
        self.searchTab.setObjectName(u"searchTab")
        self.aniSearchBox = QLineEdit(self.searchTab)
        self.aniSearchBox.setObjectName(u"aniSearchBox")
        self.aniSearchBox.setGeometry(QRect(91, 20, 811, 26))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.aniSearchBox.setFont(font)
        self.searchBtn = QPushButton(self.searchTab)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setGeometry(QRect(915, 19, 93, 28))
        self.setSiteAni24rBtn = QRadioButton(self.searchTab)
        self.setSiteRbtnGroup = QButtonGroup(MainWindow)
        self.setSiteRbtnGroup.setObjectName(u"setSiteRbtnGroup")
        self.setSiteRbtnGroup.addButton(self.setSiteAni24rBtn)
        self.setSiteAni24rBtn.setObjectName(u"setSiteAni24rBtn")
        self.setSiteAni24rBtn.setGeometry(QRect(1015, 11, 63, 19))
        self.setSiteYaAni24rBtn = QRadioButton(self.searchTab)
        self.setSiteRbtnGroup.addButton(self.setSiteYaAni24rBtn)
        self.setSiteYaAni24rBtn.setObjectName(u"setSiteYaAni24rBtn")
        self.setSiteYaAni24rBtn.setGeometry(QRect(1015, 37, 79, 19))
        self.newTop20rBtn = QRadioButton(self.searchTab)
        self.setTop20RbtnGroup = QButtonGroup(MainWindow)
        self.setTop20RbtnGroup.setObjectName(u"setTop20RbtnGroup")
        self.setTop20RbtnGroup.addButton(self.newTop20rBtn)
        self.newTop20rBtn.setObjectName(u"newTop20rBtn")
        self.newTop20rBtn.setGeometry(QRect(11, 65, 101, 19))
        self.genreTop20rBtn = QRadioButton(self.searchTab)
        self.setTop20RbtnGroup.addButton(self.genreTop20rBtn)
        self.genreTop20rBtn.setObjectName(u"genreTop20rBtn")
        self.genreTop20rBtn.setGeometry(QRect(118, 65, 101, 19))
        self.quarterTop20rBtn = QRadioButton(self.searchTab)
        self.setTop20RbtnGroup.addButton(self.quarterTop20rBtn)
        self.quarterTop20rBtn.setObjectName(u"quarterTop20rBtn")
        self.quarterTop20rBtn.setGeometry(QRect(225, 65, 101, 19))
        self.yearTop20rBtn = QRadioButton(self.searchTab)
        self.setTop20RbtnGroup.addButton(self.yearTop20rBtn)
        self.yearTop20rBtn.setObjectName(u"yearTop20rBtn")
        self.yearTop20rBtn.setGeometry(QRect(333, 65, 101, 19))
        self.yearLabel = QLabel(self.searchTab)
        self.yearLabel.setObjectName(u"yearLabel")
        self.yearLabel.setGeometry(QRect(448, 64, 41, 20))
        self.yearLabel.setFont(font)
        self.yearSpinBox = QSpinBox(self.searchTab)
        self.yearSpinBox.setObjectName(u"yearSpinBox")
        self.yearSpinBox.setGeometry(QRect(490, 63, 61, 24))
        self.yearSpinBox.setMinimum(2010)
        self.yearSpinBox.setMaximum(2030)
        self.quarterLabel = QLabel(self.searchTab)
        self.quarterLabel.setObjectName(u"quarterLabel")
        self.quarterLabel.setGeometry(QRect(568, 64, 41, 20))
        self.quarterLabel.setFont(font)
        self.quarterSpinBox = QSpinBox(self.searchTab)
        self.quarterSpinBox.setObjectName(u"quarterSpinBox")
        self.quarterSpinBox.setGeometry(QRect(608, 63, 31, 24))
        self.quarterSpinBox.setMinimum(1)
        self.quarterSpinBox.setMaximum(4)
        self.gerneLabel = QLabel(self.searchTab)
        self.gerneLabel.setObjectName(u"gerneLabel")
        self.gerneLabel.setGeometry(QRect(656, 63, 41, 20))
        self.gerneLabel.setFont(font)
        self.gerneComboBox = QComboBox(self.searchTab)
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.addItem("")
        self.gerneComboBox.setObjectName(u"gerneComboBox")
        self.gerneComboBox.setGeometry(QRect(700, 64, 91, 21))
        self.searchList = QTableWidget(self.searchTab)
        self.searchList.setObjectName(u"searchList")
        self.searchList.setGeometry(QRect(11, 94, 1081, 631))
        self.enableSearchBoxRBtn = QRadioButton(self.searchTab)
        self.setTop20RbtnGroup.addButton(self.enableSearchBoxRBtn)
        self.enableSearchBoxRBtn.setObjectName(u"enableSearchBoxRBtn")
        self.enableSearchBoxRBtn.setGeometry(QRect(11, 24, 71, 19))
        self.label = QLabel(self.searchTab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(817, 63, 271, 21))
        self.tabWidget.addTab(self.searchTab, "")
        self.downloadTab = QWidget()
        self.downloadTab.setObjectName(u"downloadTab")
        self.downloadBox = QLineEdit(self.downloadTab)
        self.downloadBox.setObjectName(u"downloadBox")
        self.downloadBox.setFont(font)
        self.downloadBox.setGeometry(QRect(22, 10, 951, 31))
        self.epiSearchBtn = QPushButton(self.downloadTab)
        self.epiSearchBtn.setObjectName(u"epiSearchBtn")
        self.epiSearchBtn.setGeometry(QRect(982, 9, 101, 31))
        self.downloadList = QListWidget(self.downloadTab)
        self.downloadList.setObjectName(u"downloadList")
        self.downloadList.setGeometry(QRect(22, 90, 331, 621))
        self.epiListLabel = QLabel(self.downloadTab)
        self.epiListLabel.setObjectName(u"epiListLabel")
        self.epiListLabel.setGeometry(QRect(21, 64, 91, 20))
        self.downloadLogLabel = QLabel(self.downloadTab)
        self.downloadLogLabel.setObjectName(u"downloadLogLabel")
        self.downloadLogLabel.setGeometry(QRect(480, 64, 101, 20))
        self.downloadBtn = QPushButton(self.downloadTab)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setGeometry(QRect(360, 370, 111, 51))
        self.downloadLog = QTableView(self.downloadTab)
        self.downloadLog.setObjectName(u"downloadLog")
        self.downloadLog.setGeometry(QRect(480, 90, 601, 591))
        self.checkAllBox = QCheckBox(self.downloadTab)
        self.checkAllBox.setObjectName(u"checkAllBox")
        self.checkAllBox.setGeometry(QRect(261, 64, 91, 19))
        self.downloadStatusBar = QProgressBar(self.downloadTab)
        self.downloadStatusBar.setObjectName(u"downloadStatusBar")
        self.downloadStatusBar.setGeometry(QRect(480, 690, 611, 23))
        self.downloadStatusBar.setValue(0)
        self.tabWidget.addTab(self.downloadTab, "")
        self.setConfigTab = QWidget()
        self.setConfigTab.setObjectName(u"setConfigTab")
        self.dirLabel = QLabel(self.setConfigTab)
        self.dirLabel.setObjectName(u"dirLabel")
        self.dirLabel.setGeometry(QRect(42, 105, 181, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.dirLabel.setFont(font1)
        self.downloadDirLoction = QLineEdit(self.setConfigTab)
        self.downloadDirLoction.setObjectName(u"downloadDirLoction")
        self.downloadDirLoction.setGeometry(QRect(230, 110, 651, 31))
        self.authorLabel = QLabel(self.setConfigTab)
        self.authorLabel.setObjectName(u"authorLabel")
        self.authorLabel.setGeometry(QRect(30, 470, 121, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.authorLabel.setFont(font2)
        self.authorLabel_2 = QLabel(self.setConfigTab)
        self.authorLabel_2.setObjectName(u"authorLabel_2")
        self.authorLabel_2.setGeometry(QRect(30, 520, 631, 41))
        self.authorLabel_2.setFont(font2)
        self.authorLabel_3 = QLabel(self.setConfigTab)
        self.authorLabel_3.setObjectName(u"authorLabel_3")
        self.authorLabel_3.setGeometry(QRect(30, 570, 421, 41))
        self.authorLabel_3.setFont(font2)
        self.authorLabel_4 = QLabel(self.setConfigTab)
        self.authorLabel_4.setObjectName(u"authorLabel_4")
        self.authorLabel_4.setGeometry(QRect(30, 620, 341, 41))
        self.authorLabel_4.setFont(font2)
        self.chooseDirBtn = QPushButton(self.setConfigTab)
        self.chooseDirBtn.setObjectName(u"chooseDirBtn")
        self.chooseDirBtn.setGeometry(QRect(900, 110, 93, 31))
        self.fileextLabel = QLabel(self.setConfigTab)
        self.fileextLabel.setObjectName(u"fileextLabel")
        self.fileextLabel.setGeometry(QRect(43, 160, 181, 41))
        self.fileextLabel.setFont(font1)
        self.fileExt = QLineEdit(self.setConfigTab)
        self.fileExt.setObjectName(u"fileExt")
        self.fileExt.setGeometry(QRect(230, 164, 651, 31))
        self.tabWidget.addTab(self.setConfigTab, "")
        self.ani24Addr = QLabel(self.centralwidget)
        self.ani24Addr.setObjectName(u"ani24Addr")
        self.ani24Addr.setGeometry(QRect(330, 10, 201, 16))
        self.yaani24Addr = QLabel(self.centralwidget)
        self.yaani24Addr.setObjectName(u"yaani24Addr")
        self.yaani24Addr.setGeometry(QRect(550, 10, 201, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        self.searchBtn.clicked.connect(self.onClickedSearchBtn)

        self.enableSearchBoxRBtn.setChecked(True)
        self.setSiteAni24rBtn.setChecked(True)

        self.enableSearchBoxRBtn.toggled.connect(self.setSearchWithKeyWord)
        self.newTop20rBtn.toggled.connect(self.setSearchWithNewTop20)
        self.genreTop20rBtn.toggled.connect(self.setSearchWithGerneTop20)
        self.quarterTop20rBtn.toggled.connect(self.setSearchWithQuarterTop20)
        self.yearTop20rBtn.toggled.connect(self.setSearchWithYearTop20)

        self.setSiteAni24rBtn.toggled.connect(self.setSiteSettings)
        self.setSiteYaAni24rBtn.toggled.connect(self.setSiteSettings)

        self.checkAllBox.stateChanged.connect(self.checkAllList)
        self.epiSearchBtn.clicked.connect(self.setEpisodeItem)


        self.downloadBtn.clicked.connect(self.onClickedDownloadBtn)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.setSiteAni24rBtn.setText(QCoreApplication.translate("MainWindow", u"Ani24", None))
        self.setSiteYaAni24rBtn.setText(QCoreApplication.translate("MainWindow", u"YaAni24", None))
        self.newTop20rBtn.setText(QCoreApplication.translate("MainWindow", u"\uc2e0\uc791 Top20", None))
        self.genreTop20rBtn.setText(QCoreApplication.translate("MainWindow", u"\uc7a5\ub974 Top20", None))
        self.quarterTop20rBtn.setText(QCoreApplication.translate("MainWindow", u"\ubd84\uae30 Top20", None))
        self.yearTop20rBtn.setText(QCoreApplication.translate("MainWindow", u"\uc62c\ud574 Top20", None))
        self.yearLabel.setText(QCoreApplication.translate("MainWindow", u"\uc5f0\ub3c4", None))
        self.quarterLabel.setText(QCoreApplication.translate("MainWindow", u"\ubd84\uae30", None))
        self.gerneLabel.setText(QCoreApplication.translate("MainWindow", u"\uc7a5\ub974", None))
        self.gerneComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc561\uc158", None))
        self.gerneComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\ub85c\ub9e8\uc2a4", None))
        self.gerneComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\ub4dc\ub77c\ub9c8", None))
        self.gerneComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\ud310\ud0c0\uc9c0", None))
        self.gerneComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\uba3c\uce58\ud0a8", None))
        self.gerneComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\uba58\ubd95", None))
        self.gerneComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\uacf5\ud3ec", None))
        self.gerneComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\ub2a5\ub825", None))
        self.gerneComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"\ucf54\ubbf8\ub514", None))
        self.gerneComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"\ud559\uc6d0", None))
        self.gerneComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"\ud558\ub818", None))
        self.gerneComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"BL", None))
        self.gerneComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"\ubd80\ud65c\ub3d9", None))
        self.gerneComboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"\ub9c8\ubc95", None))
        self.gerneComboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"SF", None))
        self.gerneComboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"\uc804\uc7c1", None))
        self.gerneComboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"\uad70", None))
        self.gerneComboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"\uba54\uce74\ub2c9", None))
        self.gerneComboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"\ud1f4\ub9c8", None))
        self.gerneComboBox.setItemText(19, QCoreApplication.translate("MainWindow", u"\uc720\ub839", None))
        self.gerneComboBox.setItemText(20, QCoreApplication.translate("MainWindow", u"\uadc0\uc2e0", None))
        self.gerneComboBox.setItemText(21, QCoreApplication.translate("MainWindow", u"\uc694\uad34", None))
        self.gerneComboBox.setItemText(22, QCoreApplication.translate("MainWindow", u"\uc774\uc138\uacc4", None))
        self.gerneComboBox.setItemText(23, QCoreApplication.translate("MainWindow", u"\uc5ec\ub3d9\uc0dd", None))
        self.gerneComboBox.setItemText(24, QCoreApplication.translate("MainWindow", u"\ubbf8\uc2a4\ud14c\ub9ac", None))
        self.gerneComboBox.setItemText(25, QCoreApplication.translate("MainWindow", u"\uc2a4\ud3ec\uce20", None))
        self.gerneComboBox.setItemText(26, QCoreApplication.translate("MainWindow", u"\ubc94\uc8c4", None))
        self.gerneComboBox.setItemText(27, QCoreApplication.translate("MainWindow", u"\uc815\ub839", None))
        self.gerneComboBox.setItemText(28, QCoreApplication.translate("MainWindow", u"\ubc40\ud30c\uc774\uc5b4", None))
        self.gerneComboBox.setItemText(29, QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub3cc", None))

        self.enableSearchBoxRBtn.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uc5b4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"* \uc124\uc815 \ud6c4 \uac80\uc0c9 \ubc84\ud2bc\uc744 \uaf2d \ub20c\ub7ec\uc8fc\uc138\uc694. *", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchTab), QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\ud558\uae30", None))
        self.epiSearchBtn.setText(QCoreApplication.translate("MainWindow", u"\ud69f\ucc28 \uac80\uc0c9", None))
        self.epiListLabel.setText(QCoreApplication.translate("MainWindow", u"\ud69f\ucc28 \ub9ac\uc2a4\ud2b8", None))
        self.downloadLogLabel.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc6b4\ub85c\ub4dc \ub85c\uadf8", None))
        self.downloadBtn.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc6b4\ub85c\ub4dc", None))
        self.checkAllBox.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4 \uc120\ud0dd", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.downloadTab), QCoreApplication.translate("MainWindow", u"\ub2e4\uc6b4\ub85c\ub4dc", None))
        self.dirLabel.setText(QCoreApplication.translate("MainWindow", u"\ub3d9\uc601\uc0c1 \ub2e4\uc6b4\ub85c\ub4dc \ud3f4\ub354", None))
        self.downloadDirLoction.setText(QCoreApplication.translate("MainWindow", u"./", None))
        self.authorLabel.setText(QCoreApplication.translate("MainWindow", u"\uc81c\uc791\uc790: kdr", None))
        self.authorLabel_2.setText(QCoreApplication.translate("MainWindow", u"Github: https://github.com/kdrkdrkdr", None))
        self.authorLabel_3.setText(QCoreApplication.translate("MainWindow", u"Blog: https://blog.naver.com/powerapollon", None))
        self.authorLabel_4.setText(QCoreApplication.translate("MainWindow", u"Email: kdrhacker1234@gmail.com", None))
        self.chooseDirBtn.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc124\uc815", None))
        self.fileextLabel.setText(QCoreApplication.translate("MainWindow", u"\ub3d9\uc601\uc0c1 \ud655\uc7a5\uc790", None))
        self.fileExt.setText(QCoreApplication.translate("MainWindow", u"mp4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setConfigTab), QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.ani24Addr.setText(QCoreApplication.translate("MainWindow", u"Ani24: https://ani24do.com", None))
        self.yaani24Addr.setText(QCoreApplication.translate("MainWindow", u"YaAni24: https://yaani24.net", None))
    # retranslateUi


    def setBaseURL(self):
        if self.setSiteAni24rBtn.isChecked():
            return self.ani24URL

        else:
            return self.yaani24URL



    def setSiteSettings(self):
        baseURL = self.setBaseURL()

        self.gerneComboBox.clear()
        self.producerComboBox.clear()

        if baseURL == self.ani24URL:
            gerneList = ['로맨스', '드라마', '판타지', '먼치킨', '멘붕', '공포', '공포', '능력', '코미디', '학원', '하렘', 'BL', '부활동', '마법', 'SF', '전쟁', 
                 '군', '메카닉', '액션', '퇴마', '유령', '귀신', '요괴', '이세계', '여동생', '미스테리', '스포츠', '범죄', '정령', '뱀파이어', '아이돌']



        else:
            gerneList = [
                '선생님', '서큐버스', '간호사', '메이드', '레이프', '선생님', '근친', '엘프', '촉수', '여동생,오빠','누나,남동생', '후타나리', '갸루', 
                '아가씨', '공주', '최면', '지하철', '엄마', '유부녀', '시간정지', '투명인간', '살인', '아이돌', '백합', '노모', '회사원', '외계인', '아나운서'
            ]



        for g in gerneList: 
            self.gerneComboBox.addItem(g)



    def getSoup(self, url):
        s.acquire()
        req = get(url, headers={'user-agent':'Mozilla 5.0', 'referer':url})
        html = req.text
        s.release()
        return BeautifulSoup(html, 'html.parser')



    def setSearchTableWidget(self, data):
        baseURL = self.setBaseURL()

        horizonHeader = self.searchList.horizontalHeader()
        horizonHeader.setSectionResizeMode(QHeaderView.ResizeToContents)
        verticalHeader = self.searchList.verticalHeader()
        verticalHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.searchList.setColumnCount(3)
        self.searchList.setRowCount(len(data))

        self.searchList.setHorizontalHeaderLabels(['제목', '장르', '애니 링크'])

        for dataIdx, dataContent in enumerate(data):
            for i, c in enumerate(dataContent):
                self.searchList.setItem(dataIdx, i, QTableWidgetItem(c))



    def onClickedSearchBtn(self):

        baseURL = self.setBaseURL()
        data = []


        if self.enableSearchBoxRBtn.isChecked():
            url = f"{baseURL}/ani/search.php?query=" + quote_plus(self.aniSearchBox.text())
            soup = self.getSoup(url)

            infoBox = soup.find('div', {'class':'ani_search_list_box'}).find_all('div', {'class':'ani_search_info_box'})
                
            for i in infoBox:
                aniTitle = i.find('a', {'class':'subject'})['title']
                aniGerne = i.find('div', {'class':'genre'})['title']
                aniLink = baseURL + i.find('a', {'class':'thumbnail'})['href']
                data.append([aniTitle, aniGerne, aniLink])



        elif self.newTop20rBtn.isChecked():
            url = f"{baseURL}/ani/top10.html"
            soup = self.getSoup(url)

            infoBox = soup.find('div', {'class':'ani_list_top_center'}).find_all('a', {'class':'top_info'})
            
            for i in infoBox:
                aniTitle = i.find('div', {'class':'subject'}).text
                aniGerne = i.find('div', {'class':'genre'}).text
                aniLink = baseURL + i['href']
                data.append([aniTitle, aniGerne, aniLink])
            


        elif self.genreTop20rBtn.isChecked():
            url = f"{baseURL}/ani/top10.html?type=genre&genre={quote_plus(self.gerneComboBox.currentText())}"
            soup = self.getSoup(url)

            infoBox = soup.find('div', {'class':'ani_list_top_center'}).find_all('a', {'class':'top_info'})
            
            for i in infoBox:
                aniTitle = i.find('div', {'class':'subject'}).text
                aniGerne = i.find('div', {'class':'genre'}).text
                aniLink = baseURL + i['href']
                data.append([aniTitle, aniGerne, aniLink])



        elif self.quarterTop20rBtn.isChecked():
            url = f"{baseURL}/ani/top10.html?type=quarter&year={self.yearSpinBox.text()}&quarter={self.quarterSpinBox.text()}"
            soup = self.getSoup(url)

            infoBox = soup.find('div', {'class':'ani_list_top_center'}).find_all('a', {'class':'top_info'})
            
            for i in infoBox:
                aniTitle = i.find('div', {'class':'subject'}).text
                aniGerne = i.find('div', {'class':'genre'}).text
                aniLink = baseURL + i['href']
                data.append([aniTitle, aniGerne, aniLink])



        elif self.yearTop20rBtn.isChecked():
            url = f"{baseURL}/ani/top10.html?type=year&year={self.yearSpinBox.text()}"
            soup = self.getSoup(url)

            infoBox = soup.find('div', {'class':'ani_list_top_center'}).find_all('a', {'class':'top_info'})
            
            for i in infoBox:
                aniTitle = i.find('div', {'class':'subject'}).text
                aniGerne = i.find('div', {'class':'genre'}).text
                aniLink = baseURL + i['href']
                data.append([aniTitle, aniGerne, aniLink])



        else:
            print("버튼 오류라구??")


        self.setSearchTableWidget(data)
        self.searchList.setEditTriggers(QAbstractItemView.NoEditTriggers)
    

    def setSearchWithKeyWord(self):
        self.aniSearchBox.setDisabled(False)
        self.yearSpinBox.setDisabled(True)
        self.quarterSpinBox.setDisabled(True)
        self.gerneComboBox.setDisabled(True)



    def setSearchWithNewTop20(self):
        self.aniSearchBox.setDisabled(True)
        self.yearSpinBox.setDisabled(True)
        self.quarterSpinBox.setDisabled(True)
        self.gerneComboBox.setDisabled(True)



    def setSearchWithGerneTop20(self):
        self.aniSearchBox.setDisabled(True)
        self.yearSpinBox.setDisabled(True)
        self.quarterSpinBox.setDisabled(True)
        self.gerneComboBox.setDisabled(False)



    def setSearchWithQuarterTop20(self):
        self.aniSearchBox.setDisabled(True)
        self.yearSpinBox.setDisabled(False)
        self.quarterSpinBox.setDisabled(False)
        self.gerneComboBox.setDisabled(True)



    def setSearchWithYearTop20(self):
        self.aniSearchBox.setDisabled(True)
        self.yearSpinBox.setDisabled(False)
        self.quarterSpinBox.setDisabled(True)
        self.gerneComboBox.setDisabled(True)

    # ========================================================================#

    def getTitleAndLink(self, aniURL):
        soup = self.getSoup(aniURL)
        infoDict = {}

        baseURL = urlparse(self.downloadBox.text()).netloc
        inputBaseURL = self.yaani24URL if ('yaani24' in baseURL) else self.ani24URL

        aniVideoList = soup.find('div', {'class':'ani_video_list'}).find_all('a')
        for a in aniVideoList:
            epiSubject = a.find('div', {'class':'subject'}).text
            epiLink = inputBaseURL + a['href']
            infoDict[epiSubject] = epiLink

        return infoDict




    def setEpisodeItem(self):
        self.downloadList.clear()

        aniInfoURL = self.downloadBox.text()
        info = self.getTitleAndLink(aniInfoURL)

        for k, v in info.items():
            item = QListWidgetItem()
            item.setText(k)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.downloadList.addItem(item)



    def getCheckedList(self):
        checkItemsIndex = []
        
        for index in range(self.downloadList.count()):
            if self.downloadList.item(index).checkState() == Qt.Checked:
                checkItemsIndex.append(index)

        return checkItemsIndex




    def checkAllList(self):
        for index in range(self.downloadList.count()):
            if self.checkAllBox.isChecked():
                self.downloadList.item(index).setCheckState(Qt.Checked)
            
            else:
                self.downloadList.item(index).setCheckState(Qt.Unchecked)






    def onClickedDownloadBtn(self):
        aniURL = self.downloadBox.text()
        getDownloadInfo = self.getTitleAndLink(aniURL)

        baseURL = urlparse(self.downloadBox.text()).netloc
        inputBaseURL = self.yaani24URL if ('yaani24' in baseURL) else self.ani24URL
        
        idxList = self.getCheckedList()
        
        for info in enumerate(getDownloadInfo):
            if info[0] in idxList:

                aniLink = getDownloadInfo[info[1]]
                print(aniLink)

                if inputBaseURL == self.ani24URL:
                    aniVideoLink = 'http://test.ani24image.com/ani/download.php?id=' + sub('[\D]', '', aniLink.split('ani_view/')[1])

                # https://ani24do.com/ani_view/3315.html
                else:
                    aniVideoLink = self.getSoup(aniLink).find('video', {'id':'video'})['src']
                    
                thr = downloadThreads(self, info[1], aniVideoLink)
                thr.start()
                TimerMessageBox(99999, contents="다운로드중").exec_()
                thr.join()

                msgbox.close()

            

# downloadThreads(self)
class downloadThreads(Thread):
    def __init__(self, window, filename, fileurl, parent=None):
        super().__init__()
        self.window = window
        self.filename = filename
        self.fileurl = fileurl

    def setHookProgress(self, p):
        s.acquire()

        status = p['status']
        if status == 'finished':
            self.window.downloadStatusBar.setValue(55)

        if status == 'downloading':
            percent = p['_percent_str'].replace('%', '')
            self.window.downloadStatusBar.setValue(int(percent))

        s.release()


    def run(self):
        s.acquire()

        downloadOptions = {
            'outtmpl': self.filename,
            'progress_hooks': [self.setHookProgress],
            # 'external_downloader':'./aria2c.exe',
            # 'external_downloader_args':'-x 8 -s 16 -k 1M',
            'verbose':True,
        }
        try:
            with DownloadFile(downloadOptions) as d:
                d.download([self.fileurl])

        except:
            TimerMessageBox(3, contents="에러발생!!").exec_()

        s.release()



if __name__ == "__main__": 
    import sys 
    app = QApplication(sys.argv) 
    form = QMainWindow() 
    ui = Ui_MainWindow() 
    ui.setupUi(form) 
    form.show() 
    sys.exit(app.exec_()) 
