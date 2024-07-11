"""
Uses reqAccountUpdatesMulti() in order to extract:
    NLV & TotalCashValue for the inputted account ID(s)
"""

from ibapi.client import *
from ibapi.wrapper import *
import threading
import time

global nlv_list, cash_list
nlv_list = []
cash_list = []

#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-=-==--=-=-INPUTS-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-=====-==-=-=-=====-==-
#==================================================================================================================
account1 = "accountId"                    #Account IDs can also be retreived via reqFamilyCodes and/or requestFA(3)
account2 = "accountId"

model_list = ['Model1', 'Model2', 'Model3', 'Model4']   #Enter models here


#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-=-=-EWrapper Functions-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-=====-==-==-=-==
#==================================================================================================================
class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
              
    def accountUpdateMulti(self, reqId: int, account: str, modelCode: str, key: str, value: str, currency: str):
        if key == "NetLiquidation":
            print("Account:", account, "ModelCode:", modelCode, "Key:", key, "Value:", value, "Currency:", currency)
            nlv_list.append(float(value))
            
        if key == "TotalCashValue":
            print("Account:", account, "ModelCode:", modelCode, "Key:", key, "Value:", value, "Currency:", currency)
            cash_list.append(float(value))
    
    ##### Uncomment this if you're calling reqPositionsMulti() as well #####
    # def positionMulti(self, reqId: int, account: str, modelCode: str, contract: Contract, pos: Decimal, avgCost: float):      
    #    print("Account:", account,
    #          "ModelCode:", modelCode, "Symbol:", contract.symbol, "SecType:",
    #          contract.secType, "Currency:", contract.currency, "Position:",
    #          decimalMaxString(pos), "AvgCost:", floatMaxString(avgCost))  
    
#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-=-==-EClient Requests-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-=====-==-=-=-=-=-
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
print(f"Grabbing NLV & Cash ({account1}):")

reqId = 0
i=0
while i<len(model_list):
    account = account1
    model = model_list[i]

    app.reqAccountUpdatesMulti(reqId, account, model, "") 
    #app.reqPositionsMulti(reqId, account, model)         #to request Open Positions as well 
    time.sleep(2)
    reqId+=1
    i+=1
#---------------------------------------------------------------------------------------------------------------------------------
print("")
print(f"Grabbing NLV & Cash ({account2}):")

i=0
while i<len(model_list):
    account = account2
    model = model_list[i]

    app.reqAccountUpdatesMulti(reqId, account, model, "") 
    #app.reqPositionsMulti(reqId, account, model)         #to request Open Positions as well 
    time.sleep(2)
    reqId+=1
    i+=1
    
time.sleep(1)
app.disconnect()       