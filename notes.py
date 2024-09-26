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