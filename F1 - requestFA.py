"""
Request the available FA group/profile names + U-account IDs included in those groups/profiles - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#request-fa
"""

from ibapi.client import *
from ibapi.wrapper import *
import time

port = 7497 

class TestApp(EClient, EWrapper):

    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        self.requestFA(1)                    #Request FA group info.
        self.requestFA(2)                    #Request FA profile info.
        #self.requestFA(3)


    def receiveFA(self, faData: FaDataType, cxml: str):
        if faData==1:
            print("FA Group (1) info received:")
            print(cxml)
            print("")
        elif faData==2:
            print("FA Profile (2) info received:")
            print(cxml)
            print("")
        elif faData==3:
            print("FA Alias (3) info received:")
            print(cxml)      
            print("")

app = TestApp()
app.connect("127.0.0.1", port, 1001)
time.sleep(2)
app.run()
