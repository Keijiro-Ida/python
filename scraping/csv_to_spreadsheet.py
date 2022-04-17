import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3
import csv
import datetime

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

#jsonファイル(秘密鍵)を指定
credentials = ServiceAccountCredentials.from_json_keyfile_name('chromedriver_key_linen.json', scope)

# 認証
gc = gspread.authorize(credentials)

# 読み込むスプレッドシートをファイル名で指定
target_book = gc.open('sheet')


# ワークシート
target_sheet = target_book.sheet1
sold_sheet = target_book.worksheet('sheet_name')
new_arrival_sheet = target_book.worksheet('sheet_name')

dt_now = datetime.datetime.now()
today_ = dt_now.strftime('%Y_%m_%d')

target_book.values_update(
    'マスター',
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values':list(csv.reader(open('your_csv' + today_ + '.csv', encoding='utf_8_sig')))}
)

target_book.values_update(
    '実売アイテム',
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values':list(csv.reader(open('sold_your_csv' + today_ + '.csv', encoding='utf_8_sig')))}
)

target_book.values_update(
    '新入荷',
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values':list(csv.reader(open('sold_your_csv' + today_ + '.csv', encoding='utf_8_sig')))}
)
