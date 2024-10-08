"""
reqNewsProviders - Retrieve news sources which you’re currently subscribed to. A list of available subscribed news sources is returned to the function EWrapper::newsProviders
"""

from ibapi.client import EClient
from ibapi.wrapper import *
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def newsProviders(self, newsProviders: ListOfNewsProviders):
        print("NewsProviders: ", newsProviders) 

def websocket_con():
    app.run()        
               
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

app.reqNewsProviders()