"""
Request Execution details for filled orders via reqExecutions - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#exec-details
"""

from ibapi.client import *
from ibapi.wrapper import *

port = 7497

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        exec_filter = ExecutionFilter()
        #exec_filter.time = "20221121-0:00:00"    #If you prefer to specify an execution "filter"
        
        self.reqExecutions(123, exec_filter)

    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        print("ExecDetails. ReqId:", reqId, "Symbol:", contract.symbol, "SecType:", contract.secType, "Currency:", contract.currency, execution)
        #print("Filled", execution.shares, "shares", contract.symbol, "@", execution.price)
        #print(execution)
        #print("")
    
    # def commissionReport(self, commissionReport: CommissionReport):
    #     print("CommissionReport.", commissionReport)
        
    def execDetailsEnd(self, reqId: int):
        print("")
        print("ExecDetailsEnd. ReqId:", reqId)


app = TestApp()
app.connect("127.0.0.1", port, 1010)
app.run()
