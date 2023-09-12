

import websocket
import json
import mysql.connector
import config

API_KEY = 'VLQd7y0l2OQhtWZz3TWCjSyV3m7Yuip095BbAjrEZuzcUGl3aSgqR5JkUTbblGrX'

DB_HOST = 'waishing_binance'
DB_NAME = 'hkwaishing.com'
DB_USER = 'waishing_trendy'
DB_PASSWORD = 'Socool666'

# Replace with your Binance API key


# Connect to PostgreSQL database
mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.passwd,
    database=config.database
)
# Create a cursor object to interact with the database
cursor = mydb.cursor()

# Define the WebSocket URL for the BTCUSDT ticker
socket_url = "wss://stream.binance.com:9443/ws/btcusdt@ticker"

# Define the function to handle WebSocket messages
def on_message(ws, message):
    message = json.loads(message)
    # Check if the message is a price update
    if "ticker" in message:
        # Extract the price from the message
        price = message["ticker"]["lastPrice"]
        # Insert the price into the database
        # query = "INSERT INTO prices (symbol, price) VALUES (%s, %s)"
        # values = ("BTCUSDT", price)
        # cursor.execute(query, values)
        # mydb.commit()
        print("Price updated: BTCUSDT", price)

# Connect to the WebSocket and subscribe to the BTCUSDT ticker
ws = websocket.WebSocketApp(socket_url, on_message=on_message)
ws.run_forever()
