from flask import Flask, render_template, request, flash, redirect, jsonify, url_for
import function, oo_backtest ,config, csv, datetime
from binance.client import Client
from binance.enums import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from flask_ngrok import run_with_ngrok
import io, random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


app = Flask(__name__)
#run_with_ngrok(app)
app.secret_key = 'ddt98765433224566'

client = Client(config.api_key, config.api_secret)


# def get_plot():
#     data = {
#         'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)
#     }
#     data['b'] = data['a'] + 10 * np.random.randn(50)
#     data['d'] = np.abs(data['d']) * 100
#
#     plt.scatter('a', 'b', c='c', s='d', data=data)
#     plt.xlabel('X label')
#     plt.ylabel('Y label')
#     return plt
#
#
# # Root URL
# def single_converter():
#     # Get the matplotlib plot
#     plot = get_plot()
#
#     # Save the figure in the static directory
#     plot.savefig(os.path.join('static', 'images', 'plot.png'))
#
#     return render_template('matplotlib-plot1.html')
class PageResult:
   def __init__(self, data, page = 1, number = 20):
     self.__dict__ = dict(zip(['data', 'page', 'number'], [data, page, number]))
     self.full_listing = [self.data[i:i+number] for i in range(0, len(self.data), number)]
   def __iter__(self):
     for i in self.full_listing[self.page-1]:
       yield i
   def __repr__(self): #used for page linking
     return "/displayitems/{}".format(self.page+1) #view the next page

@app.route('/displayitems/<pagenum>')
def displayitems(pagenum):
  item_list = ['item1', 'item2', 'item3']
  item_list =[item for item in range(1, 50)]
  return render_template('displayitems.html', listing = PageResult(item_list, int(pagenum)))

def getdata(self):

    self.df = pd.DataFrame(client.get_historical_klines(self.symbol,  self.period, self.start_date, self.end_date))
    self.df = self.df.iloc[:, :6]
    self.df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    self.df.set_index('Time', inplace=True)
    self.df.index = pd.to_datetime(self.df.index, unit='ms')
    self.df = self.df.astype(float)

def setdata(symbol,period,start_date,end_date):
    self.symbol = symbol
    self.period = period
    self.start_date = start_date
    self.end_date = end_date

        #self.df = yf.download(self.symbol, start='2023-07-10',period = "1y",interval = "1h")
    self.getdata()

# @app.route('/plot.png')
# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')
#
# def create_figure():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]
#     axis.plot(xs, ys)
#     return fig
#
# @app.route('/test')
# def chartTest():
#     price=([1,2,3,4],[3,4,5,6])
#     lnprice=np.log(price)
#     plt.plot(lnprice)
#     plt.savefig('/static/images/new_plot.png')
#     return render_template('untitled1.html', name = 'new_plot', url ='/static/images/new_plot.png')
@app.route('/')
def index():
    title = 'Back Testing System'

    account = client.get_account()

    balances = account['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('backtest.html', title=title, my_balances=balances, symbols=symbols)

if __name__=="__main__":
    app.run(port=4000)

@app.route('/buy', methods=['POST'])
def buy():
    print(request.form)
    in_value=""
    pro_count=0
    profits=0
    buyarr=[]
    symbol=request.form['symbol']
    start_date=request.form['start_date']
    end_date=request.form['end_date']
    period=request.form['period']
    rules=request.form['rules']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']
    in_value=(rules,symbol,start_date,end_date,period)
    print(in_value)


    try:
        print(rules)
        if (rules=='1'):
            data=function.getdata(symbol, start_date, end_date, period)

            profits,pro_list,pro_count,buyarr,plt=function.get_rules1(data)
            profits=(profits-1) * 100
            #plot=get_plot(plt)
            #plt.savefig(os.path.join('static', 'images', 'plot.png'))
            print("rules 1")
        if (rules=='2'):
            instance = oo_backtest.Backtest(symbol, start_date, end_date, period)

            print(instance.buy_arr)
            print(instance.buy_arr.index)
            print(instance.sell_arr)
            print(instance.profit)

            buyarr = ((zip(instance.buy_arr.index, instance.buy_arr, instance.sell_arr, instance.profit)))

            print(buyarr)

            profits = (instance.cumul_profit) * 100
            pro_count = ((pd.Series(instance.profit) > 0).value_counts())

            print("rules 2")

        # count_profits=((pd.Series(profits) > 0).value_counts())
        # print((pd.Series(profits) + 1).prod())
        # print((pd.Series(profits) + 1).cumprod())


        print(rules,symbol,start_date,end_date,period)
    except Exception as e:
        flash(e.message, "error")



    return render_template('backtest.html', line=profits, symbols=symbols, in_value=in_value, pro_list=buyarr, pro_count=pro_count)

@app.route('/list')
def list():

    return render_template('style.html')



@app.route('/alert')
def alert():
    return 'alert'

@app.route('/sell')
def sell():
    return 'sell'


@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history')
def history():
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jul, 2020", "12 Jul, 2020")

    processed_candlesticks = []

    for data in candlesticks:
        candlestick = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4]
        }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)