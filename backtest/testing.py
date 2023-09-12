{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "8b3e3944-9a32-4663-aacf-14d66e1829ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[*********************100%***********************]  1 of 1 completed\n"
     ]
    },
    {
     "ename": "KeyError",
     "evalue": "167.12051391601562",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "File \u001b[0;32m~/PycharmProjects/binance/venv/lib/python3.10/site-packages/pandas/core/indexes/base.py:2898\u001b[0m, in \u001b[0;36mIndex.get_loc\u001b[0;34m(self, key, method, tolerance)\u001b[0m\n\u001b[1;32m   2897\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m-> 2898\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_engine\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_loc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcasted_key\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   2899\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n",
      "File \u001b[0;32mpandas/_libs/index.pyx:70\u001b[0m, in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
      "File \u001b[0;32mpandas/_libs/index.pyx:101\u001b[0m, in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
      "File \u001b[0;32mpandas/_libs/hashtable_class_helper.pxi:1675\u001b[0m, in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
      "File \u001b[0;32mpandas/_libs/hashtable_class_helper.pxi:1683\u001b[0m, in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 167.12051391601562",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Input \u001b[0;32mIn [27]\u001b[0m, in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     92\u001b[0m         plt\u001b[38;5;241m.\u001b[39maxhline(y \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m30\u001b[39m, color \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mr\u001b[39m\u001b[38;5;124m'\u001b[39m, linestyle \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mdashed\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m     93\u001b[0m         \u001b[38;5;66;03m# plt.scatter(self.buy_arr.index,self.buy_arr.index,marker='^', c='g')\u001b[39;00m\n\u001b[1;32m     94\u001b[0m         \u001b[38;5;66;03m# plt.scatter(self.sell_arr.index,self.sell_arr.index,marker='v', c='r')\u001b[39;00m\n\u001b[0;32m---> 97\u001b[0m instance \u001b[38;5;241m=\u001b[39m \u001b[43mBacktest\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mETH-USD\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m    101\u001b[0m \u001b[38;5;28mprint\u001b[39m(instance\u001b[38;5;241m.\u001b[39mbuy_arr)\n\u001b[1;32m    103\u001b[0m \u001b[38;5;28mprint\u001b[39m(instance\u001b[38;5;241m.\u001b[39msell_arr)\n",
      "Input \u001b[0;32mIn [27]\u001b[0m, in \u001b[0;36mBacktest.__init__\u001b[0;34m(self, symbol)\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m     15\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcalc_indicators()\n\u001b[0;32m---> 16\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mgenerate_signals\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     17\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mloop_it()\n\u001b[1;32m     18\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprofit\u001b[38;5;241m=\u001b[39mnp\u001b[38;5;241m.\u001b[39mround(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcalc_profit(),\u001b[38;5;241m3\u001b[39m)\n",
      "Input \u001b[0;32mIn [27]\u001b[0m, in \u001b[0;36mBacktest.generate_signals\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     53\u001b[0m     position\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[1;32m     54\u001b[0m     target\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdf\u001b[38;5;241m.\u001b[39mClose \u001b[38;5;241m+\u001b[39m tp\n\u001b[0;32m---> 55\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m position \u001b[38;5;241m&\u001b[39m (\u001b[43mrow\u001b[49m\u001b[43m[\u001b[49m\u001b[43mrow\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mClose\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m]\u001b[49m \u001b[38;5;241m>\u001b[39m target):\n\u001b[1;32m     56\u001b[0m     position\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m\n",
      "File \u001b[0;32m~/PycharmProjects/binance/venv/lib/python3.10/site-packages/pandas/core/series.py:882\u001b[0m, in \u001b[0;36mSeries.__getitem__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    879\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_values[key]\n\u001b[1;32m    881\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m key_is_scalar:\n\u001b[0;32m--> 882\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_get_value\u001b[49m\u001b[43m(\u001b[49m\u001b[43mkey\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    884\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m is_hashable(key):\n\u001b[1;32m    885\u001b[0m     \u001b[38;5;66;03m# Otherwise index.get_value will raise InvalidIndexError\u001b[39;00m\n\u001b[1;32m    886\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m    887\u001b[0m         \u001b[38;5;66;03m# For labels that don't resolve as scalars like tuples and frozensets\u001b[39;00m\n",
      "File \u001b[0;32m~/PycharmProjects/binance/venv/lib/python3.10/site-packages/pandas/core/series.py:990\u001b[0m, in \u001b[0;36mSeries._get_value\u001b[0;34m(self, label, takeable)\u001b[0m\n\u001b[1;32m    987\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_values[label]\n\u001b[1;32m    989\u001b[0m \u001b[38;5;66;03m# Similar to Index.get_value, but we do not fall back to positional\u001b[39;00m\n\u001b[0;32m--> 990\u001b[0m loc \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mindex\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_loc\u001b[49m\u001b[43m(\u001b[49m\u001b[43mlabel\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    991\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mindex\u001b[38;5;241m.\u001b[39m_get_values_for_loc(\u001b[38;5;28mself\u001b[39m, loc, label)\n",
      "File \u001b[0;32m~/PycharmProjects/binance/venv/lib/python3.10/site-packages/pandas/core/indexes/base.py:2900\u001b[0m, in \u001b[0;36mIndex.get_loc\u001b[0;34m(self, key, method, tolerance)\u001b[0m\n\u001b[1;32m   2898\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_engine\u001b[38;5;241m.\u001b[39mget_loc(casted_key)\n\u001b[1;32m   2899\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n\u001b[0;32m-> 2900\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(key) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01merr\u001b[39;00m\n\u001b[1;32m   2902\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m tolerance \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m   2903\u001b[0m     tolerance \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_convert_tolerance(tolerance, np\u001b[38;5;241m.\u001b[39masarray(key))\n",
      "\u001b[0;31mKeyError\u001b[0m: 167.12051391601562"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import ta\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "class Backtest:\n",
    "    def __init__(self, symbol):\n",
    "        self.symbol = symbol\n",
    "        self.df = yf.download(self.symbol, interval = \"1d\",start='2020-01-01',end='2023-1-27')\n",
    "        if self.df.empty:\n",
    "            print('No data pulled')\n",
    "        else:\n",
    "            self.calc_indicators()\n",
    "            self.generate_signals()\n",
    "            self.loop_it()\n",
    "            self.profit=np.round(self.calc_profit(),3)\n",
    "            self.max_dd= self.profit.min()\n",
    "            self.cumul_profit= (self.profit + 1).prod() \n",
    "            self.total=sum(self.profit)\n",
    "\n",
    "\n",
    "\n",
    "    def calc_indicators(self):\n",
    "        self.df['ma_20'] = self.df.Close.rolling(20).mean()\n",
    "        self.df['vol'] = self.df.Close.rolling(20).std()\n",
    "        self.df['upper_bb'] = self.df.ma_20 + (2 * self.df.vol)\n",
    "        self.df['lower_bb'] = self.df.ma_20 - (2 * self.df.vol)\n",
    "        self.df['rsi'] = ta.momentum.rsi(self.df.Close, window=6)\n",
    "        self.df.dropna(inplace=True)\n",
    "\n",
    "    def generate_signals(self):\n",
    "        if self.symbol==\"ETH-USD\":\n",
    "            tp=10\n",
    "        if self.symbol==\"BTC-USD\":\n",
    "            tp=200\n",
    "\n",
    "        conditions = [(self.df.rsi < 30) & (self.df.Close < self.df.lower_bb),\n",
    "                      ((self.df.rsi > 70) & (self.df.Close > self.df.upper_bb))]\n",
    "        #conditions = [(self.df.rsi < 30) & (self.df.Close < self.df.lower_bb),\n",
    "         #             (self.df.rsi > 70) ]\n",
    "        \n",
    "        choices = ['Buy', 'Sell']\n",
    "        self.df['signal'] = np.select(conditions,choices)\n",
    "        self.df.signal=self.df.signal.shift()\n",
    "        self.df.dropna(inplace=True)\n",
    "        target=0\n",
    "        \n",
    "        for index, row in self.df.iterrows():\n",
    "            position= False\n",
    "            if not position and row['signal']== 'Buy':\n",
    "                position=True\n",
    "                target=self.df.Close + tp\n",
    "            if position & (row[row['Close']] > target):\n",
    "                position=False\n",
    "                #self.df['signal']='Sell'\n",
    "                \n",
    "    def loop_it(self):\n",
    "        position = False\n",
    "        buydates,selldates=[],[]\n",
    "        \n",
    "        for index, row in self.df.iterrows():\n",
    "            if not position and row['signal']== 'Buy':\n",
    "                position=True\n",
    "                buydates.append(index)\n",
    "            if position and row['signal']=='Sell':\n",
    "                position=False\n",
    "                selldates.append(index)\n",
    "        \n",
    "        self.buy_arr=self.df.loc[buydates].Open\n",
    "        self.sell_arr=self.df.loc[selldates].Open\n",
    "\n",
    "    def calc_profit(self):\n",
    "        if self.buy_arr.index[-1] > self.sell_arr.index[-1]:\n",
    "            self.buy_arr=self.buy_arr[:-1]\n",
    "        return ((self.sell_arr.values - self.buy_arr.values)/self.buy_arr.values * 100)\n",
    "\n",
    "    def plot_chart(self):\n",
    "        plt.figure(figsize=(10,5))\n",
    "        plt.plot(self.df.Close)\n",
    "        # plt.plot(self.df.lower_bb, color='b')\n",
    "        # plt.plot(self.df.upper_bb, color='r')\n",
    "\n",
    "        plt.scatter(self.buy_arr.index,self.buy_arr.values,marker='^', c='g')\n",
    "        plt.scatter(self.sell_arr.index,self.sell_arr.values,marker='v', c='r')\n",
    "    \n",
    "    def plot_chart_rsi(self):\n",
    "        plt.figure(figsize=(10,5))\n",
    "        plt.plot(self.df.rsi)\n",
    "        plt.axhline(y = 70, color = 'r', linestyle = 'dashed')\n",
    "        plt.axhline(y = 30, color = 'r', linestyle = 'dashed')\n",
    "        # plt.scatter(self.buy_arr.index,self.buy_arr.index,marker='^', c='g')\n",
    "        # plt.scatter(self.sell_arr.index,self.sell_arr.index,marker='v', c='r')\n",
    "\n",
    "    \n",
    "instance = Backtest('ETH-USD')\n",
    "\n",
    "\n",
    "\n",
    "print(instance.buy_arr)\n",
    "\n",
    "print(instance.sell_arr)\n",
    "      \n",
    "print(instance.profit)\n",
    "\n",
    "print(instance.total)\n",
    "\n",
    "instance.plot_chart()\n",
    "\n",
    "instance.plot_chart_rsi()\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2352cd1c-c562-483e-a005-b46e5f2fe2bb",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [5]\u001b[0m, in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mdf\u001b[49m\u001b[38;5;241m.\u001b[39mloc[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m2022-10\u001b[39m\u001b[38;5;124m'\u001b[39m:]\u001b[38;5;241m.\u001b[39mindex[\u001b[38;5;241m2\u001b[39m]\n",
      "\u001b[0;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "93ba2e17-486a-495b-ba0a-94bd19d3b6e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Backtest at 0x12b106170>"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "instance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a1e7d58-1d89-4a69-9743-898d257d1a09",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d03a72cf-a635-4e00-99bd-af8b5fd2f1da",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45fd7c98-3c0c-4a74-82e9-5370817ca275",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
