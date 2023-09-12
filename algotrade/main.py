import yfinance as yf


class balance:
    def __init__(self,currency,amount):
        self.currency=currency
        self.amount=amount

class strategy:
    def __init__(self,start_time,end_time,intraval,balance):
        self.start_time=start_time
        self.end_time=end_time
        self.intraval=intraval
    def run(self,obj):
        print(obj.currency)
        print(obj.amount)


x=balance("BTC",10)
y=strategy('01-11-2020','01-11-2022',"1d",x)
y.run(x)