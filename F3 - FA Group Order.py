"""
Place an order to be allocated accross multiple U-accounts (or an "FA Group") - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#unification-groups-profiles

NOTE:
TWS > File/Edit (top-left corner) > Global Configuration > API > Settings > “Use Account Groups with Allocation Methods” leave this un-checked if you would like the ability to allocate orders to a group using any allocation method 

Once submitted to TWS, you may double-check the desired allocation via:
TWS > Actvity/Orders panel > right-click on the Order > Check margin/performance profile
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
        self.nextValidOrderId = orderId
        print("NextValidId:", orderId)

def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

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

