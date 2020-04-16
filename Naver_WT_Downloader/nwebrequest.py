#-*-coding:utf-8 -*-

from bs4 import BeautifulSoup
from requests import get, exceptions
from img2pdf import convert as pdfConvert
from signal import signal, SIGINT, SIG_IGN
from ping3 import ping
from sys import exit as terminate
from shutil import rmtree
from os import mkdir, chdir
from PIL.Image import open as IMGOPEN
from re import sub
from click import clear as ClearWindow
from threading import Thread
from queue import Queue


baseURL = "https://comic.naver.com"

hParser = 'html.parser'

infoBanner = "[Naver-WebToon-Downloader]"

header = {
    'User-agent' : 'Mozilla/5.0',
    'Referer' : baseURL,
}

PrintInfo = lambda info: print(f"\n{infoBanner} {info}\n")


def InitPool():
    signal(SIGINT, SIG_IGN)


def CheckInternet():
    try:
        if ping('8.8.8.8') == None:
            terminate('인터넷 연결 또는 서버가 내려갔는지 확인하세요.')
    except ( OSError ):
        terminate('리눅스 사용자는 root권한을 이용해주세요.')


def PrintBanner():
    print(
'''
마지막 수정 날짜 : 2020/03/09
제작자 : kdr (https://github.com/kdrkdrkdr/)
      .-. .-.  .--.  .-. .-..----..----.            
      |  `| | / {} \ | | | || {_  | {}  }           
      | |\  |/  /\  \\ \_/ /| {__ | .-. \           
      `-' `-'`-'  `-' `---' `----'`-' `-'           
.-. . .-..----..----.  .---.  .----.  .----. .-. .-.
| |/ \| || {_  | {}  }{_   _}/  {}  \/  {}  \|  `| |
|  .'.  || {__ | {}  }  | |  \      /\      /| |\  |
`-'   `-'`----'`----'   `-'   `----'  `----' `-' `-'
         Naver WebToon Downloader by kdr
''')



def PrintProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='#'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + ' ' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total: 
        print()


def GetIMGsSize(imgPath):
    while True:
        try:
            img = IMGOPEN(imgPath)
            return img.size
        except:
            continue


def MakePDF(ImageList, Filename, DirLoc):
    try:
        with open(Filename, 'wb') as pdf:
            pdf.write(pdfConvert(ImageList))
    except:
        PrintInfo('PDF 제작에 오류가 발생했습니다.')
    
    finally:
        rmtree(DirLoc, ignore_errors=True)


def GetSoup(queue, url):
    while True:
        try:
            html = get(url, headers=header).text
            soup = BeautifulSoup(html, hParser)
            break
        except (exceptions.ChunkedEncodingError, exceptions.SSLError, exceptions.Timeout, exceptions.ConnectionError):
            pass

    queue.put(soup)


def FastGetSoup(url):

    q = Queue()
    t = Thread(target=GetSoup, args=(q, url, ))
    t.start()

    soupObj = q.get()
    t.join()

    t._stop()

    return soupObj
    



def ImageDownload(filename, url):
    while True:
        try:
            with open(f"{filename}", 'wb') as f:
                resp = get(url, headers=header, ).content
                f.write(resp)
                break

        except ( exceptions.ChunkedEncodingError, 
                 exceptions.Timeout,
                 exceptions.ConnectionError ):
            continue




def FastDownload(filename, url):
    t = Thread(target=ImageDownload, args=(filename, url,))
    t.setDaemon(False)
    t.start()
    t.join()
    t._stop()



def MakeDirectory(DirPath):
    try:
        mkdir(DirPath)
    except FileExistsError:
        rmtree(DirPath, ignore_errors=True)
        mkdir(DirPath)
    finally:
        chdir(DirPath)


def WebToonInfo(kWord):
    pCount = 0
    rList = []

    pSoup = FastGetSoup(f"{baseURL}/search.nhn?m=webtoon&keyword={kWord}&type=title&page={pCount+1}")
    pTotal = ( int(sub('[\D]', '', pSoup.find('span', {'class':'total'}).text.split('/')[1])) // 10 ) + 1

    
    for i in range(pTotal):
        soup = FastGetSoup(f"{baseURL}/search.nhn?m=webtoon&keyword={kWord}&type=title&page={pCount+1}")
        titleLink = soup.find_all('h5')
        resultList = soup.find_all('ul', {'class':'resultListItem'})

        titleList = [tl.a.text for tl in titleLink]
        linkList = [baseURL + tl.a['href'] for tl in titleLink]
        thumbnailList = [FastGetSoup(t).find('div', {'class':'thumb'}).img['src'] for t in linkList]
        
        for i, r in enumerate(resultList):
            li = r.find_all('li')

            info = [thumbnailList[i], titleList[i], linkList[i]]

            for l in li:
                em = l.find_all('em')
                info.append(sub('[\n\t ]', '', em[0].text))

            rList.append(tuple(info))

        pCount += 1

    return rList


def GetTitleAndLink(wLink):
    soup = FastGetSoup(wLink)
    epiCount = int(str(soup.find('td', {'class':'title'}).a['onclick']).split("\'")[-2])
    pageCount = (epiCount // 10) + 1

    epiList = []
    for i in range(1, pageCount+1, 1):
        wtEpis = FastGetSoup(wLink + f'&page={i}').find_all('td', {'class':'title'})
        for w in wtEpis:
            epiList.append([w.a.text, baseURL + w.a['href']])

    # [소제목, 링크]
    return epiList



def GetFileName(filename):
    toReplace = {
        '\\':'', '/':'', ':':'-', '\"':'',
        '?':'', '<':'[', '>':']', '|':'-', '*':''
    }

    for key, value in toReplace.items():
        filename = str(filename).replace(key, value)

    return filename


def DownloadWebtoon(filename, imgURLs):
    imgPaths = []

    for i in enumerate(imgURLs):
        imgPath = filename+str(i[0])+'.jpg'

        FastDownload(imgPath, i[1])

        imgPaths.append('./naver_download_temp/'+imgPath)
    
    return imgPaths





def GetIMGsURL(EpisURL):
    soup = FastGetSoup(EpisURL).find('div', {'class':'wt_viewer'}).find_all('img')
    ListOfIMGsURL = [i['src'] for i in soup]
    return ListOfIMGsURL


