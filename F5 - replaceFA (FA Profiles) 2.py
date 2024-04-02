"""
Create FA Profile(s) (i.e. a group of U-accounts) via replaceFA - https://www.ibkrguides.com/tws/usersguidebook/financialadvisors/create%20an%20account%20group%20for%20share%20allocation.htm?Highlight=group | https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#replace-fa
   TWS -> Advisor Setup (top-left corner) -> Create Group / Edit / etc.

Available Methods:
   Percent | Ratio | ContractsOrShares | MonetaryAmount             

This assumes the following setting IS checked:
   TWS > File (top-left corner) > Global Configuration > API > Settings > see: Use Account Groups with Allocation Methods   
"""

from ibapi.client import *
from ibapi.wrapper import *
import time

port = 7497 

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        self.nextValidOrderId = orderId
        
        FaFourProfile = "".join(("<?xml version=\"1.0\" encoding=\"UTF-8\"?>"              
                    , "<ListOfGroups>"
                    	, "<Group>"
                    		, "<name>PERCENT</name>"
                    		, "<defaultMethod>Percent</defaultMethod>"
                    		, "<ListOfAccts varName=\"list\">"
                    			, "<Account>"
                    				, "<acct>DU2372888</acct>"
                    				, "<amount>80.0</amount>"
                    			, "</Account>"
                    			, "<Account>"
                    				, "<acct>DU2372889</acct>"
                    				, "<amount>20.0</amount>"
                    			, "</Account>"
                    		, "</ListOfAccts>"
                    	, "</Group>"
                        
                    	, "<Group>"
                    		, "<name>RATIO</name>"
                    		, "<defaultMethod>Ratio</defaultMethod>"
                    		, "<ListOfAccts varName=\"list\">"
                    			, "<Account>"
                    				, "<acct>DU2372888</acct>"
                    				, "<amount>5.0</amount>"
                    			, "</Account>"
                    			, "<Account>"
                    				, "<acct>DU2372889</acct>"
                    				, "<amount>4.0</amount>"
                    			, "</Account>"
                    		, "</ListOfAccts>"
                    	, "</Group>"
                        
                    	, "<Group>"
                    		, "<name>CONTRACTS/SHARES</name>"
                    		, "<defaultMethod>ContractsOrShares</defaultMethod>"
                    		, "<ListOfAccts varName=\"list\">"
                    			, "<Account>"
                    				, "<acct>DU2372888</acct>"
                    				, "<amount>2.0</amount>"
                    			, "</Account>"
                    			, "<Account>"
                    				, "<acct>DU2372889</acct>"
                    				, "<amount>1.0</amount>"
                    			, "</Account>"
                    		, "</ListOfAccts>"
                    	, "</Group>"
                        
                    	, "<Group>"
                    		, "<name>CASH</name>"
                    		, "<defaultMethod>MonetaryAmount</defaultMethod>"
                    		, "<ListOfAccts varName=\"list\">"
                    			, "<Account>"
                    				, "<acct>DU2372888</acct>"
                    				, "<amount>5.0</amount>"
                    			, "</Account>"
                    			, "<Account>"
                    				, "<acct>DU2372889</acct>"
                    				, "<amount>4.0</amount>"
                    			, "</Account>"
                    		, "</ListOfAccts>"
                    	, "</Group>"
                    , "</ListOfGroups>"))
        
        
        self.replaceFA(orderId, 1, FaFourProfile)                     
        print("Processing replaceFA() request", orderId, "...")
        time.sleep(.5)
        print("")
        print("")
        print("New FA Profiles:")
        self.requestFA(FaDataTypeEnum.PROFILES)
        time.sleep(.5)
        self.disconnect()
        
    def receiveFA(self, faData: FaDataType, cxml: str):
        print(cxml)

app = TestApp()
app.connect("127.0.0.1", port, 1)
time.sleep(2)
app.run()