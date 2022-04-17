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

#DB登録
con = sqlite3.connect('data.db', isolation_level=None)
cur = con.cursor()


# データベースからCSVへの反映

#マスターcsv
file = open('data_' + today_ + '.csv', mode='w', encoding="utf-8_sig", newline="")
w = csv.writer(file)
w.writerow(['id', 'TITLE', 'ARTIST', 'CONDITION', 'PRICE', 'URL', 'FORMAT', '出品日', '実売日'])
file.close()

# マスターDB検索

cur.execute("SELECT id, title, artist, condition, price, url, format, listing_date, sold_date FROM master ORDER BY id ASC")
list = cur.fetchall()

# マスターデータの取得
id = []
title = []
artist = []
condition = []
price = []
url = []
format = []
listing_date = []
sold_date = []

for i in range(len(list)):
    id.append(list[i][0])
    title.append(list[i][1])
    artist.append(list[i][2])
    condition.append(list[i][3])
    price.append(list[i][4])
    url.append(list[i][5])
    format.append(list[i][6])
    listing_date.append(list[i][7])
    sold_date.append(list[i][8])

data = {
    'id': id,
    'title': title,
    'artist': artist,
    'condition': condition,
    'price': price,
    'url': url,
    'format': format,
    'listing_date': listing_date,
    'sold_date': sold_date
}

df = pd.DataFrame(data)
file_path = 'master_' + today_ + '.csv'
df.to_csv(file_path, mode = 'a', index=False, header=False)


# new arrivalcsv
file = open('new_arrival_' + today_ + '.csv', mode='w', encoding="utf-8_sig", newline="")
w = csv.writer(file)
w.writerow(['id', 'TITLE', 'ARTIST', 'CONDITION', 'PRICE', 'URL', 'FORMAT', '出品日'])
file.close()

# マスターDB検索

cur.execute("SELECT id, title, artist, condition, price, url, format, listing_date FROM new_arrival ORDER BY listing_date DESC")
list = cur.fetchall()

# マスターデータの取得
id = []
title = []
artist = []
condition = []
price = []
url = []
format = []
listing_date = []

for i in range(len(list)):
    id.append(list[i][0])
    title.append(list[i][1])
    artist.append(list[i][2])
    condition.append(list[i][3])
    price.append(list[i][4])
    url.append(list[i][5])
    format.append(list[i][6])
    listing_date.append(list[i][7])


data = {
    'id': id,
    'title': title,
    'artist': artist,
    'condition': condition,
    'price': price,
    'url': url,
    'format': format,
    'listing_date': listing_date,
}

df = pd.DataFrame(data)
file_path = 'new_arrival_' + today_ + '.csv'
df.to_csv(file_path, mode = 'a', index=False, header=False)

#マスターcsv
file = open('sold_' + today_ + '.csv', mode='w', encoding="utf-8_sig", newline="")
w = csv.writer(file)

w.writerow(['id', 'TITLE', 'ARTIST', 'CONDITION', 'PRICE', 'URL', 'FORMAT', '出品日', '実売日'])
file.close()

# マスターDB検索

cur.execute("SELECT id, title, artist, condition, price, url, format, listing_date, sold_date FROM sold ORDER BY sold_date DESC")
list = cur.fetchall()

# マスターデータの取得
id = []
title = []
artist = []
condition = []
price = []
url = []
format = []
listing_date = []
sold_date = []

for i in range(len(list)):
    id.append(list[i][0])
    title.append(list[i][1])
    artist.append(list[i][2])
    condition.append(list[i][3])
    price.append(list[i][4])
    url.append(list[i][5])
    format.append(list[i][6])
    listing_date.append(list[i][7])
    sold_date.append(list[i][8])

data = {
    'id': id,
    'title': title,
    'artist': artist,
    'condition': condition,
    'price': price,
    'url': url,
    'format': format,
    'listing_date': listing_date,
    'sold_date': sold_date
}


df = pd.DataFrame(data)
file_path = 'sold_' + today_ + '.csv'
df.to_csv(file_path, mode = 'a', index=False, header=False)

con.close()
