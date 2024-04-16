"""
Request open order details via reqOpenOrders / reqAllOpenOrders - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#request-active-orders
"""

from ibapi.client import *
from ibapi.wrapper import *
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
        #print(orderId, contract, order, orderState)
        print("Open Order. Id:", orderId, contract, order)
        
    def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
        print("OrderStatus. Id:", orderId, "Status:", status, "Filled:", decimalMaxString(filled),
                 "Remaining:", decimalMaxString(remaining), "AvgFillPrice:", floatMaxString(avgFillPrice),
                 "PermId:", intMaxString(permId), "ParentId:", intMaxString(parentId), "LastFillPrice:",
                 floatMaxString(lastFillPrice), "ClientId:", intMaxString(clientId), "WhyHeld:",
                 whyHeld, "MktCapPrice:", floatMaxString(mktCapPrice))

def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

#app.reqOpenOrders()
app.reqAllOpenOrders()

time.sleep(1)
