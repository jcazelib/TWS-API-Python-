"""
reqMktData - Request contract-specific news headlines, the News Source is identified by the genericTickList. The resulting headlines are returned to EWrapper::tickNews
reqNewsArticle - After requesting news headlines, the body of a news article can be requested with the article ID returned by invoking this function. The body of the news article is returned to the function EWrapper::newsArticle

API news requires news subscriptions that are specific to the API; most news services in TWS are not also available in the API. Beginning in TWS v966, three API news services are enabled in accounts by default and available from the API. They are:
-	Briefing.com General Market Columns (BRFG)
-	Briefing.com Analyst Actions (BRFUPDN)
-	Dow Jones Newsletters (DJNL)
"""

from ibapi.client import *
from ibapi.wrapper import *
import threading
import time

#==================================================================================================================
#--------------------------------------------INPUTS----------------------------------------------------------------
#==================================================================================================================
tickers = ["AAPL"]
articleID = "BRFG$1895ccba"


#==================================================================================================================
#--------------------------------------EWrapper Functions----------------------------------------------------------
#==================================================================================================================
class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def tickNews(self, tickerId: int, timeStamp: int, providerCode: str,
                 articleId: str, headline: str, extraData: str):
        print("TickNews. TickerId:", tickerId, "TimeStamp:", intMaxString(timeStamp),
              "ProviderCode:", providerCode, "ArticleId:", articleId,
              "Headline:", headline, "ExtraData:", extraData)
        print("")
        
    def newsArticle(self, reqId: int, articleType: int, articleText: str):
        print("NewsArticle. ReqId:", reqId, "ArticleType:", articleType,
              "ArticleText:", articleText)
        
def API_contract(symbol, sec_type="STK", currency="USD", exchange="SMART"):
    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    contract.primaryExchange = "ISLAND"
    return contract 

def streamNewsHeadlines(req_num, contract):
    app.reqMktData(reqId=req_num, 
                   contract=contract,
                   genericTickList="mdoff,292:BRFG+DJNL",          #The News Source is identified by the genericTickList
                   snapshot=False,
                   regulatorySnapshot=False,
                   mktDataOptions=[])

def websocket_con():
    app.run()        

#==================================================================================================================
#-----------------------------------------EClient Requests---------------------------------------------------------
#==================================================================================================================               
app = TradingApp()
app.connect(host='127.0.0.1', port=7497, clientId=1) 
time.sleep(1)
con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()


#==================================================================================================================
#--------------------------------------reqMktData for news Headlines-----------------------------------------------
#==================================================================================================================
for ticker in tickers:
    streamNewsHeadlines(tickers.index(ticker), API_contract(ticker))
    time.sleep(2) 


#==================================================================================================================
#------------------------------reqNewsArticle in order to retreive the body of a news article----------------------
#==================================================================================================================
print("Retreiving the details of article ID", articleID, "......")
time.sleep(2)
app.reqNewsArticle(123, "BRFG", articleID, [])
