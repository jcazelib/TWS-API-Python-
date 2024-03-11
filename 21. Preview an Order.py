"""
Preview an order using order.whatIf = True ( https://www.ibkrguides.com/tws/usersguidebook/realtimeactivitymonitoring/checkmargin.htm | https://interactivebrokers.github.io/tws-api/margin.html )
"""

from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def nextValidId(self, orderId):
        self.nextValidOrderId = orderId
        #print("NextValidId:", orderId)
        
    def openOrder(
        self,
        orderId: OrderId,
        contract: Contract,
        order: Order,
        orderState: OrderState,
    ):
        print("")
        print(f"orderId: {orderId}",)
        print(f"Open order: {order} ",)
        print("")
        print("Margin changes:")
        print("  initMarginBefore = ", orderState.initMarginBefore)
        print("  initMarginAfter = ", orderState.initMarginAfter)
        print("  initMarginChange = ",  orderState.initMarginChange)
        print("")
        print("  maintMarginBefore = ", orderState.maintMarginBefore)
        print("  maintMarginAfter = ", orderState.maintMarginAfter)
        print("  maintMarginChange = ",  orderState.maintMarginChange)
        print("")
        print("ELV changes:")
        print("  ELV before = ", orderState.equityWithLoanBefore)
        print("  ELV after = ", orderState.equityWithLoanAfter)
        print("  ELV change = ", orderState.equityWithLoanChange)
        print("")
        print("Expected commissions:")
        print("  Min. Commission =", orderState.minCommission)
        print("  Max. Commission =", orderState.maxCommission)
        print("  Commission =", orderState.commission)
        print("  Commission Currrency =", orderState.commissionCurrency)

def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

def Ticker(symbol):
    contract = Contract()
    contract.symbol = "AAPL"    
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.secType = "STK"
    contract.primaryExchange = "NASDAQ"
    return contract 

def whatIfOrder(quantity, limitPrice):            #What-if order or "margin preview" - https://www.ibkrguides.com/tws/usersguidebook/realtimeactivitymonitoring/checkmargin.htm | https://interactivebrokers.github.io/tws-api/margin.html
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.outsideRth = False
    order.tif="DAY"
    order.account = 'DU2372888'
    order.whatIf = True
    return order


time.sleep(.2)
app.placeOrder(app.nextValidOrderId , Ticker(""), whatIfOrder(100, 100))

