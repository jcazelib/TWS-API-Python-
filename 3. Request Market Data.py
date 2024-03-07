"""
Requests TWS (Watchlist) market data - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#available-tick-types | https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#watchlist-data

EWrapper methods:
tickPrice - Handles all price-related ticks. A tickPrice value of -1 or 0 followed by a tickSize of 0 indicates there is no data for this field currently available
tickSize - Handles all size-related ticks (Bid Size / Volume / Last Size etc.)
tickString - Handles certain market data ticks (Bid Exchange / UNIX Timestamp of the last trade / IB Dividends / etc.)
tickGeneric - Handles certain market data ticks (Shortable status / Halted status / etc.)
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time

#tickers = ["A", "AAPL", "B", "TSLA", "ZM"]
tickers = ["AAPL"]

class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 

    def tickPrice(self, reqId, tickType, price, attrib):
        print("TickPrice. TickerId:", reqId, "tickType:", tickType, "Price:", price)
        
    # def tickSize(self, reqId, tickType, size):
    #     print("TickSize. TickerId:", reqId, "TickType:", tickType, "Size: ", '{:0,.0f}'.format(size))

    # def tickString(self, reqId, tickType, value: str):
    #     print("TickString. TickerId:", reqId, "Type:", tickType, "Value:", value)
    
    # def tickGeneric(self, reqId, tickType, value: float):
    #     print("TickGeneric. TickerId:", reqId, "TickType:", tickType, "Value:", '{:0,.0f}'.format(value))    
    
def stockContract(symbol, sec_type="STK", currency="USD", exchange="SMART"):
    contract = Contract()
    contract.symbol = symbol
    contract.currency = currency
    contract.secType = sec_type
    contract.exchange = exchange
    return contract 

def streamMarketData(req_num,contract):
    #app.reqMarketDataType(3)
    app.reqMktData(reqId=req_num, 
                   contract=contract,
                   genericTickList="",      #Refer to "Generic tick required" here - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#available-tick-types
                   snapshot=False,
                   regulatorySnapshot=False,
                   mktDataOptions=[])
    
def websocket_con():
    app.run()

app = TradeApp()
app.connect(host='127.0.0.1', port=7497, clientId=1) 
time.sleep(1)
con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1)


for ticker in tickers:
    streamMarketData(tickers.index(ticker), stockContract(ticker))

    
