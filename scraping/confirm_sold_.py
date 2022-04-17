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
today_ = dt_now.strftime('%Y_%m_%d')

con = sqlite3.connect('data.db', isolation_level=None)
cur = con.cursor()

pre_day = '2021_11_15'
today_ = '2021_11_15'
cur.execute("SELECT * from find_sold")

list = cur.fetchall()
id = []
artist = []
title = []
type = []
format = []
price = []
url = []
listing_date = []
for item in list:
    id.append(item[0])
    artist.append(item[1])
    title.append(item[2])
    type.append(item[3])
    format.append(item[4])
    price.append(item[5])
    url.append(item[6])
    listing_date.append(item[7])

for i in range(10):

    target_url = url[i]

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--proxy-server=http://127.0.0.1:24000")
    options.add_argument('user-agent='+UserAgent().random)

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptInsecureCerts'] = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, desired_capabilities=capabilities)

    driver.get(target_url)
    order = driver.find_element_by_class_name('singleShoppingReserve').text
    print(order)

    # random_seconds = random.random() * 10
    # print(str(j) + ':' + str(random_seconds))
    # time.sleep(random_seconds)
    # if 'エラー' not in driver.title or 'アクセス' not in driver.title :
    #     print('在庫あり' + driver.title + str(id[i]))
    #     # cur.execute("DELETE FROM lp_sold WHERE id = ?", (id[i],))
    #     # cur.execute('UPDATE lp_master SET sold_date = NULL WHERE id = ?', (id[i],))
    #     # cur.execute('UPDATE lp_' + pre_day + ' SET sold_date = NULL WHERE id = ?', (id[i],))


    # else:
    #     print('在庫無し' + driver.title + str(id[i]))
