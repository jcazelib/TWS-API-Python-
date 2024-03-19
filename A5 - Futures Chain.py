"""
Retreive the ES Futures chain (Contract IDs / localSymbols) for various ES Futures contracts which are not yet expired - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#option-chain

Uses reqContractDetails
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
        contract.symbol = "ES"
        contract.secType = "FUT"
        contract.exchange = "CME"
        contract.currency = "USD"
        
        #Optional:
        #contract.lastTradeDateOrContractMonth = "202402"
        #contract.includeExpired = True

        self.reqContractDetails(reqId=123, contract=contract)
        
        
    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        attrs = vars(contractDetails)
        print(contractDetails.contract.symbol)
        #print("Symbol = ", contractDetails.contract.symbol)
        print("localSymbol =", contractDetails.contract.localSymbol)
        print("Expiration = ", contractDetails.contract.lastTradeDateOrContractMonth)
        print("CONID = ", contractDetails.contract.conId)
        print("Trading Class = ", contractDetails.contract.tradingClass)
        print("Multiplier = ", contractDetails.contract.multiplier)
        print("" )
        
        #To print full contract details:
        # print(
        #     "contractDetails.",
        #     f"reqId:{reqId}",
        #     "\n",
        #     "\n".join(f"{name}: {value}" for name, value in attrs.items()),
        # )
        
        self.contract_counter += 1
        
        
    def contractDetailsEnd(self, reqId: int):
        print(
            "contractDetailsEnd.",
            f"reqId:{reqId}",
            f"Contract Count:{self.contract_counter}",
        )
        self.disconnect()
 
app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
