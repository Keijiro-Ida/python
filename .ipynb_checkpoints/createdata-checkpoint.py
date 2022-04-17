import pandas as pd
pd.set_option('display.max_rows', 10)


df = pd.read_excel('customer.xlsx', header = [0])
print(df)
