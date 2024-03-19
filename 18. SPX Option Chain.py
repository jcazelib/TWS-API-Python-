"""
Retreive the SPX Option Chain (Contract IDs / localSymbols / etc.) for larger chains make sure strike/right/lastTradeDateOrContractMonth are specified - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#option-chain

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
        contract.symbol = "SPX"   
        contract.secType = "OPT"
        contract.exchange = "SMART"
        contract.currency = "USD"
        contract.strike = 5000
        contract.tradingClass = "SPX"
        
        #Optional:
        #contract.lastTradeDateOrContractMonth = "202404"
        #contract.right = "C"
        #contract.strike = 5000
        
        self.reqContractDetails(reqId=12345, contract=contract)
        
        
    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        attrs = vars(contractDetails)
        
        #print("Symbol = ", contractDetails.contract.symbol)
        print(contractDetails.contract.symbol)
        print("localSymbol =", contractDetails.contract.localSymbol)
        print("Expiration = ", contractDetails.contract.lastTradeDateOrContractMonth)
        print("CONID = ", contractDetails.contract.conId)
        print("Trading Class = ", contractDetails.contract.tradingClass)
        print("Multiplier = ", contractDetails.contract.multiplier)
        print("")
        
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
