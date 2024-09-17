import numpy as np
import pandas as pd
from pprint import pprint
import requests
import time

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 320)


data = {'A': [10, 100, 1000, 10000, 100000],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Taking the natural logarithm of column 'A'
df['log_A'] = np.log(df['A'])

print(df)
exit()
finished_path = "D:\\backtest\\cryptocurrency\\glassnode\\felix_v3_reversion\\+v1+metrics+addresses+count\\24h"
symbol = "FET"
set = "backtest_set"

symbol_csv = f"{finished_path}/{symbol}/{set}/full_result/{symbol}.csv"
symbol_df  = pd.read_csv(symbol_csv)

print(symbol_df)

for i in range(len(symbol_df)):
    highest_sharpe = symbol_df["strat_sharpe"].iloc[i]
    num_of_trade   = symbol_df["num_of_trade"].iloc[i]

    if num_of_trade > 0:
        print(highest_sharpe)
        break

print(highest_sharpe)
print(num_of_trade)