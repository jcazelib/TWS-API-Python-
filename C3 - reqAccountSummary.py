"""
Request Account & Portfolio data via reqAccountSummary - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#requesting-account-summary
"""

from ibapi.client import *
from ibapi.wrapper import *
from ibapi.account_summary_tags import *

port = 7497

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        self.reqAccountSummary(
            reqId=123,
            groupName="All",
            
            tags=AccountSummaryTags.AllTags
            #tags="$LEDGER",  
            #tags="$LEDGER:ALL",  
            #tags="$LEDGER:USD",  
        )

    def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency: str):
        print("AccountSummary. ReqId:", reqId, "Account:", account,"Tag: ", tag, "Value:", value, "Currency:", currency)
 
    def accountSummaryEnd(self, reqId: int):
        print("End of Account Summary")
        self.disconnect()

app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()

