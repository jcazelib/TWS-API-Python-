"""
Request Profit & Loss values (PnL) via reqPnL / reqPnLSingle - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#pnl
"""

from ibapi.client import *
from ibapi.wrapper import EWrapper
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def pnl(self, reqId: int, dailyPnL: float, unrealizedPnL: float, realizedPnL: float):
        print("Daily PnL. ReqId:", reqId, "DailyPnL:", dailyPnL, "UnrealizedPnL:", unrealizedPnL, "RealizedPnL:", realizedPnL) 

    def pnlSingle(self, reqId: int, pos: Decimal, dailyPnL: float, unrealizedPnL: float, realizedPnL: float, value: float):
        print("Daily PnL Single. ReqId:", reqId, "Position:", pos, "DailyPnL:", dailyPnL, "UnrealizedPnL:", unrealizedPnL, "RealizedPnL:", realizedPnL, "Value:", value)

app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)
time.sleep(1) 

print("")
app.reqPnL(123, "DU2372889", "")                      #specifying the IBKR Account Number may be required
#app.reqPnLSingle(1234, "DU2372889", "", 265598)   #to specify PnL for a specific security 

app.run()
