"""
Requests Market Depth (Level 2) data via reqMktDepth - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#market-depth
"""

from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import Contract
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
                
    def mktDepthExchanges(self, depthMktDataDescriptions:ListOfDepthExchanges):
        print("MktDepthExchanges:")
        for desc in depthMktDataDescriptions:
            print("DepthMktDataDescription.", desc)
        
    def updateMktDepth(self, reqId: TickerId, position: int, operation: int, side: int, price: float, size: Decimal):
        print("UpdateMarketDepth. ReqId:", reqId, "Position:", position, "Operation:", operation, "Side:", side, "Price:", floatMaxString(price), "Size:", decimalMaxString(size))
    
    def updateMktDepthL2(self, reqId: TickerId, position: int, marketMaker: str, operation: int, side: int, price: float, size: Decimal, isSmartDepth: bool):
        print("UpdateMarketDepthL2. ReqId:", reqId, "Position:", position, "MarketMaker:", marketMaker, "Operation:", operation, "Side:", side, "Price:", floatMaxString(price), "Size:", decimalMaxString(size), "isSmartDepth:", isSmartDepth)
        
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)
time.sleep(2)

contract = Contract()
contract.symbol = "AAPL"
contract.currency = "USD"
contract.secType = "STK"
contract.exchange = "SMART"
contract.primaryExchange = "NASDAQ"


app.reqMktDepth(1, contract, 20, True, [])    
#app.reqMktDepth(2, contract, 20, False, [])   

#app.reqMktDepthExchanges()      #Requests venues for which market data is returned to updateMktDepthL2 (those with market makers)

app.run()
