"""
Place a VWAP Algo order via placeOrder - https://interactivebrokers.github.io/tws-api/algos.html | https://www.interactivebrokers.com/en/trading/ordertypes.php

Once a Algo order is placed to TWS, you may double-check the details via TWS -> Activity/Orders panel -> right-click on the order -> Modify -> Order Ticket -> IBALGO
"""

from ibapi.client import *
from ibapi.wrapper import *
from ibapi.tag_value import TagValue

port = 7497

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.primaryExchange = "NASDAQ"
        
        order = Order()
        order.action = "BUY"
        order.totalQuantity = 1
        order.orderType = "LMT"
        order.lmtPrice = 1
        order.algoStrategy = "Vwap"
        #order.account = ""           #To specify the U-account number 

        order.algoParams = []
        #order.algoParams.append(TagValue("maxPctVol", .3))
        order.algoParams.append(TagValue("startTime", "20240909 15:15:00 US/Eastern"))
        order.algoParams.append(TagValue("endTime", "20240909 15:30:00 US/Eastern"))
        order.algoParams.append(TagValue("allowPastEndTime",int(0)))
        order.algoParams.append(TagValue("noTakeLiq", int(0)))

        self.placeOrder(orderId, contract, order)   
    

app = TestApp()
app.connect("127.0.0.1", port, 1006)
app.run()

