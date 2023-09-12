
import requests
import time

# specify the trading pair and interval
symbol = 'BTC_USDT'
interval = '1d'

# specify the start and end dates
start_date = '2021-01-01'
end_date = '2021-12-31'

# convert the start and end dates to Unix timestamp format
start_timestamp = int(time.mktime(time.strptime(start_date, '%Y-%m-%d')))
end_timestamp = int(time.mktime(time.strptime(end_date, '%Y-%m-%d')))

# make the API request
url = f'https://www.mxc.com/open/api/v2/market/kline?symbol={symbol}&interval={interval}&start_time={start_timestamp}&end_time={end_timestamp}'
response = requests.get(url)

# parse the response
if response.status_code == 200:
    klines = response.json()['data']
    for kline in klines:
        print(kline)
else:
    print(f'Error: {response.status_code}')

#n this example, we are requesting the Kline data for the BTC/USDT trading pair with a daily interval and a date range of January 1, 2021 to December 31, 2021. We convert the start and end dates to Unix timestamp format using the `mktime()` function from the `time` module, then include these timestamps in the API request URL. The response from the API is a JSON object that contains an array of Kline data. We loop through the Kline data and print each Kline. You can modify this code to suit your specific needs, such as changing the trading pair, interval, or date range.