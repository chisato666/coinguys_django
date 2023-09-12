# Python program to read CSV file without header

# Import necessary packages
import csv
import yfinance as yf
import numpy as np
import talib

# Open file

buy_count=0
sell_count=0

buy_total=0
sell_total=0
row_count=0

balance=100000
buy_amount=0.2
sell_amount=0.2
stock_avg=0
stock_total=0

buy_ranking=14
sell_ranking=15
closing=2
in_position=False




with open('buy_10d.csv') as file_obj:
    # Skips the heading
    # Using next() method
    heading = next(file_obj)

    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)

    # Iterate over each row in the csv file
    # using reader object
    for row in reader_obj:
        if row_count>0:
            #print("time {} buy_ranking {} sell_ranking {} ".format(row[0],row[20],row[21]))
            if (int(row[buy_ranking])==1):
                if in_position:
                    print("It is overbought, but you already own it.")

                elif balance>(buy_amount *float(row[closing])):
                    buy_total = buy_total + (buy_amount * float(row[closing]))
                    buy_count=buy_count+buy_amount
                    balance=balance - (buy_amount * float(row[closing]))
                    stock_total=stock_total + (buy_amount * float(row[closing]))
                    stock_avg=stock_total / buy_count
                    print("BUY  time {} buy_count {} balance {} price {} stock_avg {} ".format(row[0], buy_count, balance, float(row[closing])  , stock_avg))
                    in_position=True


            if (int(row[sell_ranking])==1 and buy_count>0 and float(row[closing])>stock_avg ):

                if (buy_count >= sell_amount) and in_position:

                    sell_total= sell_total + (sell_amount * float(row[closing]))
                    buy_count=buy_count-sell_amount
                    stock_total=stock_avg * buy_count
                    balance= balance+(sell_amount * float(row[closing]))
                    sell_count=sell_count+1
                    in_position=False
                    print("Sell  time {} buy_count {} balance {} price {} stock_avg {} ".format(row[0], buy_count, balance, float(row[closing])  , stock_avg))
                else:
                    print("It is overbought, but we don't own any")
        row_count=row_count+1



print("buy_total {} buy_count {} sell_total {} sell_count{} balance {} price {} stock_avg {} ".format(buy_total,buy_count,sell_total,sell_count, balance,float(row[closing]),stock_avg))