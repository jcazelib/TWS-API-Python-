"""
Request Family Codes (via reqFamilyCodes) - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#family-codes

For instance, if individual account U112233 is under a financial advisor with account number F445566, if the function reqFamilyCodes is invoked for the user of account U112233, the family code “F445566A” will be returned, indicating that it belongs within that account family
"""

from ibapi.client import *
from ibapi.wrapper import *
import time

port = 7497

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def familyCodes(self, familyCodes: ListOfFamilyCode):
        print("")
        print("Family Codes:")
        for familyCode in familyCodes:
            print(familyCode)
        
app = TestApp()   
app.connect('127.0.0.1', port, clientId=1)
time.sleep(.5)

app.reqFamilyCodes()
app.run()
