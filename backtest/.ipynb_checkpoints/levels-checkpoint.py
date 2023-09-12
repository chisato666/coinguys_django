{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "329f1ae4-2084-4798-87ea-6d3a557c8c5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from binance.client import Client\n",
    "import numpy as np\n",
    "client= Client()\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "3885fb0d-070e-4d57-9750-a282d64de9db",
   "metadata": {},
   "source": [
    "def getdata(symbol, start):\n",
    "    frame= pd.DataFrame(client.get_historical_klines(symbol,'1h',start))\n",
    "    \n",
    "    \n",
    "    frame= frame.iloc[:,:6]\n",
    "    frame.columns = ['Time','Open','High','Low','Close','Volume']\n",
    "    frame.set_index('Time',inplace=True)\n",
    "    frame.index= pd.to_datetime(frame.index,unit='ms')\n",
    "    frame = frame.astype(float)\n",
    "    return frame\n",
    "\n",
    "def get_levels(date):\n",
    "    values=[-0.618,0.618,1.618]\n",
    "    series_ = df.loc[date:][1:2].squeeze()\n",
    "    diff = series_.High - series_.Low\n",
    "    levels = [series_.Close + i * diff for i in values]\n",
    "    return levels\n",
    "\n",
    "df=getdata('ETHUSDT','2022-01-01')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "9b73f44b-f613-4842-8613-82ea6e14ae3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['price']=df.Open.shift(-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "107cb066-99cc-421d-bc4a-a693ea581bd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "dates = np.unique(df.index.date)\n",
    "\n",
    "buys,sells= [],[]\n",
    "trade_dates = []\n",
    "\n",
    "in_position = False\n",
    "\n",
    "for date in dates:\n",
    "    for index,row in df[date:][2:].iterrows():\n",
    "        if not in_position:\n",
    "            sl,entry,tp = get_levels(date)\n",
    "            if row.Close >= entry:\n",
    "                buys.append(row.price)\n",
    "                trade_dates.append(date)\n",
    "                in_position = True\n",
    "            if in_position:\n",
    "                if row.Close >= tp or row.Close <= sl:\n",
    "                    sells.append(row.price)\n",
    "                    in_position=False\n",
    "                    break\n",
    "trades=pd.DataFrame([buys,sells])\n",
    "trades.columns=trade_dates\n",
    "trades.index = ['Buy','Sell']\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5e00cd6-0894-4e25-be07-84704310d1bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "trades=trades.T"
   ]
  },
  {
   "cell_type": "raw",
   "id": "c0882554-7dc2-4538-aa7e-e0450df6c943",
   "metadata": {},
   "source": [
    "trades['PnL'] = trades.Sell - trades.Buy\n",
    "trades['PnL_rel'] = trades.PnL/trades.Buy\n",
    "print((trades.PnL_rel + 1).cumprod())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d26b31a-307c-499f-85e9-758b73f002d1",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84edddcc-c0a0-4088-b842-2a0e33d6e6db",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "784b57c1-516b-48b9-90e1-6c6bb42f6edd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "raw",
   "id": "2d9bd9af-8d2d-4b02-a456-80b7406eaa02",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68a91339-9c73-4189-b0eb-506430906f8b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "491d8d30-6ce7-4c73-bb56-d25e1bf77e03",
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
