import collections

try:
    collectionsAbc = collections.abc
except AttributeError:
    collectionsAbc = collections

try:
    from collections.abc import Callable  # noqa
except ImportError:
    from collections import Callable  # noqa

from fastquant import get_stock_data
jfc = get_stock_data("NVDA", "2018-01-01", "2019-01-01")
from fastquant import get_crypto_data

crypto = get_crypto_data("BTC/USDT", "2021-12-01", "2022-02-20")

print(jfc.head())
from fastquant import backtest
#backtest('smac', crypto, fast_period=15, slow_period=40)

backtest('rsi', crypto, rsi_period=14, rsi_upper=70, rsi_lower=30)
