"""
reqHistoricalNews - Request historical news headlines. The resulting headlines are returned to EWrapper::historicalNews

API news requires news subscriptions that are specific to the API; most news services in TWS are not also available in the API. Beginning in TWS v966, three API news services are enabled in accounts by default and available from the API. They are:
-	Briefing.com General Market Columns (BRFG)
-	Briefing.com Analyst Actions (BRFUPDN)
-	Dow Jones Newsletters (DJNL)
"""

from ibapi.client import EClient
from ibapi.wrapper import *
import threading
import time

#==================================================================================================================
#--------------------------------------EWrapper Functions----------------------------------------------------------
#==================================================================================================================
class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def historicalNews(self, requestId: int, time: int, providerCode: str, articleId: str, headline: str):
        print("historicalNews. RequestId:", requestId, "Time:", time, "ProviderCode:", providerCode, "ArticleId:", articleId, "Headline:", headline)
        print("Article ID = ", articleId)
        print("")
        
    # def historicalDataEnd(self, reqId: int, hasMore: bool):
    #     print("historicalDataEnd. ReqId:", reqId, "Has More:", hasMore)        

def websocket_con():
    app.run()        
               
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(2) 

#==================================================================================================================
#--------------------------------------reqHistoricalNews request---------------------------------------------------
#==================================================================================================================
app.reqHistoricalNews(
    reqId=123, 
    conId=265598,                         #IBKR specific contract identifier for AAPL stock
    providerCodes="BRFG+BRFUPDN+DJNL",    #BRFG+BRFUPDN+DJNL 
    startDateTime="", 
    endDateTime="", 
    totalResults= 10, 
    historicalNewsOptions=[])

time.sleep(1)