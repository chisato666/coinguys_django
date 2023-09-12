
import requests
import time
import pandas as pd
from datetime import datetime
import pytz

symbol = 'BTCUSD'  # replace with the symbol you want to retrieve data for

# set up the API endpoint and parameters
endpoint = 'https://api.bybit.com/v2/public/kline/list'
interval = '1'  # 1-minute interval
start_time = int(time.time()) - 3600  # start time is one hour ago
end_time = int(time.time())
print(end_time)
# make the API call and retrieve the data
params = {'symbol': symbol, 'interval': interval, 'from': start_time, 'to': end_time}
response = requests.get(endpoint, params=params)



if response.status_code != 200:
    print(f'Error: {response.status_code} {response.reason}')
else:
    data = df = pd.DataFrame(response.json()['result'])
    #print(data.head(1)['close'])
#df['date'] = pd.to_datetime(df['open_time'], unit='s')


df['datetime'] = pd.to_datetime(df['open_time'], unit='s').dt.tz_localize('UTC')
hong_kong_tz = pytz.timezone('Asia/Hong_Kong')
df['datetime_hk'] = df['datetime'].dt.tz_convert(hong_kong_tz)
#data['date']=(pd.datetime.utcfromtimestamp(int(data['open_time'])).strftime('%Y-%m-%d %H:%M:%S'))
print(df.head(1)['close'])
print(df.tail(1)['close'])