"""
Sample TWS API request to retrieve Real FX balances via reqAccountSummary. 

In TWS, RealFX balances may be seen via the TWS "Account Window"
   TWS -> Account (top-left corner) -> Account Window -> Expand & View “Real FX Balances”
"""

from ibapi.client import *
from ibapi.wrapper import EWrapper
import time

port = 7497

global Currencies, Currency_Positions
Currencies = []
Currency_Positions = []

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        self.reqAccountSummary(
            reqId=12345,
            groupName="All",
            tags = "$LEDGER:AED, $LEDGER:AUD, $LEDGER:BGN, $LEDGER:BRL, $LEDGER:CAD, $LEDGER:CHF, $LEDGER:CNH, $LEDGER:CZK, $LEDGER:DKK, $LEDGER:EUR, $LEDGER:GBP, $LEDGER:HKD, $LEDGER:HRK, $LEDGER:HUF, $LEDGER:ILS, $LEDGER:INR, $LEDGER:ISK, $LEDGER:JPY, $LEDGER:KRW, $LEDGER:MXN, $LEDGER:NOK, $LEDGER:NZD, $LEDGER:PLN, $LEDGER:RON, $LEDGER:RUB, $LEDGER:SAR, $LEDGER:SEK, $LEDGER:SGD, $LEDGER:THB, $LEDGER:TRY, $LEDGER:ZAR"
        )
        time.sleep(.2)
        print("")
        print("Real FX balances:")

    def accountSummary(self, reqId: int, account: str, tag: str, value: str,currency: str):
            #print("AccountSummary. ReqId:", reqId, "Account:", account,"Tag: ", tag, "Value:", value, "Currency:", currency)        if tag == "TotalCashBalance":
                
            if tag == "TotalCashBalance" or tag == "TotalCashValue":
                print(account, "-", tag, value, currency)
                Currencies.append(currency)
                Currency_Positions.append(value)

    def accountSummaryEnd(self, reqId: int):
        print("End of Account Summary")
        self.disconnect()                     #Disconnect API client after receiveing Real FX positions
       
app = TestApp()
app.connect("127.0.0.1", port, 1001)
time.sleep(.1)
app.run()

