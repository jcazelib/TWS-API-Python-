"""
Place a Limit (LMT) order on AAPL stock via placeOrder - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#place-order
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def nextValidId(self, orderId):
        super().nextValidId(orderId)
        self.nextValidOrderId = orderId
        print("NextValidId:", orderId)

def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

def stockContract(symbol):
    contract = Contract()
    contract.symbol = symbol   
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
    #order.account = 'DUXXXX123'      #To specify the U-account number 
    #order.transmit = False           #To send the order to TWS, but not yet transmit it
    return order

time.sleep(.2)
order_id = app.nextValidOrderId     

app.placeOrder(order_id, stockContract("AAPL"), limitOrder(1, 1))  #Place a LMT order (BUY 1 share AAPL @ 1)

#---------------------------------------------------------------------------------------------------------

time.sleep(7)
app.placeOrder(order_id, stockContract("AAPL"), limitOrder(2, 2))   #Modify Order (BUY 1 share @ 1) -> to BUY 2 shares @ 2
print("Order Modified")

#Cancelling orders - https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-doc/#cancel-order


