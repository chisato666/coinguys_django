# Sure, here's a Python script that connects to the Binance WebSocket stream and continuously retrieves the current ETH price every second. It then inserts the price into a PostgreSQL database using the psycopg2 library.
#
# Make sure to replace the placeholders for the database credentials and Binance API key with your own.
#
# ```python
import json
import asyncio
import time
import config
import psycopg2
from binance import Client
from binance.streams import BinanceSocketManager
import mysql.connector


queue = asyncio.Queue()

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

db = mydb.cursor()


# Create Binance client and socket manager
client = Client(api_key=API_KEY)
bm = BinanceSocketManager(client)

# Define callback function for receiving WebSocket data
def process_message(msg):
    if msg['e'] == 'error':
        print('Error:', msg['m'])
    else:
        price = float(msg['c'])
        timestamp = int(time.time())
        print('ETH price:', price)
        db.execute("INSERT INTO eth_price (price, timestamp) VALUES (%s, %s)", (price, timestamp))
        mydb.commit()

# Subscribe to ETH ticker WebSocket stream
socket = bm.trade_socket('ETHUSDT')

await socket.__aenter__()
msg= await socket.recv()
print(msg)
await socket.__aexit__(None,None,None)
# Start WebSocket stream

# Keep script running indefinitely
# while True:
#     time.sleep(1)

# ```
#
# This script creates a connection to a PostgreSQL database and initializes a cursor for executing SQL queries. It then creates a Binance client and socket manager using your API key.
#
# The `process_message` function is called whenever the WebSocket stream receives data. It checks if the message is an error message and prints the error message if it is. Otherwise, it extracts the current ETH price from the message, gets the current timestamp using the `time` module, prints the price to the console, and inserts the price and timestamp into the `eth_price` table in the PostgreSQL database using an SQL query.
#
# The script then subscribes to the ETH ticker WebSocket stream using the `bm.start_symbol_ticker_socket` method and starts the WebSocket stream using the `bm.start` method.
#
# Finally, the script enters an infinite loop to keep the script running indefinitely, with a one-second delay between each iteration. This is necessary to keep the WebSocket stream open and continue receiving data.