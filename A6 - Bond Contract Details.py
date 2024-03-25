"""
Requests Bond Contract details via reqContractDetails - https://ibkrcampus.com/ibkr-api-page/twsapi-doc/#receive-bond-details

Contract Details can also be retreived manually, via TWS - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#tws-contract-details

For Treasuries:
    contract.symbol = ISIN
    or
    contract.conId = CONID
    
For Corporate Bonds + Muni Bonds:
    contract.symbol = CUSIP
    or
    contract.conId = CONID
"""

from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime
import time

port = 7497

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        contract = Contract()
        contract.symbol = "037833DW7"       #CUSIP / ISIN
        contract.secType = "BOND"
        contract.exchange = "SMART"
        contract.currency = "USD"
        
        # contract = Contract()
        # contract.conId = "420616003"       #CONID
        # contract.exchange = "SMART"
        
        self.reqContractDetails(reqId=orderId, contract=contract)
        
        
    def bondContractDetails(self, reqId: int, contractDetails: ContractDetails):
        attrs = vars(contractDetails)
        
        #To print the full Bond contract details:
        print(
            datetime.now().strftime("%H:%M:%S.%f")[:-3],
            "contractDetails.",
            f"reqId:{reqId}",
            "\n",
            "\n".join(f"{name}: {value}" for name, value in attrs.items()),
        )
        
        #To print specific identifiers:
        print("")
        print("Bond SEC ID List = ", contractDetails.secIdList)
        print("Bond CUSIP = ", contractDetails.cusip)            #may only be delivered with CUSIP market data sub (check secIdList) 
        print("")
        print("Bond details = ", contractDetails.descAppend)



    def contractDetailsEnd(self, reqId: int):
        print("")
        print("ContractDetailsEnd. ReqId:", reqId)
        self.disconnect()
    
time.sleep(2)        
app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()