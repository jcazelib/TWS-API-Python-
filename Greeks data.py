"""
One way to retrieve Option Greeks + Implied Volatility is to use reqMktData for the Option contract - https://ibkrcampus.com/ibkr-api-page/twsapi-doc/#option-greeks |  https://ibkrcampus.com/ibkr-api-page/twsapi-doc/#available-tick-types 
-> Values are returned to EWrapper::tickOptionComputation - https://ibkrcampus.com/ibkr-api-page/twsapi-doc/#receive-options-data 
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
    
    def tickOptionComputation(self, reqId, tickType, tickAttrib, impliedVol, delta, 
                              optPrice, pvDividend, gamma, vega, theta, undPrice):
        """print("TickOptionComputation. TickerId:", reqId, "TickType:", tickType, "ImpliedVolatility:", impliedVol, 
                  "Delta:", delta, "OptionPrice:", optPrice, "pvDividend:", pvDividend, "Gamma: ", gamma, 
                  "Vega:", vega, "Theta:", theta, "UnderlyingPrice:", undPrice)"""
        print("ImpliedVolatility = ", impliedVol)
        print("Option Price = ", optPrice)
        print("UnderlyingPrice = ", undPrice)
        print("Delta = ", delta)
        print("Gamma = ", gamma)
        print("Vega = ", vega)
        print("Theta = ", theta)
        print("")


def usTechOpt(symbol):
    contract = Contract()
    contract.symbol = "AAPL" 
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.secType = "OPT"
    contract.strike = 150
    contract.right = "C"
    contract.lastTradeDateOrContractMonth = "20250117"
    return contract

def streamSnapshotData(tickers):
    for ticker in tickers:
        #app.reqMarketDataType(1)
        app.reqMktData(reqId=tickers.index(ticker), 
                       contract=usTechOpt(ticker),
                       genericTickList="",          
                       snapshot=False,
                       regulatorySnapshot=False,
                       mktDataOptions=[])
            
def connection():
    app.run()

app = TradeApp()
app.connect(host='127.0.0.1', port=7497, clientId=1) 
time.sleep(2)

ConThread = threading.Thread(target=connection)
ConThread.start()

streamSnapshotData(tickers)

