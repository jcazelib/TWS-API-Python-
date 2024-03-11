"""
Place a Limit (LMT) order on AAPL stock via placeOrder - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#place-order

EWrapper::openOrder and EWrapper::orderStatus can also be included to retreive order updates via Python - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#open-orders
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
        print("NextValidId:", orderId)
        
    # def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
    #     print("OrderStatus. Id:", orderId, "Status:", status)
    #     print("")

def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

def stockContract(symbol):
    contract = Contract()
    contract.symbol = "AAPL"   
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.secType = "STK"
    contract.primaryExchange = "NASDAQ"
    return contract 

def limitOrder(quantity, lmt_price):
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = lmt_price
    order.outsideRth = False
    order.account = ''                #To specify the U-account number 
    #order.transmit = False           #To send the order to TWS, but not yet transmit it
    return order

time.sleep(.2)
order_id = app.nextValidOrderId       #Generate the next order ID programatically 


app.placeOrder(order_id, stockContract(""), limitOrder(1, 1))   #Place a LMT order (BUY 1 share AAPL @ 1)

#---------------------------------------------------------------------------------------------------------

# time.sleep(5)
# app.placeOrder(order_id, stockContract(""), limitOrder(2, 2))   #Modify Order (BUY 1 share @ 1) -> to BUY 2 shares @ 2
# print("Order Modified")

# time.sleep(5)
# app.cancelOrder(order_id, "")   #Cancel Order
# print("Order Canceled")
