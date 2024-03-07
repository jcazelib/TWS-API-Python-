"""
Sample TWS API connection via app.connect()
"""

from ibapi.client import *
from ibapi.wrapper import *
import time

port = 7497

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
          
    
app = TradingApp()      
app.connect("127.0.0.1", port, clientId=1)
app.run()


