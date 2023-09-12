import yfinance as yf
import pandas as pd
import numpy as np
import ta
import matplotlib.pyplot as plt


class Backtest:
    def __init__(self, symbol):
        self.symbol = symbol
        self.df = yf.download(self.symbol, start='2022-01-01')
        if self.df.empty:
            print('No data pulled')
        else:
            self.calc_indicators()

    def calc_indicators(self):
        self.df['ma_20'] = self.df.Close.rolling(20).mean()
        self.df['vol'] = self.df.Close.rolling(20).std()
        self.df['upper_bb'] = self.df.ma_20 + (2 * self.df.vol)
        self.df['lower_bb'] = self.df.ma_20 - (2 * self.df.vol)
        self.df['rsi'] = ta.momentum.rsi(self.df.Close, window=6)
        self.df.dropna(inplace=True)

    # def generate_signals(self):
    #     conditions = [(self.df.rsi < 30) & (self.df.Close < self.df.lower_bb),
    #                   (self.df.rsi > 70) & (self.df.Close > self.df.upper_bb)]
    #     choices = ['Buy', 'Sell']
    #     self.df['signal'] = np.


instance = Backtest('ETH-USD')

instance.df