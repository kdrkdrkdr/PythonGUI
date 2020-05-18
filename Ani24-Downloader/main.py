from ani24ui import *

from os.path import isfile

from os import listdir

from threading import Thread, Semaphore

from requests import Session

from bs4 import BeautifulSoup

from urllib.parse import quote_plus, urlparse

from os import system, mkdir

from os.path import isfile, isdir, getsize

from shutil import rmtree, move

import codecs

import sys

import ctypes

from re import sub

from datetime import datetime




s = Semaphore(5)


class thrSearchAni(Thread):

    def __init__(self, window):
        super().__init__()
        self.window = window


    def run(self):
        s.acquire()
        baseURL = self.window.setBaseURL()
        data = []

        currentYear = self.window.yearComboBox.currentText().replace('년', '')
        currentQuarter = self.window.quarterComboBox.currentText().replace('분기', '')
        currentGenre = quote_plus('' if '장르' in self.window.gerneComboBox.currentText() else self.window.gerneComboBox.currentText())
        currentProducer = quote_plus('' if '제작사' in self.window.producerComboBox.currentText() else self.window.producerComboBox.currentText())

        if self.window.searchKeyWordRBtn.isChecked():
            url = f"{baseURL}/ani/search.php?query=" + quote_plus(self.window.aniSearchBox.text()).replace('%0A', '')
            soup = self.window.getSoup(url)
            infoBox = soup.find('div', {'class':'ani_search_list_box'}).find_all('div', {'class':'ani_search_info_box'})
                
            for i in infoBox:
                aniTitle = i.find('a', {'class':'subject'})['title']
                aniGerne = i.find('div', {'class':'genre'})['title']
                aniLink = baseURL + i.find('a', {'class':'thumbnail'})['href']
                data.append([aniTitle, aniGerne, aniLink])


        elif self.window.newTop20rBtn.isChecked():
            url = f"{baseURL}/ani/top10.html".replace('%0A', '')
            soup = self.window.getSoup(url)
            infoBox = soup.find('div', {'class':'ani_list_top_center'}).find_all('a', {'class':'top_info'})
            
            for i in infoBox:
                aniTitle = i.find('div', {'class':'subject'}).text
                aniGerne = i.find('div', {'class':'genre'}).text
                aniLink = baseURL + i['href']
                data.append([aniTitle, aniGerne, aniLink])


        elif self.window.genreTop20rBtn.isChecked():
            url = f"{baseURL}/ani/top10.html?type=genre&genre={currentGenre}".replace('%0A', '')
            soup = self.window.getSoup(url)
            infoBox = soup.find('div', {'class':'ani_list_top_center'}).find_all('a', {'class':'top_info'})

            for i in infoBox:
                aniTitle = i.find('div', {'class':'subject'}).text
                aniGerne = i.find('div', {'class':'genre'}).text
                aniLink = baseURL + i['href']
                data.append([aniTitle, aniGerne, aniLink])


        elif self.window.quarterTop20rBtn.isChecked():
            url = f"{baseURL}/ani/top10.html?type=quarter&year={currentYear}&quarter={currentQuarter}".replace('%0A', '')
            soup = self.window.getSoup(url)
            infoBox = soup.find('div', {'class':'ani_list_top_center'}).find_all('a', {'class':'top_info'})
            
            for i in infoBox:
                aniTitle = i.find('div', {'class':'subject'}).text
                aniGerne = i.find('div', {'class':'genre'}).text
                aniLink = baseURL + i['href']
                data.append([aniTitle, aniGerne, aniLink])


        elif self.window.yearTop20rBtn.isChecked():
            url = f"{baseURL}/ani/top10.html?type=year&year={currentYear}".replace('%0A', '')
            soup = self.window.getSoup(url)
            infoBox = soup.find('div', {'class':'ani_list_top_center'}).find_all('a', {'class':'top_info'})
            
            for i in infoBox:
                aniTitle = i.find('div', {'class':'subject'}).text
                aniGerne = i.find('div', {'class':'genre'}).text
                aniLink = baseURL + i['href']
                data.append([aniTitle, aniGerne, aniLink])


        elif self.window.completeRBtn.isChecked():
            if baseURL == self.window.ani24BaseURL:
                url = f'{baseURL}/ani/search.php?type=all&order=new&genre={currentGenre}&producer={currentProducer}'.replace('%0A', '')
                soup = self.window.getSoup(url)
                infoBox = soup.find('div', {'class':'ani_search_list_box'}).find_all('div', {'class':'ani_search_info_box'})
                
                for i in infoBox:
                    aniTitle = i.find('a', {'class':'subject'})['title']
                    aniGerne = i.find('div', {'class':'genre'})['title']
                    aniLink = baseURL + i.find('a', {'class':'thumbnail'})['href']
                    data.append([aniTitle, aniGerne, aniLink])


        elif self.window.tasteRBtn.isChecked():
            if baseURL == self.window.yaani24BaseURL:
                currentGenre = quote_plus(self.window.gerneComboBox.currentText())
                currentHairStyle = quote_plus(self.window.hairStyleComboBox.currentText())
                currentHairColor = quote_plus(self.window.hairColorComboBox.currentText())
                currentClothes = quote_plus(self.window.clothesComboBox.currentText())
                currentPlayWay = quote_plus(self.window.playWayComboBox.currentText())
                currentType = quote_plus(self.window.typeComboBox.currentText())

                url = f'{baseURL}/ani/search.php?type=all&order=new&head_color={currentHairColor}&head_style={currentHairStyle}&dress={currentClothes}&play={currentPlayWay}&genre={currentGenre}&type={currentType}'.replace('%0A', '')
                soup = self.window.getSoup(url)
                infoBox = soup.find('div', {'class':'ani_search_list_box'}).find_all('div', {'class':'ani_search_info_box'})
                    
                for i in infoBox:
                    aniTitle = i.find('a', {'class':'subject'})['title']
                    aniGerne = i.find('div', {'class':'genre'})['title']
                    aniLink = baseURL + i.find('a', {'class':'thumbnail'})['href']
                    data.append([aniTitle, aniGerne, aniLink])

                
        else:
            print("ERROR")

        self.window.setSearchTableWidget(data)

        s.release()







class thrSetEpiItem(Thread):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def run(self):
        s.acquire()

        self.window.aniEpiList.clear()

        aniInfoURL = self.window.aniEpiLinkBox.text()

        info = self.window.getTitleAndLink(aniInfoURL)

        for k, v in info.items():
            item = QListWidgetItem()
            item.setText(k)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.window.aniEpiList.addItem(item)
    

        s.release()








class thrDownload(Thread):

    def __init__(self, window):
        super().__init__()
        self.window = window


    def run(self):
        s.acquire()

        aniURL = self.window.aniEpiLinkBox.text()
        getDownloadInfo = self.window.getTitleAndLink(aniURL)

        baseURL = urlparse(self.window.aniEpiLinkBox.text()).netloc
        inputBaseURL = self.window.yaani24BaseURL if ('yaani24' in baseURL) else self.window.ani24BaseURL
        
        idxList = self.window.getCheckedList()

        finalDirectory = f'.\\애니_다운로드_리스트\\{self.window.getBigTitle(aniURL)}\\'

        threads = []
        for info in enumerate(getDownloadInfo):

            if info[0] in idxList:
                aniLink = getDownloadInfo[info[1]]

                videoInfo = self.window.getVideoInfo(inputBaseURL, aniLink)

                aria = Aria2cDownload(
                    output=f'{videoInfo[0]}.mp4',
                    directory=finalDirectory,
                    fileurl=videoInfo[1],
                    window=self.window,
                    total=len(idxList)
                )
                threads.append(aria)
                

        for thr in threads:
            thr.start()

        for thr in threads:
            thr.join()

        system(f'explorer {finalDirectory}')

        s.release()






class Aria2cDownload(Thread):

    def __init__(self, output, directory, fileurl, window, total):
        super().__init__()
        self.output = output
        self.directory = directory
        self.fileurl = fileurl
        self.window = window
        self.total = total
        

        self.ariaLocation = '.\\utils\\aria2c.exe '
        self.ariaCommandArgs = ' '.join(
            [   
                '--out={}'.format(self.output),
                
                '--dir=.\\temp',
                
                '--file-allocation=none',

                '--check-certificate=false',
                
                '--max-connection-per-server=16',
                
                '--split=128',
                
                '--min-split-size=1M',

                '--user-agent="Mozilla 5.0"',

                # '--referer="{}"'.format(self.fileurl),

                '{}'.format(self.fileurl)
            ]
        )

    
    def run(self):
        s.acquire()

        try:
            mkdir(self.directory)
        except ( FileExistsError ):
            pass
        

        system(self.ariaLocation + self.ariaCommandArgs)
        move(f'.\\temp\\{self.output}', f'{self.directory}\\{self.output}')

        self.window.downloadProgressBar.setValue(100 * int(len(listdir(self.directory)) / self.total))


        s.release()







class Ani24(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ani24BaseURL = 'https://ani24do.com'
        self.yaani24BaseURL = 'https://yaani24.net'

        self.setWindowTitle('애니24 다운로더')

        self.searchKeyWordRBtn.toggled.connect(self.setSearchWithKeyWord)
        self.newTop20rBtn.toggled.connect(self.setSearchWithNewTop20)
        self.genreTop20rBtn.toggled.connect(self.setSearchWithGerneTop20)
        self.quarterTop20rBtn.toggled.connect(self.setSearchWithQuarterTop20)
        self.yearTop20rBtn.toggled.connect(self.setSearchWithYearTop20)
        self.completeRBtn.toggled.connect(self.setSearchWithCompleted)
        self.tasteRBtn.toggled.connect(self.setSearchWithTaste)

        self.aniSearchBtn.clicked.connect(self.onClickedSearchBtn)
        self.aniEpiSearchBtn.clicked.connect(self.setEpisodeItem)
        self.aniDownloadBtn.clicked.connect(self.onClickedDownloadBtn)


        self.setSiteAni24rBtn.toggled.connect(self.setSiteSettings)
        self.setSiteYaAni24rBtn.toggled.connect(self.setSiteSettings)

        self.checkAllBox.stateChanged.connect(self.checkAllList)

        self.loadNewInfo.clicked.connect(self.checkInfoFiles)

        self.show()


    def loadCurrentTime(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S")



    def setBaseURL(self):
        if self.setSiteAni24rBtn.isChecked():
            return self.ani24BaseURL

        else:
            return self.yaani24BaseURL





    def openInfoFile(self, filename):
        f = codecs.open(filename, 'r', encoding='utf-8')
        c = f.readlines()
        f.close()
        return c




    def makeInfoFiles(self, filename, content=[]):
        content = '\n'.join([c.replace('\n', '') for c in content])
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)




    def checkInfoFiles(self):
        ani24InfoFiles = [
            'ani24_genre.txt', 'ani24_producer.txt', 'ani24_year.txt', 'ani24_quarter.txt'
        ]

        yaani24InfoFiles = [
            'yaani24_type.txt', 'yaani24_gerne.txt', 'yaani24_year.txt', 'yaani24_quarter.txt', 
            'yaani24_playway.txt', 'yaani24_clothes.txt', 'yaani24_hairstyle.txt', 'yaani24_haircolor.txt'
        ]

        s = Session()
        s.headers = {
            'user-agent':'Mozilla 5.0',
            'referer':'https://ani24do.com'
        }
        
        r1 = s.get('https://ani24do.com/ani/search.php?type=all').text
        s1 = BeautifulSoup(r1, 'html.parser').find_all('select')
        
        a24P = [p.text for p in s1[0].find_all('option')[1:]]
        a24G = [g.text for g in s1[1].find_all('option')[1:]]

        r2 = s.get('https://ani24do.com/ani/top10.html?type=quarter').text
        s2 = BeautifulSoup(r2, 'html.parser').find_all('select')

        a24Q = [q.text for q in s2[0].find_all('option')]
        a24Y = [y.text for y in s2[1].find_all('option')]


        r3 = s.get('https://yaani24.net/ani/search.php?type=all').text
        s3 = BeautifulSoup(r3, 'html.parser').find_all('select')

        ya24T = [g.text for g in s3[0].find_all('option')]
        ya24G = [g.text for g in s3[1].find_all('option')]
        ya24hC = [hC.text for hC in s3[2].find_all('option')]
        ya24hS = [hS.text for hS in s3[3].find_all('option')]
        ya24C = [c.text for c in s3[4].find_all('option')]
        ya24p = [p.text for p in s3[5].find_all('option')]


        r4 = s.get('https://yaani24.net/ani/top10.html?type=quarter').text
        s4 = BeautifulSoup(r4, 'html.parser').find_all('select')

        ya24Q = [q.text for q in s4[0].find_all('option')]
        ya24Y = [g.text for g in s4[1].find_all('option')]



        ani24Info = [a24G, a24P, a24Y, a24Q]
        yaani24Info = [ya24T, ya24G, ya24Y, ya24Q, ya24p, ya24C, ya24hS, ya24hC]

        for idx, a in enumerate(ani24Info):
            self.makeInfoFiles(f'./info/{ani24InfoFiles[idx]}', a)


        for idx, y in enumerate(yaani24Info):
            self.makeInfoFiles(f'./info/{yaani24InfoFiles[idx]}', y)

        msg = QMessageBox()
        msg.about(self, "애니24 다운로더", "새 정보를 불러왔습니다.")





    def setSiteSettings(self):
        baseURL = self.setBaseURL()

        self.gerneComboBox.clear()
        self.producerComboBox.clear()
        self.yearComboBox.clear()
        self.quarterComboBox.clear()
        self.playWayComboBox.clear()
        self.clothesComboBox.clear()
        self.hairStyleComboBox.clear()
        self.hairColorComboBox.clear()

        try:
            if baseURL == self.ani24BaseURL:
                yearList = self.openInfoFile('./info/ani24_year.txt')
                quarterList = self.openInfoFile('./info/ani24_quarter.txt')
                gerneList = self.openInfoFile('./info/ani24_genre.txt')
                producerList = self.openInfoFile('./info/ani24_producer.txt')

                for g in gerneList: self.gerneComboBox.addItem(g)
                for y in yearList: self.yearComboBox.addItem(y)
                for q in quarterList: self.quarterComboBox.addItem(q)
                for p in producerList: self.producerComboBox.addItem(p)

                self.completeRBtn.setDisabled(False)
                self.tasteRBtn.setDisabled(True)


            else:
                yearList = self.openInfoFile('./info/yaani24_year.txt')
                quarterList = self.openInfoFile('./info/yaani24_quarter.txt')
                gerneList = self.openInfoFile('./info/yaani24_gerne.txt')
                playWayList = self.openInfoFile('./info/yaani24_playway.txt')
                clothesList = self.openInfoFile('./info/yaani24_clothes.txt')
                hairStyleList = self.openInfoFile('./info/yaani24_hairstyle.txt')
                hairColorList = self.openInfoFile('./info/yaani24_haircolor.txt')
                typeList = self.openInfoFile('./info/yaani24_type.txt')

                
                for g in gerneList: self.gerneComboBox.addItem(g)
                for y in yearList: self.yearComboBox.addItem(y)
                for q in quarterList: self.quarterComboBox.addItem(q)
                for p in playWayList: self.playWayComboBox.addItem(p)
                for c in clothesList: self.clothesComboBox.addItem(c)
                for hS in hairStyleList: self.hairStyleComboBox.addItem(hS)
                for hC in hairColorList: self.hairColorComboBox.addItem(hC)
                for t in typeList: self.typeComboBox.addItem(t)

                self.completeRBtn.setDisabled(True)
                self.tasteRBtn.setDisabled(False)

        except:
            error = QMessageBox()
            error.about(self, "파일 로드 에러", "설정 및 도움말 탭에서 새 정보를 로드하세요.")   



    def setSearchWithKeyWord(self):
        self.aniSearchBox.setDisabled(False)
        self.gerneComboBox.setDisabled(True)
        self.producerComboBox.setDisabled(True)
        self.yearComboBox.setDisabled(True)
        self.quarterComboBox.setDisabled(True)
        self.playWayComboBox.setDisabled(True)
        self.clothesComboBox.setDisabled(True)
        self.hairStyleComboBox.setDisabled(True)
        self.hairColorComboBox.setDisabled(True)
        self.typeComboBox.setDisabled(True)


    def setSearchWithNewTop20(self):
        self.aniSearchBox.setDisabled(True)
        self.gerneComboBox.setDisabled(True)
        self.producerComboBox.setDisabled(True)
        self.yearComboBox.setDisabled(True)
        self.quarterComboBox.setDisabled(True)
        self.playWayComboBox.setDisabled(True)
        self.clothesComboBox.setDisabled(True)
        self.hairStyleComboBox.setDisabled(True)
        self.hairColorComboBox.setDisabled(True)
        self.typeComboBox.setDisabled(True)


    def setSearchWithGerneTop20(self):
        self.aniSearchBox.setDisabled(True)
        self.gerneComboBox.setDisabled(False)
        self.producerComboBox.setDisabled(True)
        self.yearComboBox.setDisabled(True)
        self.quarterComboBox.setDisabled(True)
        self.playWayComboBox.setDisabled(True)
        self.clothesComboBox.setDisabled(True)
        self.hairStyleComboBox.setDisabled(True)
        self.hairColorComboBox.setDisabled(True)
        self.typeComboBox.setDisabled(True)


    def setSearchWithQuarterTop20(self):
        self.aniSearchBox.setDisabled(True)
        self.gerneComboBox.setDisabled(True)
        self.producerComboBox.setDisabled(True)
        self.yearComboBox.setDisabled(False)
        self.quarterComboBox.setDisabled(False)
        self.playWayComboBox.setDisabled(True)
        self.clothesComboBox.setDisabled(True)
        self.hairStyleComboBox.setDisabled(True)
        self.hairColorComboBox.setDisabled(True)
        self.typeComboBox.setDisabled(True)


    def setSearchWithYearTop20(self):
        self.aniSearchBox.setDisabled(True)
        self.gerneComboBox.setDisabled(True)
        self.producerComboBox.setDisabled(True)
        self.yearComboBox.setDisabled(False)
        self.quarterComboBox.setDisabled(True)
        self.playWayComboBox.setDisabled(True)
        self.clothesComboBox.setDisabled(True)
        self.hairStyleComboBox.setDisabled(True)
        self.hairColorComboBox.setDisabled(True)
        self.typeComboBox.setDisabled(True)


    def setSearchWithCompleted(self):
        self.aniSearchBox.setDisabled(True)
        self.gerneComboBox.setDisabled(False)
        self.yearComboBox.setDisabled(True)
        self.producerComboBox.setDisabled(False)
        self.quarterComboBox.setDisabled(True)
        self.playWayComboBox.setDisabled(True)
        self.clothesComboBox.setDisabled(True)
        self.hairStyleComboBox.setDisabled(True)
        self.hairColorComboBox.setDisabled(True)
        self.typeComboBox.setDisabled(True)


    def setSearchWithTaste(self):
        self.aniSearchBox.setDisabled(True)
        self.gerneComboBox.setDisabled(False)
        self.producerComboBox.setDisabled(True)
        self.yearComboBox.setDisabled(True)
        self.quarterComboBox.setDisabled(True)
        self.playWayComboBox.setDisabled(False)
        self.clothesComboBox.setDisabled(False)
        self.hairStyleComboBox.setDisabled(False)
        self.hairColorComboBox.setDisabled(False)
        self.typeComboBox.setDisabled(False)



    def setSearchTableWidget(self, data):
        baseURL = self.setBaseURL()

        horizonHeader = self.searchTable.horizontalHeader()
        horizonHeader.setSectionResizeMode(QHeaderView.ResizeToContents)
        verticalHeader = self.searchTable.verticalHeader()
        verticalHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.searchTable.setColumnCount(3)
        self.searchTable.setRowCount(len(data))

        self.searchTable.setHorizontalHeaderLabels(['제목', '장르', '애니 링크'])

        for dataIdx, dataContent in enumerate(data):
            for i, c in enumerate(dataContent):
                self.searchTable.setItem(dataIdx, i, QTableWidgetItem(c))




    def getSoup(self, url, referer=''):
        sess = Session()
        if referer == '':
            referer = self.setBaseURL()

        sess.headers = {
            'user-agent':'Mozilla 5.0',
            'referer':referer,
        }
        req = sess.get(url)
        html = req.text
        return BeautifulSoup(html, 'html.parser')



    def getBigTitle(self, aniURL):
        return self.getSoup(aniURL).find('h1', {'class':'ani_info_title_font_box'}).text



    def getTitleAndLink(self, aniURL):
        
        infoDict = {}

        baseURL = urlparse(self.aniEpiLinkBox.text()).netloc
        inputBaseURL = self.yaani24BaseURL if ('yaani24' in baseURL) else self.ani24BaseURL


        soup = self.getSoup(aniURL, referer=inputBaseURL)
        aniVideoList = soup.find('div', {'class':'ani_video_list'}).find_all('a')
        
        for a in aniVideoList:
            epiSubject = a.find('div', {'class':'subject'}).text
            epiLink = inputBaseURL + a['href']
            infoDict[epiSubject] = epiLink

        return infoDict



    def getCheckedList(self):
        checkItmemsIndex = []

        for idx in range(self.aniEpiList.count()):
            if self.aniEpiList.item(idx).checkState() == Qt.Checked:
                checkItmemsIndex.append(idx)

        return checkItmemsIndex


    
    def checkAllList(self):
        for idx in range(self.aniEpiList.count()):
            if self.checkAllBox.isChecked():
                self.aniEpiList.item(idx).setCheckState(Qt.Checked)
            else:
                self.aniEpiList.item(idx).setCheckState(Qt.Unchecked)




    def getVideoInfo(self, baseURL, aniURL):

        s = Session()
        aniVideoTitle, aniVideoLink = "", ""

        if baseURL == self.ani24BaseURL:
            videoId = sub('[\D]', '', aniURL.split('/ani_view/')[1])
            html = s.get(
                f'https://fileiframe.com/ani_video4/{videoId}.html?player=', 
                headers={'referer':f'https://ani24do.com/ani_view/{videoId}.html'}
            ).text

            soup = BeautifulSoup(html, 'html.parser')
            pb = soup.find('div', {'class':'player_button'})

            aniVideoTitle = self.getSoup(f'https://ani24do.com/ani_view/{videoId}.html').find('div', {'class':'view_info_box'}).div.text
            aniVideoLink = pb.find('button', {'class':'link_button link_video'})['data-link']

        else:
            html = s.get(
                aniURL,
                headers={'referer':aniURL}
            ).text
            soup = BeautifulSoup(html, 'html.parser')

            aniVideoTitle = soup.find('div', {'class':'view_info_box'}).div.text
            aniVideoLink = soup.find('video', {'id':'video'})['src']

        return [aniVideoTitle.replace(' ', '_'), aniVideoLink]
        
        


    def setEpisodeItem(self):
        msg = runmsg()
        thr = thrSetEpiItem(self)
        thr.start()
        thr.join()




    def onClickedSearchBtn(self):
        msg = runmsg()
        thr = thrSearchAni(self)
        thr.start()
        thr.join()




    def onClickedDownloadBtn(self):
        msg = runmsg()
        thr = thrDownload(self)
        thr.start()
        thr.join()



class runmsg:
    def __init__(self):
        self.win = QDialog()
        self.ui = Ui_MessageDialog()
        self.win.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.win.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui.setupUi(self.win)
        self.win.show()




class Ui_MessageDialog(object):
    def setupUi(self, MessageDialog):
        if not MessageDialog.objectName():
            MessageDialog.setObjectName(u"MessageDialog")
        MessageDialog.resize(450, 1)
        MessageDialog.setMaximumSize(QSize(450, 1))

        self.retranslateUi(MessageDialog)

        QMetaObject.connectSlotsByName(MessageDialog)
    # setupUi

    def retranslateUi(self, MessageDialog):
        MessageDialog.setWindowTitle(QCoreApplication.translate("MessageDialog", "작업이 완료될 때 까지 기다려주세요!", None))
    # retranslateUi







def runDivert():
    from pydivert import WinDivert
    with WinDivert("tcp.SrcPort == 443 and tcp.PayloadLength == 0") as w:
            try:
                for packet in w:
                    packet.tcp.rst = False
                    w.send(packet)
            except:
                w.close()



if __name__ == "__main__":
    
    if ctypes.windll.shell32.IsUserAnAdmin():
        runTLS = Thread(target=runDivert)
        runTLS.start()

        app = QApplication(sys.argv)
        ex = Ani24()
        app.exec_()
        sys.exit()


    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
