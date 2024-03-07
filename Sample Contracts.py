"""
Sample TWS API contracts for Python:
    1. Stocks | 2. Options | 3. Forex | 4. Futures | 5. Future Options | 
    6. Indexes | 7. Warrants | 8. Mutual Funds | 9. CFDs | 10. Bonds |
    11. Cryptocurrencies | 12. Commodities | 13. Options spread | 14. Futures spread |
"""

from ibapi.contract import Contract

#1. STOCKS --------------------------------------------------------------------
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.exchange = "SMART"
contract.currency = "USD"

contract = Contract()
contract.symbol = "TSLA"
contract.secType = "STK"
contract.exchange = "SMART"
contract.currency = "USD"
contract.primaryExchange = "NASDAQ"     #Not always required, but for stocks - add the primaryExchange if you receive any 200 Errors "The contract description specified for <Symbol> is ambiguous"   

contract2 = Contract()
contract2.symbol = "F"
contract2.secType = "STK"
contract2.exchange = "SMART"
contract2.currency = "USD"
contract2.primaryExchange = "NYSE"

contract3 = Contract()
contract3.symbol = "SPY"
contract3.secType = "STK"
contract3.exchange = "SMART"
contract3.currency = "USD"
contract3.primaryExchange = "ARCA"

contractCAD = Contract()
contractCAD.symbol = "ACQ"
contractCAD.secType = "STK"
contractCAD.exchange = "SMART"
contractCAD.currency = "USD"
contractCAD.primaryExchange = "CAD"

contractFIGI = Contract()
contractFIGI.secIdType = "FIGI"
contractFIGI.secId = "BBG000B9XRY4"     #AAPL Stock defined via Bloomberg FIGI code (FIGI may only be usable for Stocks)
contractFIGI.exchange = "SMART"
contractFIGI.currency = "USD"

contract = Contract()
contract.conId = 265598                 #ConId or "IBKR Contract Identifier" may also be used to point to a Stock/Option/Futures contract etc. - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#tws-contract-details    
contract.exchange = "SMART"

contract = Contract()
contract.symbol = "SPY"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "IBKRATS"           #IBKRATS contract - https://www.interactivebrokers.com/en/trading/orders/ibkrats.php


#2. OPTIONS -------------------------------------------------------------------
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "OPT"
contract.currency = "USD"
contract.exchange = "SMART"
contract.right = "C"
contract.strike = 170
contract.lastTradeDateOrContractMonth = "20260116"

contract = Contract()
contract.conId = 653073040              #ConId or "IBKR Contract Identifier" may also be used to point to a Stock/Option/Futures contract etc. - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#tws-contract-details    
contract.exchange = "SMART"

contract2 = Contract()
contract2.symbol = "SPX"
contract2.secType = "OPT"
contract2.currency = "USD"
contract2.exchange = "SMART"
contract2.right = "C"
contract2.strike = 5100
contract2.lastTradeDateOrContractMonth = "20241231"
contract2.tradingClass = "SPXW"          #Not always required, but for SPX Options - add the tradingClass (SPX / SPXW) if you receive any 200 Errors "The contract description specified for <Symbol> is ambiguous"  


#3. FOREX ---------------------------------------------------------------------
contract = Contract()                  #EUR.USD
contract.symbol = "EUR"
contract.secType = "CASH"
contract.currency = "USD"
contract.exchange = "IDEALPRO"

contract2 = Contract()                 #USD.JPY
contract2.symbol = "USD"
contract2.secType = "CASH"
contract2.currency = "JPY"
contract2.exchange = "IDEALPRO"

contract3 = Contract()                 #CAD.JPY
contract3.symbol = "CAD"
contract3.secType = "CASH"
contract3.currency = "JPY"
contract3.exchange = "IDEALPRO"   


#4. FUTURES -------------------------------------------------------------------
contract = Contract()
contract.symbol = "ES"
contract.secType = "FUT"
contract.exchange = "CME"
contract.currency = "USD"
contract.lastTradeDateOrContractMonth = "202803"
#contract.multiplier = 50

contract = Contract()
contract.localSymbol = "ESH8"          #localSymbol may be used instead of specifying lastTradeDateOrContractMonth (expiration)
contract.secType = "FUT"
contract.exchange = "CME"
contract.currency = "USD"

contract2 = Contract()
contract2.symbol = "ZS"
contract2.secType = "FUT"
contract2.exchange = "CBOT"
contract2.currency = "USD"
contract2.lastTradeDateOrContractMonth = "20271112"

contract3 = Contract()             
contract3.symbol = "ES"
contract3.secType = "CONTFUT"          #Continuous futures contract, for Historical Data requests ONLY 
contract3.exchange = "CME"
contract3.currency = "USD"

        
#5. FUTURE OPTIONS ------------------------------------------------------------
contract = Contract()
contract.symbol = "ES"
contract.secType = "FOP"
contract.currency = "USD"
contract.exchange = "CME"
contract.right = "C"
contract.strike = 5500
contract.lastTradeDateOrContractMonth = "20281215"
contract.tradingClass = "ES"  
#contract.multiplier = 50

contract = Contract()
contract.conId = 673297163            #ConId or "IBKR Contract Identifier" may also be used to point to a Stock/Option/Futures contract etc. - https://ibkrcampus.com/ibkr-api-page/trader-workstation-api/#tws-contract-details   
contract.exchange = "CME"

contract2 = Contract()
contract2.symbol = "ES"
contract2.secType = "FOP"
contract2.currency = "USD"
contract2.exchange = "CME"
contract2.right = "C"
contract2.strike = 5500
contract2.lastTradeDateOrContractMonth = "20281215"
contract2.tradingClass = "EW3"   


#6. INDEXES -------------------------------------------------------------------
contract = Contract() 
contract.symbol = "SPX"          #S&P 500 Stock Index
contract.secType = "IND"
contract.exchange = "CBOE"
contract.currency = "USD"

contract2 = Contract()
contract2.symbol = "INDU"        #Dow Jones Industrial Average
contract2.secType = "IND"
contract2.exchange = "CME"
contract2.currency = "USD"

contract3 = Contract() 
contract3.symbol = "COMP"        #NASDAQ-COMPOSITE INDEX
contract3.secType = "IND"
contract3.exchange = "NASDAQ"
contract3.currency = "USD"

contract4 = Contract() 
contract4.symbol = "NDX"         #NASDAQ 100 Stock Index
contract4.secType = "IND"
contract4.exchange = "NASDAQ"
contract4.currency = "USD"

contract5 = Contract() 
contract5.symbol = "ES"          #E-mini S&P 500
contract5.secType = "IND"
contract5.exchange = "CME"
contract5.currency = "USD"

contract6 = Contract() 
contract6.symbol = "RUT"         #Russell 2000 Stock Index
contract6.secType = "IND"
contract6.exchange = "RUSSELL"
contract6.currency = "USD"

contract7 = Contract() 
contract7.symbol = "T-BOND"       #US T BOND
contract7.secType = "IND"
contract7.exchange = "CBOT"
contract7.currency = "USD"


#7. WARRANTS ------------------------------------------------------------------
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "WAR"
contract.exchange = "FWB"
contract.currency = "EUR"
contract.right = "C"
contract.strike = 180
contract.lastTradeDateOrContractMonth = "20281214"

contract2 = Contract()
contract2.symbol = "AAPL"
contract2.secType = "WAR"
contract2.exchange = "SWB"
contract2.currency = "EUR"
contract2.right = "C"
contract2.strike = 180
contract2.lastTradeDateOrContractMonth = "20281214"


#8. MUTUAL FUNDS --------------------------------------------------------------
contract = Contract()
contract.symbol = "VINIX"    
contract.exchange = "FUNDSERV"
contract.currency = "USD"
contract.secType = "FUND"


#9. CFDs ----------------------------------------------------------------------
contract = Contract()
contract.symbol = "IBUS500"    
contract.exchange = "SMART"
contract.currency = "USD"
contract.secType = "CFD"

contract2 = Contract()
contract2.symbol = "AAPL"    
contract2.exchange = "SMART"
contract2.currency = "USD"
contract2.secType = "CFD"


#10. BONDS (contract.symbol = CUSIP or ISIN) --------------------------------------------------------------------
contract = Contract()
contract.symbol= "037833DW7"        #AAPL corporate bond (contract.symbol=CUSIP)
contract.secType = "BOND"
contract.exchange = "SMART"
contract.currency = "USD"

contract = Contract()
contract.conId = 420616003          #Bonds can also be defined with the conId and exchange as with any security type. 
contract.exchange = "SMART"

contract2 = Contract()
contract2.symbol= "452152FP1"       #State of Illinois municipal bond (contract.symbol=CUSIP)
contract2.secType = "BOND"
contract2.exchange = "SMART"
contract2.currency = "USD"

contract3 = Contract()
contract3.symbol= "US912797FS14"    #US-Treasury bill (contract.symbol=ISIN)
contract3.secType = "BOND"
contract3.exchange = "SMART"
contract3.currency = "USD"


#11. CRYPTOCURRENCIES ---------------------------------------------------------
contract = Contract()
contract.symbol = "BTC"             #Bitcoin
contract.secType = "CRYPTO"
contract.currency = "USD"
contract.exchange = "PAXOS"

contract2 = Contract()
contract2.symbol = "BCH"            #Bitcoin Cash
contract2.secType = "CRYPTO"
contract2.currency = "USD"
contract2.exchange = "PAXOS"

contract3 = Contract()
contract3.symbol = "ETH"            #Ethereum
contract3.secType = "CRYPTO"
contract3.currency = "USD"
contract3.exchange = "PAXOS"

contract4 = Contract()
contract4.symbol = "LTC"            #Litecoin
contract4.secType = "CRYPTO"
contract4.currency = "USD"
contract4.exchange = "PAXOS"


#12. COMMODITIES --------------------------------------------------------------
contract = Contract()
contract.symbol = "USGOLD"
contract.secType = "CMDTY"
contract.currency = "USD"
contract.exchange = "IBMETAL"

contract2 = Contract()
contract2.symbol = "XAUUSD"
contract2.secType = "CMDTY"
contract2.currency = "USD"
contract2.exchange = "SMART"


from ibapi.contract import *


#13. OPTION SPREAD (has to use the IBKR Contract ID for each leg of the spread) --------------------------------------------------------------
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "BAG"
contract.currency = "USD"
contract.exchange = "SMART"

leg1 = ComboLeg()
leg1.conId = 653073040  
leg1.ratio = 1
leg1.action = "BUY"
leg1.exchange = "SMART"

leg2 = ComboLeg()
leg2.conId = 653076420
leg2.ratio = 1
leg2.action = "SELL"
leg2.exchange = "SMART"

# leg3 = ComboLeg()
# leg3.conId = 653073171
# leg3.ratio = 1
# leg3.action = "BUY"
# leg3.exchange = "SMART"

# leg4 = ComboLeg()
# leg4.conId = 653076542
# leg4.ratio = 1
# leg4.action = "SELL"
# leg4.exchange = "SMART"
    
contract.comboLegs = []
contract.comboLegs.append(leg1)
contract.comboLegs.append(leg2)
#contract.comboLegs.append(leg3)
#contract.comboLegs.append(leg4)


#14. FUTURES SPREAD -----------------------------------------------------------
contract = Contract()
contract.symbol = "ES"
contract.secType = "BAG"
contract.currency = "USD"
contract.exchange = "CME"                #SMART may also be usable - https://interactivebrokers.github.io/tws-api/spread_contracts.html#bag_fut
 
leg1 = ComboLeg()
leg1.conId = 649180666  
leg1.ratio = 1
leg1.action = "BUY"
leg1.exchange = "CME"

leg2 = ComboLeg()
leg2.conId = 649180690
leg2.ratio = 1
leg2.action = "SELL"
leg2.exchange = "CME"
    
contract.comboLegs = []
contract.comboLegs.append(leg1)
contract.comboLegs.append(leg2)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
