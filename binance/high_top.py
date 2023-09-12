# Sure, here's an example Python code that backtests a trading strategy based on the conditions you specified:
#
# ```python
import ccxt
import pandas as pd

# Initialize Binance exchange object
exchange = ccxt.binance()

# Define the symbol and timeframe
symbol = 'BTC/USDT'
timeframe = '1m'

# Load the last year of price data
ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=exchange.milliseconds()-31536000000, limit=525600)

# Convert the price data to a Pandas DataFrame
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# Calculate the high tops for each day
df['day'] = pd.to_datetime(df['timestamp'], unit='ms').dt.date
df_highs = df.groupby('day')['high'].max()

# Initialize variables
position_size = 0
entry_price = 0
stop_loss = 0
take_profit = 0
stop_loss_increase = 0.01
take_profit_increase = 0.01
trades = []

# Simulate the trading strategy
for i in range(1440, len(df)):
    # Check if the last candle is the high top
    if df.iloc[i]['high'] == df_highs[df.iloc[i]['day']]:
        # Check if the next minute's close price is lower than the high top
        if df.iloc[i-1]['close'] < df.iloc[i]['high']:
            # Open a short position
            position_size = 0.01
            entry_price = df.iloc[i]['close']
            stop_loss = entry_price * 1.01
            take_profit = entry_price * 0.99
            stop_loss_increase = 0.01
            take_profit_increase = 0.01
        else:
            continue
    # Check if we have an open position
    if position_size > 0:
        # Check if the stop loss or take profit has been hit
        if df.iloc[i]['low'] <= stop_loss:
            # Hit stop loss, exit position
            pnl = position_size * (stop_loss - entry_price)
            trades.append({'entry_time': df.iloc[i-1]['timestamp'], 'exit_time': df.iloc[i]['timestamp'], 'entry_price': entry_price, 
                           'exit_price': stop_loss, 'pnl': pnl})
            position_size = 0
            entry_price = 0
            stop_loss = 0
            take_profit = 0
            stop_loss_increase = 0.01
            take_profit_increase = 0.01
        elif df.iloc[i]['high'] >= take_profit:
            # Hit take profit, exit position
            pnl = position_size * (take_profit - entry_price)
            trades.append({'entry_time': df.iloc[i-1]['timestamp'], 'exit_time': df.iloc[i]['timestamp'], 'entry_price': entry_price, 
                           'exit_price': take_profit, 'pnl': pnl})
            position_size = 0
            entry_price = 0
            stop_loss = 0
            take_profit = 0
            stop_loss_increase = 0.01
            take_profit_increase = 0.01
        else:
            # Increase the stop loss and take profit by 1% if the price decreases
            if df.iloc[i]['close'] < entry_price * (1 - stop_loss_increase):
                stop_loss = df.iloc[i]['close'] * 1.01
                stop_loss_increase += 0.01
            elif df.iloc[i]['close'] > entry_price * (1 + take_profit_increase):
                take_profit = df.iloc[i]['close'] * 0.99
                take_profit_increase += 0.01

# Calculate performance metrics
total_return = sum([t['pnl'] for t in trades])
winning_trades = [t for t in trades if t['pnl'] > 0]
losing_trades = [t for t in trades if t['pnl'] <= 0]

if len(trades)>0:
    win_rate = len(winning_trades) / len(trades)
    average_win = sum([t['pnl'] for t in winning_trades]) / len(winning_trades)
    average_loss = sum([t['pnl'] for t in losing_trades]) / len(losing_trades)
    max_drawdown = max([sum([t['pnl'] for t in trades[:i]]) for i in range(len(trades))])

# Print performance metrics
print('Total return: {:.2f}%'.format(total_return * 100))
print('Win rate: {:.2f}%'.format(win_rate * 100))
print('Average win: {:.2f}%'.format(average_win * 100))
print('Average loss: {:.2f}%'.format(average_loss * 100))
print('Max drawdown: {:.2f}%'.format(max_drawdown * 100))

# This code uses the CCXT library to interact with the Binance API and fetches the last year of BTC price data for the 1-minute timeframe. It then calculates the high tops for each day and simulates the trading strategy you specified.
#
# The strategy opens a short position when the last candle is the high top and the next minute's close price is lower than the high top. It sets the stop loss at 1% above the entry price and the take profit at 1% below the entry price, and increases the stop loss and take profit by 1% each time the price decreases or increases, respectively.
#
# The code keeps track of the position size, entry price, stop loss, take profit, and stop loss and take profit increase amounts, and exits the position either when the stop loss or take profit is hit, or when a new high top is detected. It records each trade's entry and exit time, entry and exit price, and profit or loss, and calculates the total return, win rate, average win, average loss, and maximum drawdown of the strategy.
#
# Note that this is a very simple example and is meant only as a starting point. You may want to add additional checks and conditions, such as checking for existing open positions, adjusting the stop loss and take profit based on market conditions, or implementing a trailing stop, among others. Additionally, you should always test your trading strategies thoroughly before committing real capital.