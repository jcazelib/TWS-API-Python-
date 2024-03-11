"""
Conditional orders samples - https://interactivebrokers.github.io/tws-api/order_conditions.html

Once a Conditional order is placed to TWS, you may double-check the details via TWS -> Activity/Orders panel -> right-click on the order -> Modify -> Order Ticket -> Conditional  
"""

from ibapi.client import *
from ibapi.wrapper import *
import ibapi.order_condition as oc

port = 7497

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        print(f"nextValidId. orderId={orderId}")

        # - Available Conditions - 
        # price_condition = oc.Create(oc.OrderCondition.Price)
        # price_condition.conId = 4391
        # price_condition.exchange = "ISLAND"
        # price_condition.isMore = True
        # price_condition.triggerMethod = 2 # Last price trigger
        # price_condition.price = 133
        # price_condition.isConjunctionConnection = True # True = And, False = Or

        # volume_condition = oc.Create(oc.OrderCondition.Volume)
        # volume_condition.conId = 4391 # AMD
        # volume_condition.exchange = "ISLAND"
        # volume_condition.isMore = True
        # volume_condition.volume = 5000
        # volume_condition.isConjunctionConnection = True # And

        # time_condition = oc.Create(oc.OrderCondition.Time)
        # time_condition.isMore = True # After
        # time_condition.time = "20220112"
        # time_condition.isConjunctionConnection = True # And

        # percent_condition = oc.Create(oc.OrderCondition.PercentChange)
        # percent_condition.conId = 272093 # MSFT
        # percent_condition.exchange = "ISLAND"
        # percent_condition.isMore = True
        # percent_condition.changePercent = 3.0
        # percent_condition.isConjunctionConnection = True
        
        conditions = [
            oc.VolumeCondition(
                conId=4391, 
                exch="SMART", 
                isMore=True, 
                volume=1000000
                
            ).And(),
            oc.PercentChangeCondition(
                conId=4391, 
                exch="ISLAND", 
                isMore=True, 
                changePercent=0.25
                
            ).Or(),
            oc.PriceCondition(
                triggerMethod=2,
                conId=4391,
                exch="ISLAND",
                isMore=False,
                price=4.75,
                
            ).And(),
            oc.TimeCondition(
                isMore=True, 
                time="20170101 09:30:00"
                
            ).And(),
            oc.MarginCondition(
                isMore=False, 
                percent=20             # percentage within a range of (0, 100)
                
            ).Or(),
            oc.ExecutionCondition(
                secType="STK", 
                exch="SMART", 
                symbol="AMD"
            )
        ]

        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.primaryExchange = "NASDAQ"
        
        order = Order()
        order.orderId = orderId
        order.action = "BUY"
        order.orderType = "LMT"
        order.totalQuantity = 1
        order.lmtPrice = 1
        order.tif = "Day"
        order.outsideRth = True
        
        for c in conditions:
            order.conditions.append(c)

        self.placeOrder(orderId, contract, order)


app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
