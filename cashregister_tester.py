#TO-DO: write purpose of this file
#!/usr/bin/env python3
# Author: Daniel Tian
# Date: November 6th, 2024
# Purpose: Calls the CahsRegister Class

from cashregister import CashRegister

def main():
    reg1 = CashRegister()
    reg1.addItem(13.5)
    print("Item Count:", reg1.getCount(), "Price:" ,reg1.getTotal())
    reg1.addItem(15.8)
    print("Item Count:", reg1.getCount(), "Price:" ,reg1.getTotal())
    reg1.undo()
    print("Item Count:", reg1.getCount(), "Price:" ,reg1.getTotal())
    reg1.undo()
    print("Item Count:", reg1.getCount(), "Price:" ,reg1.getTotal())
    reg1.undo()

if __name__ == "__main__":
    main()