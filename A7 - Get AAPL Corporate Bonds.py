"""
Retreive AAPL Corporate Bonds + identifiers (Contract IDs / CUSIPs / etc.) via reqContractDetails. The data is returned to EWrapper::bondContractDetails specifically - https://ibkrcampus.com/ibkr-api-page/twsapi-doc/#api-introduction
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
        contract.symbol = "MSFT"   
        contract.secType = "BOND"
        contract.exchange = "SMART"
        contract.currency = "USD"
        
        self.reqContractDetails(reqId=12345, contract=contract)
        
        
    def bondContractDetails(self, reqId: int, contractDetails: ContractDetails):
        attrs = vars(contractDetails)
        
        #To print full contract details:
        # print(
        #     "contractDetails.",
        #     f"reqId:{reqId}",
        #     "\n",
        #     "\n".join(f"{name}: {value}" for name, value in attrs.items()),
        # )
        
        print("CONID = ", contractDetails.contract.conId)
        print("Bond details = ", contractDetails.descAppend)
        print("Bond SEC ID List = ", contractDetails.secIdList)
        print("")
                
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