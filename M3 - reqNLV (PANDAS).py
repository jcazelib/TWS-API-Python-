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
#-=-=-=-==---=-=-=-=-======-==-=-=-=-==--=-=-IMPORT PANDAS (for Excel)-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-===
#==================================================================================================================
import pandas as pd
global b1, b2, b3, b4
b1 = []
b2 = []
b3 = []
b4 = []

global c1, c2, c3, c4
c1 = []
c2 = []
c3 = []
c4 = []

df1 = pd.DataFrame()    #NLV
df2 = pd.DataFrame()    #Cash


#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-=-=-EWrapper Functions-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-=====-==-=-=-=--
#==================================================================================================================
class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
              
    def accountUpdateMulti(self, reqId: int, account: str, modelCode: str, key: str, value: str, currency: str):
        if key == "NetLiquidation":
            print("Account:", account, "ModelCode:", modelCode, "Key:", key, "Value:", value, "Currency:", currency)
            nlv_list.append(float(value))
            b1.append(account)
            b2.append(modelCode)
            b3.append(key)
            b4.append("{:,.2f}".format(float(value)))

        if key == "TotalCashValue":
            print("Account:", account, "ModelCode:", modelCode, "Key:", key, "Value:", value, "Currency:", currency)
            cash_list.append(float(value))
            c1.append(account)
            c2.append(modelCode)
            c3.append(key)
            c4.append("{:,.2f}".format(float(value)))
    
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

    app.reqAccountUpdatesMulti(reqId, account1, model, "") 
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

    app.reqAccountUpdatesMulti(reqId, account2, model, "") 
    time.sleep(2)
    reqId+=1
    i+=1
    
time.sleep(1)
app.disconnect()       #NLV & Available Funds snapshots should all have been retreived, so disconnect API client


#==================================================================================================================
#-=-=-=-==---=-=-=-=-======-==-=-=-=-==-MOVE TO EXCEL-==-=-=-===-=-==-=-=-=-----=-=-=-=-==-=-=-=====-==-=-=-=-=-=-=
#==================================================================================================================
from datetime import date
today = str(date.today())            #Returns the current local date
today.replace("-", ".")

print("")
print("For Excel:")
df1['Account'] = b1
df1['Model'] = b2
df1['Metric'] = b3
df1['Value ($)'] = b4

df2['Account'] = c1
df2['Model'] = c2
df2['Metric'] = c3
df2['Value ($)'] = c4

print(df1)
print("")
print(df2)
print("")
# df1.to_csv(f'{account1} {today}.csv', index=False)  #Ouput the Pandas dataframe to excel
# df2.to_csv(f'{account2} {today}.csv', index=False)  



