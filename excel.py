import pandas as pd
import csv
import yfinance as yf

#df = yf.Ticker('BTC-USD').history(period='4y')[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]


df = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "BTC-USD",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "1d",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

#print(df)

csvfile=open('x.csv','w',newline='')
candlestick_writer= csv.writer(csvfile, delimiter=',')
candlestick_writer.writerows(df)
# Create a Pandas dataframe from some data.
#df = pd.DataFrame({'Numbers':    [1010, 2020, 3030, 2020, 1515, 3030, 4545],
#                    'Percentage': [.1,   .2,   .33,  .25,  .5,   .75,  .45 ],
# })

# Create a Pandas Excel writer using XlsxWriter as the engine.
#writer = pd.ExcelWriter("btcusdt-1m1d.xlsx", engine='xlsxwriter')
#
# csvfile = open('15min.csv','w',newline='')
# writer= csv.writer(csvfile, delimiter=',')

# Convert the dataframe to an XlsxWriter Excel object.
#df['Datetime'] = df['Datetime'].dt.tz_localize(None)

#df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
#workbook  = writer.book
#worksheet = writer.sheets['Sheet1']

# Add some cell formats.
# format1 = workbook.add_format({'num_format': '#,##0.00'})
# format2 = workbook.add_format({'num_format': '0%'})

# Note: It isn't possible to format any cells that already have a format such
# as the index or headers or any cells that contain dates or datetimes.

# Set the column width and format.
#worksheet.set_column(1, 1, 18, format1)

# Set the format but not the column width.
#worksheet.set_column(2, 2, None, format2)

# Close the Pandas Excel writer and output the Excel file.
#writer.save()