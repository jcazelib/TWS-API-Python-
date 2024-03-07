from decimal import Decimal
from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime

port = 7497

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        contract = Contract()
        contract.symbol = "AAPL" 
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.secType = "STK"
        contract.primaryExchange = "NASDAQ"
        
        self.reqRealTimeBars(reqId=123, contract=contract, barSize=5,
            whatToShow="TRADES",
            useRTH=True,
            realTimeBarsOptions=[],
        )

    def realtimeBar(self, reqId: TickerId, time: int, open_: float, high: float, low: float, close: float, volume: Decimal, wap: Decimal, count: int):
        print(
            datetime.now().strftime("%H:%M:%S.%f")[:-3], 
            "realtimeBar.",
            f"reqId:{reqId}",
            f"time:{time}",    
            f"Open:{open_}",
            f"High:{high}",
            f"Low:{low}",
            f"Close:{close}", 
            f"Volume:{volume}",
            f"Wap:{wap}",
            f"Count:{count}",
        )
        

app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()


