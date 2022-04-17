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
today = dt_now.strftime('%Y年%m月%d日以前')

proxies = {
    'http': 'http://127.0.0.1:24000',
    'https': 'http://127.0.0.1:24000'
}

#DB登録
con = sqlite3.connect('data.db', isolation_level=None)
cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS master")
cur.execute("CREATE TABLE master(id integer primary key, title text, artist text, condition text, price integer, url text, format text, listing_date text, sold_date text)")
# cur.execute("DROP TABLE IF EXISTS super_master")
cur.execute("CREATE TABLE super_master(id integer primary key, title text, artist text, condition text, price integer, url text, format text, listing_date text, sold_date text)")

max = 288
hmv_url = 'https://target'

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

        # cur.execute("SELECT * FROM master WHERE hmv_id = ? AND url = ?", (id[i], url[i]))
        # list = cur.fetchone()

        # if list is None:
            # print(str(id[i]) + 'リスト無し')
        # print(str(id[i]))
        # print(title[i])
        # print(artist[i])
        # print(condition[i])
        # print(str(price[i]))
        # print(url[i])
        # print(listing_date[i])
        # print(format[i])

        # cur.execute('SELECT * FROM hmv_master WHERE id = ?', (id[i],))
        # list = cur.fetchone()
        try:
        #     # if list is None:
        #     print('データなし' + id[i])
            cur.execute("INSERT INTO master(id, title, artist, condition, price, url, format, listing_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                (id[i], title[i], artist[i], condition[i], price[i], url[i], format[i], listing_date[i]))
            # else:
            #     print('データあり' + str(list[0]) + ' ' + list[5])

        except Exception as e:
            print(str(i) + ' ' + "masterエラー" + str(id[i]) + " " + url[i])
            print(e)

        try:
            cur.execute("INSERT INTO master(id, title, artist, condition, price, url, format, listing_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                        (id[i], title[i], artist[i], condition[i], price[i], url[i], format[i], listing_date[i]))
        except Exception as e:
            print("super_masterエラー" + str(id[i]) + " " + url[i])
            print(e)

    random_seconds = round(random.random() * 5)
    print(str(j) + ':' + str(random_seconds))
    time.sleep(random_seconds)


# データベースからCSVへの反映

#マスターcsv
file = open('csv/master.csv', mode='w', encoding="utf-8_sig", newline="")
w = csv.writer(file)
w.writerow(['id', 'TITLE', 'ARTIST', 'CONDITION', 'PRICE', 'URL', 'FORMAT', '出品日'])
file.close()

# マスターDB検索

cur.execute("SELECT id, title, artist, condition, price, url, format, listing_date FROM master ORDER BY id ASC")
list = cur.fetchall()

# マスターデータの取得
id_master = []
title_master = []
artist_master = []
condition_master = []
price_master = []
url_master = []
format_master = []
listing_date_master = []


for i in range(len(list)):
    id_master.append(list[i][0])
    title_master.append(list[i][1])
    artist_master.append(list[i][2])
    condition_master.append(list[i][3])
    price_master.append(list[i][4])
    url_master.append(list[i][5])
    format_master.append(list[i][6])
    listing_date_master.append(list[i][7])

data = {
    'id': id_master,
    'title': title_master,
    'artist': artist_master,
    'condition': condition_master,
    'price': price_master,
    'url': url_master,
    'format': format_master,
    'listing_date': listing_date_master,
}

df = pd.DataFrame(data)
file_path = 'csv/master.csv'
df.to_csv(file_path, mode = 'a', index=False, header=False)


con.close()
