"""
Take the XML response from requestFA  ->  convert it to usable format for replaceFA

Could be used to share FA Groups from 1 TWS user to another, etc. 
"""


# string2 = """<?xml version="1.0" encoding="UTF-8"?>
# <ListOfGroups>
# 	<Group>
# 		<name>EqualQuantity</name>
# 		<ListOfAccts varName="list">
# 			<String>DU2372888</String>
# 			<String>DU2372889</String>
# 		</ListOfAccts>
# 		<defaultMethod>Equal</defaultMethod>
# 		<linkedHFGroup>false</linkedHFGroup>
# 	</Group>
# </ListOfGroups>
# """

string2 = """<?xml version="1.0" encoding="UTF-8"?>
<ListOfAllocationProfiles>
	<AllocationProfile>
		<name>PERCENT</name>
		<type>1</type>
		<ListOfAllocations varName="listOfAllocations">
			<Allocation>
				<acct>DU2372888</acct>
				<amount>80.0</amount>
			</Allocation>
			<Allocation>
				<acct>DU2372889</acct>
				<amount>20.0</amount>
			</Allocation>
		</ListOfAllocations>
	</AllocationProfile>
</ListOfAllocationProfiles>
"""


string3 = string2.splitlines()
xl = "xml version"
spaces = []
beginstr = ', "'
endstr = '"'
car = "<"

onespace = "\t"
twospace = "\t\t"
threespace = "\t\t\t"
fourspace = "\t\t\t\t"


#Find the number of spaces for each item in receiveFA response -=-=---=-=--===-=-=----=-=-===-=-=-=----=-=-=-===-=-=-=----=-=-==
for item in string3:
    if xl in item:
        pass    
    if car in item:            
        z2 = item.find(car)
        #print(z2)
        spaces.append(z2)

print("")    
#print(string3[0])    
# for item in spaces:
#     print(item)    
    

#Add the , " formatting for each line -=-=---=-=--===-=-=----=-=-===-=-=-=----=-=-=-===-=-=-=----=-=-==
al = []    
for item in string3:    
    if xl in item:
        al.append(item)
    elif "ListOfAccts varName" in item:
        astr = '<ListOfAccts varName=\\"list\\">'
        zstr = beginstr+astr+endstr
        #print("FOUND")
        #print(zstr)
        al.append(zstr)
    elif "ListOfAllocations varName" in item:
        astr = '<ListOfAllocations varName=\\"listOfAllocations\\">'
        zstr = beginstr+astr+endstr
        #print("FOUND")
        #print(zstr)
        al.append(zstr)        
    else:        
        astr = item.strip()    
        zstr = beginstr+astr+endstr
        al.append(zstr)
  
    
#Add the correct spacing & indentation -=-=---=-=--===-=-=----=-=-===-=-=-=----=-=-=-===-=-=-=----=-=-==
bl = []    
i=0
while i<len(al):
    if spaces[i] == 0:
        zitem = al[i]
    elif spaces[i] == 1:
        zitem = onespace + al[i]
    elif spaces[i] == 2:
        zitem = twospace + al[i]
    elif spaces[i] == 3:
        zitem = threespace + al[i]
    elif spaces[i] == 4:
        zitem = fourspace + al[i]    
    bl.append(zitem)

    i+=1
   
for item in bl:
    print(item)    