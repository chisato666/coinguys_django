import mexc_spot_v3

hosts = "https://api.mexc.com"
mexc_key = "mx0vglXboBEpB212qD"
mexc_secret = "e5eb82c6688a488ba111cf52aa1bd350"

# Market Data
"""get kline"""
data = mexc_spot_v3.mexc_market(mexc_hosts=hosts)
params = {
    'symbol': 'BTCUSDT',
    'interval': '5m',
    'limit': 10
}
response = data.get_kline(params)
#print(response)

#s_info=(mexc_spot_v3.mexc_market.get_defaultSymbols("BTCUSDT"))
# Spot Trade
print("place an order")
trade = mexc_spot_v3.mexc_trade(mexc_key=mexc_key, mexc_secret=mexc_secret, mexc_hosts=hosts)
params = {
    "symbol": "PEPEUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "quantity": 10,
    "price": "29000"
}
# response = trade.post_order(params)
# print(response)

print("get account selfSymbols")
response = trade.get_selfSymbols()
print(response)

print("get account  get_openorders")
params = {
    "symbol": "PEPEUSDT"
}
response = trade.get_openorders(params)
print(response)



print("get account get allorders")
params = {
    "symbol": "PEPEUSDT"
}
response = trade.get_allorders(params)
print(response)

