from decimal import Decimal
from pickle import FALSE, TRUE
from tkinter.tix import Tree
from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime
from ibapi.contract import *
from ibapi.order_condition import Create, OrderCondition
import time

port = 7497

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        print(f"nextValidId. orderId={orderId}")

        ###################################### Contracts ###################################################
        parent = Contract()
        parent.conId = 29831612        #DPZ (Domino's Pizza)
        parent.exchange = "SMART"

        hedgeChild = Contract()
        hedgeChild.conId = 273538      #PZZA (Papa John's)
        hedgeChild.exchange = "SMART"
        
        ###################################### Parent Order ###################################################
        parentOrder = Order()
        parentOrder.orderId = orderId
        parentOrder.action = "BUY"
        parentOrder.orderType = "MKT"
        #parentOrder.orderType = "LMT"
        #parentOrder.lmtPrice = 400
        
        parentOrder.totalQuantity = 1
        parentOrder.transmit = False
        #parentOrder.account = ""
        ###################################### Hedged Child Order ###################################################
        hedgeChildOrder = Order()
        hedgeChildOrder.orderId = orderId + 1
        hedgeChildOrder.parentId = orderId
        hedgeChildOrder.action = "SELL"
        hedgeChildOrder.orderType = "MKT"
        hedgeChildOrder.hedgeType = "P"        #P for Pair Trade
        hedgeChildOrder.hedgeParam = 5         #Hedge Ratio
        hedgeChildOrder.transmit = True
        #hedgeChildOrder.account = ""
        hedgeChildOrder.totalQuantity = 0      #may not be required
        ###################################### Executions ###################################################
        
        self.placeOrder(parentOrder.orderId, parent, parentOrder)               #parentOrder
        time.sleep(.2)                                                          #may not be required
        self.placeOrder(hedgeChildOrder.orderId, hedgeChild, hedgeChildOrder)   #hedgeChildOrder


    def openOrder(
        self,
        orderId: OrderId,
        contract: Contract,
        order: Order,
        orderState: OrderState,
    ):
        print(
            "openOrder.",
            f"orderId:{orderId}",
            f"contract:{contract}",
            f"order:{order}",
            # f"orderState:{orderState}",
        )

    def orderStatus(
        self,
        orderId: OrderId,
        status: str,
        filled: Decimal,
        remaining: Decimal,
        avgFillPrice: float,
        permId: int,
        parentId: int,
        lastFillPrice: float,
        clientId: int,
        whyHeld: str,
        mktCapPrice: float,
    ):
        print(
            "orderStatus.",
            f"orderId:{orderId}",
            f"status:{status}",
            f"filled:{filled}",
            f"remaining:{remaining}",
            f"avgFillPrice:{avgFillPrice}",
            # f"permId:{permId}",
            f"parentId:{parentId}",
            f"lastFillPrice:{lastFillPrice}",
            # f"clientId:{clientId}",
            # f"whyHeld:{whyHeld}",
            # f"mktCapPrice:{mktCapPrice}",
        )

app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
