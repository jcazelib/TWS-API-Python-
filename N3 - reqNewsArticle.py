"""
reqNewsArticle - After requesting news headlines, the body of a news article can be requested with the article ID returned by invoking this function. The body of the news article is returned to the function EWrapper::newsArticle
"""

from ibapi.client import EClient
from ibapi.wrapper import *
import threading
import time

articleID = "BRFG$1895ccba"


#==================================================================================================================
#--------------------------------------EWrapper Functions----------------------------------------------------------
#==================================================================================================================
class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def newsArticle(self, reqId: int, articleType: int, articleText: str):
        print("NewsArticle. ReqId:", reqId, "ArticleType:", articleType,
              "ArticleText:", articleText)

def websocket_con():
    app.run()        


#==================================================================================================================
#------------------------------reqNewsArticle in order to retreive the body of a news article----------------------
#==================================================================================================================                
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

print("Retreiving the details of article ID", articleID, "......")
time.sleep(2)
app.reqNewsArticle(123, "BRFG", articleID, [])
