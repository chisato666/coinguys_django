from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests

from binance.client import Client
from binance.enums import *
from myapp.include import config, function, oo_backtest, check_decrease_alert
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io, random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime



client = Client(config.api_key, config.api_secret)

from myapp.models import PriceAlert

def show_alert(request):
    alert = PriceAlert(
        symbol='symbol',
        interval='17min',
        percentage_decrease=4,
        timestamp=datetime.now()
    )
    alert.save()
    alerts = PriceAlert.objects.all().order_by('-timestamp')
    context = {'alerts': alerts}
    return render(request, 'show_alert.html', context)

# Create your views here.
def say_hello(request):
    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']
    #print(symbols)
    return render(request,'backtest.html',{'symbols': symbols})

def check_alert(request):

    symbol_list = ["TARA_USDT", "ASTRA_USDT",'GFT_USDT','BTC_USDT','AUCTION_USDT','WEMIX_USDT','ARKM_USDT','CLORE_USDT']  # Add more symbols as needed
    check_decrease_alert.check_price_decrease(symbol_list)
    alerts = PriceAlert.objects.all().order_by('-timestamp')
    context = {'alerts': alerts}
    return render(request, 'show_alert.html', context)


def ajax(request):
    return render(request,'ajax.html')


def submit_backtest(request):

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    if request.method=="POST":
        print(request.POST.get('symbol'))
        rsi=(request.POST.get('RSI'))
        rules=(request.POST.get('rules'))

        symbol = request.POST.get('symbol')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        period = request.POST.get('period')



        try:
            print(rules)
            if (rules == '1'):
                df = function.getdata(symbol, start_date, end_date, period)
                print(df)
                profits, pro_list, pro_count, buyarr, plt = function.get_rules1(df)
                profits = (profits - 1) * 100
                # plot=get_plot(plt)
                # plt.savefig(os.path.join('static', 'images', 'plot.png'))
                print("rules 1")
            if (rules == '2'):
                instance = oo_backtest.Backtest(symbol, start_date, end_date, period)

                print(instance.buy_arr)
                print(instance.buy_arr.index)
                print(instance.sell_arr)
                print(instance.profit)

                buyarr = ((zip(instance.buy_arr.index, instance.buy_arr, instance.sell_arr, instance.profit)))


                profits = (instance.cumul_profit) * 100
                pro_count = ((pd.Series(instance.profit) > 0).value_counts())

                print("rules 2")

            # count_profits=((pd.Series(profits) > 0).value_counts())
            # print((pd.Series(profits) + 1).prod())
            # print((pd.Series(profits) + 1).cumprod())

            # print(rules, symbol, start_date, end_date, period)

        except Exception as e:
            return HttpResponse((e))


    data = {
        "profit": profits,
        "count": pro_count
    }

    context = {"data": data, 'symbols': symbols , 'buyarr': buyarr}
    return render(request,'backtest.html',context)



def get_btcusdt_price(request):
    # Replace YOUR_API_KEY with your actual Binance API key
    # api_key = 'VLQd7y0l2OQhtWZz3TWCjSyV3m7Yuip095BbAjrEZuzcUGl3aSgqR5JkUTbblGrX'
    #
    # # Make a request to Binance API to get the ticker price
    # url = 'https://api.binance.com/api/v3/ticker/price'
    # params = {
    #     'symbol': 'BTCUSDT'
    # }
    # headers = {
    #     'X-MBX-APIKEY': api_key
    # }
    #
    # response = requests.get(url, params=params, headers=headers)
    # data = response.json()
    #btcusdt_price = data['price']


    rate = 0.05
    data = function.get_symbols_with_price_increase(rate)

    # for symbol in data:
    #     symbol_name=symbol[0]
    #     increase_percent=symbol[1]
    # # Extract the price from the response

    # Return the price as a JSON response
    return JsonResponse({'symbol_name': data})


def getProfiles(request):
    rate=0.05
    symbols =function.get_symbols_with_price_increase(rate)

    #print(symbols)
    return JsonResponse({'symbols': list(symbols)})


def list_symbol(request):
    rate=0.05
    symbols =function.get_symbols_with_price_increase(rate)

    #print(symbols)
    return JsonResponse({'symbols': list(symbols)})

# def list_symbol(request):
#     rate=0.05
#     symbols =function.get_symbols_with_price_increase(rate)
#
#     #print(symbols)
#     return render(request,'list_symbol.html',{'symbols': symbols})