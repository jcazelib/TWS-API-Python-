"""
Requests open positions in Stocks/Options/Futures/Future Options/Bonds/Cryptocurrencies/etc. (via reqPositions) - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#positions
"""

from ibapi.client import *
from ibapi.wrapper import *
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def position(self, account: str, contract: Contract, position: Decimal, avgCost: float):
        print("Position.", "Account:", account, "Contract:", contract, "Position:", position, "Avg cost:", avgCost)
            
    def positionMulti(self, reqId: int, account: str, modelCode: str, contract: Contract, pos: Decimal, avgCost: float):
       print("PositionMulti. RequestId:", reqId, "Account:", account, "ModelCode:", modelCode, "Contract:", contract, ",Position:", pos, "AvgCost:", avgCost)         
        
    def positionEnd(self):
       print("")
       print("PositionEnd")
       
    def positionMultiEnd(self, reqId: int):
        print("")
        print("PositionMultiEnd. RequestId:", reqId)       
       

def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

app.reqPositions()
#app.reqPositionsMulti(2, "DU2372888", "")  #To specify a U-account number
#app.reqPositionsMulti(3, "Group1", "")     #To specify a Financial Advisor Group / Profile 
time.sleep(1)

