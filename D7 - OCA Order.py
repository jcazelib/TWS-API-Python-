"""OCA Order using placeOrder

May be useful for a trader which is already long/short a position (AAPL stock) and is looking to manage risk by adding a profit taker + stop loss
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time

#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-=-==--=-=-INPUTS-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-====-=-=-===-=-==---==
#==================================================================================================================
ticker = "AAPL"    
profittaker = 240
stoploss = 225


#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-EWrapper & EClient requests-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-=-=-=-=-===
#==================================================================================================================
class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
                
    def nextValidId(self, orderId):
        super().nextValidId(orderId)
        self.nextValidOrderId = orderId
        #print("NextValidId:", orderId)

def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

def usTechStk(symbol,sec_type="STK",currency="USD",exchange="SMART"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    return contract 

def limitOrder(direction, quantity, lmt_price):
    order = Order()
    order.action = direction
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = lmt_price
    return order

def profitTaker(direction, quantity):
    order = Order()
    order.action = direction
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = profittaker
    order.ocaGroup = 3                            #String used to identify the OCA group name
    #order.ocaType = 2                            #To specify OCA Type - https://interactivebrokers.github.io/tws-api/oca.html
    order.account = "DU2372888"

    return order

def StopOrder(direction, quantity):
    order = Order()
    order.action = direction
    order.orderType = "STP"
    order.totalQuantity = quantity
    order.auxPrice = stoploss         
    order.ocaGroup = 3                            #String used to identify the OCA group name
    #order.ocaType = 2                            #To specify OCA Type - https://interactivebrokers.github.io/tws-api/oca.html
    order.account = "DU2372888"

    return order


#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-Calling placeOrder-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-====-=-=-=-=-=-===--
#==================================================================================================================
order_id = app.nextValidOrderId
app.placeOrder(order_id, usTechStk(ticker), profitTaker("SELL", 1))        #Profit Taker
app.reqIds(-1)
time.sleep(2)

order_id = app.nextValidOrderId
app.placeOrder(order_id, usTechStk(ticker), StopOrder("SELL", 1))         #Stop Loss
time.sleep(2)









