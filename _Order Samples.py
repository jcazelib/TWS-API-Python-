"""
API order samples using app.placeOrder - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#place-order | https://interactivebrokers.github.io/tws-api/basic_orders.html

Sections:
   1. Common Order types
   2. Additional Order attrbiutes
   3. Algo Order samples 
   4. Cryptocurrency orders (MKT & LMT)


Available Time-in-force (order.tif) values - https://ibkrguides.com/tws/usersguidebook/ordertypes/time%20in%20force%20for%20orders.htm
"""

from ibapi.contract import Contract
from ibapi.order import Order

contract = Contract()
contract.symbol = "TSLA"
contract.secType = "STK"
contract.exchange = "SMART"
contract.currency = "USD"
contract.primaryExchange = "NASDAQ" 

#How to use below functions: 
#self.placeOrder(order_id, contract, marketOrder(1))                 MKT
#self.placeOrder(order_id, contract, limitOrder(1, 1))               LMT
#self.placeOrder(order_id, contract, stopOrder(1, 1))                STP
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1. Common Order types (MKT | LMT | STP | STP LMT | TRAIL | TRAIL LMT | MOO | MOC | LOO | LOC | MIT | LIT) - https://interactivebrokers.github.io/tws-api/basic_orders.html

def marketOrder(quantity):                              #Market (MKT) order - https://www.interactivebrokers.com/en/trading/orders/market.php
    order = Order()
    order.action = "BUY"
    order.orderType = "MKT" 
    order.totalQuantity = quantity
    order.account = ''
    return order

def limitOrder(quantity, limitPrice):                   #Limit (LMT) order - https://www.interactivebrokers.com/en/trading/orders/limit.php
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.outsideRth = False
    order.tif="DAY"
    order.account = ''
    return order

def stopOrder(quantity, triggerPrice):                  #Stop loss (STP) order - https://www.interactivebrokers.com/en/trading/orders/stop.php
    order = Order()
    order.action = "BUY"
    order.orderType = "STP"
    order.totalQuantity = quantity
    order.auxPrice = triggerPrice
    order.account = ''
    return order

def stopLimitOrder(quantity, limitPrice, triggerPrice):   #Stop limit (STP LMT) order - https://www.interactivebrokers.com/en/trading/orders/stop-limit.php
    order = Order()
    order.action = "BUY"
    order.orderType = "STP LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.auxPrice = triggerPrice
    order.account = ''
    return order

def trailStopOrder(quantity, trailingStopPrice):           #Trailing Stop (TRAIL) order - https://www.interactivebrokers.com/en/trading/orders/trailing-stops.php
    order = Order()
    order.action = "BUY"
    order.orderType = "TRAIL"
    order.totalQuantity = quantity
    order.auxPrice = trailingStopPrice
    #order.TrailingPercent  = trailingPercent              #Trailing % can also be specified https://interactivebrokers.github.io/tws-api/classIBApi_1_1Order.html#ab6dd5e6425dcafecaf83c03d97688b92
    order.account = ''
    return order

def trailStopLimitOrder(quantity, trailingStopPrice, trailingAmount, lmtOffset):      #Trailing Stop Limit (TRAIL LMT) order - https://www.interactivebrokers.com/en/trading/orders/trailing-stop-limit.php
    order = Order()
    order.action = "BUY"
    order.orderType = "TRAIL LIMIT"
    order.totalQuantity = quantity
    order.trailStopPrice = trailingStopPrice
    order.auxPrice = trailingAmount
    order.lmtPriceOffset = lmtOffset
    order.account = ''
    return order

def whatIfOrder(quantity, limitPrice):            #What-if order or "margin preview" - https://www.ibkrguides.com/tws/usersguidebook/realtimeactivitymonitoring/checkmargin.htm | https://interactivebrokers.github.io/tws-api/margin.html
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.outsideRth = False
    order.tif="DAY"
    order.account = ''
    order.whatIf = True
    return order

def mooOrder(quantity):                         #Market on open (MKT) order - https://www.interactivebrokers.com/en/trading/orders/moo.php
    order = Order()
    order.action = "BUY"
    order.orderType = "MKT"
    order.totalQuantity = quantity
    order.account = ''
    order.tif="OPG"                             
    return order

def looOrder(quantity, limitPrice):              #Limit on open (LMT) order - https://www.interactivebrokers.com/en/trading/orders/loo.php
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.auxPrice = limitPrice
    order.tif="OPG"
    order.account = ''
    return order

def mocOrder(quantity):                         #Market on close (MOC) order - https://www.interactivebrokers.com/en/trading/orders/moc.php
    order = Order()
    order.action = "BUY"
    order.orderType = "MOC"
    order.totalQuantity = quantity
    order.account = ''
    return order

def locOrder(quantity, limitPrice):              #Limit on close (LOC) order - https://www.interactivebrokers.com/en/trading/orders/loc.php
    order = Order()
    order.action = "BUY"
    order.orderType = "LOC"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.account = ''
    return order

def mitOrder(quantity, triggerPrice):            #Market if touched (MIT) order - https://www.interactivebrokers.com/en/trading/orders/mit.php
    order = Order()
    order.action = "BUY"
    order.orderType = "MIT"
    order.totalQuantity = quantity
    order.auxPrice = triggerPrice
    order.account = ''
    return order

def litOrder(quantity, limitPrice, triggerPrice):  #Limit if touched (LIT) order - https://www.interactivebrokers.com/en/trading/orders/lit.php
    order = Order()
    order.action = "BUY"
    order.orderType = "LIT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.auxPrice = triggerPrice
    order.account = ''
    return order

def mtlOrder(quantity, limitPrice, triggerPrice):    #Market to Limit (MTL) order - https://www.interactivebrokers.com/en/trading/orders/mtl.php
    order = Order()
    order.action = "BUY"
    order.orderType = "MTl"
    order.totalQuantity = quantity
    order.account = ''
    return order

def relativeOrder(quantity, priceCap, offsetAmount):  #Relative/Pegged to Primary (REL) order - https://www.interactivebrokers.com/en/trading/orders/pegged-to-primary.php
    order = Order()
    order.action = "BUY"
    order.orderType = "REL"
    order.totalQuantity = quantity
    order.lmtPrice = priceCap
    order.auxPrice = offsetAmount
    order.account = ''
    return order

def cashQtyOrder(cashquantity, limitPrice):         #LMT order using cashQty (cash quantity) instead of share quantity | TWS > File/Edit (top-left corner) > Global Configuration > Presets > Stocks > Size (section) > see "Cash Quantity Estimate Factor" (estFactor) > acceptable values are 5% - 100%  
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = 0                         #Must be 0 for cashQty orders
    order.cashQty = cashquantity
    order.lmtPrice = limitPrice
    order.account = ''
    return order

def pegMktOrder(quantity, offsetAmount):             #Pegged to Market (PEG MKT) order - https://www.interactivebrokers.com/en/trading/orders/pegged-to-market.php
    order = Order()   
    order.action = "BUY"
    order.orderType = "PEG MKT"
    order.totalQuantity = quantity
    order.auxPrice = offsetAmount
    order.account = ''
    return order

def pegStockOrder(quantity, dlta, stockReferencePrice, startingPrice):         #Pegged to Stock (PEG STK) order - https://www.interactivebrokers.com/en/trading/orders/pegged-to-stock.php 
    order = Order()   
    order.action = "BUY"
    order.orderType = "PEG STK"
    order.totalQuantity = quantity
    order.delta = dlta
    order.stockRefPrice  = stockReferencePrice
    order.startingPrice = startingPrice
    order.account = ''
    return order

def pegMidOrder(quantity, limitPrice, offsetAmount):             #Pegged to Midpoint (PEG MID) order - https://www.interactivebrokers.com/en/trading/orders/pegged-to-midpoint.php
    order = Order()   
    order.action = "BUY"
    order.orderType = "PEG MID"
    order.totalQuantity = quantity
    order.lmtPrice  = limitPrice
    order.auxPrice = offsetAmount
    order.account = ''
    return order

#For all other samples (for more obscure order types - C:\TWS API\samples\Python\Testbed )
#-----------------------------------------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Additional order attributes

def outsideRthLimitOrder(quantity, limitPrice):
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.outsideRth = True                #To specify "allow this order to fill outside of regular trading hours"
    order.tif="DAY"
    order.account = ''
    return order

def atsLimitOrder(quantity, limitPrice):   #Used with contract.exchange = "IBKRATS" - https://www.interactivebrokers.com/en/trading/orders/ibkrats.php | https://interactivebrokers.github.io/tws-api/ibkrats.html
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.notHeld = True
    return order

def pmaLimitOrder(quantity, limitPrice): 
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.usePriceMgmtAlgo = True          #Uses IBKR's Price Management algo - https://interactivebrokers.github.io/tws-api/classIBApi_1_1Order.html#aa2951544e2b775b4fc971cbdc43f01e0
    order.account = ''
    return order

def refLimitOrder(quantity, limitPrice):
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.orderRef = "Random strings are Ok here"    #Specify a random string/order reference which will be shown in TWS
    order.account = ''
    return order

def hiddenLimitOrder(quantity, limitPrice):
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.hidden = True
    #order.displaySize = 50        #Set a publicly disclosed order size < actual order size - https://interactivebrokers.github.io/tws-api/classIBApi_1_1Order.html#a87316898d4e44f4537555f5999088457 
    order.account = ''
    return order

def gtdLimitOrder(quantity, limitPrice):
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.outsideRth = False
    order.goodTillDate = "20240408 10:23:00 US/Eastern"     #Enter date+time for which the order will work until (end time / good until date) - https://www.interactivebrokers.com/en/trading/orders/gtd.php
    order.tif = "GTD"
    return order

def gatLimitOrder(quantity, limitPrice):
    order = Order()
    order.action = "BUY"
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.outsideRth = False
    order.goodAfterTime = "20240408 10:23:00 US/Eastern"     #Enter date+time (start time) for the order - https://www.interactivebrokers.com/en/trading/orders/gat.php
    return order
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. Algo order samples - https://interactivebrokers.github.io/tws-api/algos.html 

# Once an Algo order is placed to TWS, you may double-check the details via:
#   TWS -> Activity/Orders panel -> right-click on the order -> Modify -> Order Ticket -> IBALGO

from ibapi.tag_value import TagValue


#VWAP algo (for Stocks/Futures) - https://www.interactivebrokers.com/en/trading/orders/vwap-algo.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"
order.lmtPrice = 1
order.algoStrategy = "Vwap"

order.algoParams = []
order.algoParams.append(TagValue("maxPctVol", .3))
order.algoParams.append(TagValue("startTime", "20240909 15:15:00 US/Eastern"))
order.algoParams.append(TagValue("endTime", "20240909 15:30:00 US/Eastern"))
order.algoParams.append(TagValue("allowPastEndTime",int(0)))
order.algoParams.append(TagValue("noTakeLiq", int(0)))
order.algoParams.append(TagValue("speedUp", int(0)))
#self.placeOrder(orderId, contract, order)                                     #To place the algo order


#Adaptive algo (for Stocks/Options/Futures) - https://www.interactivebrokers.com/en/trading/orders/adaptive-algo.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            #MKT or LMT
order.lmtPrice = 1
order.algoStrategy = "Adaptive"
         
order.algoParams = []
order.algoParams.append(TagValue("adaptivePriority", "Urgent"))



#Arrival price algo  (for Stocks/Forex) - https://www.interactivebrokers.com/en/trading/orders/arrival-price.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "ArrivalPx"
           
order.algoParams = []
order.algoParams.append(TagValue("maxPctVol", .3))
order.algoParams.append(TagValue("riskAversion", "Aggressive"))
order.algoParams.append(TagValue("startTime", "20240909 15:15:00 US/Eastern"))
order.algoParams.append(TagValue("endTime", "20240909 15:30:00 US/Eastern"))
order.algoParams.append(TagValue("allowPastEndTime",int(0)))
order.algoParams.append(TagValue("forceCompletion", int(0)))



#Close price algo  (for Stocks/Options) - https://www.interactivebrokers.com/en/trading/orders/close-price-strategy.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "ClosePx"
           
order.algoParams = []
order.algoParams.append(TagValue("maxPctVol", .3))
order.algoParams.append(TagValue("riskAversion", "Aggressive"))
order.algoParams.append(TagValue("startTime", "20240909 15:15:00 US/Eastern"))
order.algoParams.append(TagValue("forceCompletion", int(0)))



#Midprice algo  (for Stocks) - https://www.interactivebrokers.com/en/trading/orders/midprice.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "MIDPRICE"            
order.lmtPrice = 1            #Set an optional price cap to define the highest price (for a buy order) or the lowest price (for a sell order) you are willing to accept



#DarkIce algo  (for Stocks/Futures) - https://www.interactivebrokers.com/en/trading/orders/dark-ice.php
order = Order()
order.action = "BUY"
order.totalQuantity = 100
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "DarkIce"

order.algoParams = []
order.algoParams.append(TagValue("displaySize", 50))
order.algoParams.append(TagValue("startTime", "20240909 15:15:00 US/Eastern"))
order.algoParams.append(TagValue("endTime", "20240909 15:30:00 US/Eastern"))
order.algoParams.append(TagValue("allowPastEndTime",int(0)))



#Accumulate/Distribute algo  (for Stocks/Options/Futures/Forex/Bonds/FOPs/Warrants) - https://www.interactivebrokers.com/en/trading/accumulate-distribute.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "AD"

order.algoParams = []
order.algoParams.append(TagValue("componentSize", 100))
order.algoParams.append(TagValue("timeBetweenOrders", 30))   #Time interval in seconds between each order	
order.algoParams.append(TagValue("randomizeTime20", 1))
order.algoParams.append(TagValue("randomizeSize55", 0))
#order.algoParams.append(TagValue("giveUp", ))
order.algoParams.append(TagValue("catchUp", 1))
order.algoParams.append(TagValue("waitForFill", 1))
order.algoParams.append(TagValue("activeTimeStart", "15:58:59"))
order.algoParams.append(TagValue("activeTimeEnd", "15:59:59"))



#Percentage of Volume algo  (for Stocks/Futures) - https://www.interactivebrokers.com/en/trading/orders/percent-of-volume.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "PctVol"

order.algoParams = []
order.algoParams.append(TagValue("pctVol", .3))
order.algoParams.append(TagValue("startTime", "20240909 15:15:00 US/Eastern"))
order.algoParams.append(TagValue("endTime", "20240909 15:30:00 US/Eastern"))
order.algoParams.append(TagValue("noTakeLiq", int(0)))



#TWAP algo may be DEPRECATED (for Stocks/Options/Futures/Forex) - https://www.interactivebrokers.com/en/trading/orders/twap-algo.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "Twap"

order.algoParams = []
order.algoParams.append(TagValue("strategyType", "Marketable"))
order.algoParams.append(TagValue("startTime", "20240909 15:15:00 US/Eastern"))
order.algoParams.append(TagValue("endTime", "20240909 15:30:00 US/Eastern"))
order.algoParams.append(TagValue("allowPastEndTime",int(0)))



#Price Variant Percentage of Volume Strategy algo  - https://www.interactivebrokers.com/en/trading/orders/variant-algos.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "PctVolPx"

order.algoParams = []
order.algoParams.append(TagValue("pctVol", .3))
order.algoParams.append(TagValue("deltaPctVol", .3))
order.algoParams.append(TagValue("minPctVol4Px", .2))
order.algoParams.append(TagValue("maxPctVol4Px", .3))
order.algoParams.append(TagValue("startTime", "20240909 15:15:00 US/Eastern"))
order.algoParams.append(TagValue("endTime", "20240909 15:30:00 US/Eastern"))
order.algoParams.append(TagValue("noTakeLiq", int(0)))



#Size Variant Percentage of Volume Strategy algo  - https://www.interactivebrokers.com/en/trading/orders/variant-algos.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "PctVolSz"

order.algoParams = []
order.algoParams.append(TagValue("startPctVol", .1))
order.algoParams.append(TagValue("endPctVol", .3))
order.algoParams.append(TagValue("startTime", "20240909 15:15:00 US/Eastern"))
order.algoParams.append(TagValue("endTime", "20240909 15:30:00 US/Eastern"))
order.algoParams.append(TagValue("noTakeLiq", int(0)))



#Time Variant Percentage of Volume Strategy algo  - https://www.interactivebrokers.com/en/trading/orders/variant-algos.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "PctVolTm"

order.algoParams = []
order.algoParams.append(TagValue("startPctVol", .1))
order.algoParams.append(TagValue("endPctVol", .3))
order.algoParams.append(TagValue("startTime", "20240909 15:15:00 US/Eastern"))
order.algoParams.append(TagValue("endTime", "20240909 15:30:00 US/Eastern"))
order.algoParams.append(TagValue("noTakeLiq", int(0)))




#Balance Impact Risk algo  (for Options) - https://www.interactivebrokers.com/en/trading/orders/balance-impact-risk.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "BalanceImpactRisk"

order.algoParams = []
order.algoParams.append(TagValue("maxPctVol", .3))
order.algoParams.append(TagValue("riskAversion", "Aggressive"))
order.algoParams.append(TagValue("forceCompletion", int(0)))



#Minimize Impact algo  (for Options) - https://www.interactivebrokers.com/en/trading/orders/minimize-impact.php
order = Order()
order.action = "BUY"
order.totalQuantity = 1
order.orderType = "LMT"            
order.lmtPrice = 1
order.algoStrategy = "MinImpact"

order.algoParams = []
order.algoParams.append(TagValue("maxPctVol", .3))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#4. Cryptocurrency orders (MKT or LMT) - https://interactivebrokers.github.io/tws-api/cryptocurrency.html

contract = Contract()  
contract.symbol = "BTC"            #BTC/LTC/BCH/ETH are tradable with IBKR
contract.secType = "CRYPTO"
contract.exchange = "PAXOS"
contract.currency = "USD"


order = Order()
order.action = "BUY"
order.lmtPrice = 72550
order.totalQuantity = .1   
order.orderType = "LMT"   
order.tif = "MINUTES"               #IOC or MINUTES


order = Order()
order.action = "BUY"
order.orderType = "MKT"             
order.totalQuantity = 0
order.cashQty = 200                 #cashQty is used for MKT orders only
order.tif = "IOC"                   #IOC may be required


order = Order()
order.action = "SELL"
order.orderType = "MKT"          
order.totalQuantity = 0.00442198    #totalQuantity used for SELL orders
order.tif = "IOC"                   #IOC may be required


