
import requests

def get_available_futures():
    url = "https://contract.mexc.com/api/v1/contract/detail"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["code"] == 200:
            futures = data["data"]
            for future in futures:
                symbol = future["symbol"]
                #contract_type = future["contractType"]
                print(f"Symbol: {symbol}")
        else:
            print("Error: Unable to fetch futures data.")
    else:
        print("Error: Request failed.")

# Usage
#get_available_futures()

def get_24hr_high(symbol):
    url = "https://contract.mexc.com/api/v1/contract/ticker/"
    params = {'symbol': symbol}
    response = requests.get(url, params=params)
    data = response.json()
    return float(data['data']['high24Price']), float(data['data']['lower24Price'])


def get_symbols_with_price_increase(rate):
    url = "https://contract.mexc.com/api/v1/contract/ticker"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        symbols = []

        for ticker in data['data']:
            symbol = ticker['symbol']
            price_change_percentage = float(ticker['riseFallRate'])

            if price_change_percentage > rate:
                line = [symbol, price_change_percentage]
                symbols.append(line)

        return symbols
    else:
        print("Failed to retrieve data from MEXC API.")
        return None

def get_kline(symbol,interval,period):
    url = "https://contract.mexc.com/api/v1/contract/kline/fair_price/"+symbol+"?interval="+interval
    response = requests.get(url)

    # params = {'symbol': symbol, 'interval': interval}
    # response = requests.get(url, params=params)
    data = response.json()
    return data

url = "https://contract.mexc.com/api/v1/contract/detail"
response = requests.get(url)
df = response.json()
# for i in range (0,len(df['data'])):
#     print(i,df['data'][i]['symbol'])

print(get_24hr_high('BTC_USDT'))
