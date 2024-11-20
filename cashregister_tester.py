#TO-DO: write purpose of this file
#!/usr/bin/env python3
# Author: Daniel Tian
# Date: November 6th, 2024
# Purpose: Calls the CahsRegister Class

from cashregister import CashRegister

def main():
    reg1 = CashRegister()
    reg1.addItem(13.5)
    print(repr(reg1))
    reg1.addItem(15.8)
    print(repr(reg1))
    reg1.undo()
    print(repr(reg1))
    reg1.undo()
    print(repr(reg1))
    reg1.undo()

    reg2 =  CashRegister()
    reg2.addItem(15)
    reg2.addItem(5)
    
    reg3 = reg2 + reg1
    print(repr(reg3))

    reg3 = reg1 - reg2
    print(repr(reg3))

    reg3 = reg2 * 15
    print(repr(reg3))

    reg3 = reg2 / 15
    print(repr(reg3))

    print(repr(reg2))

if __name__ == "__main__":
    main()