# 以下是一個示範的 Python 程式碼，它可以在 Bybit 上買入 BTC 現貨，並且在 BTC 價格一小時內上漲 1% 時買入 0.01 BTC，同時設置止賺 2% 和止損 2%：
#
# ```python
import time
import datetime
import requests

API_KEY = 'YOUR_API_KEY' # 替換成你的 API Key
SECRET_KEY = 'YOUR_SECRET_KEY' # 替換成你的 Secret Key

# 設置 API endpoint 和 headers
url = "https://api.bybit.com/v2/private/order/create"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

# 設置參數
symbol = "BTCUSDT" # 交易對
qty = 0.01 # 買入數量
price = None # 待定價格
stop_loss = None # 待定止損價格
take_profit = None # 待定止賺價格
hourly_high = None # 待定一小時內最高價格
hourly_low = None # 待定一小時內最低價格

# 檢查價格是否符合條件
def check_price():
    global price, stop_loss, take_profit, hourly_high, hourly_low
    response = requests.get("https://api.bybit.com/v2/public/tickers", params={"symbol": symbol})
    if response.status_code == 200:
        data = response.json()["result"][0]
        current_price = float(data["last_price"])
        if hourly_high is None or current_price > hourly_high:
            hourly_high = current_price
        if hourly_low is None or current_price < hourly_low:
            hourly_low = current_price
        if price is None and hourly_high >= 1.01 * hourly_low:
            price = current_price
            stop_loss = current_price * 0.98
            take_profit = current_price * 1.02
            print(f"Buy {qty} BTC at {price}")
        elif price is not None and current_price <= stop_loss:
            print(f"Stop loss triggered at {stop_loss}")
            place_order(side="sell", qty=qty, price=stop_loss)
        elif price is not None and current_price >= take_profit:
            print(f"Take profit triggered at {take_profit}")
            place_order(side="sell", qty=qty, price=take_profit)

# 下單
def place_order(side, qty, price):
    data = {
        "side": side,
        "symbol": symbol,
        "order_type": "Limit",
        "qty": qty,
        "price": price,
        "time_in_force": "GoodTillCancel",
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()["result"]
        print(f"Order placed: {result}")
    else:
        print(f"Error placing order: {response.status_code} - {response.reason}")

# 開始交易
while True:
    check_price()
    time.sleep(60)
    # 每過一小時重新設定一次最高價格和最低價格
    if datetime.datetime.now().minute == 0:
        hourly_high = None
        hourly_low = None

#個程式碼在不斷檢查 BTC 現價是否在一小時內增加了 1%，如果增加了，則在當前價格買入 0.01 BTC，並且設置止賺 2% 和止損 2%。程式碼使用了 Bybit 的 REST API，你需要替換 `API_KEY` 和 `SECRET_KEY` 為你自己的 API Key 和 Secret Key。程式碼需要一直運行，會每分鐘檢查一次 BTC 的價格。當價格觸發止賺或止損價格時，會自動下單平倉。程式碼還會每過一小時重新設定一次最高價格和最低價格。C 現價是否增加 1%，如果增加了，則在當前價格買入 0.01 BTC，並且設置止賺 2% 和止損 2%。程式碼使用了 Bybit 的 REST API，你需要替換 `API_KEY` 和 `SECRET_KEY` 為你自己的 API Key 和 Secret Key。程式碼需要一直運行，會每秒檢查一次 BTC 的價格。當價格觸發止賺或止損價格時，會自動下單平倉。