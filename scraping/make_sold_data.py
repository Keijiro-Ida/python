import time
import re
import datetime
import csv
import sqlite3
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

dt_now = datetime.datetime.now()
today = dt_now.strftime('%Y年%m月%d日')
# today_ = dt_now.strftime('%Y_%m_%d')
today_ = '2021_11_17'
con = sqlite3.connect('data.db', isolation_level=None)
cur = con.cursor()

# pre_day = '2021_11_15'
today_ = '2021_11_17'
cur.execute("SELECT * from master WHERE sold_date is NULL")

list = cur.fetchall()
id = []
title = []
artist = []
condition = []
price = []
url = []
format = []
listing_date = []

for item in list:
    id.append(item[0])
    title.append(item[2])
    artist.append(item[3])
    condition.append(item[4])
    price.append(item[5])
    url.append(item[6])
    format.append(item[7])
    listing_date.append(item[8])



for i in range(len(id)):
    cur.execute("SELECT * FROM day_" + today_ + " WHERE id = ? ", (id[i],))
    list = cur.fetchone()


    if list is None:
        print(str(i) + 'データ無し:実売可能性あり' + str(id[i]))
        # masterに登録
        cur.execute("INSERT INTO find_sold (id, title, artist, condition, price, url, format, listing_date, sold_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (id[i], title[i], artist[i], condition[i], price[i], url[i], format[i], listing_date[i], today))
        # cur.execute("UPDATE master SET sold_date = ? WHERE id = ?", (today, id[i]))
