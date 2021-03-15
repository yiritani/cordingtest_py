from bs4 import BeautifulSoup
from urllib import request
import csv
import time
from typing import List, Tuple


def getHyperTextMarkUpText(url: str) -> str:
    response = request.urlopen(url)
    soup = BeautifulSoup(response)
    response.close()

    return soup


def createData(soupData):
    result = []
    try:
        name = soupData.find_all('h3', class_='Product__title')
        price = soupData.find_all('span', class_='Product__priceValue u-textRed')
        lastTime = soupData.find_all('span', class_='Product__time')
        linkUrl = soupData.find_all('a', class_='Product__titleLink')

        for i in range(len(name)):
            result.append((name[i].get_text(), price[i].get_text(), lastTime[i].get_text(), linkUrl[i].get('href')))

        return result

    except IndexError as indexerror:
        print(indexerror)
        return result


def generateCsv(csvList: List[Tuple[str]]):
    for productName, price, timeOutDate, link in csvList:
        print(productName, price, timeOutDate, link)
        with open(fileName, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([productName, price, timeOutDate, link])


if __name__ == '__main__':
    fileName = '/Users/iriyayuusuke/Desktop/csv.csv'
    with open(fileName, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['商品名', '現在値段', '残り時間', 'リンクURL'])

    cnt = 0

    for startNumIndex in range(1, 10000, 100):

        # url = 'https://auctions.yahoo.co.jp/search/search?p=macbook&va=macbook&exflg=1&b=' + str(startNumIndex) + '&n=100&mode=2'
        url = 'https://auctions.yahoo.co.jp/search/search?p=macbook+16gb&va=macbook+16gb&exflg=1&b=' + str(
            startNumIndex) + '&n=100&s1=cbids&o1=a&mode=2'

        souper = getHyperTextMarkUpText(url)

        csvDatas = createData(souper)
        if len(csvDatas) <= 0:
            print('data end.')
            exit(999)

        generateCsv(csvDatas)

        cnt += 1
        print(cnt, 'ページ目')
        time.sleep(10)
