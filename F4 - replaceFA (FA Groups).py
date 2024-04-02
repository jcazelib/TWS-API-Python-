"""
Create an FA Group (i.e. a group of U-accounts) via replaceFA - https://www.ibkrguides.com/tws/usersguidebook/financialadvisors/create%20an%20account%20group%20for%20share%20allocation.htm?Highlight=group | https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#replace-fa
    TWS -> Advisor Setup (top-left corner) -> Create Group / Edit / etc.
    
Available allocation methods:
   Equal / AvailableEquity / NetLiqs

This assumes the following setting IS NOT checked:
   TWS > File (top-left corner) > Global Configuration > API > Settings > see: Use Account Groups with Allocation Methods   
"""

#NOTE:
#replaceFA will wipe out any existing FA Groups / Profiles (not included in the XML). Be sure to make note of this or export the group before testing with replaceFA

from ibapi.client import *
from ibapi.wrapper import *
import time

port = 7497 

class TestApp(EClient, EWrapper):

    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        self.nextValidOrderId = orderId
        
        FaThreeGroups = "".join(("<?xml version=\"1.0\" encoding=\"UTF-8\"?>"               
                    ,"<ListOfGroups>"            
                                
                        , "<Group>"                                              
                            , "<name>EqualQuantity</name>"              #Name of group 1        
                            , "<ListOfAccts varName=\"list\">"               
                                , "<String>DU2372888</String>"          #U-account IDs for group 1              
                                , "<String>DU2372889</String>"            
                            , "</ListOfAccts>"                               
                            , "<defaultMethod>Equal</defaultMethod>"    #Set the allocation method here - Equal / AvailableEquity / NetLiq
                        , "</Group>"                                    
                                   
                        , "<Group>"                                              
                            , "<name>NetLiquidation</name>"                     
                            , "<ListOfAccts varName=\"list\">"               
                                , "<String>DU2372888</String>"                                
                                , "<String>DU2372889</String>"            
                            , "</ListOfAccts>"                               
                            , "<defaultMethod>NetLiq</defaultMethod>"     
                        , "</Group>"                                    
                    
                        , "<Group>"                                              
                            , "<name>AvailableEquity</name>"                      
                            , "<ListOfAccts varName=\"list\">"               
                                , "<String>DU2372888</String>"                                
                                , "<String>DU2372889</String>"            
                            , "</ListOfAccts>"                               
                            , "<defaultMethod>AvailableEquity</defaultMethod>"     
                        , "</Group>"                                                                
                    , "</ListOfGroups>"))
        
        
        self.replaceFA(orderId, 1, FaThreeGroups)                              #1 for Groups | 2 for Profiles    
        print("Processing replaceFA() request", orderId, "...")
        time.sleep(2)
        print("")
        print("")
        print("New FA Groups:")
        self.requestFA(FaDataTypeEnum.GROUPS)
        time.sleep(2)
        self.disconnect()

    def receiveFA(self, faData: FaDataType, cxml: str):
        print(cxml)

app = TestApp()
app.connect("127.0.0.1", port, 1)
time.sleep(2)
app.run()
