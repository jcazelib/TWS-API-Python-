"""
Uses reqPositionsMulti() in order to extract:
    Model Portfolio name(s)
    Model Portfolio position(s) for the inputted account ID(s)
"""

from ibapi.client import *
from ibapi.wrapper import *
import threading
import time

global model_list
model_list = []

#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-=-==--=-=-INPUTS-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-=====-==-=-=-=====-==-
#==================================================================================================================
account1 = "accountId"                    #Account IDs can also be retreived via reqFamilyCodes and/or requestFA(3)
account2 = "accountId"
faAccount = "F-accountId"


#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-=-=-EWrapper Functions-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-=====-==-=-===--
#==================================================================================================================
class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
              
    def positionMulti(self, reqId: int, account: str, modelCode: str, contract: Contract, pos: Decimal, avgCost: float):
       costBasis = float(avgCost)*float(pos)
       costBasisFormatted = "{:,.0f}".format(costBasis)

       if modelCode == "" or modelCode == " " or modelCode == "Core":
           pass
       else:
           if modelCode not in model_list:
               model_list.append(modelCode)
       
       if account == faAccount+"A" and modelCode != "Core":
            print("Account:", account,
                   "ModelCode:", modelCode, "Symbol:", contract.symbol, "SecType:",
                   contract.secType, "Currency:", contract.currency, "Position:",
                   decimalMaxString(pos), "AvgCost:", floatMaxString(avgCost), "CostBasis:", costBasisFormatted)  
      
       if account == account1 or account == account2:
            print("Account:", account,
                   "ModelCode:", modelCode, "Symbol:", contract.symbol, "SecType:",
                   contract.secType, "Currency:", contract.currency, "Position:",
                   decimalMaxString(pos), "AvgCost:", floatMaxString(avgCost), "CostBasis:", costBasisFormatted)          
    
    
#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-=-==-EClient Requests-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-=====-==-=-=-=-==
#==================================================================================================================
def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

#---------------------------------------------------------------------------------------------------------------------------------
print("")
print(f"Grabbing open positions ({faAccount}):")
app.reqPositionsMulti(1, "All", "")

#---------------------------------------------------------------------------------------------------------------------------------
time.sleep(3)
print("")
print(f"Grabbing open positions ({account1}):")
reqId = 2

i=0
while i<len(model_list):
    account = account1
    model = model_list[i]

    app.reqPositionsMulti(reqId, account, model)
    
    reqId+=1
    i+=1
    
#---------------------------------------------------------------------------------------------------------------------------------    
time.sleep(2)
print("")
print(f"Grabbing open positions ({account2}):")
i=0
while i<len(model_list):
    account = account2
    model = model_list[i]

    app.reqPositionsMulti(reqId, account, model)
    
    reqId+=1
    i+=1
    
#---------------------------------------------------------------------------------------------------------------------------------    
time.sleep(2)
print("")
print("Model Portfolio names:")   
for item in model_list:
    print(item )
