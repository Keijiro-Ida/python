import time
import re
import datetime
import csv
import sqlite3
import random
import requests
from bs4 import BeautifulSoup
import csv

dt_now = datetime.datetime.now()
today = dt_now.strftime('%Y年%m月%d日')
today_ = dt_now.strftime('%Y_%m_%d')

proxies = {
    'http': 'http://127.0.0.1:24000',
    'https': 'http://127.0.0.1:24000'
}

#DB登録
con = sqlite3.connect('master.db', isolation_level=None)
cur = con.cursor()

#マスターcsv
file = open('csv/error_' + today_ + '.csv', mode='w', encoding="utf-8_sig", newline="")
w = csv.writer(file)
w.writerow(['ページ数', '項目数', 'id', 'url', 'エラー内容'])


max = 301
hmv_url = 'https://targer'

for j in range(max):

    target_url = 'https://target' + str(j+1)

    response = requests.get(target_url, proxies=proxies)
    soup = BeautifulSoup(response.text, 'html.parser')

    id = []
    title = []
    artist = []
    condition = []
    price = []
    url = []
    format = []
    listing_date = []

    text = [tag for tag in soup.find_all('div', {'class': 'itemText'})]

    for i in range(len(text)):
        href = text[i].find('a').get('href')
        url.append(hmv_url + href)
        num = text[i].find('a').get('href').split('_')[-1]
        id.append(int(num))
        fmt = text[i].find('span', {'class', 'greenItemWide'}).text
        format.append(fmt)
        name = text[i].find('p', {'class', 'name'}).text.replace('\n', '')
        artist.append(name)
        titles = text[i].find('h3', {'class', 'title'}).text.strip()

        if len(titles.split('】')) == 1:
            title.append(titles.split('(')[0].split('【')[0].strip())
            conditions = ''
        else:
            title.append(titles.split('】')[1].split('(')[0].split('【')[0].strip())
            conditions = titles.split('】')[0].replace('【中古:盤質', '')

        condition.append(conditions)
        prices = re.sub(r"\D", "",text[i].find('div', {'class', 'statesList'}).text)
        price.append(int(prices))
        listing_date.append(today)

        try:
            cur.execute("SELECT * FROM master WHERE id = ?", (id[i],))
            list = cur.fetchone()

            if list is None:
                print('登録' + ':' + str(j) + ':' + str(id[i]))
                cur.execute("INSERT INTO master(id, title, artist, condition, price, url, format, listing_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (id[i], title[i], artist[i], condition[i], price[i], url[i], format[i], listing_date[i]))
                cur.execute("INSERT INTO new_arrival(id, title, artist, condition, price, url, format, listing_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (id[i], title[i], artist[i], condition[i], price[i], url[i], format[i], listing_date[i]))

            else:
                print('中ループ終了' + ':' + str(j) + ':' + str(id[i]))
                break

        except Exception as e:
            print("DBエラー" + str(id[i]) + " " + url[i] + ' ' + str(len(id)))
            print(e)
            data = [str(j), str(len(id)), str(id[i]), url[i], e]
            w.writerow(data)

    if list is not None:
        print('外ループ終了' + ':' + str(j) + ':' + str(id[i]))
        break

    random_seconds = round(random.random() * 10)
    print(str(j) + ' ' + str(random_seconds))
    time.sleep(random_seconds)

file.close()
con.close()
