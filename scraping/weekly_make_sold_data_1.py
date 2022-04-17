import csv
import re
import datetime
import sqlite3
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import gc

dt_now = datetime.datetime.now()
today = dt_now.strftime('%Y年%m月%d日')
# today = '2021年12月27日'

#マスターcsv
# file = open('csv/error_make_sold_data.csv', mode='w', encoding="utf-8_sig", newline="")
# w = csv.writer(file)
# w.writerow(['日時', '何回目','id', 'url', 'エラー内容'])

#DB登録
con = sqlite3.connect('used.db', isolation_level=None)
cur = con.cursor()

cur.execute('SELECT id, url FROM master WHERE sold_date IS NULL ORDER BY id ASC')
list = cur.fetchall()
id = []
url = []

for item in list:
    id.append(item[0])
    url.append(item[1])
print(today)
print(str(len(id)))
print(str(len(url)))

for i in range(0, 10000):
    random_seconds = round(random.random() * 10)
    target_url = url[i]

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--proxy-server=http://127.0.0.1:24000")
        options.add_argument('user-agent='+UserAgent().random)
        # options.add_experimental_option('detach', True)
        options.add_argument('--disable-popup-blocking')
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptInsecureCerts'] = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, desired_capabilities=capabilities)
        random_seconds = round(random.random() * 10)
        driver.implicitly_wait(random_seconds)

        driver.execute_cdp_cmd('Network.enable', {})
        driver.execute_cdp_cmd('Network.setBlockedURLs', {
            'urls': [
                'www.facebook.com',
                'www.google.co.jp',
                'www.google-analytics.com',
                'analytics.twitter.com',
                'yahoo.co.jp',
                'www.yahoo.co.jp',
                'www.twitter.com',
                'www.googleadservices.com',
                'www.googletagmanager.com',
                'www.googletagservices.com',
                'platform.twitter.com',
                'connect.facebook.net',
                'syndication.twitter.com:',
                'facebook.com',
                'update.googleapis.com',
                's.yjtag.jp',
                'lhe-beacon.team-rec.jp',
                'lhe-webapi.team-rec.jp:',
                'update.googleapis.com',
                'accounts.google.com',
            ]})

        driver.get(target_url)

        sold_check_box = driver.find_elements_by_xpath('//*[@id="productStockArea"]/div/p[1]')
        if len(sold_check_box) == 0:
            sold_check_box = driver.find_elements_by_xpath('//*[@id="soldoutContent"]/p[1]')

            if len(sold_check_box) != 0:
                for tag in sold_check_box:
                    sold_check = tag.text
            else:
                sold_check = ''
            # print('当たり')
            # print(sold_check)
        else:
            for tag in sold_check_box:
                sold_check = tag.text
        # print(str(id[i]) + ':' + url[i])
        # print(sold_check)
        # print(sold_check == '注文不可')
        # print(sold_check == '在庫あり')


        if sold_check == '注文不可' or '品切れ' in sold_check:

            print('実売 id: ' + str(id[i]))
            print(str(i) + '回目')

            cur.execute('UPDATE master SET sold_date = ? WHERE id = ?', (today, id[i]))
            cur.execute('SELECT title, artist, condition, price, format, listing_date FROM master WHERE id = ?', (id[i],))
            list = cur.fetchone()
            title = list[0]
            artist = list[1]
            condition = list[2]
            price = list[3]
            format = list[4]
            listing_date = list[5]
            print(id[i])
            print(url[i])
            print(title)
            print(artist)
            print(condition)
            print(price)
            print(format)
            print(listing_date)
            cur.execute('INSERT INTO sold(id, title, artist, condition, price, url, format, listing_date, sold_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', (id[i], title, artist, condition, price, url[i], format, listing_date, today))
            # break

            del title, artist, condition, price, format, listing_date, list

        else:
            print(str(i) + '回目:' + '在庫あり id: ' + str(id[i]))
        # print(str(i) + ' ' + str(random_seconds))
        # time.sleep(random_seconds)



    except Exception as e:
        print("エラー" + ':' + str(i) + ':' + str(id[i]) + ':' + url[i])
        print(e)
        # data = [today, str(i), str(id[i]), url[i], e]
        # w.writerow(data)
        time.sleep(15)



driver.close()
# file.close()
con.close()
