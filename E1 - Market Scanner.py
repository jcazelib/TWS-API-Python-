"""
Simple market scanner for US listed stocks via reqScannerSubscription - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#market-scanner
"""

from ibapi.scanner import ScannerSubscription
from ibapi.tag_value import TagValue
from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from threading import Thread
import time

port = 7497

class StockScanner(EWrapper, EClient):      
    def __init__(self, addr, port, client_id):
        EClient. __init__(self, self)
                
        self.connect(addr, port, client_id)

        thread = Thread(target=self.run)
        thread.start()
        
    def scannerData(self, reqId, rank, details, distance, benchmark, projection, legsStr):
        #Print the symbols in the returned results
        print('{}: {}'.format(rank, details.contract.symbol, distance, benchmark, projection, legsStr))
                
                          
def main():
    client = StockScanner('127.0.0.1', port, 1)
    time.sleep(1)

    ss = ScannerSubscription()
    ss.instrument = 'STK'
    ss.locationCode = 'STK.US.MAJOR'   #Which exchanges would you like to scan?
    ss.scanCode = 'TOP_PERC_GAIN'      #Scan code (see the "Scanner Parameters" xml)
    ss.numberOfRows = 30        
    
    
    tagvalues1 = []
    tagvalues1.append(TagValue('priceBelow', '15'))  


    client.reqScannerSubscription(123, ss, [], tagvalues1)
    time.sleep(5)      

        
       
if __name__ == '__main__':
    main()
    


    
    
    
    
    
    
    
