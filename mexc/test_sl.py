#以下是一個簡單的 Python btc 交易策略，當現價大於 10 天平均線時買入，並且當現價大於買入價加 100 時，止蝕位加 50，不斷移動止蝕位向上，直至現值回調到止蝕位平倉。

import ccxt
import time

# 設置交易所和交易對
exchange = ccxt.binance()
symbol = 'BTC/USDT'

# 設置參數
ma_period = 10  # 移動平均線的天數
stop_loss = 0  # 止蝕位
stop_loss_step = 50  # 止蝕位步長
amount = 0.001  # 買入數量

# 獲取歷史數據
ohlcv = exchange.fetch_ohlcv(symbol, '1d')
close_prices = [ohlcv[i][4] for i in range(len(ohlcv))]

# 計算移動平均線
ma = sum(close_prices[-ma_period:]) / ma_period

while True:
    # 獲取最新價格
    ticker = exchange.fetch_ticker(symbol)
    last_price = ticker['last']

    # 如果現價大於移動平均線，則買入
    if last_price > ma:
        order = exchange.create_market_buy_order(symbol, amount)

        # 設置止蝕位
        stop_loss = order['price'] - stop_loss_step

    # 如果現價大於止蝕位加 100，則調整止蝕位
    if last_price > stop_loss + 100:
        stop_loss += stop_loss_step

    # 如果現價小於等於止蝕位，則平倉
    if last_price <= stop_loss:
        exchange.create_market_sell_order(symbol, amount)
        break

    time.sleep(60)  # 等待一分鐘後再次檢查

#請注意，此代碼僅為示範目的，實際交易前應仔細測試並請務必注意風險。另外，此代碼中使用了 ccxt 模塊，需先安裝。