import json
import pandas as pd
import websocket
from websocket import create_connection

#连接到 WebSocket 服务器
ws = create_connection("wss://fstream.binance.com/ws/btcusdt@kline_1m")

# 订阅 Kline 数据流
ws.send(json.dumps({
    "method": "SUBSCRIBE",
    "params": ["btcusdt@kline_1m"],
    "id": 123
}))


# def on_open(ws):
#     sub_msg={"method": "SUBSCRIBE","params": ["btcusdt@kline_1m"],"id":1}
#     ws.send(json.dumps(sub_msg))
#     print("Opened connection")
#
# def on_message(ws,message):
#     data= json.loads(message)
#     for x in data:
#         print(x['s'],x['c'])
#
# url= "wss://fstream.binance.com/ws"
# ws=websocket.WebSocketApp(url,on_open=on_open,on_message=on_message)
# ws.run_forever()

# 接收并打印消息
while True:
    result = ws.recv()
    # print(result)

    candle = result
    is_candle_closed = candle['x']
    close = candle['c']
    high = candle['h']
    print(close)

# 关闭连接
ws.close()

