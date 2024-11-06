#TO-DO: write purpose of this file
#!/usr/bin/env python3
# Author: Daniel Tian
# Date: November 6th, 2024
# Purpose: Calls the Dog Class

# import the Dog class from dog file
from dog import Dog
def main():
  #TO-DO:
  # Create an object of the Dog class, pass appripate attributes values.
  My_Dog = Dog("Doggo","Shiba Inu")
  # Call the .bark() method
  print(My_Dog.bark())

if __name__ == "__main__":
  main()
