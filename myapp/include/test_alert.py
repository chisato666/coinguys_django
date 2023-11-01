# Certainly! Here's an example Django script that can be used to write all price decrease alerts into a database using Django's ORM (Object-Relational Mapping):
#
# 1. Set up a Django project and create a new Django app. You can refer to the Django documentation for more details on setting up a Django project: https://docs.djangoproject.com/
#
# 2. Create a new model in your Django app's `models.py` file to represent the alerts. For example, let's assume you have an app named `pricealerts`:
#
# ```python
from django.db import models

class PriceAlert(models.Model):
    symbol = models.CharField(max_length=50)
    interval = models.CharField(max_length=10)
    percentage_decrease = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
# ```
#
# 3. Run the Django migrations to create the necessary database table for the `PriceAlert` model:
#
# ```shell
python manage.py makemigrations
python manage.py migrate
```

4. Update the `check_price_decrease()` function to save the alerts into the database:

```python
import requests
import time
from django.utils import timezone
from pricealerts.models import PriceAlert

def check_price_decrease(symbol_list):
    url = "https://www.mxc.com/open/api/v1/market/kline"
    intervals = ["15min", "30min", "1hour"]
    candle_limit = 2
    seen_candles = set()

    while True:
        for symbol in symbol_list:
            for interval in intervals:
                params = {
                    "symbol": symbol,
                    "interval": interval,
                    "limit": candle_limit
                }

                response = requests.get(url, params=params)
                data = response.json()

                # Extract the close prices for the previous and current candles
                previous_close = float(data["data"][0][4])
                current_close = float(data["data"][1][4])

                # Calculate the percentage decrease
                percentage_decrease = (current_close - previous_close) / previous_close * 100

                candle_id = f"{symbol}-{interval}-{data['data'][1][0]}"  # Unique identifier for the candle

                if candle_id not in seen_candles and percentage_decrease <= -3:
                    alert = PriceAlert(
                        symbol=symbol,
                        interval=interval,
                        percentage_decrease=round(percentage_decrease, 2),
                        timestamp=timezone.now()
                    )
                    alert.save()
                    seen_candles.add(candle_id)

        time.sleep(60)  # Sleep for 1 minute before checking again
```

In this updated code, we imported the `timezone` module from Django to get the current timestamp for the alerts. Each time a price decrease alert is triggered, a new `PriceAlert` object is created and saved into the database using Django's ORM.

Ensure that your Django app is included in the `INSTALLED_APPS` setting in your project's `settings.py` file:

```python
INSTALLED_APPS = [
    # ...
    'pricealerts',
    # ...
]
```
Certainly! Here's an example HTML template that you can use to display the alert logs in Django:

1. Create a new HTML template file named `alerts.html` in your Django app's `templates` directory.

```html
<!-- alerts.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Price Alerts Log</title>
</head>
<body>
    <h1>Price Alerts Log</h1>
    <table>
        <thead>
            <tr>
                <th>Symbol</th>
                <th>Interval</th>
                <th>Percentage Decrease</th>
                <th>Timestamp</th>
            </tr>
        </thead>
        <tbody>
            {% for alert in alerts %}
            <tr>
                <td>{{ alert.symbol }}</td>
                <td>{{ alert.interval }}</td>
                <td>{{ alert.percentage_decrease }}</td>
                <td>{{ alert.timestamp }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

2. Create a view function in your Django app's `views.py` file to render the `alerts.html` template and pass the alert logs as context:

```python
# views.py

from django.shortcuts import render
from pricealerts.models import PriceAlert

def alert_log(request):
    alerts = PriceAlert.objects.all().order_by('-timestamp')
    context = {'alerts': alerts}
    return render(request, 'alerts.html', context)
```

3. Update your Django app's `urls.py` file to include a URL pattern for the `alert_log` view:

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('alerts/', views.alert_log, name='alert_log'),
    # ...
]
```

Certainly! Here's an example Django script that can be used to write all price decrease alerts into a database using Django's ORM (Object-Relational Mapping):

1. Set up a Django project and create a new Django app. You can refer to the Django documentation for more details on setting up a Django project: https://docs.djangoproject.com/

2. Create a new model in your Django app's `models.py` file to represent the alerts. For example, let's assume you have an app named `pricealerts`:

```python
from django.db import models

class PriceAlert(models.Model):
    symbol = models.CharField(max_length=50)
    interval = models.CharField(max_length=10)
    percentage_decrease = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
```

3. Run the Django migrations to create the necessary database table for the `PriceAlert` model:

```shell
python manage.py makemigrations
python manage.py migrate
```

4. Update the `check_price_decrease()` function to save the alerts into the database:

```python
import requests
import time
from django.utils import timezone
from pricealerts.models import PriceAlert

def check_price_decrease(symbol_list):
    url = "https://www.mxc.com/open/api/v1/market/kline"
    intervals = ["15min", "30min", "1hour"]
    candle_limit = 2
    seen_candles = set()

    while True:
        for symbol in symbol_list:
            for interval in intervals:
                params = {
                    "symbol": symbol,
                    "interval": interval,
                    "limit": candle_limit
                }

                response = requests.get(url, params=params)
                data = response.json()

                # Extract the close prices for the previous and current candles
                previous_close = float(data["data"][0][4])
                current_close = float(data["data"][1][4])

                # Calculate the percentage decrease
                percentage_decrease = (current_close - previous_close) / previous_close * 100

                candle_id = f"{symbol}-{interval}-{data['data'][1][0]}"  # Unique identifier for the candle

                if candle_id not in seen_candles and percentage_decrease <= -3:
                    alert = PriceAlert(
                        symbol=symbol,
                        interval=interval,
                        percentage_decrease=round(percentage_decrease, 2),
                        timestamp=timezone.now()
                    )
                    alert.save()
                    seen_candles.add(candle_id)

        time.sleep(60)  # Sleep for 1 minute before checking again


To
send
a
popup
message
on
the
browser
using
AJAX, you
can
modify
the
JavaScript
code
to
trigger
a
popup or a
browser
notification.Here
's an example implementation using JavaScript and the browser'
s
built - in `Notification`
API:

```javascript
// Function
to
send
the
popup
message
request
function
sendPopupMessage()
{
// Check if the
browser
supports
notifications
if (!("Notification" in window)) {
    console.error('Browser does not support notifications');
return;
}

// Request
permission
to
show
notifications
Notification.requestPermission()
    .then(permission= > {
if (permission === 'granted')
{
// Send
the
popup
message
const
notification = new
Notification('BTCUSDT Price Alert', {
    body: 'BTCUSDT price increased by 3% in the last 15 minutes!'
});

// Close
the
notification
after
a
few
seconds(optional)
setTimeout(() = > {
    notification.close();
}, 5000);
} else {
    console.error('Notification permission denied');
}
})
.catch(error= > {
    console.error('Error requesting notification permission:', error);
});
}

// Call
the
function
to
send
the
popup
message
sendPopupMessage();
```

In
this
example, the
`sendPopupMessage`
function
checks if the
browser
supports
the
`Notification`
API.It
then
requests
permission
to
show
notifications
using
the
`Notification.requestPermission`
method.If
permission is granted, a
new
notification
with the specified title and message is created using the `Notification` constructor.You can customize the notification's appearance and behavior by providing additional options to the constructor.

Additionally, you can include optional code to close the notification automatically after a certain duration by calling the `close` method on the notification object.
Certainly! Here's an example of how you can use Ajax to append a timestamp to a textarea element every 5 seconds using JavaScript and jQuery:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Ajax Append Timestamp to Textarea</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script>
    $(document).ready(function() {
      function appendTimestamp() {
        var timestamp = new Date().toLocaleString(); // Get the current timestamp

        $.ajax({
          url: 'your_server_endpoint',
          type: 'POST',
          data: { timestamp: timestamp }, // Send the timestamp as data
          success: function(response) {
            // Append the timestamp to the textarea
            $('#timestampTextarea').val($('#timestampTextarea').val() + '\n' + response);
          },
          error: function(xhr) {
            // Handle any errors
            alert('Error: ' + xhr.status);
          }
        });
      }

      // Append a timestamp every 5 seconds
      setInterval(appendTimestamp, 5000);
    });
  </script>
</head>
<body>
  <textarea id="timestampTextarea" rows="10" cols="50"></textarea>
</body>
</html>
```

In this example, a function named `appendTimestamp` is defined to fetch the current timestamp and send it to the server using Ajax. On a successful response from the server, the timestamp is appended to the textarea. Any errors are handled in the `error` callback function.

The `setInterval` function is used to call the `appendTimestamp` function every 5 seconds, ensuring that a new timestamp is appended at regular intervals.

Please note that you'll need to replace `'your_server_endpoint'` with the actual URL or endpoint where you want to send the timestamp data. Additionally, make sure you have included the jQuery library by adding the `<script>` tag in the `<head>` section of your HTML document.
Remember that browsers have different policies and restrictions regarding displaying notifications, and users can configure their preferences accordingly.It's important to respect the user's choice and handle cases where permission is denied or the browser does not support notifications.



Certainly! Here's an updated version of the code that checks a list of symbols (`BTCUSDT` and `ETHUSDT`) and sends an alert to the browser if any of the symbols have increased by 3% since the last check. The alert will only be triggered once.

```javascript



let lastPrices = {}; // Object to store the last checked prices

// Function to check the price of a symbol and send an alert if increased by 3%
function checkPrice(symbol) {
  // Make an Ajax request to get the symbol price
  $.ajax({
    url: `https://api.example.com/${symbol.toLowerCase()}`, // Replace with the actual API endpoint
    method: 'GET',
    success: function (response) {
      const currentPrice = response.price;

      // Check if this is the first check or if the price has increased by 3%
      if (!(symbol in lastPrices) || (currentPrice - lastPrices[symbol]) / lastPrices[symbol] >= 0.03) {
        // Send an alert to the browser
        alert(`${symbol} price has increased by 3%: ${currentPrice}`);

        // Update the last checked price for this symbol
        lastPrices[symbol] = currentPrice;
      }
    },
    error: function () {
      console.error(`Failed to fetch ${symbol} price`);
    }
  });
}

// Function to check prices for a list of symbols
function checkSymbolPrices(symbols) {
  symbols.forEach(symbol => {
    checkPrice(symbol);
  });
}

// Function to schedule the periodic checks
function scheduleChecks() {
  // Check prices for the initial list of symbols immediately
  const initialSymbols = ['BTCUSDT', 'ETHUSDT'];
  checkSymbolPrices(initialSymbols);

  // Schedule the next check after 15 minutes
  setInterval(function () {
    checkSymbolPrices(initialSymbols);
  }, 15 * 60 * 1000);
}

// Start the periodic checks
scheduleChecks();

Sure! Here's an example of Python code that checks the conditions you mentioned for a list of symbols (e.g., BTCUSDT and ETHUSDT) using the Binance API:

```python
import requests

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return float(data["price"])

def check_ema(symbol):
    # Logic to check if current price > 50EMA for the symbol
    # Replace this with your own implementation
    return True  # Placeholder value

def check_rsi(symbol):
    # Logic to check if RSI > 70 for the symbol
    # Replace this with your own implementation
    return False  # Placeholder value

def check_macd(symbol):
    # Logic to check if MACD has crossed up for 1hr candlestick for the symbol
    # Replace this with your own implementation
    return True  # Placeholder value

symbols = ["BTCUSDT", "ETHUSDT"]

for symbol in symbols:
    price = get_price(symbol)
    if check_50ema(symbol):
        print(f"{symbol}: Current price > 50EMA")
    if check_rsi(symbol):
        print(f"{symbol}: RSI > 70")
    if check_macd(symbol):
        print(f"{symbol}: MACD crossed up for 1hr candlestick")


To calculate the RSI (Relative Strength Index) and MACD (Moving Average Convergence Divergence) values for a given symbol, you can use various libraries in Python such as `pandas`, `numpy`, and `ta` (Technical Analysis Library). Here's an example of how you can calculate RSI and MACD using these libraries:

```python
import pandas as pd
import numpy as np
import ta

def calculate_rsi(df, period=14):
    close_prices = df['close'].values
    rsi = ta.momentum.RSIIndicator(close_prices, n=period)
    rsi_values = rsi.rsi()
    return rsi_values

def calculate_macd(df, fast_period=12, slow_period=26, signal_period=9):
    close_prices = df['close'].values
    macd = ta.trend.MACD(close_prices, fast_period=fast_period, slow_period=slow_period, signal_period=signal_period)
    macd_values = macd.macd()
    signal_line = macd.macd_signal()
    return macd_values, signal_line

# Example usage
symbol = "BTCUSDT"
interval = "1h"  # 1-hour candlestick data

# Fetch historical data using an API or from a CSV file
# Assuming you have OHLCV (Open, High, Low, Close, Volume) data
# stored in a pandas DataFrame named 'data'

# Assuming 'data' DataFrame has columns: ['timestamp', 'open', 'high', 'low', 'close', 'volume']
data = fetch_historical_data(symbol, interval)  # Replace this with your own data fetching logic

# Calculate RSI
data['rsi'] = calculate_rsi(data)

# Calculate MACD
data['macd'], data['signal_line'] = calculate_macd(data)

# Print RSI and MACD values for the latest candlestick
latest_rsi = data['rsi'].iloc[-1]
latest_macd = data['macd'].iloc[-1]
latest_signal_line = data['signal_line'].iloc[-1]

print(f"Latest RSI for {symbol}: {latest_rsi}")
print(f"Latest MACD for {symbol}: {latest_macd}")
print(f"Latest Signal Line for {symbol}: {latest_signal_line}")
```

In the code above, `calculate_rsi` function calculates the RSI values based on the close prices of the given DataFrame. The `calculate_macd` function calculates the MACD values and signal line based on the close prices of the given DataFrame. Finally, you can print the latest RSI and MACD values for the symbol.

Please note that you'll need to replace the `fetch_historical_data` function with your own logic for fetching historical OHLCV data for the specified symbol and interval. Additionally, you may need to install the `pandas`, `numpy`, and `ta` libraries if you haven't already by running `pip install pandas numpy ta` in your terminal or command prompt.


Apologies for the confusion. If the close price is always between the long exit and short exit, it means that there will be frequent trades with this particular strategy. If you want to avoid trading on every data point, you can add an additional condition to the backtesting logic to prevent consecutive trades within a certain period. Here's an updated version of the code that incorporates this condition:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define Chandelier Exit strategy
def chandelier_exit(df, period=1, multiplier=1.85):
    high_max = df['High'].rolling(period).max()
    atr = df['High'].rolling(period).max() - df['Low'].rolling(period).min()
    long_exit = high_max - multiplier * atr
    short_exit = df['Low'].rolling(period).min() + multiplier * atr
    return long_exit, short_exit

# Define backtesting function
def backtest_chandelier_exit(df, period=22, multiplier=3, cooldown_period=5):
    long_exit, short_exit = chandelier_exit(df, period, multiplier)
    trades = []
    position = None
    cooldown = 0
    for i in range(len(df)):
        if cooldown == 0:
            if position is None:
                if df['Close'][i] > long_exit[i]:
                    position = 'Long'
                    entry_price = df['Close'][i]
                    cooldown = cooldown_period
            elif position == 'Long':
                if df['Close'][i] < short_exit[i]:
                    exit_price = df['Close'][i]
                    profit = exit_price - entry_price
                    trades.append(profit)
                    position = None
                    cooldown = cooldown_period
        else:
            cooldown -= 1
    return trades

# Load BTCUSDT data (assuming you have a DataFrame named 'df' with columns 'time', 'Open', 'High', 'Low', 'Close')
df = pd.read_csv('btcusdt.csv')

# Convert 'time' to datetime
df['time'] = pd.to_datetime(df['time'], unit='ms')

# Perform backtest
trades = backtest_chandelier_exit(df)

# Calculate total profit return
total_profit = np.sum(trades)

# Print results
print(f"Total trades: {len(trades)}")
print(f"Total profit return: {total_profit:.2f} USDT")

# Calculate Chandelier Exit
long_exit, short_exit = chandelier_exit(df)

# Plotting the Chandelier Exit and BTCUSDT Close price
plt.figure(figsize=(12, 6))
plt.plot(df['time'], df['Close'], label='BTCUSDT Close')
plt.plot(df['time'], long_exit, label='Long Exit')
plt.plot(df['time'], short_exit, label='Short Exit')
plt.title('Chandelier Exit Strategy - BTCUSDT')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
```

To
calculate
the
Chandelier
Exit and plot
the
trade
signals
on
a
graph, you
can
modify
the
previous
code as follows:

```python
import pandas as pd
import matplotlib.pyplot as plt


def chandelier_exit(df, atr_period=22, multiplier=3.0):
    high = df['High']
    low = df['Low']
    close = df['Close']

    atr = df['High'].rolling(atr_period).max() - df['Low'].rolling(atr_period).min()
    long_exit = high - atr * multiplier
    short_exit = low + atr * multiplier

    return long_exit, short_exit


# Example data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'Open': [100, 102, 105, 103, 101] * 20,
    'High': [110, 112, 115, 113, 111] * 20,
    'Low': [95, 97, 100, 98, 96] * 20,
    'Close': [105, 107, 110, 108, 106] * 20,
}

df = pd.DataFrame(data)

# Calculate Chandelier Exit
long_exit, short_exit = chandelier_exit(df)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Close')
plt.plot(df['Date'], long_exit, label='Long Exit')
plt.plot(df['Date'], short_exit, label='Short Exit')
plt.title('Chandelier Exit')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot trade signals
for i in range(1, len(df)):
    if df['Close'][i] > long_exit[i - 1]:
        plt.plot(df['Date'][i], df['Close'][i], 'g^', markersize=8)  # Green triangle for long entry
    elif df['Close'][i] < short_exit[i - 1]:
        plt.plot(df['Date'][i], df['Close'][i], 'rv', markersize=8)  # Red triangle for short entry

plt.show()
```

In
this
modified
code, we
first
calculate
the
Chandelier
Exit
values
for long and short exits using the `chandelier_exit` function.

Then, we
plot
the
closing
prices, long
exit
values, and short
exit
values
using
`plt.plot` as before.

Next, we
iterate
over
the
DataFrame
to
identify
the
trade
signals.If
the
closing
price is above
the
previous
long
exit
value, we
plot
a
green
triangle(`'g^'`)
to
indicate
a
long
entry.If
the
closing
price is below
the
previous
short
exit
value, we
plot
a
red
triangle(`'rv'`)
to
indicate
a
short
entry.

Finally, we
display
the
graph
using
`plt.show()`.

This
modified
code
will
plot
the
Chandelier
Exit
values as well as the
trade
signals(long and short
entries) on
the
graph.te that the choice of the `cooldown_period` is subjective and depends on the specific requirements and characteristics of your trading strategy. You may need to experiment with different values to find an appropriate cooldown period that suits your needs.

I
apologize
for the confusion.It seems there was an error in the code logic.To fix the issue and correctly plot the buy and sell signals based on the Chandelier Exit points, you can modify the code as follows:

```python
import pandas as pd
import matplotlib.pyplot as plt


def chandelier_exit(df, atr_period=22, multiplier=3.0):
    high = df['High']
    low = df['Low']

    atr = high.rolling(atr_period).max() - low.rolling(atr_period).min()
    long_exit = high - atr * multiplier
    short_exit = low + atr * multiplier

    return long_exit, short_exit


# Example data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'Open': [100, 102, 105, 103, 101] * 20,
    'High': [110, 112, 115, 113, 111] * 20,
    'Low': [95, 97, 100, 98, 96] * 20,
    'Close': [105, 107, 110, 108, 106] * 20,
}

df = pd.DataFrame(data)

# Calculate Chandelier Exit
long_exit, short_exit = chandelier_exit(df)

# Plotting the Chandelier Exit
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Close')
plt.plot(df['Date'], long_exit, 'g--', label='Long Exit')
plt.plot(df['Date'], short_exit, 'r--', label='Short Exit')
plt.title('Chandelier Exit')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plotting Buy and Sell signals separately
buy_signals = []
sell_signals = []
for i in range(1, len(df)):
    if df['Close'][i] > long_exit[i - 1] and df['Close'][i - 1] <= long_exit[i - 1]:
        buy_signals.append((df['Date'][i], df['Close'][i]))
    elif df['Close'][i] < short_exit[i - 1] and df['Close'][i - 1] >= short_exit[i - 1]:
        sell_signals.append((df['Date'][i], df['Close'][i]))

buy_dates, buy_prices = zip(*buy_signals)
sell_dates, sell_prices = zip(*sell_signals)

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Close')
plt.scatter(buy_dates, buy_prices, color='green', marker='^', label='Buy')
plt.scatter(sell_dates, sell_prices, color='red', marker='v', label='Sell')
plt.title('Buy and Sell Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

plt.show()
```

In
this
modified
code, we
first
calculate
the
Chandelier
Exit
points
using
the
`chandelier_exit`
function.

Then, we
plot
the
Chandelier
Exit
points
on
a
graph as before.

Next, we
iterate
over
the
DataFrame
to
identify
the
buy and sell
signals
based
on
the
Chandelier
Exit
points.We
compare
the
current
closing
price
with the previous closing price to determine the signal.If the current closing price is above the previous long exit point and the previous closing price was below or equal to the previous long exit point, it indicates a buy signal.Similarly, if the current closing price is below the previous short exit point and the previous closing price was above or equal to the previous short exit point, it indicates a sell signal.

We
collect
the
buy and sell
signals in separate
lists(`buy_signals` and `sell_signals`) and extract
the
dates and prices
into
separate
lists(`buy_dates`, `buy_prices`, `sell_dates`, `sell_prices`).

Finally, we
plot
the
closing
prices and plot
the
buy
signals as green
triangles(`'^'`) and the
sell
signals as red
triangles(`'v'`)
on
a
separate
graph.

This
code
will
correctly
plot
the
buy and sell
signals
based
on
the
Chandelier
Exit
points.