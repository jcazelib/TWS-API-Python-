"""
Historical tick-by-tick/time & sales data (via reqTickByTickData) - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#receiving-time-and-sales
"""

from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import Contract
from datetime import datetime
from datetime import timedelta
import time

port = 7497

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
                
    def historicalTicks(self, reqId: int, ticks: ListOfHistoricalTick, done: bool):
        for tick in ticks:
            print("historicalTicks. ReqId:", reqId, tick)
            
    def historicalTicksBidAsk(self, reqId: int, ticks: ListOfHistoricalTickBidAsk, done: bool):
        for tick in ticks:
            print("historicalTicksBidAsk. ReqId:", reqId, tick)
            
    def historicalTicksLast(self, reqId: int, ticks: ListOfHistoricalTickLast, done: bool):
        for tick in ticks:
           print("HistoricalTickLast. ReqId:", reqId, tick)


app = TradingApp()      
app.connect("127.0.0.1", port, clientId=1)
time.sleep(2)

contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.exchange = "SMART"
contract.currency = "USD"
contract.primaryExchange = "NASDAQ" 


app.reqHistoricalTicks(18001, contract, "20230728 9:30:00 US/Eastern", "", 10, "BID_ASK", 0, False, [])  

time.sleep(2)
app.run()


