import sqlite3
import csv
import datetime
import pandas as pd

dt_now = datetime.datetime.now()
today = dt_now.strftime('%Y年%m月%d日')
today_ = dt_now.strftime('%Y_%m_%d')


#DB登録
con = sqlite3.connect('data.db', isolation_level=None)
cur = con.cursor()

cur.execute("SELECT  \
    case  when price < 250 then 'under 250' \
            when price between 250 and 500 then '250-500' \
            when price between 500 and 750 then '500-750' \
            when price between 750 and 1000 then '750-1000' \
            when price between 1000 and 1500 then '1000-1500' \
            when price between 1500 and 2000 then '1500-2000' \
            when price between 2000 and 3000 then '2000-3000'\
            when price between 3000 and 4000 then '3000-4000'\
            when price between 4000 and 5000 then '4000-5000' \
            when price > 5000 then 'over 5000' end as 値段, count(*) as 枚数, count(*) * 100.0 / (select count(*) from master) as 割合 FROM master group by 値段 order by price;")
list = cur.fetchall()

price = []
count = []
rate = []

file = open('data' + today_ + '.csv', mode='w', encoding="utf-8_sig", newline="")
w = csv.writer(file)
w.writerow(['マスター価格分布'])
w.writerow(['値段', '枚数', '割合'])
file.close()

for item in list:
    price.append(item[0])
    count.append(item[1])
    rate.append(round(item[2],2))

for i in range(len(price)):
    print(price[i])
    print(str(count[i]))
    print(str(rate[i]))
    print()

data = {
    'price':price,
    'count': count,
    'rate': rate
}

df = pd.DataFrame(data)
file_path = 'data' + today_ + '.csv'
df.to_csv(file_path, mode = 'a', index=False, header=False)

file = open('data' + today_ + '.csv', mode='a', encoding="utf-8_sig", newline="")
w = csv.writer(file)
w.writerow(['合計枚数', '合計金額', '平均単価'])
cur.execute("SELECT COUNT(*) as 合計枚数, SUM(price) as 合計金額, SUM(price) / COUNT(*) as 平均単価 FROM master;")
list = cur.fetchone()

count = list[0]
sum = list[1]
avg = list[2]
w.writerow([str(count), str(sum), str(avg)])
file.close()

cur.execute("SELECT  case  \
    when price < 250 then 'under 250' \
    when price between 250 and 500 then '250-500' \
    when price between 500 and 750 then '500-750' \
    when price between 750 and 1000 then '750-1000' \
    when price between 1000 and 1500 then '1000-1500' \
    when price between 1500 and 2000 then '1500-2000' \
    when price between 2000 and 3000 then '2000-3000' \
    when price between 3000 and 4000 then '3000-4000' \
    when price between 4000 and 5000 then '4000-5000' when price > 5000 then 'over 5000' end as 値段, count(*) as 枚数, sum(price), sum(price) * 100.0 / (select sum(price) from sold) as 割合 FROM sold group by 値段 order by price;")
list = cur.fetchall()

price = []
count = []
sold_total = []
rate = []

file = open('data' + today_ + '.csv', mode='a', encoding="utf-8_sig", newline="")
w = csv.writer(file)
w.writerow(['売上価格分布'])
w.writerow(['値段', '枚数', '売上', '割合'])
file.close()

for item in list:
    price.append(item[0])
    count.append(item[1])
    sold_total.append(item[2])
    rate.append(round(item[3],2))

for i in range(len(price)):
    print(price[i])
    print(str(count[i]))
    print(str(sold_total[i]))
    print(str(rate[i]))
    print()

data = {
    'price':price,
    'count': count,
    'sold_total': sold_total,
    'rate': rate
}

df = pd.DataFrame(data)
file_path = 'data_' + today_ + '.csv'
df.to_csv(file_path, mode = 'a', index=False, header=False)

file = open('csv/data_' + today_ + '.csv', mode='a', encoding="utf-8_sig", newline="")
w = csv.writer(file)
w.writerow(['合計枚数', '合計金額', '平均単価'])
cur.execute("SELECT COUNT(*) as 合計枚数, SUM(price) as 合計金額, SUM(price) / COUNT(*) as 平均単価 FROM sold;")
list = cur.fetchone()

count = list[0]
sum = list[1]
avg = list[2]
w.writerow([str(count), str(sum), str(avg)])


con.close()
file.close()
