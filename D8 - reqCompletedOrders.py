"""
Request completed orders via reqCompletedOrders - https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-doc/#req-completed-orders
"""

from ibapi.client import *
from ibapi.wrapper import *

port = 7497

class TestApp(EClient, EWrapper):

    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        self.reqCompletedOrders(apiOnly=False)

    def completedOrder(self, contract: Contract, order: Order, orderState: OrderState):
        #print(contract, order, orderState)
        print(contract, order)
        print("OrderID: ", order.orderId)
        print("Time = ", orderState.completedTime)
        print("State = ", orderState.status)
        print("")
        
    # def completedOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
    #     print(orderId, contract, order, orderState)

app = TestApp()
app.connect("127.0.0.1", port, 1)
app.run()
