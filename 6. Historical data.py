"""
Request Historical OHLCV data (via reqHistoricalData) - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#historical-bars
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time

tickers = ["AAPL"]

class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 
        self.data = {}
        
    def historicalData(self, reqId, bar):
        print("HistoricalData. ReqId:", reqId, "BarData.", bar)
        #print(bar)

def stockContract(symbol, sec_type="STK", currency="USD", exchange="SMART"):
    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"
    return contract

def histData(req_num, contract):
    #app.reqMarketDataType(3)
    app.reqHistoricalData(reqId=req_num, 
                          contract=contract,
                          endDateTime='', 
                          durationStr='5 D',
                          barSizeSetting='1 day',
                          whatToShow='Trades',
                          useRTH=0,                 #0 = Includes data outside of RTH | 1 = RTH data only 
                          formatDate=1,    
                          keepUpToDate=0,           #0 = False | 1 = True 
                          chartOptions=[])	 

def websocket_con():
    app.run()
    
app = TradeApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

for ticker in tickers:
    histData(tickers.index(ticker), stockContract(ticker))
    time.sleep(1)
    
    
    
    
    
    
    
    

