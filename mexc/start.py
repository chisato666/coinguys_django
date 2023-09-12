import json
import websocket

BASE_URL = 'wss://wbs.mexc.com/raw/ws'

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed ....")

def on_open(ws):
    params = {
        "op": "sub.symbol",
        "symbol": "ETH_USDT",
    }
    print(json.dumps(params))
    ws.send(json.dumps(params))


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(BASE_URL,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                )
    ws.on_open = on_open
    ws.run_forever(ping_timeout=10)