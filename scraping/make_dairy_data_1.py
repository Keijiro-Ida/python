import requests
import requests
from bs4 import BeautifulSoup
import csv
import re
import datetime
import sqlite3
import pandas as pd
import random
import time

dt_now = datetime.datetime.now()
today = dt_now.strftime('%Y年%m月%d日')
today_ = dt_now.strftime('%Y_%m_%d')

proxies = {
    'http': 'http://127.0.0.1:24000',
    'https': 'http://127.0.0.1:24000'
}

#DB登録
con = sqlite3.connect('data.db', isolation_level=None)
cur = con.cursor()

max =296
hmv_url = 'target_url'

for j in range(max):

    target_url = 'https://target' + str(j+1)

    for _ in range(3):
        try:

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

                # print(str(id[i]))
                # print(url[i])
                # print(format[i])
                # print(artist[i])
                # print(title[i])
                # print(condition[i])
                # print()

                cur.execute("SELECT * FROM master WHERE id = ?", (id[i], ))
                list = cur.fetchone()

                if list is None:
                    print(str(i) + 'データ無し' + str(id[i]))
                    # masterに登録
                    cur.execute("INSERT INTO master (id, title, artist, condition, price, url, format, listing_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (id[i], title[i], artist[i], condition[i], price[i], url[i], format[i], listing_date[i]))

                    # 新商品テーブルに追加
                    cur.execute("INSERT INTO new_arrival(id, title, artist, condition, price, url, format, listing_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (id[i], title[i], artist[i], condition[i], price[i], url[i], format[i], listing_date[i]))

        except Exception as e:
            print("エラー" + ':' + str(j))
            print(e)
            time.sleep(30)
        else:
            break
    else:
        pass

    random_seconds = round(random.random() * 5)
    print(str(j) + ':' + str(random_seconds))
    time.sleep(random_seconds)



con.close()
