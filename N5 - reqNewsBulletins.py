"""
reqNewsBulletins - from time to time, IBKR sends out important News Bulletins, which can be accessed via the TWS API through this function. Bulletins are delivered via EWrapper::updateNewsBulletin
"""

from ibapi.client import EClient
from ibapi.wrapper import *
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def updateNewsBulletin(self, msgId: int, msgType: int, newsMessage: str, originExch: str):
        print("News Bulletins. MsgId:", msgId, "Type:", msgType, "Message:", newsMessage, "Exchange of Origin: ", originExch)

def websocket_con():
    app.run()        
               
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

app.reqNewsBulletins(True)