import pandas as pd
import sqlite3

# pd.set_option('display.max_rows', 10)

dbname = 'customer.db'
con = sqlite3.connect(dbname)
cur = con.cursor()

# cur.execute('''
#     CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name STRING, address STRING, post_number STRING, building STRING)
# ''')

# con.commit()
# con.close()


df = pd.read_excel('customer.xlsx', header = [0])
df.to_sql('customer', con, if_exists='replace')
print(df)
