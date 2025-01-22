"""
Place a Limit (LMT) order on AAPL stock via placeOrder - https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-doc/#place-order

EWrapper::openOrder and EWrapper::orderStatus can also be included to retreive order updates via Python - https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-doc/#request-active-orders
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
    
    def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
        print("Open Order. Id:", orderId, contract, order)
        #print(orderId, contract, order, orderState)

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

def stockContract(symbol):
    contract = Contract()
    contract.symbol = symbol
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.secType = "STK"
    contract.primaryExchange = "ISLAND"
    return contract 

def Ticker(symbol,sec_type="STK",currency="USD",exchange="SMART"):
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
    order.tif = 'DAY'
    #order.transmit = False                 #IF set to Fale -> sends the order to TWS, but doesn't transmit     
    return order

time.sleep(.5)

#-----------------------------------------------------------------------------------------------------------------------------------------------
#Rather than specify a single U-account number, allocate to multiple U-accounts via an FA Group or Profile

faGroupOrder = limitOrder("BUY", 10, 1)
faGroupOrder.faGroup = "Group3"            #Name of the FA Group in TWS
faGroupOrder.faMethod = "Equal"            #Equal / AvailableEquity / NetLiq

app.placeOrder(app.nextValidOrderId, Ticker("AAPL"), faGroupOrder)

