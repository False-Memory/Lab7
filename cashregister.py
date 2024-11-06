# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: November 6th, 2024
# Purpose: models the cash register in super markets.

# TO DO 1: Complete the functions below according to given instructions. 

class CashRegister:
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0
        #add an instance variable that you might need to implement undo() method
        self._preitemCount = []
        self._prePrice = []
        
    def addItem(self, price):
        self._preitemCount.append(self._itemCount) #Appends the previous value of count before updating
        self._prePrice.append(self._totalPrice) #Appends the previous value of price before updating
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price
        
    def getTotal(self):
        return self._totalPrice
    
    def getCount(self):
        return self._itemCount
    
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0
        
    #complete the following undo() method
    def undo(self):
        if len(self._preitemCount) > 0: #Checks if the list of previous items count is empty
            self._itemCount = self._preitemCount[len(self._preitemCount)-1] #Updates the current item count to the most recent log of the itemcount
            self._totalPrice = self._prePrice[len(self._prePrice)-1] #Updates the current price to the most recent log of the pricing
            self._preitemCount.pop() #Removes the most recent log of the itemcount
            self._prePrice.pop() #Removes the most recent log of the pricing
        else:
            print("You cannot undo anymore")
        pass
        

