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

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


# dt_now = datetime.datetime.now()
# today = dt_now.strftime('%Y年%m月%d日')
# today_ = dt_now.strftime('%Y_%m_%d')

con = sqlite3.connect('data.db', isolation_level=None)
cur = con.cursor()

pre_day = '2021_11_15'
today_ = '2021_11_15'
cur.execute("SELECT * from find_sold")

proxies = {
    'http': 'http://127.0.0.1:24000',
    'https': 'http://127.0.0.1:24000'
}

list = cur.fetchall()
id = []
title = []
artist = []
condition = []
price = []
url = []
format = []


for item in list:
    id.append(item[0])
    title.append(item[2])
    artist.append(item[3])
    condition.append(item[4])
    price.append(item[5])
    url.append(item[6])
    format.append(item[7])


for i in range(1):

    target_url = 'https://target_url'

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option('detach', True)
    options.add_argument("--proxy-server=http://127.0.0.1:24000")
    options.add_argument('user-agent='+UserAgent().random)

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptInsecureCerts'] = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, desired_capabilities=capabilities)

    driver.get(target_url)
    order = driver.find_elements_by_xpath('//*[@id="productStockArea"]/div/p[1]')
    for i in range(len(order)):
        print(order[i].text)
    # if '品切れなどの理由により、販売されておりません' in title:
    #     print('売り切れ' + str(id[i]))
    #     cur.execute('UPDATE master SET sold_date = ? WHERE id = ?', (sold_date[i],id[i],))
    #     cur.execute("INSERT INTO sold (id,  title, artist, condition, price, url, format, listing_date, sold_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (id[i], title[i], artist[i], condition[i], price[i], url[i], format[i], listing_date[i], sold_date[i]))
    # else:
    #     print('在庫あり' + str(id[i]))

    # random_seconds = random.random() * 15
    # print(str(i) + ':' + str(random_seconds))
    # time.sleep(random_seconds)
