import yfinance as yf
import pandas as pd


def check_ema_crossover(crypto_list, start_date, end_date):
    result = []

    for crypto in crypto_list:
        data = yf.download(crypto, start=start_date, end=end_date)
        print(data)

        if len(data) >= 50:  # Ensure enough data points for calculations
            ema_10 = data['Close'].ewm(span=10, adjust=False).mean()
            ema_50 = data['Close'].ewm(span=50, adjust=False).mean()

            if ema_10.iloc[-2] < ema_50.iloc[-2] and ema_10.iloc[-1] > ema_50.iloc[-1]:
                result.append(crypto)

    return result


# Example usage
crypto_list = ['BTC-USD', 'ETH-USD', 'LTC-USD']  # List of cryptocurrencies to check
start_date = '2024-01-01'  # Start date of the period
end_date = '2024-02-22'  # End date of the period

crossed_cryptos = check_ema_crossover(crypto_list, start_date, end_date)
print("Cryptocurrencies that crossed above the 50-day EMA:")
print(crossed_cryptos)