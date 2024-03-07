"""
Sample request for Contract Details (on AAPL Stock) via reqContractDetails - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#contracts | https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#contract-details

Contract Details can also be retreived manually, via TWS - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#tws-contract-details
"""

from ibapi.client import *
from ibapi.wrapper import *

port = 7497

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.contract_counter = 0

    def nextValidId(self, orderId: OrderId):              
        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "STK"
        contract.currency = "USD"
        contract.exchange = "SMART"
        contract.primaryExchange = "ISLAND"
        
        self.reqContractDetails(reqId=123, contract=contract)
        

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        attrs = vars(contractDetails)
        
        print(
            "contractDetails.",
            f"reqId:{reqId}",
            "\n",
            "\n".join(f"{name}: {value}" for name, value in attrs.items()),
        )

        
    def contractDetailsEnd(self, reqId: int):
        print("ContractDetailsEnd. ReqId:", reqId)
        self.disconnect()

   
app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
