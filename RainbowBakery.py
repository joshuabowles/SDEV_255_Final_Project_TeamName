#!/usr/bin/env python
# coding: utf-8

# In[1]:


NUM_ITEMS = 6
userList = []
donutL = [["GLAZED", 2.50], ["CHOCOLATE", 2.75], ["SPRINKLES",3.00], ["CARAMEL", 3.25], ["OREO", 3.75], ["HOMER",4.00]]
result = 0
def total_price(p, q):
    return p * q

class Donut:
    def __init__(self, donutType, quantity =1, total=0):
        self.donutType = donutType
        self.quantity = quantity
        self.total = total

class Glazed(Donut):
    def __init__(self):
        return userDone[0], 1, userDone[0]
class Chocolate(Donut):
    def __init__(self):
        return userDone[1], 1, userDone[1]
class Sprinkles(Donut):
    def __init__(self):
        return userDone[2], 1, userDone[2]
class Caramel(Donut):
    def __init__(self):
        return userDone[3], 1, userDone[3]
class Oreo(Donut):
    def __init__(self):
        return userDone[4], 1, userDone[4]
class Homer(Donut):
    def __init__(self):
        return userDone[5], 1, userDone[5]

print("Welcome to Rainbow Bakery! We have 6 different types of donuts: ")
for x,y in donutL:
    print(x, y)
    
price = 0
while True:
    nextItem = []
    donut_type = input("\nEnter the type of donut you want, XXX to exit, or type EDIT to edit list: ").upper()
    print(donut_type)
    if (donut_type != "XXX") and (donut_type != "EDIT"):
        foundIt = False
        for i in range(0, NUM_ITEMS):
            if donutL[i][0] == donut_type:
                foundIt = True
                nextItem.append(donut_type)
                print(nextItem)
        if foundIt:
            quantity = int(input("\nHow many donuts do you want: "))
            print(quantity)
            nextItem.append(quantity)
            for row in donutL:
                if row[0] == donut_type:
                    price = row[1]
            #price = donutL.index(1)[donutL.index(donut_type)]
            result += total_price(price, quantity)
            userList.append(nextItem)
            print(userList)
    elif donut_type == "EDIT":
        remove_item = input("\nEnter donut you would like to remove or XXX to exit: ").upper()
        print(remove_item)
        for row in userList:
            if row[0] == remove_item:
                row[1] -= 1
                print(userList)
        for row in userList:
            if row[1] == 0:
                userList.remove(row)
                print(userList)
                
        for row in donutL:
                if row[0] == donut_type:
                    price = row[1]
        
        #price = donutL.index(1)[donutL.index(remove_item)]
        result -= total_price(price, 1)
    else:
        print("\nYou have ordered: " + str(userList) + " Your total is: $" + format(result, ".2f") + " Thank you! Goodbye!")
        break


# In[ ]:




