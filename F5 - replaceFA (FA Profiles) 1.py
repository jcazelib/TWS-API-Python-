"""
Create FA Profile(s) (i.e. a group of U-accounts) via replaceFA - https://www.ibkrguides.com/tws/usersguidebook/financialadvisors/create%20an%20account%20group%20for%20share%20allocation.htm?Highlight=group | https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#replace-fa
    TWS -> Advisor Setup (top-left corner) -> Create Group / Edit / etc.

Type:
     1 is Percent Based | 2 is Ratio Based | 3 is Contracts/Shares | 4 is Monetary Amount              

This assumes the following setting IS NOT checked:
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
                    , "<ListOfAllocationProfiles>"
                    	, "<AllocationProfile>"
                    		, "<name>PERCENT</name>"
                    		, "<type>1</type>"
                    		, "<ListOfAllocations varName=\"listOfAllocations\">"
                    			, "<Allocation>"
                    				, "<acct>DU2372888</acct>"
                    				, "<amount>80.0</amount>"
                    			, "</Allocation>"
                    			, "<Allocation>"
                    				, "<acct>DU2372889</acct>"
                    				, "<amount>20.0</amount>"
                    			, "</Allocation>"
                    		, "</ListOfAllocations>"
                    	, "</AllocationProfile>"
                        
                    	, "<AllocationProfile>"
                    		, "<name>RATIO</name>"
                    		, "<type>2</type>"
                    		, "<ListOfAllocations varName=\"listOfAllocations\">"
                    			, "<Allocation>"
                    				, "<acct>DU2372888</acct>"
                    				, "<amount>5.0</amount>"
                    			, "</Allocation>"
                    			, "<Allocation>"
                    				, "<acct>DU2372889</acct>"
                    				, "<amount>4.0</amount>"
                    			, "</Allocation>"
                    		, "</ListOfAllocations>"
                    	, "</AllocationProfile>"
                        
                    	, "<AllocationProfile>"
                    		, "<name>CONTRACTS/SHARES</name>"
                    		, "<type>3</type>"
                    		, "<ListOfAllocations varName=\"listOfAllocations\">"
                    			, "<Allocation>"
                    				, "<acct>DU2372888</acct>"
                    				, "<amount>2.0</amount>"
                    			, "</Allocation>"
                    			, "<Allocation>"
                    				, "<acct>DU2372889</acct>"
                    				, "<amount>1.0</amount>"
                    			, "</Allocation>"
                    		, "</ListOfAllocations>"
                    	, "</AllocationProfile>"
                        
                    	, "<AllocationProfile>"
                    		, "<name>CASH</name>"
                    		, "<type>4</type>"
                    		, "<ListOfAllocations varName=\"listOfAllocations\">"
                    			, "<Allocation>"
                    				, "<acct>DU2372888</acct>"
                    				, "<amount>5.0</amount>"
                    			, "</Allocation>"
                    			, "<Allocation>"
                    				, "<acct>DU2372889</acct>"
                    				, "<amount>4.0</amount>"
                    			, "</Allocation>"
                    		, "</ListOfAllocations>"
                    	, "</AllocationProfile>"
                    , "</ListOfAllocationProfiles>"))
        
        
        self.replaceFA(orderId, 2, FaFourProfile)                              #1 for Groups | 2 for Profiles    
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
