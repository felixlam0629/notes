import aiohttp
import asyncio
import os
from pprint import pprint
import requests
import time

pause_flag = False

async def fetch_data(session, path, resolution, symbol, exchange=None, miner=None):
    global pause_flag
    try:
        while pause_flag:
            await asyncio.sleep(1)
            print(symbol, "awaiting")

        print(symbol, "awaiting finished")

        if symbol == "symbol1":
            response = {"status": 429}
        else:
            response = {"status": 0}

        if response["status"] == 429:
            message = "occurred 429 Too Many Requests"
            raise Exception(f"{path}丨{resolution}丨{symbol}丨{exchange}丨{miner}丨{message}")

        return "good"

    except Exception as e:
        pause_flag = True
        await asyncio.sleep(2)  # Pause for 10 seconds
        print("ended pause_flag")
        pause_flag = False

async def main():
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(1):
            tasks.append(fetch_data(session, "path1", "resolution1", "symbol1"))
            tasks.append(fetch_data(session, "path2", "resolution2", "symbol2"))
            tasks.append(fetch_data(session, "path3", "resolution3", "symbol3"))

        results = await asyncio.gather(*tasks)
        print(results)

# Run the asyncio event loop
asyncio.run(main())

"""
symbol1 awaiting finished
symbol2 awaiting
symbol3 awaiting
ended pause_flag
symbol2 awaiting
symbol2 awaiting finished
symbol3 awaiting
symbol3 awaiting finished
[None, 'good', 'good']
"""

"""
class Test:
    def __init__(self):
        self.host       = "https://api.glassnode.com"
        self.api_key    = "2VzGLKG4ajn6srWCeRFgXxH386F"
        self.path       = "/v1/metrics/addresse/active/count"
        self.resolution = "24h"
        self.symbol     = "BTC"
        self.exchange   = None

    def _testing(self):
        now_int   = int(time.time())
        since_int = now_int - 60 * 60 * 24
        print(now_int)
        print(since_int)

        if self.exchange == None:
            params = {"api_key": self.api_key, "s": since_int, "i": self.resolution, "a": self.symbol}

        else:
            params = {"api_key": self.api_key, "i": self.resolution, "a": self.symbol, "e": self.exchange}

        url = self.host + self.path
        print(url)
        print(params)

        try:
            response = requests.get(url, params = params)
            response = response.json()
            pprint(response)

        except:
            print("error")


def main():
    test = Test()
    test._testing()

if __name__ == "__main__":
    main()
    """