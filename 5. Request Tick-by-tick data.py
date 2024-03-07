"""
Request TWS Time & Sales data (via reqTickByTickData) - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#tick-by-tick
"""

tickers = ["AAPL"]

from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import Contract
import datetime
import threading
import time

class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 
    
    def tickByTickAllLast(self, reqId: int, tickType: int, time: int, price: float, size: Decimal, tickAtrribLast: TickAttribLast, exchange: str,specialConditions: str):
        print(" ReqId:", reqId, "Time:", time, "Price:", floatMaxString(price), "Size:", size, "Exch:" , exchange, "Spec Cond:", specialConditions, "PastLimit:", tickAtrribLast.pastLimit, "Unreported:", tickAtrribLast.unreported)
                
    def tickByTickBidAsk(self, reqId: int, time: int, bidPrice: float, askPrice: float, bidSize: Decimal, askSize: Decimal, tickAttribBidAsk: TickAttribBidAsk):
        print("BidAsk. ReqId:", reqId, "Time:", time, "BidPrice:", floatMaxString(bidPrice), "AskPrice:", floatMaxString(askPrice), "BidSize:", decimalMaxString(bidSize), "AskSize:", decimalMaxString(askSize), "BidPastLow:", tickAttribBidAsk.bidPastLow, "AskPastHigh:", tickAttribBidAsk.askPastHigh)
    
    def tickByTickMidPoint(self, reqId: int, time: int, midPoint: float):
        print("Midpoint. ReqId:", reqId, "Time:", time, "MidPoint:", floatMaxString(midPoint))

def usTechStk(symbol,sec_type="STK",currency="USD",exchange="SMART"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    #contract.primaryExchange = ""
    return contract 

def streamData(req_num,contract):
    app.reqTickByTickData(reqId=req_num, 
                          contract=contract,
                          tickType="Last",
                          numberOfTicks=0,
                          ignoreSize=True)
    
def websocket_con():
    app.run()

app = TradeApp()
app.connect(host='127.0.0.1', port=7497, clientId=23) #port 4002 for ib gateway paper trading/7497 for TWS paper trading
time.sleep(1)
con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()

for ticker in tickers:
    time.sleep(.2)
    streamData(tickers.index(ticker),usTechStk(ticker))
    
