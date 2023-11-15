'''

df["Date"].plot() -> showing whether its a straight line or not

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 320)

### datetime ###
datetime.datetime.now()                                = 2022-06-22 19:09:25.194726
datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ") = 2022-06-22 19:09:25

first_data_date = datetime.date(2012, 1, 3)                   = 2012-01-03
first_data_date_int = int(first_data_date.strftime("%Y%m%d")) = 20120103

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ") + str(counter) + "//" + str(num_of_combination) +  " combination " + code + " " + freq + " data downloading...")

import requests
baseURI = "https://www.bitmex.com/api/v1"
endpoint = "/trade/bucketed"
while latestDB < bitmexLatest:
    params = {"binSize": "1m", "symbol": symbol, "count" : 300, "startTime" : latestDB}
    r = requests.get(baseURI + endpoint, params = params)
    r = r.json()
    writeToDB(r)
    latestDB = r[-1]["timestamp"]
    time.sleep(1)

# Telegram Bot (Home, Old)
def _send_tg_msg(message):
    base_url = "https://api.telegram.org/bot5419868757:AAFlcWPtfBgvAH5luFoePwObPhRIOBvsxWM/sendMessage?chat_id=-696533053&text="
    requests.get(base_url + message)

# Telegram Bot (VPS, TP)
def _send_tg_msg_to_vps_channel(message):
    base_url = "https://api.telegram.org/bot5303768975:AAGkut6ojqmO8_b7RSkeqbqmaKMXGop36_8/sendMessage?chat_id=-654455487&text="
    requests.get(base_url + message)

# Telegram Bot (Home, Data)
def _send_tg_msg_to_data_channel(message):
    base_url = "https://api.telegram.org/bot6361635435:AAE5OdF3wdaRcz5imeDO7OCqnqS0ZNLoGCE/sendMessage?chat_id=-812574620&text="
    requests.get(base_url + message)

# Telegram Bot (Home, Backtest)
def _send_tg_msg_to_backtest_channel(message):
    base_url = "https://api.telegram.org/bot6233469935:AAHayu1tVZ4NleqRFM-61F6VQObWMCwF90U/sendMessage?chat_id=-809813823&text="
    requests.get(base_url + message)

# Telegram Bot (HTrading)
def _send_tg_msg_to_trading_channel(message):
    base_url = "https://api.telegram.org/bot6118524526:AAFxO28kTOeymD7aJ_v-0sWOmpPp-UY2Mng/sendMessage?chat_id=-853145017&text="
    requests.get(base_url + message)

-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEASZPgUtvqxnNFmKvdlEKiw/tQi2exrdr1ANc/CSgpyew=
-----END PUBLIC KEY-----

-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIGB8ICMy6sKwQSHtBlBLIdgYw/rbWtc7u0NJj5VfWbgv
-----END PRIVATE KEY-----

API_KEY= "ril6Zrw7XwjASLZ8a6OhPW5RAKAWclBR9JDc8aYSmAMwKvLA3RYZdHYonpaUtRyy"
PRIVATE_KEY_PATH = "C:\\Users\\USER\\Desktop\\program_trading\\api\\cryptocurrency\\binance\\private_key.txt"

# round up and down
df_a        = pd.DataFrame({"val": [0, -1, 0.01, 106700, 295400]})
df_a["val"] = (df_a["val"] / 1000).astype(int) * 1000 # round down to nearest 1000

print(df_a)

df_b        = pd.DataFrame({"val": [0, -1, 0.01, 106766, 295412]})
df_b["val"] = df_b["val"].round(-3) # round up and down to the nearest 1000

print(df_b)

df_c = pd.DataFrame({"val": [0, -1, 0.01, 106766, 295412]}) # round up and down to the nearest 1000
df_c = df_c.round({"val": -3})

print(df_c)

df_d = pd.DataFrame({"val": [0, -1, 0.01, 106766, 295412]})  # round up and down to the nearest 1000
df_d = df_d.round(decimals = {"val": -3})

print(df_d)

// lambda

add_10 = lambda x: x + 10

def add10_func(x):
    return x + 10

y = add_ten(5)
z = add10_func(5)





// Error Handling

# Unknown bug
try:
    a = 5 / 0

except Exception as e:
    print(e) # division by zero



# Known bug
try:
    a = 5 / 0
    b = a + 4

except ZeroDivisionError as e:
    print(e) # division by zero

except TypeError as e:
    print(e) # unsupported operand type(s) for +: "float" and "str"

else:
    print("everything is fine")

finally:
    print("cleaning up...")



# Define bug handling
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value   = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")

    if x < 5:
        raise ValueTooSmallError("value is too small", x)

try:
    test_value(0)

except ValueTooHighError as e:
    print(e)

except ValueTooSmallError as e:
    print(e.message, e.value)

'''