
import function, config, csv, datetime

rules='1'
symbol='ETHUSDT'
start_date='2023-05-01'
end_date='2023-08-01'
period='1h'


profits = function.getdata(symbol, start_date, end_date, period)
print("PROFITS" + str(profits))

