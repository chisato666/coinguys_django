import requests
import json
import datetime as dt
import pandas as pd
from datetime import datetime, timedelta


def get_bybit_bars(symbol, interval, startTime, endTime):
    url = "https://api.bybit.com/v2/public/kline/list"

    # startTime = str(int(startTime.timestamp()))
    # endTime = str(int(endTime.timestamp()))

    req_params = {"symbol": symbol, 'interval': interval, 'from': startTime, 'to': endTime}
    print(req_params)
    df = pd.DataFrame(json.loads(requests.get(url, params=req_params).text)['result'])

    if (len(df.index) == 0):
        return None

   # df.index = [dt.datetime.fromtimestamp(x) for x in df.open_time]

    return df


interval = 3600  # 1 hour in seconds

response = requests.get("https://api-testnet.bybit.com/spot/v3/public/quote/kline?symbol=ETHUSDT&interval=1h&limit=10")
result = response.json()
end_time = datetime.now()

dt = datetime.now()
ts = datetime.timestamp(dt)
print(ts)
start_time = int(end_time.timestamp()) - interval
print(str(int(end_time.timestamp())))

df=(get_bybit_bars("BTCUSDT", '1', start_time,int(end_time.timestamp())))
print(df.head(1))

# for i in result:
#     print(i['orderTypes'])