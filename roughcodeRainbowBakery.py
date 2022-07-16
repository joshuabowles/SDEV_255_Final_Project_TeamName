#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def donut_price(donut_type):
    if donut_type == 'Glazed':
        return 2.50
    elif donut_type == 'Chocolate':
        return 3.50
    elif donut_type == 'Homer':
        return 4.25

def total_price(price, quantity):
    total = price * quantity
    print("Total price: $" + str(total) )


donut_type = input("Enter the type of donut you want: ")
quantity = int(input("How many donuts do you want: "))
price = donut_price(donut_type)
total_price(price, quantity)


# In[ ]:


class donut:
    def __init__(self, donut, quantity, total)
    self.name = name


# In[ ]:


donutType = ["Glazed", "Chocolate", "Sprinkles", "Caramel", "Oreo", "Homer"]
donutPrices = [2.50, 3.00, 2.50, 2.75, 3.75]

